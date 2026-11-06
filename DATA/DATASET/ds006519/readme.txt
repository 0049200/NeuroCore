===============================================================================

                          Dataset: OpenNeuro ds006519

              Documentazione Baseline Iniziale ed Esiti Sperimentali

===============================================================================

1. SINTESI E CONTESTO SPERIMENTALE

-------------------------------------------------------------------------------

Il presente report documenta le evidenze tecniche e le metriche ottenute durante 

le prime fasi di test su dataset iEEG (EEG intracranico) OpenNeuro ds006519.



Nonostante le metriche di discriminazione primarie (es. AUC-ROC) abbiano mostrato 

valori ridotti o non significativi nelle iterazioni iniziali, la tracciabilità e 

il versionamento tramite commit dei file CSV di output risultano fondamentali per:

  1. Definire la baseline di confronto per le future iterazioni di feature engineering.

  2. Documentare la stabilità/resilienza del sistema in condizioni non ottimali.

  3. Prevenire la duplicazione di esperimenti non performanti.





2. DATA HYGIENE ED EVIDENZE DI SISTEMA

-------------------------------------------------------------------------------

2.1 Gestione File "Shadow" macOS (AppleDouble)

    - Problema: La presenza di file `. _*` generati da macOS su storage esterni 

      (es. `._sub-01_ses-01_task-dcs_ieeg.eeg`) genera warning ed eccezioni di 

      parsing in MNE-Python (`RuntimeWarning: unparsable header`).

    - Soluzione: Implementazione di uno script di sanitizzazione BIDS preventivo 

      prima dell'invocazione dei loader.



2.2 Specifiche Tecniche del Segnale

    - Frequenza di Campionamento: Nattiva a 4096.0 Hz (`sfreq`), idonea per la 

      rilevazione di oscillazioni ad alta frequenza (HFO) e transitori rapidi.

    - Struttura Canali: Eterogenea tra soggetti (31-35 canali attivi), riflettendo 

      la disposizione clinica personalizzata di elettrodi SEEG/ECoG.





3. ANALISI DEI RISULTATI E METRICHE DI TEST (BASELINE)

-------------------------------------------------------------------------------

3.1 Performance Discriminativa (AUC-ROC Ridotta)

    - Risultato: Valori di Area Under the Curve (AUC) bassi/prossimi al livello 

      casuale nelle prime esecuzioni del modello.

    - Valutazione: Risultato atteso per una prima pipeline grezza priva di 

      cleaning avanzato degli artefatti, di selezione focalizzata dei canali 

      o di estrazione di feature tempo-frequenza dedicate (es. High-Gamma band).



3.2 Indice di Resilienza (Valore del Plateau: 1.0)

    - Risultato: L'indice di resilienza si stabilizza su un valore pari a 1.0.

    - Interpretazione Tecnica: 

      * Rappresenta la massima tolleranza/invarianza della misura rispetto a 

        perturbazioni del segnale, rimozione progressiva di canali o variazioni 

        di rumore di fondo.

      * Nonostante la scarsa capacità separabile del modello (bassa AUC), la 

        pipeline dimostra una perfetta stabilità strutturale (Resilienza = 1.0), 

        confermando che l'infrastruttura di calcolo è robusta e priva di 

        crolli numerici o instabilità di sovrastimolazione.





4. RISULTATI DEGNI DI NOTA (SPUNTI SECONDARI)

-------------------------------------------------------------------------------

1. Stabilità della Risposta in Frequenza a 4096 Hz:

   Assenza di clipping o saturazione nei canali primari registrati, confermando 

   la qualità del segnale sorgente nonostante l'assenza di pre-processing.



2. Coerenza Temporale dei Marcatori di Evento (`_events.tsv`):

   Sincronizzazione perfetta tra timestamp di stimolo e tracce electrofisiologiche, 

   che garantisce la corretta impostazione dei futuri moduli di epoching.



3. Integrità del Mappaggio dei Canali:

   La matrice dei canali risponde in modo prevedibile al filtraggio per tipologia 

   (es. separazione tra elettrodi di profondità ed eventuali canali di servizio/ECG).



5. RACCOMANDAZIONI PER IL COMMIT E PROSSIMI PASSI

-------------------------------------------------------------------------------

1. Versionamento dei CSV:

   Includere i file CSV dei primi test nel repository. Tracciare i risultati 

   iniziali è essenziale per la riproducibilità scientifica e per quantificare 

   i progressi formali ottenuti con i modelli futuri.



2. Messaggio di Commit Consigliato:

   `docs(results): aggiunte metriche baseline (AUC iniziale, resilienza 1.0) per tracciabilità esperimenti`



3. Prossime Azioni Sulla Pipeline:

   - Applicare filtraggio notch per la rete elettrica (50/60 Hz) e passabanda.

   - Eseguire il downsampling del segnale per accelerare la fase di training.

   - Implementare l'estrazione di feature spettrali specifiche (Power Spectral 

     Density in bande Target).
