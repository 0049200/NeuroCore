
# NeuroCore™ — Phase 2/7: Postsynaptic Potentials

> **Conceptual Architecture | Research Draft | Implementation Pending**

## 1. Objective

Investigate how chemical synaptic signals are converted into postsynaptic electrical responses.

This phase focuses on receptor activation, ion flow, membrane potential changes, and the formation of excitatory and inhibitory postsynaptic potentials (EPSPs and IPSPs).

**Long-term vision:** Explore functional principles of signal reception and electrical state regulation for computational and robotic architectures.

## 2. Biological Reference

The proposed architecture examines:

- **Reception:** Neurotransmitter binding and receptor activation.
- **Transduction:** Ligand-gated ion channels and ionic conductance.
- **Excitation:** Excitatory postsynaptic potentials (EPSPs).
- **Inhibition:** Inhibitory postsynaptic potentials (IPSPs).
- **Regulation:** Membrane properties, receptor kinetics, and synaptic modulation.
- **Recovery:** Neurotransmitter clearance and receptor deactivation.

### Functional Boundaries

| Interface | Description |
|---|---|
| Input | Synaptic neurotransmitter signals |
| Output | Local postsynaptic membrane potential changes |
| Internal state | Membrane voltage, conductance, receptor activation |
| Next phase | Spatial and Temporal Integration |

## 3. Mathematical Reference

A simplified conductance-based membrane model:

$$
C_m \frac{dV_m}{dt}
=
-g_L(V_m-E_L)
-
\sum_i g_i(t)(V_m-E_i)
+
I_{\mathrm{ext}}(t)
$$

Where:

| Symbol | Definition |
|---|---|
| $C_m$ | Membrane capacitance |
| $V_m$ | Membrane potential |
| $g_L$ | Leak conductance |
| $E_L$ | Leak reversal potential |
| $g_i(t)$ | Time-dependent synaptic conductance |
| $E_i$ | Synaptic reversal potential |
| $I_{\mathrm{ext}}$ | External current |

The postsynaptic voltage response can be represented as:

$$
\Delta V_m(t)=V_m(t)-V_{\mathrm{rest}}
$$

These equations provide a biological modeling reference, not an implemented NeuroCore algorithm.

## 4. Functional Architecture

Each candidate group follows the proposed NeuroCore interface contract:

$$
G_i =
(X_i,U_i,Y_i,\Theta_i,\mathcal{C}_i,\mathcal{V}_i)
$$

The objective is to identify which functional properties can be preserved through software, electronic, neuromorphic, or biohybrid implementations.

Biological equivalence is not assumed.

## 5. Development Roadmap

1. Define receptor and membrane reference models.
2. Formalize electrical states, inputs, and outputs.
3. Model excitatory and inhibitory responses.
4. Evaluate temporal dynamics and recovery.
5. Compare simulations against established baselines.
6. Establish interfaces with Phase 3.

## 6. Integration with NeuroCore

Phase 2 connects synaptic transmission to spatial and temporal integration.

The proposed functional sequence is:

$$
\text{Chemical Input}
\rightarrow
\text{Receptor Activation}
\rightarrow
\text{Ionic Response}
\rightarrow
\Delta V_m(t)
$$

NeuroCore's mathematical operators may subsequently be investigated as tools for characterizing state evolution, stability, and regulation.

Their biological correspondence remains unvalidated.

## 7. Research Status

**Status: Conceptual specification — implementation and validation pending.**

No claim of complete biological replication or functional equivalence is made.

Future validation requires reproducible models, quantitative baselines, sensitivity analysis, and independent verification.

---

[← Seven-Phase Architecture Index](../README.md)
