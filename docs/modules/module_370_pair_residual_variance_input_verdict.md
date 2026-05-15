# Module 370: Pair-residual variance input verdict

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a steering verdict.
```

Best-module selection:

```text
The best current module is PairResidualVarianceInputVerdict_370(P_minor^0).
```

Reason:

```text
Modules 368 and 369 classified the pair-residual Fourier energy as a
same-family variance target and decomposed it into exact covariance rows.
The next useful attack is to decide whether this decomposition is genuinely
smaller than the original variance row, or whether it shows that the
no-twist anti-diagonal route needs a new same-family pair variance input.
```

Define:

```text
PairResidualVarianceInputVerdict_370(P_minor^0).
```

Verdict:

```text
PairResidualVarianceInputVerdict_370(P_minor^0):
  STRUCTURAL / EXTRACTION.

VariancePackageSufficiency_370:
  PROVEN.

CrossTermCauchyCircularity_370:
  PROVEN.

SmallModelSecondMomentAbsorptionCriterion_370:
  CONDITIONAL.

NondegenerateRectangleOnlyClosure_370:
  FALSE / BLOCKED.

CurrentPairResidualVarianceClosure_370:
  FALSE / BLOCKED.

SameFamilyPairVarianceNewInput_370:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
  Next best attack.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful outcome is a verdict. The covariance package from Module 369 is a
correct decomposition, but current tools do not make it smaller than the
original same-family pair variance. The pair-residual branch should therefore
be paused as a primary algebraic branch unless a genuinely new variance input
is supplied. The least-attacked part of the Module 359 split is now the
diagonal-overlap large-value row.

## 2. Why this would advance the main theorem

The no-twist anti-diagonal route requires coefficient top-mass control. The
Module 359 split left three branches:

```text
1. pair-residual large values,
2. rectangle-defect large values,
3. diagonal-overlap large values.
```

Modules 360 and 361-369 have stressed the first two analytic branches enough
to expose variance-strength inputs:

```text
AntiDiagonalRectangleVarianceTarget_360,
SameFamilyPairBDHVarianceTarget_368.
```

This module decides that the pair-residual variance decomposition is not
presently a closure path. That prevents the project from spending more
iterations on algebraic rewrites that only rename the same variance theorem.
It also identifies the next best attack: the diagonal-overlap large-value row
from Module 359, because it remains the least classified part of the current
coefficient top-mass split.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ.
```

Let:

```text
S_scale=D^(-1)K_UK_V.
```

Use the model convention from Modules 363-369:

```text
kappa_model^0(a),
E_pair,model^0(a)=P_nu^0(a)-kappa_model^0(a).
```

Define:

```text
Energy_pair^0(model)
  =
  E_a |E_pair,model^0(a)|^2.
```

From Module 369, write:

```text
Rect_ND^0
  =
  E_{a,q}1_ND(a,q)Delta_rect^0(a,q),

Rect_Deg^0
  =
  E_{a,q}1_Deg(a,q)Delta_rect^0(a,q),

Cross_pair^0
  =
  E_a kappa_model^0(a)E_pair,model^0(a),

Def_model^0
  =
  E_a(R_diag,model^0(a)-kappa_model^0(a)^2).
```

Then Module 369 gives:

```text
Energy_pair^0(model)
  =
  Rect_ND^0
  + Rect_Deg^0
  - 2 Cross_pair^0
  + Def_model^0.
```

Also define:

```text
M_model^0
  =
  E_a |kappa_model^0(a)|^2.
```

## 4. Assumptions

This module assumes:

```text
Modules 359-369,
finite cyclic Fourier algebra,
and the active status ledger.
```

It does not assume:

```text
SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361,
NondegenerateRectangleCovarianceTarget_369,
DegenerateRectangleCovarianceRows_369,
WeightedPairResidualCorrelationTarget_369,
RectangleDiagonalModelDefectTarget_369,
AntiDiagonalRectangleVarianceTarget_360,
DiagonalOverlapLargeValueTarget_359,
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
the nondegenerate rectangle covariance alone proves pair variance,
Cauchy on the weighted cross term is a non-circular proof,
generic rectangle HL controls model-defect and degenerate rows,
pair-residual variance closure proves signed local-model insertion.
```

## 5. Proof / disproof / reduction

### A. Variance package sufficiency

Assume the four rows satisfy:

```text
S_scale |Rect_ND^0|=o_W(1),
S_scale |Rect_Deg^0|=o_W(1),
S_scale |Cross_pair^0|=o_W(1),
S_scale |Def_model^0|=o_W(1).
```

Then by the exact Module 369 decomposition:

```text
S_scale Energy_pair^0(model)
  <=
  S_scale |Rect_ND^0|
  + S_scale |Rect_Deg^0|
  + 2S_scale |Cross_pair^0|
  + S_scale |Def_model^0|
  =
  o_W(1).
```

Thus the four-row covariance package is sufficient for:

```text
SameFamilyPairBDHVarianceTarget_368.
```

Classification:

```text
VariancePackageSufficiency_370:
  PROVEN.
```

This is a finite algebraic implication. It does not prove any of the four
rows.

### B. Cauchy control of the weighted cross term is circular

By Cauchy:

```text
|Cross_pair^0|
  =
  |E_a kappa_model^0(a)E_pair,model^0(a)|
  <=
  (M_model^0)^(1/2)
  (Energy_pair^0(model))^(1/2).
```

After multiplying by `S_scale`:

```text
S_scale |Cross_pair^0|
  <=
  (S_scale M_model^0)^(1/2)
  (S_scale Energy_pair^0(model))^(1/2).
```

Therefore, a proof of the cross term using only this Cauchy inequality
requires either:

```text
S_scale M_model^0=o_W(1),
```

or prior control of:

```text
S_scale Energy_pair^0(model).
```

The second option is exactly the target. Hence Cauchy alone is circular
unless the small model-second-moment condition is separately proved.

Classification:

```text
CrossTermCauchyCircularity_370:
  PROVEN.

SmallModelSecondMomentAbsorptionCriterion_370:
  CONDITIONAL.
```

The current ledger does not prove `S_scale M_model^0=o_W(1)` for the active
threshold schedules.

### C. Nondegenerate rectangle covariance alone is insufficient

Even if the nondegenerate row were proved:

```text
S_scale |Rect_ND^0|=o_W(1),
```

the decomposition still contains:

```text
Rect_Deg^0,
Cross_pair^0,
Def_model^0.
```

Module 369 showed that these are not notation errors. They represent
degenerate rectangle strata, a weighted residual correlation, and an exact
diagonal rectangle model-defect row.

Thus:

```text
NondegenerateRectangleOnlyClosure_370:
  FALSE / BLOCKED.
```

This blocks the route:

```text
generic nondegenerate rectangle HL => pair-residual variance.
```

### D. Current pair-residual variance closure verdict

The current ledger has:

```text
PairResidualParsevalIdentity_368,
PairResidualRectangleEnergyExpansion_368,
PairResidualCovarianceDecomposition_369,
VariancePackageSufficiency_370.
```

It does not have:

```text
NondegenerateRectangleCovarianceTarget_369,
DegenerateRectangleCovarianceRows_369,
WeightedPairResidualCorrelationTarget_369,
RectangleDiagonalModelDefectTarget_369,
SmallModelSecondMomentAbsorptionCriterion_370.
```

Therefore:

```text
CurrentPairResidualVarianceClosure_370:
  FALSE / BLOCKED.

SameFamilyPairVarianceNewInput_370:
  OPEN.
```

The phrase "new input" means a theorem stronger than the current first-moment
and algebraic ledger: a same-family variance theorem with the exact model
convention, W-residue, cyclic range, dyadic scale, threshold schedule, and
limit order.

### E. Best next attack

After Modules 360 and 361-370, two coefficient-top-mass branches have been
stressed to variance-strength obstructions:

```text
RectangleDefectLargeValueTarget_359
  -> AntiDiagonalRectangleVarianceTarget_360,

PairResidualLargeValueTarget_359
  -> SameFamilyPairBDHVarianceTarget_368.
```

The Module 359 split still contains:

```text
DiagonalOverlapLargeValueTarget_359:
  sum_xi |A(xi)|o_abs(xi)=o_W(1).
```

This row has not yet received a comparable direct stress test. The next best
attack is therefore:

```text
DiagonalOverlapLargeValueStress_371(P_minor^0).
```

Classification:

```text
DiagonalOverlapLargeValueTarget_359:
  OPEN.
  Next best attack.
```

## 6. Edge cases

### Cancellation among rows

The exact decomposition may have cancellation among `Rect_ND^0`,
`Rect_Deg^0`, `Cross_pair^0`, and `Def_model^0`. The sufficient package in
part A deliberately avoids relying on such cancellation. A future proof using
row cancellation must state it as a signed theorem in the same family.

### Model-second-moment absorption

If a future module proves `S_scale M_model^0=o_W(1)`, then Cauchy can absorb
the weighted cross term. This is not currently in the ledger.

### Diagonal conventions

Every row depends on the same `kappa_model^0` convention. Switching between
off-diagonal, finite diagonal, or renormalized diagonal models changes both
`Cross_pair^0` and `Def_model^0`.

### Degenerate rectangle strata

Degenerate strata are lower-rank local problems. They may be easier than the
nondegenerate covariance in some ranges, but they are not automatically
controlled by a generic four-form theorem.

### Threshold scaling

All row estimates must survive multiplication by `S_scale=D^(-1)K_UK_V`.
Unscaled local covariance statements are not enough.

## 7. Project-map location

```text
PairResidualFourierEnergyAudit_368
  -> PairResidualCovarianceIsolation_369
  -> PairResidualVarianceInputVerdict_370
  -> DiagonalOverlapLargeValueStress_371.
```

This module is a verdict on the pair-residual variance branch. It pauses the
branch as a primary algebraic route unless a new same-family variance input
is supplied.

## 8. What remains open

Still open:

```text
DiagonalOverlapLargeValueStress_371(P_minor^0),
DiagonalOverlapLargeValueTarget_359,
SameFamilyPairVarianceNewInput_370,
SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361,
AntiDiagonalRectangleVarianceTarget_360,
NondegenerateRectangleCovarianceTarget_369,
DegenerateRectangleCovarianceRows_369,
WeightedPairResidualCorrelationTarget_369,
RectangleDiagonalModelDefectTarget_369,
PairResidualLargeValueTarget_359,
PairMixedDiagonalAbsorptionCriterion_363,
full P_minor^0 pair-model minor top-mass without PolyR_rho,
RectangleDefectLargeValueTarget_359,
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
Latest completed module: 370
Post-Reflective_1 solving count: 189
Long-term-plan count: 183

183 is not divisible by 9, so no plan update is due in this module.
183 is not divisible by 15, so no plan challenge is due in this module.
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
The rectangle model-defect row is kept. No replacement of Theta_model^0 by
kappa_model^0(a)^2 is made.
```

Limit-order check:

```text
All implications are finite cyclic implications. No N/w/R/eta limit is
exchanged.
```

Uniformity check:

```text
The same-family variance input remains open and is not assumed.
```

Endpoint-circularity check:

```text
The proof does not assume SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361, AntiDiagonalRectangleVarianceTarget_360,
PhaseKernelBound_273^0, NarrowMinorArc_3^B, ResCube_3^sharp,
CPC_3^sharp, RBDH_pair_short, or AU^3.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
PairResidualVarianceInputVerdict_370(P_minor^0):
  STRUCTURAL / EXTRACTION.

VariancePackageSufficiency_370:
  PROVEN.

CrossTermCauchyCircularity_370:
  PROVEN.

SmallModelSecondMomentAbsorptionCriterion_370:
  CONDITIONAL.

NondegenerateRectangleOnlyClosure_370:
  FALSE / BLOCKED.

CurrentPairResidualVarianceClosure_370:
  FALSE / BLOCKED.

SameFamilyPairVarianceNewInput_370:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
  Next best attack.
```

Do not cite this module as proving pair-residual variance. It proves only the
sufficiency of a full row package and shows why current partial routes do not
close the package.

## Red flags / forbidden upgrades

- Do not treat Cauchy on the cross term as non-circular unless the small
  model-second-moment condition is proved.
- Do not treat the nondegenerate rectangle row as the whole variance package.
- Do not use generic rectangle HL for degenerate or model-defect rows.
- Do not assign `PROVEN` status to pair-residual variance, signed local
  insertion, or the residual cube target.
- Keep the original selected-average problem at `OPEN`.
