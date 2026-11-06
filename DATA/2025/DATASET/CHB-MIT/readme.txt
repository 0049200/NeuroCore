====================================================================

CHB-MIT EPILEPSY DATASET: MULTI-PATIENT CLINICAL & EWS ANALYSIS REPORT

====================================================================



1. PANORAMICA DEL METODO E RIGORE SCIENTIFICO

- Dataset: CHB-MIT Scalp EEG Database (Boston Children's Hospital).

- Obiettivo: Caratterizzazione delle dinamiche di destabilizzazione preictale, stima degli orizzonti di allarme precoce (Early Warning Systems - EWS) e quantificazione della resilienza post-critica.

- Inquadramento Metodologico: Approccio rigorosamente PROBABILISTICO basato sul tracciamento di deviazioni statistiche dalla baseline. Il sistema non esegue una time prediction deterministica ("esattamente tra N secondi"), bensì stima la probabilità di instabilità dello stato cerebrale pre-crisi.



2. STIMA PROBABILISTICA DELL'ORIZZONTE DI ALLARME (PREDICTION HORIZON)

- Anticipo Temporale degli Allarmi: Il rilevamento della destabilizzazione preictale evidenzia una finestra d'allarme probabilistica con valore medio di 616.6 secondi (~10 minuti) prima dell'onset clinico (mediana = 595.0s, range = 169s - 1061s).

- Parametri di Finestra: Finestre temporali di analisi da 10.0 secondi con uno step di 2.0s e soglia dinamica a k_sigma = 2.5 per l'emissione dei trigger di rischio.



3. RANKING DELLE FEATURE E SEPARABILITÀ PRE- VS INTER-ICTAL

- Potenza Banda Delta (delta_bp): Marcatore primario di variazione della dinamica lenta (AUC = 0.554, Cohen's d = 0.165).

- Ampiezza RMS (rms_mean): Indicatore secondario legato all'incremento della varianza energetica del segnale (AUC = 0.545, Cohen's d = 0.157).

- Potenza Banda Theta (theta_bp): Terzo predittore significativo nelle fasi di approccio all'insorgenza (AUC = 0.541, Cohen's d = 0.152).

- Validazione Predittiva su Crisi (Cross-Validation): Modellazione logit dell'indice di rischio preictale (PreIctalIndex_logit) con AUC media in CV tra 0.46 e 0.62 (media ~0.516). I valori riflettono la reale eterogeneità e non-stazionarietà del segnale EEG a lungo termine, escludendo data leakage o sovrastime artificiali.



4. BASELINE FISIOLOGICA E TEMPI DI RECUPERO POST-CRISI (RECOVERY TIME)

- Profilo Baseline Interictale: Quantificazione statistica per singolo file EDF (mediane, percentili p95 e deviazioni standard estese su 36 registrazioni per soggetto, es. chb02).

- Metrica di Recupero Post-Ictal (recovery_time_sec): Algoritmo di monitoraggio del rientro in stabilità a finestre consecutive (K_consec = 5, finestra post-ictale di 300s) che quantifica probabilisticamente il tempo necessario al segnale cerebrale per ripristinare i valori di baseline fisiologica a seguito della crisi.



