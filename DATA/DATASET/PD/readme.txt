feat(parkinson): 

- Aggiunta dell'estrazione feature di dinamica di stato (stabilità, entropia, z_combo, resilienza) 
  su 85 sessioni EEG (56 soggetti unici, da sub-001 a sub-056).
- Clustering non supervisionato con identificazione di due fenotipi distinti:
  * Cluster 0 (n=66): Stabilità = 0.51 ± 0.05 | Entropia = 1.62 ± 0.10
  * Cluster 1 (n=19): Stabilità = 0.63 ± 0.04 | Entropia = 1.36 ± 0.08
- Rilevata separazione netta tra gruppi con effect size elevati (Cohen's d: Resilienza -3.05, Stabilità -2.75, Entropia +2.62).
- Tracciamento di 15 soggetti borderline per l'analisi longitudinale delle transizioni.
- Integrazione completa dei metadati clinici (PD-Table1/Table2: MoCA, BDI, UPDRS, velocità cammino) 
