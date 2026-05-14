# Module 272: Tool compatibility audit for the transverse phase kernels

## 1. Precise theorem / claim being advanced

This module compares standard tools against the exact phase-kernel objects
extracted in Module 271.

Define:

```text
PhaseToolCompatAudit_272(s;D,R,eta,w).
```

The tools audited are:

```text
large sieve,
additive energy,
ordinary pair-BDH,
rectangle-BDH,
first-moment Hardy-Littlewood,
generic finite-complexity Hardy-Littlewood.
```

The conclusion is:

```text
No listed off-the-shelf tool currently proves PhaseIncidenceGate_271.
```

Several tools give useful diagnostics or possible conditional subroutes, but
none supplies the exact same-family, restricted-kernel, weighted residual
estimate needed for `TransIncBound_269`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a compatibility audit. It does not prove `PhaseIncidenceGate_271`,
`TransIncBound_269`, `ThresholdOnlyClosure_270`, `NarrowMinorArc_3^B`, or any
endpoint estimate.

## 3. Definitions and variables

Use the notation of Modules 269-271:

```text
f_s=nu_s-1
F_{d,s}(n)=f_s(n+d)conj(f_s(n))
beta_s(d,xi)=E_n F_{d,s}(n)e(-xi n)
I_trans_s(lambda)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Minor(R,eta),
        |beta_s(d,xi)|>=lambda,
        E_{d,s}(lambda)<=mu(lambda),
        N_{xi,s}(lambda)<=K(lambda) }.
```

Module 271 identified the relevant kernels:

```text
same-frequency pair:
  E_{n,m} F_{d1,s}(n)conj(F_{d2,s}(m))K_S(n-m),

same-shift pair:
  E_{n,m} F_{d,s}(n)conj(F_{d,s}(m))K_Xi(n,m),

rectangle:
  E_{n1,n2,n3,n4}
    F_{d1,s}(n1)conj(F_{d2,s}(n2))
    conj(F_{d1,s}(n3))F_{d2,s}(n4)
    K(n1,n2,n3,n4).
```

A tool can serve as a direct input to `PhaseIncidenceGate_271` only if it
meets all required fit tests:

```text
R1 same selector/model class s;
R2 restricted minor-arc or large-spectrum frequency kernel, not full delta;
R3 weighted residual coefficients, not only incidence counts;
R4 dyadic shift range D<|d|<=2D;
R5 W-residue, prime-power, cutoff, and truncation compatibility;
R6 lambda-summed output strong enough for TransIncBound_269;
R7 no assumption of NarrowMinorArc_3^B, ResCube_3^sharp, CPC_3^sharp,
   RBDH_pair_short, AU^3, or selector transfer;
R8 uniformity over the declared parameter family.
```

## 4. Assumptions

This audit assumes only:

- the exact Module 271 expansions;
- the Module 270 threshold-removal notation;
- the fixed selector/model class `s`.

It does not assume:

```text
PhaseIncidenceGate_271,
TransIncBound_269,
ThresholdOnlyClosure_270,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
selector transfer,
RBDH_pair_short,
CPC_3^sharp,
AU^3,
ResCube_3^sharp,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Large sieve

A large-sieve input can control averages of linear exponential sums over
well-spaced frequencies or fixed frequency sets. In this setting it can
diagnose quantities like:

```text
sum_{xi in S} |sum_d c_d beta_s(d,xi)|^2
```

for fixed coefficients and a fixed set `S`, provided the model supplies the
needed spacing and norm estimates.

This does not directly match `PhaseIncidenceGate_271` because:

- `S` may be a data-dependent large-spectrum subset;
- the target involves weighted same-frequency pairs and rectangles, not only
  a linear `L^2` norm;
- the minor-arc kernel `K_S` is not the full diagonal kernel;
- the output must be lambda-summed and same-family in `s`.

Verdict:

```text
LargeSieveFit_272: diagnostic only.
```

It may help formulate a future `Gamma_trans`, but it is not presently a proof
of the transverse phase gate.

### B. Additive energy

Additive-energy methods can count configurations such as bipartite rectangles
or repeated differences. For the transverse graph, the relevant unweighted
rectangle count is:

```text
#{(d1,d2,xi1,xi2) :
    (d1,xi1),(d1,xi2),(d2,xi1),(d2,xi2)
      in I_trans_s(lambda)}.
```

But Module 271's rectangle object is weighted:

```text
R_s(d1,d2;xi1,xi2)
  =
  beta_s(d1,xi1)conj(beta_s(d2,xi1))
  conj(beta_s(d1,xi2))beta_s(d2,xi2),
```

and after expansion it contains restricted phase kernels. Counting rectangles
alone does not estimate this signed or complex weighted residual correlation.

Verdict:

```text
AddEnergyFit_272: structural count, not an analytic bound.
```

It is useful for locating degeneracies, but not enough for
`PhaseIncidenceGate_271`.

### C. Ordinary pair-BDH

Ordinary pair-BDH type information controls averaged two-point distribution
errors. It is naturally closer to full-frequency or interval variance objects
than to data-dependent minor-arc kernels.

The Module 271 same-frequency pair requires control of:

```text
E_{n,m}
  F_{d1,s}(n)conj(F_{d2,s}(m))K_S(n-m)
```

where `S` may be a restricted minor-arc or large-spectrum fiber. Pair-BDH does
not by itself supply:

- the restricted kernel `K_S`;
- the residual weights `F_{d,s}`;
- the lambda-level large-spectrum selection;
- the selector/model transfer rows.

Verdict:

```text
PairBDHFit_272: direct shortcut blocked.
```

It may become a side input only after an exact restricted-kernel conversion
theorem is supplied.

### D. Rectangle-BDH

Rectangle-BDH is the closest listed family to the Module 271 rectangle object
because it is designed for four-point or rectangular fluctuations. However,
the needed row is not a generic rectangle statement. It would have to control:

```text
F_{d1,s}(n1)conj(F_{d2,s}(n2))
conj(F_{d1,s}(n3))F_{d2,s}(n4)
```

with:

```text
restricted minor-arc kernels,
large-spectrum-selected frequencies,
dyadic short shifts,
W-residue restrictions,
prime-power and cutoff side rows,
and the declared selector/model class.
```

Verdict:

```text
RectangleBDHFit_272: potentially relevant only as a new exact restricted
weighted rectangle theorem.
```

As currently recorded in the ledger, it is not an available proof of
`PhaseIncidenceGate_271`.

### E. First-moment Hardy-Littlewood

First-moment Hardy-Littlewood information supplies mean local densities for
fixed patterns. The transverse phase gate is a second- and fourth-order
large-spectrum problem with residual weights and data-dependent kernels.

First moments do not control:

- variance or fourth moments;
- large-spectrum multiplicity;
- weighted rectangles;
- restricted minor-arc kernels;
- selector transfer.

Verdict:

```text
FirstMomentHLFit_272: direct shortcut blocked.
```

It remains a local-model ingredient elsewhere, not a transverse incidence
estimate.

### F. Generic finite-complexity Hardy-Littlewood

Generic finite-complexity HL can be useful for fixed systems of linear forms
inside a declared model. It is not automatically uniform over:

```text
data-dependent large-spectrum subsets,
minor-arc frequency kernels,
lambda-level threshold families,
W-residue and cutoff choices,
dyadic shift ranges,
or actual sharp moving selectors.
```

Verdict:

```text
FiniteComplexityHLFit_272: conditional local/model input only.
```

It may estimate fixed faces after the frequency kernels have been reduced to
fixed linear systems. Module 271 shows that this reduction is exactly what is
missing for restricted minor-arc kernels.

### G. Compatibility matrix

```text
Tool                         Direct fit?   Main mismatch
---------------------------------------------------------------
large sieve                  no            linear/fixed-set L2, not weighted
                                           data-dependent rectangles
additive energy              no            counts rectangles, does not bound
                                           residual phase weights
ordinary pair-BDH            no            pair variance lacks restricted
                                           large-spectrum kernels
rectangle-BDH                conditional   would need a new exact restricted
                                           weighted rectangle theorem
first-moment HL              no            means only, no spectrum/moments
finite-complexity HL         conditional   fixed model systems, not automatic
                                           uniform data-dependent kernels
```

Therefore:

```text
AvailableToolClosure_272 is not established.
```

The next stage should formulate a candidate gate that states exactly which
combination of restricted-kernel, weighted-rectangle, and same-family
uniformity estimates would be enough.

## 6. Edge cases

- A full-frequency identity is not a minor-arc estimate.
- A fixed frequency set is not the same as a data-dependent large-spectrum
  subset.
- Unweighted graph energy is not weighted residual cancellation.
- Pair estimates do not automatically control rectangles.
- Rectangle estimates outside the exact selector/model class do not transfer
  to the active sharp object.
- First-moment local models do not control fourth moments.
- Generic finite-complexity estimates must specify the family, complexity,
  W-limit order, cutoff, and selector class before they can be used.
- Any tool that assumes `TransIncBound_269` or `NarrowMinorArc_3^B` is
  circular in this branch.

## 7. Where it fits in the project map

```text
Module 271
  -> exact phase-kernel objects

Module 272
  -> compatibility audit for standard tools
```

The next useful step is:

```text
Module 273:
  formulate a non-tautological transverse incidence gate with a candidate
  Gamma_trans(lambda;D,R,eta,w) and explicit non-endpoint criteria.
```

## 8. What remains open

This module does not prove:

- `AvailableToolClosure_272`;
- `PhaseIncidenceGate_271`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- transverse energy smallness;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- selector transfer to the actual sharp moving selector;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- `ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`,
  or `ProjectedModelNeutrality_3^major`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite large sieve as a weighted rectangle estimate unless the exact
  restricted-kernel conversion is proved.
- Do not cite additive energy as cancellation.
- Do not use ordinary pair-BDH as a transverse phase-kernel theorem.
- Do not use rectangle-BDH unless it is the exact restricted weighted version
  in the same selector/model family.
- Do not use first-moment HL to control variance or fourth moments.
- Do not use generic finite-complexity HL without fixed-system and uniformity
  rows matching the active family.
- Do not treat `AvailableToolClosure_272` as proved.
