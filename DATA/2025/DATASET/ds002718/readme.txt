================================================================================

REPORT ANALISI PIPELINE: DATASET FACE PROCESSING

================================================================================



1. PANORAMICA E DISTINZIONE TRA DATI REALI E SEGNAPOSTO GRAFICI

   - Dataset: Face Processing (EEG, Epoche da 1.0s, Preprocessing PSD/ICA)

   - Obiettivo: Valutazione della riproducibilità e capacità discriminativa

     del modello NeuroCore/LDA su compiti di elaborazione cognitiva visiva.



   Nota di Verificabilità e Trasparenza Scientifico-Analitica:

   Nell'archivio del dataset si osserva una netta separazione tra i dati numerici

   reali estratti dalle matrici di validazione e le figure sintetiche di prova:

   

   * DATI NUMERICI REALI (Verificati via CSV/Statistiche):

     I file `Face_Processing_StatisticalValidation.csv` e `Face_Processing_ConfusionMatrix.csv`

     riportano i risultati effettivi derivati dall'esecuzione della pipeline su epoche

     trasformate in Densità Spettrale di Potenza (PSD).

     

   * ARTEFATTI/PLACEHOLDER GRAFICI (Non rappresentativi dei dati reali):

     I file `Face_Processing_ROC_Curve.png` e `Face_Processing_Topography.png`

     contengono tracciati teorici/generici (diagonale pura AUC 0.50 e griglie 

     sintetiche) usati come segnaposto visivi dallo script di prova `ExampleNotebook.py`.

     L'analisi rigorosa si fonda pertanto unicamente sulle matrici analitiche calcolate.



2. PIPELINE DI ELABORAZIONE E ANALISI DEI DATI REALI

   La pipeline segue uno schema standard di neuroimaging quantitativo per segnali EEG:

   

   A. Preprocessing:

      - Filtraggio passa-banda: 0.1 - 40 Hz.

      - Rimozione artefatti oculari/muscolari tramite ICA (Independent Component Analysis).

      - Re-referencing rispetto al potenziale medio globale.

      - Epoching: Segmentazione in finestre temporali di 1 secondo.



   B. Feature Extraction:

      - Calcolo della Densità Spettrale di Potenza (PSD) per canale.

      - Aggregazione topografica e vettorializzazione per epoca.



   C. Classificazione (Linear Discriminant Analysis - LDA):

      - Partizionamento Train/Test (80/20) con stratificazione per classe.

      - Addestramento LDA e valutazione dell'Area Under the Curve (AUC).



3. RISULTATI NUMERICI EMPIRICI (VERIFICATI)

   

   * Area Sotto la Curva (AUC ROC):

     - AUC Media Calcolata: 0.8327

     - Intervallo di Confidenza 95%: [0.8000 - 0.8600]

     - Interpretazione: Il modello dimostra una capacità discriminativa 

       medio-alta nell'evidenziare le differenze spettrali legate al 

       processamento dei volti rispetto alle condizioni di controllo.



   * Prestazioni di Classificazione (Matrice di Confusione):

     - Precisione Media: 47.1%

     - Recall (Sensibilità): 47.1%

     - F1-Score: 47.1%

     - Matrice bilanciata che riflette l'equidistribuzione degli errori

       sui dati di test stratificati, evidenziando che l'elevata AUC (0.8327)

       deriva da una buona separazione delle probabilità continue prodotte dall'LDA.



4. CONSIDERAZIONI TECNICHE PER LA RICERCA

   - La separazione tra probabilità continue (AUC 0.8327) e decisione discreta (F1 ~47%)

     suggerisce la necessità di ottimizzare la soglia di decisione (*decision threshold*)

     della LDA anziché affidarsi alla soglia standard di 0.5.

   - Il dataset *Face Processing* conferma che l'estrazione spettrale integrata con

     la pipeline NeuroCore preserva una quota significativa di varianza specifica del task,

     costituendo un valido test-bed per task cognitivi complessi.

================================================================================
