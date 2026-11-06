================================================================================

                    SEEG_Resting_State_Recording_005670

================================================================================

Pipeline Version   : NeuroCore Universal iEEG Loader v3 / Feature Extractor v3



[NOTA STORICA / BENCHMARK INIZIALE]

Questo report riassume uno dei primi test condotti con la piattaforma 

NeuroCore. L'esperimento è stato eseguito per convalidare il flusso di calcolo 

delle primitive di regime su registrazioni SEEG ad alta frequenza di 

campionamento in condizione di Resting State.



--------------------------------------------------------------------------------

1. RIASSUNTO ESECUZIONE & CARICAMENTO DATASET

--------------------------------------------------------------------------------

Files Trovati Totali     : 4

Files Validi Caricati    : 2

Files Falliti / Ignorati : 2



Note sul caricamento:

- I 2 fallimenti sono dovuti a file nascosti di sistema generati da macOS 

  (prefisso `._`, es: `._sub-01_task-rest_ieeg.edf`).

- I 2 file EDF validi (`sub-01` e `sub-02`) sono stati correttamente letti ed 

  elaborati tramite il modulo MNE.

- Frequenza di campionamento rilevata elevata: 2000.0 Hz.



--------------------------------------------------------------------------------

2. METRICHE PRINCIPALI DI REGIME (NEUROCORE PRIMITIVES)

--------------------------------------------------------------------------------

Frequenza di Campionamento (sfreq) : 2000.0 Hz

Dimensione Finestra Analisi        : 2.0 secondi (4000 campioni/finestra)

Area Under Curve (AUC Totale)      : 0.009295270312577486



Risultati Dettagliati per Soggetto:



* File: sub-01_task-rest_ieeg.edf

  - Canali            : 238

  - Campioni Totali   : 866,048

  - Lambda            : 0.006086508743464947

  - Resilience        : 0.9993529915809631

  - Dynamic Pressure  : 0.008895482867956161



* File: sub-02_task-rest_ieeg.edf

  - Canali            : 186

  - Campioni Totali   : 880,024

  - Lambda            : 0.006152351386845112

  - Resilience        : 0.9992850422859192

  - Dynamic Pressure  : 0.009695057757198810
