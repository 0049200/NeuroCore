# REPORT ANALISI PIPELINE: DATASET VISUOMOTOR (TASK-GAME)


1. PANORAMICA 

- Nome Dataset: Visuomotor Dataset (Task: `game`, acquisizioni iEEG/EDF)

- Rilevanza Progettuale: Trattandosi di uno dei primissimi dataset testati e validati all'interno della pipeline NeuroCore, funge da benchmark fondamentale per il tracciamento delle risposte dinamiche visuomotorie.

- Dimensione Campione: 16 file iEEG/EDF analizzati (8 soggetti: da `sub-01` a `sub-08`, registrati in due sessioni temporali: `ses-01` e `ses-02`).

- Area Sotto la Curva (AUC): 0.03500768 (parametro indicativo dell'accumulo di pressione dinamica durante lo svolgimento del task visuomotorio).



2. ANALISI DELLA PIPELINE ED ESECUZIONE TECNICA

La pipeline NeuroCore applica il suo algoritmo di Regime Transition per elaborare i segnali intracranici durante l'esecuzione del task visuomotorio:

- Screening Spettrale e Dinamico: Elaborazione dei segnali iEEG multi-canale.

- Metriche Calcolate:

  * Dynamic Pressure ($P_d$): Indicatore del carico di sollecitazione della rete neurale (range osservato: da 0.001103 a 0.004568).

  * Resilience ($R$): Grado di stabilità e capacità della rete di mantenere lo stato stazionario ($R \approx 1.0$).

  * Lambda ($\lambda$): Tasso di divergenza / fluttuazione del sistema neurale.

- Tracciamento delle Transizioni: I dati vengono ordinati per pressione dinamica crescente per quantificare la transizione tra regimi di coordinazione visuomotoria a bassa ed elevata sollecitazione.



3. RISULTATI CHIAVE ED ELEMENTI DI INTERESSE

- Altissima Resilienza Sistemica ($R \ge 0.999991$):

  In tutti i 16 tracciati iEEG del task visuomotorio, la resilienza rimane vicina al valore massimo teorico (1.0). Questo dimostra che il circuito cortico-sottocorticale coinvolto nell'integrazione visuomotoria mantiene una stabilità strutturale estremamente elevata.

- Profilo di Pressione Dinamica (Curva a Due Fasi):

  * Fase a Basso Carico (File 0-10): La pressione dinamica cresce gradualmente da 0.001103 a 0.002279.

  * Impennata ad Alto Carico (File 11-15): Nelle ultime 4 condizioni si osserva una netta accelerazione, con il picco massimo raggiunto in `sub-05_ses-01` ($P_d = 0.004568$, $\lambda = 0.002506$).

- Variabilità Inter-Soggetto e Differenze Tra Sessioni:

  * `sub-08` dimostra la massima efficienza neuro-dinamica durante il task (valore minimo $P_d = 0.001103$ in `ses-02`).

  * `sub-05` presenta la massima sollecitazione dinamica e il più alto esponente $\lambda$ sia nella prima che nella seconda sessione.

  * La differenza tra `ses-01` e `ses-02` nei vari soggetti evidenzia come la pipeline riesca a rilevare plasticità, apprendimento motorio o affaticamento visivo tra le diverse sessioni sperimentali.



4. CONCLUSIONI PER LO SVILUPPO DELLA PIPELINE

- La validation sul dataset visuomotorio dimostra la capacità della pipeline NeuroCore di caratterizzare in modo riproducibile i regimi dinamici corticali in task attivo.

- La curva di transizione rappresenta un eccellente benchmark di riferimento per la taratura dei parametri di controllo dinamico su futuri dataset.
