# EEG Sample — Statistical Summary

## 1. Sample Overview

| Parameter | Value |
|---|---:|
| Unique subjects analyzed | **125** |
| Total EEG segments (runs / analyzed traces) | **2,387** |

## 2. Statistical Distribution of the Asymptotic Invariant

The following statistics describe the distribution of the `asymptotic_invariant` variable across the analyzed EEG segments.

| Statistical measure | Value |
|---|---:|
| Mean | `0.4673` |
| Median | `0.4558` |
| Standard deviation | `0.2020` |
| Interquartile range (IQR) | `0.2631` |
| First quartile (Q1) | `0.3185` |
| Third quartile (Q3) | `0.5816` |

## 3. Proximity Analysis to the Reference Value

The analysis evaluates the distribution of observations around the experimental reference value:

\[
p = 0.55
\]

Two numerical intervals were considered.

### 3.1 Critical Tolerance Interval

\[
0.53 \leq x \leq 0.57
\]

- Segments within the interval: **183**
- Percentage of the total sample: **7.67%**

### 3.2 Extended Transition Interval

\[
0.50 \leq x \leq 0.60
\]

- Segments within the interval: **432**
- Percentage of the total sample: **18.10%**

## 4. Distributional Observations

The third quartile is:

\[
Q_3 = 0.5816
\]

This indicates that 75% of the analyzed observations are at or below `0.5816`, while the remaining 25% are above this value.

The observed distribution provides an initial quantitative description of the relationship between the analyzed EEG segments and the experimental reference value of `0.55`.

However, proximity to this reference value does not independently establish physiological stability, an epileptic transition, or a predictive relationship with seizure onset.

## 5. Research Interpretation and Validation Status

These statistics constitute a preliminary descriptive analysis of 2,387 EEG segments from 125 unique subjects.

Further investigation is required to determine:

- Whether the observed distribution is reproducible across subjects.
- Whether proximity to the reference value is associated with independently annotated physiological events.
- Whether temporal changes in the metric precede, coincide with, or follow relevant events.
- Whether the observed patterns remain consistent across independent datasets.
- Whether the reference value retains statistical relevance under alternative preprocessing and normalization procedures.

**Research status:** Preliminary statistical observations — independent validation pending.

**Project:** NeuroCore  
**Software reference:** v1.5  
**Metric:** `asymptotic_invariant`  
**Experimental reference value:** `0.55`
