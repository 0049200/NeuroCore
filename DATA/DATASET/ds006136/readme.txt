================================================================================

                             OWM-Dataset_ds006136

================================================================================

Pipeline Version   : NeuroCore Universal iEEG Loader v3 / Feature Extractor v3

Questo report rappresenta una delle prime esecuzioni pilota di test effettuate 

dall'architettura NeuroCore (anno 2025). È stato utilizzato come dataset di 

validazione primaria per verificare la stabilità del caricatore multi-formato v3 

e la corretta convergenza delle metriche di regime dinamico.


--------------------------------------------------------------------------------

1. RIASSUNTO ESECUZIONE & CARICAMENTO DATASET

--------------------------------------------------------------------------------

Files Trovati Totali     : 28

Files Validi Caricati    : 14

Files Falliti / Ignorati : 14



Note sul caricamento:

- I 14 fallimenti sono dovuti alla presenza di file di sistema nascosti di macOS 

  (prefisso `._`, es: `._sub-MU1_task-OWM_ieeg.edf`), che non contengono header 

  EDF validi.

- Tutti i 14 file EDF effettivi dei soggetti (sub-MU1 ... sub-MU6, sub-P1 ... sub-P7) 

  sono stati caricati con successo senza errori critici.

- Warning di sistema riscontrati: "Invalid measurement date encountered in the header" 

  (gestito correttamente da MNE-Python).



--------------------------------------------------------------------------------

2. METRICHE PRINCIPALI DI REGIME (NEUROCORE PRIMITIVES)

--------------------------------------------------------------------------------

Frequenza di Campionamento (sfreq) : 1000.0 Hz (costante su tutti i file)

Dimensione Finestra Analisi        : 2.0 secondi (2000 campioni/finestra)

Area Under Curve (AUC Totale)      : 0.000640958441181283



Estratto Metriche Campione (Primi 5 soggetti):



* File: sub-MU1_task-OWM_ieeg.edf

  - Canali: 6 | Campioni: 598,000

  - Lambda           : 1.179700e-05

  - Resilience       : 1.000000

  - Dynamic Pressure : 2.137866e-05



* File: sub-MU2_ses-01_task-OWM_ieeg.edf

  - Canali: 8 | Campioni: 683,000

  - Lambda           : 2.617995e-05

  - Resilience       : 1.000000

  - Dynamic Pressure : 5.004817e-05



* File: sub-MU2_ses-02_task-OWM_ieeg.edf

  - Canali: 9 | Campioni: 501,000

  - Lambda           : 2.510303e-05

  - Resilience       : 1.000000

  - Dynamic Pressure : 5.516343e-05



* File: sub-MU3_task-OWM_ieeg.edf

  - Canali: 5 | Campioni: 702,000

  - Lambda           : 1.342445e-05

  - Resilience       : 1.000000

  - Dynamic Pressure : 2.529591e-05



* File: sub-MU4_task-OWM_ieeg.edf

  - Canali: 7 | Campioni: 657,000

  - Lambda           : 1.320147e-05

  - Resilience       : 1.000000

  - Dynamic Pressure : 2.576779e-05



