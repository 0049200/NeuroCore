## 1. Panoramica del Dataset (India+Tanzania)
* **File Principali:** `INDIA__df_clean.csv` (N = 94 unità analitiche) e `INDIA__df_z.csv` (N = 2793 osservazioni ad alta risoluzione temporale).
* **Finalità:** Quantificare la stabilità, la complessità strutturale e la disruzione dinamica globale del sistema attraverso metriche di transizione e spettrali.

## 2. Risultati Descrittivi Principali
* **Indice di Disruzione (`dynamic_disruption`):** Varia da un minimo di -5.12 a un massimo di +5.19, mostrando una distribuzione simmetrica ideale per distinguere stati di quiete da stati di forte alterazione/transizione.
* **Complessità e Stabilità:** I valori di complessità spaziano da ~0.01 a 2.58, evidenziando una buona eterogeneità nei comportamenti dinamici registrati.
* **Normalizzazione (`df_z`):** Tutte le metriche chiave (inclusi i changepoint temporali, l'indeterminatezza e la dispersione spaziale) sono state correttamente centrate e scalate ($z$-score con $\sigma = 1.0$), pronte per modelli di machine learning o analisi statistiche avanzate.

