# Module 368: Pair-residual Fourier energy audit

## 1. Target claim

Chosen attack mode:

```text
E. Residual obstruction route.
```

Best-module selection:

```text
The best current module is PairResidualFourierEnergyAudit_368(P_minor^0).
```

Reason:

```text
Module 367 paused the pair-model coefficient branch as the primary attack.
The remaining active pair-residual obstruction is the same-family Fourier
energy E_a |P_nu^0(a)-kappa_model^0(a)|^2 from Module 361. This object feeds
both the square pair-residual row and the mixed row once a model coefficient
convention is fixed.
```

Define:

```text
PairResidualFourierEnergyAudit_368(P_minor^0).
```

Verdict:

```text
PairResidualFourierEnergyAudit_368(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualParsevalIdentity_368:
  PROVEN.

PairResidualRectangleEnergyExpansion_368:
  PROVEN.

MeanCalibrationZeroModeOnly_368:
  PROVEN.

FirstMomentPairHLToEnergy_368:
  FALSE / BLOCKED.

OrdinaryPairBDHShortcut_368:
  FALSE / BLOCKED.

SameFamilyPairBDHVarianceTarget_368:
  OPEN.

PairResidualFourierEnergyTarget_361:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful outcome is a precise classification: the pair residual energy is a
same-family variance theorem, not a consequence of first-moment pair
calibration. If "pair-BDH" means exactly this variance with the same
W-residue, model convention, diagonal rule, cyclic range, and limit order,
then it is the target rather than a proved input.

## 2. Why this would advance the main theorem

Module 361 reduced the pair-residual large-value row to:

```text
D^(-1)K_UK_V
  E_a |P_nu^0(a)-kappa_model^0(a)|^2
  =
  o_W(1),
```

plus the mixed model-coefficient criterion. Modules 362-367 attacked the
model coefficient side. They did not prove pair-residual energy.

If the energy target were proved in the same model convention, then:

```text
A_star,|E_+^0|^2(m_{U,V})
```

would be controlled by Module 361's Parseval bound, and the mixed row would
combine this energy with the model-coefficient result from Modules 363-367.

This module shows exactly what is still missing: a same-family pair variance
input. It is not supplied by zero-mode pair Hardy-Littlewood and it is not
supplied by naming an ordinary pair-BDH theorem unless that theorem matches
the exact object below.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ.
```

Use:

```text
e_N(t)=exp(2 pi i t/N),

widehat{F}(xi)=E_{a in G_N}F(a)e_N(-xi a),
F_+(xi)=E_{a in G_N}F(a)e_N(xi a).
```

The physical pair correlation is:

```text
P_nu^0(a)
  =
  E_{r in G_N} nu_0(r)nu_0(r+a).
```

Let:

```text
kappa_model^0(a)
```

denote the exact pair model used in the branch. It must include the
diagonal/off-diagonal convention from Modules 363-367. The residual is:

```text
E_pair,model^0(a)
  =
  P_nu^0(a)-kappa_model^0(a).
```

Its transform is:

```text
E_{model,+}^0(xi)
  =
  E_{a in G_N}E_pair,model^0(a)e_N(xi a).
```

The target energy is:

```text
Energy_pair^0(model)
  =
  E_{a in G_N}|E_pair,model^0(a)|^2.
```

For the rectangle expansion use the Module 351 four-point model:

```text
Theta_w^4(a,b;q)
  =
  prod_{p>w}
    (1-1/p)^(-4)
    (1-#({0,a,q,q+b} mod p)/p),

R_w^0(a,b)
  =
  E_{q in G_N} Theta_w^4(a,b;q).
```

The diagonal rectangle model is:

```text
R_diag^0(a)=R_w^0(a,a).
```

## 4. Assumptions

This module assumes:

```text
Modules 351, 361, and 362-367,
finite cyclic Fourier algebra,
and the active status ledger.
```

It does not assume:

```text
PairResidualFourierEnergyTarget_361,
SameFamilyPairBDHVarianceTarget_368,
PairResidualLargeValueTarget_359,
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
PairModelMinorTopMassTarget_361 in full P_minor^0,
PairMixedDiagonalAbsorptionCriterion_363,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
actual sharp moving-selector transfer,
full-gap transfer,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

Forbidden assumptions:

```text
zero-mode pair calibration controls the nonzero pair spectrum,
first-moment Hardy-Littlewood implies pair variance,
ordinary pair-BDH with a different model/range/convention implies this row,
the model diagonal convention can change without changing the residual.
```

## 5. Proof / disproof / reduction

### A. Parseval identity for the pair residual

By normalized Parseval on `G_N`:

```text
Energy_pair^0(model)
  =
  E_a |E_pair,model^0(a)|^2
  =
  sum_{xi in G_N} |E_{model,+}^0(xi)|^2.
```

Separating the zero mode:

```text
Energy_pair^0(model)
  =
  |E_a E_pair,model^0(a)|^2
  +
  sum_{xi != 0} |E_{model,+}^0(xi)|^2.
```

Classification:

```text
PairResidualParsevalIdentity_368:
  PROVEN.
```

This proves that first-moment pair calibration only addresses the zero mode.
It does not estimate the nonzero Fourier energy.

### B. Rectangle expansion of the energy

For any declared model `kappa_model^0` and any auxiliary function
`R_diag^0(a)`, the identity:

```text
|P_nu^0(a)-kappa_model^0(a)|^2
  =
  (P_nu^0(a)^2-R_diag^0(a))
  - 2 kappa_model^0(a)(P_nu^0(a)-kappa_model^0(a))
  + (R_diag^0(a)-kappa_model^0(a)^2)
```

holds pointwise, since the right side expands to:

```text
P_nu^0(a)^2 - 2kappa_model^0(a)P_nu^0(a)
  + kappa_model^0(a)^2.
```

With the Module 351 rectangle model:

```text
R_diag^0(a)=R_w^0(a,a),
```

averaging gives:

```text
Energy_pair^0(model)
  =
  E_a(P_nu^0(a)^2-R_w^0(a,a))
  -2 E_a kappa_model^0(a)(P_nu^0(a)-kappa_model^0(a))
  +E_a(R_w^0(a,a)-kappa_model^0(a)^2).
```

Also:

```text
E_a P_nu^0(a)^2
  =
  E_{a,r,s}
    nu_0(r)nu_0(r+a)nu_0(s)nu_0(s+a).
```

Writing `q=s-r` turns this into the diagonal rectangle average:

```text
E_{a,r,q}
  nu_0(r)nu_0(r+a)nu_0(r+q)nu_0(r+q+a).
```

Classification:

```text
PairResidualRectangleEnergyExpansion_368:
  PROVEN.
```

This expansion shows that the energy row is a rectangle/variance row with a
weighted pair-residual cross term. It is not a first-moment pair row.

### C. First moment controls only the zero mode

The pair first moment has the shape:

```text
E_a(P_nu^0(a)-kappa_model^0(a)).
```

This is exactly:

```text
E_{model,+}^0(0).
```

By part A, the target energy also contains:

```text
sum_{xi != 0} |E_{model,+}^0(xi)|^2.
```

Finite counterexample to implication:

```text
F(a)=e_N(a).
```

Then:

```text
E_a F(a)=0,
```

but:

```text
E_a |F(a)|^2=1.
```

Thus zero-mode cancellation does not imply energy cancellation, even as a
finite Fourier statement.

Classification:

```text
MeanCalibrationZeroModeOnly_368:
  PROVEN.

FirstMomentPairHLToEnergy_368:
  FALSE / BLOCKED.
```

This is not a claim that the prime residual equals `e_N(a)`. It is a proof
that the logical implication from first moment to variance is invalid without
additional distribution input.

### D. Ordinary pair-BDH is either the target or insufficient

The exact same-family variance row needed by Module 361 is:

```text
SameFamilyPairBDHVarianceTarget_368:
  D^(-1)K_UK_V
  E_a |P_nu^0(a)-kappa_model^0(a)|^2
  =
  o_W(1),
```

with:

```text
same W-residue b,
same cyclic group G_N,
same diagonal/off-diagonal model convention,
same fixed-w then N->infty order,
same threshold schedules K_U,K_V,m_{U,V},
same dyadic family,
and same selector/model class P_minor^0.
```

If a theorem called "pair-BDH" proves exactly this statement, then it is not
an external shortcut; it is the missing target. If it proves a different
average, a different model, an unweighted shift range, or a zero-mode
calibration, it does not imply the needed row.

Classification:

```text
OrdinaryPairBDHShortcut_368:
  FALSE / BLOCKED.

SameFamilyPairBDHVarianceTarget_368:
  OPEN.
```

### E. Current closure verdict

The current ledger has:

```text
finite Fourier reductions from Module 361,
conditional model coefficient control from Modules 362-367,
and exact energy identities from this module.
```

It does not have:

```text
SameFamilyPairBDHVarianceTarget_368.
```

Therefore:

```text
PairResidualFourierEnergyTarget_361:
  OPEN.
```

The best next smaller target is to isolate the exact off-diagonal
shifted-prime covariance object inside the energy expansion.

## 6. Edge cases

### Model convention changes

If `kappa_model^0` changes by removing or retaining a diagonal atom, then
`E_pair,model^0` changes. The energy target must be restated in the same
convention as the mixed-row model coefficient.

### Zero shift

If the pair diagonal `a=0` is retained, `P_nu^0(0)` and the model diagonal
must be routed consistently. Removing `a=0` is not the same as proving it is
negligible.

### Zero frequency

First-moment pair estimates only control `xi=0`. The active large-value rows
depend on nonzero minor frequencies, and the energy target sums all
frequencies.

### Rectangle model diagonal

The rectangle expansion uses `R_w^0(a,a)`, not `kappa_model^0(a)^2`.
Replacing one by the other is exactly a model-defect row and is not free.

### Threshold scaling

Even if unweighted energy is small, Module 361 requires the scaled quantity:

```text
D^(-1)K_UK_V Energy_pair^0(model)
```

to be `o_W(1)`. The threshold schedules are part of the same-family target.

## 7. Project-map location

```text
PairResidualLargeValueStress_361
  -> PairModelMinorTopMassVerdict_367
  -> PairResidualFourierEnergyAudit_368
  -> PairResidualCovarianceIsolation_369.
```

This is the correct attack after the pair-model verdict. It identifies the
residual energy as a same-family variance theorem rather than another
deterministic model-coefficient problem.

## 8. What remains open

Still open:

```text
PairResidualCovarianceIsolation_369(P_minor^0),
SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
PairMixedDiagonalAbsorptionCriterion_363,
full P_minor^0 pair-model minor top-mass without PolyR_rho,
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as an estimate,
NoTwistColumnProfileCorrelation_356(P_minor^0),
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
full-gap transfer,
the all-alpha theorem,
and the original selected-average problem.
```

The current cadence after this module is:

```text
Latest completed module: 368
Post-Reflective_1 solving count: 187
Long-term-plan count: 181

181 is not divisible by 9, so no plan update is due in this module.
181 is not divisible by 15, so no plan challenge is due in this module.
The next reflective log is expected around Module 381.
```

## 9. Red-team audit

Selector check:

```text
All statements remain inside P_minor^0. No actual sharp moving-selector
statement is proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, dyadic tail, or empty-interval statement is used.
```

Local-factor check:

```text
The pair model convention is kept visible, and the rectangle diagonal model
is not replaced by kappa_model^0(a)^2 for free.
```

Limit-order check:

```text
All identities are finite cyclic identities. No N/w/R/eta limit is exchanged.
```

Uniformity check:

```text
The exact same-family variance target is named but not proved.
```

Endpoint-circularity check:

```text
The proof does not assume SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361, PhaseKernelBound_273^0,
NarrowMinorArc_3^B, ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short, or AU^3.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
PairResidualFourierEnergyAudit_368(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualParsevalIdentity_368:
  PROVEN.

PairResidualRectangleEnergyExpansion_368:
  PROVEN.

MeanCalibrationZeroModeOnly_368:
  PROVEN.

FirstMomentPairHLToEnergy_368:
  FALSE / BLOCKED.

OrdinaryPairBDHShortcut_368:
  FALSE / BLOCKED.

SameFamilyPairBDHVarianceTarget_368:
  OPEN.

PairResidualFourierEnergyTarget_361:
  OPEN.
```

Do not cite this module as proving pair-residual smallness. It proves exact
finite identities and classifies the missing input as a same-family pair
variance theorem.

## Red flags / forbidden upgrades

- Do not treat first-moment pair Hardy-Littlewood as pair-residual energy.
- Do not cite ordinary pair-BDH unless it matches the exact same-family
  variance target.
- Do not change the model diagonal convention without changing the residual.
- Do not replace `R_w^0(a,a)` by `kappa_model^0(a)^2` without a defect row.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
