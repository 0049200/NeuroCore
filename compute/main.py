
import os
import io
import zipfile
import json
from pathlib import PurePosixPath

import numpy as np
import pandas as pd

from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest

app = FastAPI(title="NeuroCore Labs API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"]
)

MAX_MB = int(os.getenv("MAX_UPLOAD_MB", "1024"))
ZIP_MB = int(os.getenv("MAX_ZIP_UNPACKED_MB", "4096"))
MAX_MEM = int(os.getenv("MAX_ZIP_MEMBERS", "10000"))

EXT = {
    ".csv", ".tsv", ".txt", ".json", ".xlsx",
    ".parquet", ".npy", ".npz", ".mat",
    ".edf", ".bdf", ".fif"
}


def zip_member(data):
    archive = zipfile.ZipFile(io.BytesIO(data))
    items = archive.infolist()

    if len(items) > MAX_MEM:
        raise ValueError("ZIP member count exceeds configured limit")

    if any(item.flag_bits & 1 for item in items):
        raise ValueError("Encrypted ZIP is not supported")

    if sum(item.file_size for item in items) > ZIP_MB * 1024 * 1024:
        raise ValueError("ZIP expanded size exceeds configured limit")

    candidates = [
        item for item in items
        if not item.is_dir()
        and PurePosixPath(item.filename).suffix.lower() in EXT
    ]

    if not candidates:
        raise ValueError("No supported file in ZIP")

    selected = max(candidates, key=lambda item: item.file_size)

    return selected.filename, archive.read(selected)


def load_data(name, data):
    ext = PurePosixPath(name).suffix.lower()

    if ext in {".csv", ".tsv", ".txt"}:
        return pd.read_csv(
            io.BytesIO(data),
            sep="\t" if ext == ".tsv" else None,
            engine="python"
        )

    if ext == ".json":
        obj = json.loads(data.decode())
        if isinstance(obj, (dict, list)):
            return pd.json_normalize(obj)
        return pd.DataFrame({"value": [obj]})

    if ext == ".xlsx":
        return pd.read_excel(io.BytesIO(data))

    if ext == ".parquet":
        return pd.read_parquet(io.BytesIO(data))

    if ext == ".npy":
        arr = np.load(io.BytesIO(data), allow_pickle=False)
        return pd.DataFrame(np.asarray(arr).reshape(-1, 1))

    if ext == ".npz":
        archive = np.load(io.BytesIO(data), allow_pickle=False)
        return pd.DataFrame({
            key: np.asarray(archive[key]).reshape(-1)
            for key in archive.files
            if np.asarray(archive[key]).ndim <= 1
        })

    if ext == ".mat":
        from scipy.io import loadmat

        obj = loadmat(io.BytesIO(data))

        return pd.DataFrame({
            key: np.asarray(value).reshape(-1)
            for key, value in obj.items()
            if not key.startswith("__")
            and np.asarray(value).ndim <= 2
        })

    if ext in {".edf", ".bdf", ".fif"}:
        import tempfile
        import mne

        suffix = ext

        with tempfile.NamedTemporaryFile(suffix=suffix) as temp:
            temp.write(data)
            temp.flush()

            if ext == ".fif":
                raw = mne.io.read_raw_fif(
                    temp.name,
                    preload=True,
                    verbose="ERROR"
                )
            else:
                raw = mne.io.read_raw(
                    temp.name,
                    preload=True,
                    verbose="ERROR"
                )

            return pd.DataFrame(raw.get_data().T)

    raise ValueError("Unsupported file format")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.2.0"
    }


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    x_api_key: str | None = Header(default=None)
):
    expected = os.getenv("NEUROCORE_API_KEY")

    if expected and x_api_key != expected:
        raise HTTPException(401, "Invalid API key")

    data = await file.read(MAX_MB * 1024 * 1024 + 1)

    if len(data) > MAX_MB * 1024 * 1024:
        raise HTTPException(413, "Upload exceeds MAX_UPLOAD_MB")

    name = file.filename or "data.bin"

    try:
        if name.lower().endswith(".zip"):
            name, data = zip_member(data)

        df = load_data(name, data)

        numeric = (
            df.select_dtypes(include=[np.number])
            .replace([np.inf, -np.inf], np.nan)
            .dropna(axis=1, how="all")
        )

        if numeric.empty:
            raise ValueError("No numeric columns available")

        x = numeric.fillna(numeric.median()).to_numpy(float)

        if len(x) < 2:
            raise ValueError("At least two observations required")

        x = np.nan_to_num(x)

        std = np.std(x, axis=0)
        std[std == 0] = 1

        z = (x - x.mean(axis=0)) / std

        delta = np.diff(z, axis=0)

        transition = float(
            np.mean(np.linalg.norm(delta, axis=1))
        )

        fs = float(1 / (1 + np.mean(np.abs(delta))))
        fr = float(1 / (1 + transition))

        variance = np.var(z, axis=0)
        mi = float(np.mean(variance / (1 + variance)))

        pca = PCA(
            n_components=min(3, z.shape[1], z.shape[0])
        )
        pca.fit(z)

        anomalies = IsolationForest(
            random_state=42
        ).fit_predict(z)

        return {
            "file": file.filename,
            "analyzed_member": name,
            "shape": {
                "rows": len(df),
                "columns": len(df.columns),
                "numeric_columns": numeric.shape[1]
            },
            "metrics": {
                "FS": round(fs, 6),
                "DV": round(transition, 6),
                "FR": round(fr, 6),
                "MI": round(mi, 6)
            },
            "exploratory": {
                "pca_variance_ratio":
                    pca.explained_variance_ratio_.tolist(),
                "anomaly_fraction":
                    float(np.mean(anomalies == -1))
            },
            "limitations": [
                "Exploratory indicators, not clinically validated.",
                "ZIP selects one largest supported member; "
                "multi-file BIDS ingestion is not implemented."
            ]
        }

    except Exception as error:
        raise HTTPException(400, str(error))
