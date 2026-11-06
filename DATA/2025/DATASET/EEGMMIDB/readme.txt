==================================================================
EEG MOTOR MOVEMENT/IMAGERY DATASET (EEGMMIDB)
==================================================================

1. ARCHITETTURA E COORTE DATI
- Coorte completa: 109 soggetti unici (da S001 a S109) per un totale di 1.526 file EDF.
- Configurazione segnale: Campionamento a 160 Hz, riduzione della dimensionalità tramite PCA (top 10 canali a varianza massima).
- Copertura varianza: La selezione PCA a 10 canali mantiene l'85.5% ± 8.0% della varianza totale del segnale.

2. METRICHE CHIAVE DI DINAMICA DI STATO (HMM & K-MEANS)
- Entropia di Stato (HMM): 1.38 ± 0.38
  * Evidenzia la complessità di commutazione tra le reti corticali durante i compiti di movimento/immaginazione motoria.
- Probabilità di Transizione (HMM): 69.8% ± 28.4%
  * Elevata flessibilità e dinamicità corticale durante i task motori attivi.
- Frequenza di Autotransizione / Stabilità: 22.3% ± 14.2%

3. PARAMETRI SPETTRALI & REGIMI MOTORI (V2.1)
- Rapporti spettrali di riferimento: Delta/Alpha (R_delta_alpha ≈ 14.25) e (Delta+Theta)/Alpha (R_deltatheta_alpha ≈ 16.26).
- Profilatura stabilità funzionale: Classificazione dei run motori per singolo soggetto (es. S001, 12 file EDF, stabilità media 0.0097) per distinguere regimi di esecuzione rigidi vs flessibili.
