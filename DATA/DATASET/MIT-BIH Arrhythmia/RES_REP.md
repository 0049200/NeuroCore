# NeuroCore™

## Research and Validation Report

### Computational Architecture, Asymptotic Operators and Cross-Domain Experimental Investigations

**Author:** Davide Luca Nicoletti  
**ORCID:** [0009-0002-2605-7729](https://orcid.org/0009-0002-2605-7729)  
**Software reference:** NeuroCore v1.5  
**Report date:** 4 November 2026  
**Research status:** Experimental — independent validation pending

---

# 1. Research Objective

NeuroCore is an experimental computational architecture developed to investigate the organization and evolution of heterogeneous dynamic systems.

The central research hypothesis concerns the possibility of identifying common structural or dynamic properties across systems whose physical, biological or informational implementations differ.

The current research investigates:

- Dynamic stability and deviations from reference states.
- Structural invariance under iterative transformations.
- State transitions and symmetry-breaking indicators.
- Temporal evolution and progressive degradation.
- Cross-dataset consistency.
- Potential generalization across different system representations.

The research is not restricted to biological electrophysiology or mechanical systems. These domains represent experimental environments for investigating the broader computational hypothesis.

# 2. Mathematical Operator

The current implementation employs a nonlinear iterative transformation:

$$
L(x)=x-\alpha\tanh(x-p)
$$

where:

- \(x\): input scalar.
- \(p\): reference pivot.
- \(\alpha\): transformation coefficient.
- \(p=0.55\): current experimental reference value.
- \(\alpha=0.1\): current transformation coefficient.

The iterative process is defined as:

$$
x_{n+1}=L(x_n)
$$

Equivalently:

$$
x_{n+1}=x_n-\alpha\tanh(x_n-p)
$$

The resulting value after \(N\) iterations is designated:

$$
\hat{c}_N=L^{(N)}(x_0)
$$

where:

- \(x_0\) is the initial input value.
- \(N\) is the number of iterations.
- \(L^{(N)}\) denotes the repeated application of the operator.

The current implementations use:

| Parameter | C++ | Python |
|---|---:|---:|
| Reference pivot \(p\) | 0.55 | 0.55 |
| Transformation coefficient \(\alpha\) | 0.1 | 0.1 |
| Iterations \(N\) | 30 | 50 |
| Deviation threshold \(\epsilon\) | 0.05 | 0.05 |

## 2.1 Fixed Point and Reference-State Distance

A fixed point \(x^\ast\) satisfies:

$$
L(x^\ast)=x^\ast
$$

For the current operator:

$$
x^\ast=p=0.55
$$

The distance from the reference pivot is calculated as:

$$
\Delta_N=\left|\hat{c}_N-p\right|
$$

The current experimental classification is:

$$
S(\hat{c}_N)=
\begin{cases}
\text{Homeostasis}, & \Delta_N\leq\epsilon\\
\text{Deviation}, & \Delta_N>\epsilon
\end{cases}
$$

where:

$$
\epsilon=0.05
$$

The original implementation uses the labels `Homeostasis` and `Ictal / Crisis`.

For cross-domain reporting, `Deviation` is preferable because the same numerical classification cannot automatically be interpreted as a clinical crisis across different physiological or mechanical systems.

# 3. C++ Embedded Implementation

The C++ implementation introduces a lightweight computational engine intended to explore portability into embedded and resource-constrained environments.

Its main components are:

- Nonlinear transformation.
- Iterative fixed-point calculation.
- Distance measurement from the reference pivot.
- Binary state classification.

## 3.1 Experimental Input

The experimental input segment is:

$$
X=\{0.577,\;0.736\}
$$

The initial segment mean is:

$$
x_0=\frac{1}{2}\sum_{i=1}^{2}x_i
$$

Therefore:

$$
x_0=\frac{0.577+0.736}{2}=0.6565
$$

The implementation applies 30 iterations:

$$
x_{n+1}=x_n-0.1\tanh(x_n-0.55)
$$

The resulting distance is:

$$
\Delta_{30}=|x_{30}-0.55|
$$

The classification is then determined by comparison with the threshold:

$$
S=
\begin{cases}
\text{Homeostasis}, & \Delta_{30}\leq0.05\\
\text{Deviation}, & \Delta_{30}>0.05
\end{cases}
$$

For the supplied input, the iterative result is approximately:

$$
x_{30}\approx0.554525
$$

and:

$$
\Delta_{30}\approx0.004525
$$

This falls within the current reference-state threshold.

## 3.2 Implementation Considerations

The current C++ implementation returns the reference pivot when the input segment is empty. This behavior should be replaced by explicit invalid-input handling in a research-grade implementation.

The `<utility>` header should also be explicitly included for `std::pair`.

# 4. Python Dataset-Level Implementation

The Python implementation introduces dataset-level processing through NumPy and Pandas.

Its processing sequence is:

1. Load a CSV dataset.
2. Retrieve the asymptotic invariant and system coherence.
3. Construct a two-variable input segment.
4. Apply the iterative transformation.
5. Calculate deviation from the reference pivot.
6. Assign a state classification.
7. Export the resulting observations as a Pandas DataFrame.

## 4.1 Expected Input Fields

| Field | Function |
|---|---|
| `source_file` | Source record identification |
| `asymptotic_invariant` | Previously calculated invariant |
| `system_coherence` | System coherence measure |

## 4.2 Output Fields

| Field | Function |
|---|---|
| `source_file` | Original record |
| `asymptotic_invariant_computed` | Transformed value |
| `distance` | Distance from reference pivot |
| `state` | Assigned classification |

The input vector for each observation is:

$$
X_i=
\left[
a_i,\;c_i
\right]
$$

where:

- \(a_i\) is the previously calculated asymptotic invariant.
- \(c_i\) is the system coherence measure.

The initial scalar supplied to the iterative operator is:

$$
x_{0,i}=\frac{a_i+c_i}{2}
$$

The resulting transformed value is:

$$
\hat{c}_{N,i}=L^{(N)}(x_{0,i})
$$

The corresponding distance is:

$$
\Delta_{N,i}=
\left|\hat{c}_{N,i}-p\right|
$$

The current script requires the input columns to exist and contain valid numerical values.

An additional validation layer is required for:

- Missing values.
- Empty segments.
- Non-finite observations.
- Inconsistent numerical ranges.
- Invalid or incomplete records.

The Python implementation should therefore be considered an experimental dataset-processing implementation rather than a validated production system.

# 5. Biological Signal Investigation — MIT-BIH

**Dataset:** MIT-BIH Arrhythmia Database  
**Source:** PhysioNet  
**Sampling frequency:** 360 Hz  
**Resolution:** 12-bit  
**Reported corpus:** 48 records  
**Reference implementation:** NeuroCore v1.5

## 5.1 Experimental Objective

The investigation explores whether the proposed reference-state metric can distinguish relatively stable signal configurations from observations exhibiting substantial numerical deviations.

The experimental configuration uses:

$$
p=0.55
$$

and:

$$
\epsilon=0.05
$$

## 5.2 Reported Observations

The following values were included in the preliminary analytical report.

| Record | Reported invariant | Distance | Original classification |
|---|---:|---:|---|
| 100 | 0.2025 | 0.3475 | Deviation |
| 101 | 0.1415 | 0.4085 | Deviation |
| 102 | 0.2642 | 0.2858 | Deviation |
| 103 | 0.1580 | 0.3920 | Deviation |
| 104 | 0.3329 | 0.2171 | Deviation |
| 107 | 0.5594 | 0.0094 | Homeostasis |
| 117 | 0.5482 | 0.0018 | Homeostasis |
| 217 | 0.5410 | 0.0090 | Homeostasis |
| 108 | 0.7003 | 0.1503 | Deviation |
| 109 | 0.4585 | 0.0915 | Deviation |

These values represent observations reported in the preliminary audit. They require reconciliation with the exact executable version, input data and processing outputs.

In particular, the reported values must be distinguished from the values generated by the current iterative operator. They should not be interpreted as verified outputs of the supplied Python implementation until the complete computation has been reproduced.

## 5.3 Interpretation

The preliminary analysis suggests that distance from the reference pivot may provide a numerical descriptor for differentiating signal configurations.

However, the correspondence between calculated values and actual physiological annotations must be independently established.

The current classifier is not a validated arrhythmia detector and does not establish diagnostic or prognostic performance.

# 6. Mechanical Systems Investigation — NASA C-MAPSS

**Dataset:** NASA C-MAPSS Turbofan Engine Degradation Simulation  
**Investigated subsets:** FD002 and FD003

## 6.1 Experimental Objective

The mechanical investigation explores the potential transferability of reference-state analysis from biological electrophysiological signals to multivariate degradation processes.

The dataset contains sensor observations collected across engine operating cycles, including progressive degradation and different operational conditions.

The proposed analytical objectives are:

- Identification of changes in system organization.
- Measurement of progressive deviations from reference configurations.
- Investigation of potential transition indicators.
- Evaluation of relationships between dynamic metrics and Remaining Useful Life (RUL).

## 6.2 Preliminary Reported Observations

The following values were reported in the initial experimental analysis.

| Dataset | Operating conditions | Reported reference value |
|---|---|---:|
| MIT-BIH | Cardiac electrophysiology | 0.55 ± 0.02 |
| FD002 | Multiple operating conditions and fault modes | 0.553 |
| FD003 | Single fault mode | 0.548 |

The preliminary report also proposed three interpretative regions:

| Region | Proposed interpretation |
|---|---|
| Above 0.55 | Nominal operating region |
| Around 0.55 | Reference-state region |
| Below 0.30 | Potential advanced degradation region |

These regions are preliminary hypotheses, not established universal thresholds.

## 6.3 Validation Requirements

The proposed relationship between the reference metric and mechanical degradation requires further testing through:

- Engine-level train/test separation.
- Operating-condition normalization.
- Sensor-level preprocessing.
- Cycle-by-cycle metric computation.
- Independent RUL estimation.
- Comparison against established predictive-maintenance baselines.
- Evaluation of false alarms and detection lead time.

The reported values alone do not establish predictive accuracy or the onset of irreversible mechanical damage.

# 7. Cross-Domain Research Hypothesis

The biological and mechanical investigations motivate a broader research question:

**Can a common computational representation identify comparable organizational changes across systems with different underlying physical mechanisms?**

The proposed research direction investigates whether structural or dynamic properties remain comparable after suitable normalization and representation.

Potential future domains include:

- Biological and physiological systems.
- Mechanical and engineering systems.
- Robotics and autonomous systems.
- Computational and informational systems.
- Semantic representations and relational structures.
- Other complex systems with measurable temporal or structural evolution.

The extension to semantic systems remains an open research direction and requires a dedicated representation of meaning, relations and semantic change.

# 8. Mathematical and Computational Limitations

The present implementation requires an important distinction between mathematical convergence and empirical invariance.

The current operator is:

$$
L(x)=x-0.1\tanh(x-0.55)
$$

Its first derivative is:

$$
L'(x)=1-0.1\operatorname{sech}^{2}(x-0.55)
$$

Since:

$$
0<\operatorname{sech}^{2}(z)\leq1
$$

for finite real \(z\), the derivative satisfies:

$$
0.9\leq L'(x)<1
$$

The operator therefore has a stable fixed point at:

$$
x^\ast=0.55
$$

For finite real initial values, the transformation moves the iterates toward this fixed point.

Consequently, convergence toward \(0.55\) is an intrinsic mathematical property of the selected transformation. It is not, by itself, evidence that the input data contain an independently discovered invariant.

## 8.1 Dependence on Iteration Count

The resulting distance depends on the number of iterations:

$$
\Delta_N=
\left|L^{(N)}(x_0)-p\right|
$$

Therefore:

$$
\Delta_{30}\neq\Delta_{50}
$$

in general.

The Python implementation applies 50 iterations, while the C++ implementation applies 30. Their outputs are not directly interchangeable without a controlled comparison.

## 8.2 Reconciliation of Preliminary Results

The preliminary MIT-BIH table contains values and classifications that must be traced to their exact processing stage.

The reported observations cannot be assumed to be outputs of the supplied Python implementation without reproducing the computation from the original inputs.

A reproducible audit should record:

- Original input values.
- Initial scalar \(x_0\).
- Transformation parameters.
- Iteration count \(N\).
- Final transformed value.
- Calculated distance.
- Assigned classification.
- Software version and execution environment.

This distinction is essential for determining whether observed differences originate from the dataset, preprocessing, operator configuration or implementation.

# 9. Required Validation Protocol

The next research stage should establish:

1. Reproducibility of identical results from identical input data.
2. Sensitivity to pivot and transformation parameters.
3. Comparison with alternative nonlinear transformations.
4. Comparison against randomized and shuffled baselines.
5. Independence from arbitrary normalization choices.
6. Generalization to previously unseen records and datasets.
7. Temporal evaluation of transition detection.
8. Quantification of false-positive and false-negative rates.
9. Comparison with independent reference methods.
10. Reproducibility across Python and C++ implementations.

For predictive applications, the evaluation should additionally include:

- ROC-AUC and precision-recall AUC.
- Detection horizon.
- False alarm rate.
- Sensitivity and specificity.
- Recovery time, where applicable.
- RUL prediction error for mechanical degradation.

All predictive evaluations should use appropriate data separation to prevent information leakage between training and testing observations.

# 10. Research Position

NeuroCore is currently an experimental computational research architecture.

Its central objective is to investigate whether common dynamic and structural properties can be operationalized across heterogeneous systems.

The current investigations provide a starting point for evaluating this hypothesis, but do not yet establish:

- Universal invariance.
- Clinical prediction.
- Mechanical failure prediction.
- Validated transition forecasting.
- Semantic generalization.

Independent implementation, reproducibility testing, controlled comparisons and cross-domain validation are necessary to establish the scientific scope of the architecture.

---

**Author:** Davide Luca Nicoletti  
**ORCID:** [0009-0002-2605-7729](https://orcid.org/0009-0002-2605-7729)  
**Project:** NeuroCore  
**Software reference:** v1.5  
**Research documentation:** Associated Zenodo DOI publications  
**Copyright:** © 2025 Davide Luca Nicoletti
