====================================================================
ALZHEIMER EEG BIOMARKERS CLASSIFICATION (OpenNeuro ds004504)
====================================================================

1. PANORAMICA DEL PROGETTO
Questo repository raccoglie i risultati dell'analisi predittiva e dei biomarcatori basati su elettroencefalografia (EEG) per la classificazione automatica tra soggetti di controllo sani e pazienti affetti da Malattia di Alzheimer (AD), utilizzando il dataset pubblico OpenNeuro ds004504.

2. METODOLOGIA E MODELLI
- Preprocessing: Segmentazione dei segnali in finestre temporali da 2.0 secondi (durata segmento: 120s).
- Validazione: Utilizzo di una strategia di validazione incrociata nidificata (Nested Cross-Validation) per garantire l'affidabilità e la generalizzabilità dei modelli di classificazione.
- Evoluzione delle Feature (Confronto Versioni):
  * Versione Base (ds004504): Filtraggio a banda larga (1.0 - 40.0 Hz) su 54 soggetti (29 controlli, 25 AD). Prestazioni limitate (AUC media ~0.499, Sensibilità 12%).
  * Versione Ottimizzata v2.1: Introduzione di bande spettrali mirate (delta: 1-4 Hz, theta: 4-8 Hz, alpha: 8-12 Hz, beta: 13-30 Hz), indici di interazione spettrale (FSI, BP) e rapporti di banda dedicati (es. R_delta_alpha) su 65 soggetti (29 controlli, 36 AD).

3. RISULTATI PRINCIPALI (VERSIONE V2.1)
- Area Under the Curve (Mean AUC): 0.715 (± 0.179)
- Precision-Recall AUC (PR-AUC): 0.668
- Sensibilità (TPR @ 0.5): 72.2%
- Specificità (TNR @ 0.5): 55.2%

4. CONCLUSIONI
L'ingegneria delle feature basata sulle bande di frequenza spettrale e sui loro rapporti incrementa drasticamente la capacità predittiva rispetto all'analisi a banda larga, confermando l'efficacia dei marker spettrali EEG come biomarcatori non invasivi per l'Alzheimer.
====================================================================
