===============================================================================

                       NEUROCORE fNIRS METRICS SUMMARY

                  Dataset: Hypoalgesia_ds006902 (Pain Task)

===============================================================================



1. PANORAMICA GENERALE ED ELABORAZIONE PIPELINE

-------------------------------------------------------------------------------

* Soggetti Elaborati: 10 validi (sub-VP01, VP02, VP03, VP05, VP06, VP07, VP08, 

  VP09, VP11, VP13) su 22 file SNIRF totali identificati nella scansione ricorsiva.

* File Scartati: Rimossi automaticamente i file nascosti di sistema macOS (._*) 

  che causavano errori di firma HDF5.

* Granularità Dataset: 1.120 righe totali (~112 canali optodici per soggetto).

* Parametri Elaborati: AUC (Area Under the Curve), Resilience Index, 

  Transitions (Conteggio transizioni di stato stocastiche).

* Filtraggio Segnale: Filtro Butterworth passa-banda di 2° ordine (0.01 - 0.2 Hz) 

  per isolare le fluttuazioni emodinamiche ed eliminare rumore fisiologico e drift.





2. RIGORE METODOLOGICO: VALIDAZIONE E CORREZIONE DELL'AUC

-------------------------------------------------------------------------------

NOTA CRITICA SULL'AGGREGAZIONE DELL'AUC:

La media aritmetica semplice dell'AUC tra canali o per soggetto NON è 

neurofisiologicamente valida. I segnali fNIRS presentano sia canali in 

attivazione/iperemia (AUC > 0) sia canali in washout/deattivazione (AUC < 0). 

La media semplice provoca l'elisione algebrica (cancellazione dei valori 

opposti), restituendo medie vicine allo zero che mascherano la reale attività cerebrale.



Per un'analisi rigorosa e autentica dell'AUC si utilizzano 3 metriche standard:

1. Reattività Assoluta (|AUC|): Media dei valori assoluti dell'AUC sui canali 

   |AUC_i|, misurando l'energia emodinamica complessiva indipendentemente dal segno.

2. Bilanciamento Polarità: Rapporto tra Canali Attivi (AUC > 0) e Deattivi (AUC < 0).

3. Peak Channels: Identificazione dei canali con la massima risposta locale (+/-).





3. PROFILI EMODINAMICI E REATTIVITÀ PER SOGGETTO

-------------------------------------------------------------------------------

* sub-VP09 (Profilo Iper-Reattivo Globale):

  - Reattività Assoluta Media (|AUC|): 0.245 (la più alta della coorte).

  - Sbilanciamento: 84% dei canali presenta AUC > 0 (attivazione diffusa).

  - Canale Peak: S8_D15 (AUC max = +0.892).



* sub-VP01 (Profilo a Doppia Polarità / Reattività Locale):

  - Media aritmetica semplice vicina a zero, ma Reattività Assoluta (|AUC|) 

    elevata (0.182).

  - Presenza concomitante di canali ad alta attivazione (S2_D4: AUC = +0.612) 

    e canali a forte washout/deattivazione (S11_D18: AUC = -0.584).



* sub-VP13 / sub-VP03 (Risposta Emodinamica Contenuta):

  - Reattività Assoluta Media (|AUC|): 0.041.

  - Risposta attenuata distribuita omogeneamente sui canali.





4. CORRELAZIONI INCROCIATE E DINAMICA DEL SEGNALE

-------------------------------------------------------------------------------

A. CORRELAZIONE RESILIENZA vs TRANSIZIONI (r ≈ -0.58)

   Forte correlazione inversamente proporzionale. I canali ad alta instabilità 

   dinamica (flickering/cambi di stato stocastici) mostrano un crollo rigido 

   dell'Indice di Resilienza. Ciò consente di separare nettamente canali 

   "stabili/rigidi" da canali "dinamici/reattivi".



B. CORRELAZIONE AMPIEZZA EMODINAMICA vs INSTABILITÀ (|AUC| vs Transitions, r ≈ 0.39)

   L'ampiezza assoluta della risposta emodinamica correla positivamente con 

   il numero di transizioni. I canali che registrano le variazioni 

   emodinamiche più elevate sono anche quelli soggetti a maggiore variabilità 

   stocastica durante lo stimolo doloroso.





5. HOTSPOT SPAZIALI E CANALI DI RIFERIMENTO (BASELINE)

-------------------------------------------------------------------------------

* Hotspot di Instabilità Spaziale (Canali Critici):

  Analizzando la media tra tutti i soggetti, emergono coppie optodiche 

  sistematicamente instabili e reattive allo stimolo doloroso:

  - Canale S9_D19 (850 nm): Transizioni medie ≈ 234.6 | |AUC| ≈ 0.45.

  - Canale S16_D23 (850 nm): Transizioni medie ≈ 224.4.

  Questi canali rappresentano regioni anatomiche a elevata dinamicità neurale.



* Canali di Riferimento Stabili (Controllo Interno):

  Coppie optodiche che mantengono transizioni prossime a zero e resilienza elevata:

  - Canale S5_D7 (760 nm e 850 nm) e S9_D9: Transizioni medie ≈ 2.0, 

    Resilienza ≈ 6500, |AUC| ≈ 0.01.

  Fungono da baseline di controllo spaziale per verificare l'assenza di drift.





6. QUALITÀ DEL SEGNALE ED ESCLUSIONE ARTEFATTI

-------------------------------------------------------------------------------

* Saturazione Optodi (sub-VP05):

  In sub-VP05, 14 canali raggiungono il limite massimo di resilienza (10004.5) 

  con 1 sola transizione (es. S1_D12, S3_D1, S6_D8). 

  Indicativo di segnale piatto o disconnessione optode-scalpo. I canali vanno 

  esclusi dalle analisi di gruppo per evitare distorsioni.





7. PROSSIMI PASSI 

-------------------------------------------------------------------------------

1. Mappatura ROI (Region of Interest): Raggruppare i canali optodici in macro-aree 

   anatomiche (es. Corteccia Somatosensoriale Primaria S1, Corteccia Prefrontale PFC).

2. Data Cleaning: Esclusione formale dei 14 canali saturi del soggetto sub-VP05.

3. Correlazione Clinica: Incrociare la Reattività Assoluta (|AUC|) con i punteggi 

   di percezione del dolore (VAS/NPRS) se disponibili nei metadati.

===============================================================================
