from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Abilita la comunicazione con il frontend su Netlify

@app.route('/analizza', methods=['GET', 'POST'])
def analizza_dataset():
    try:
        # Percorso del dataset (puoi metterlo nella stessa cartella del progetto)
        # Sostituisci 'tuo_dataset.csv' con il nome reale del tuo file
        file_path = 'tuo_dataset.csv'
        
        if not os.path.exists(file_path):
            return jsonify({
                "errore": f"Il file {file_path} non è stato trovato nella cartella del server."
            }), 404

        # Caricamento del dataset con Pandas
        df = pd.read_csv(file_path) # Usa pd.read_excel se è un file Excel (.xlsx)

        # Esempio di elaborazione dati (puoi modificarlo in base alle tue esigenze)
        # Ad esempio: statistiche descrittive, medie, conteggi, ecc.
        riassunto_statistico = df.describe().to_dict()
        righe_totali = len(df)
        colonne = list(df.columns)

        # Risposta da inviare al tuo sito su Netlify
        risultato = {
            "stato": "successo",
            "righe_totali": righe_totali,
            "colonne": colonne,
            "statistiche": riassunto_statistico
        }

        return jsonify(risultato)

    except Exception as e:
        return jsonify({"errore": str(e)}), 500

if __name__ == '__main__':
    # Avvio locale (su Render la porta viene gestita automaticamente)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
