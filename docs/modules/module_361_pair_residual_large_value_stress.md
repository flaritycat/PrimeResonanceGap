# Module 361: Pair-residual large-value stress test

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Module 359 split the coefficient top-mass problem into pair-residual,
rectangle-defect, and diagonal-overlap targets. Module 360 stressed the
rectangle-defect branch and reduced it to an anti-diagonal variance row. This
module attacks the pair-residual branch:

```text
PairResidualLargeValueTarget_359(P_minor^0).
```

Define:

```text
PairResidualLargeValueStress_361(P_minor^0).
```

Verdict:

```text
PairResidualLargeValueStress_361(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualSquareEnergyBound_361:
  PROVEN.

PairResidualMixedModelBound_361:
  PROVEN.

PairResidualEnergyCriterion_361:
  CONDITIONAL.

PairResidualMixedCriterion_361:
  CONDITIONAL.

CurrentPairResidualLargeValueClosure_361:
  FALSE / BLOCKED.

PairResidualFourierEnergyTarget_361:
  OPEN.

PairModelMinorTopMassTarget_361:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful extraction is that the pair-residual square top-mass row would
follow from a strong same-family Fourier-energy estimate for the exact pair
residual `E_pair^0`. The mixed row `|E_+^0K_+^0|` additionally requires
minor-frequency control of the exact pair-model coefficient `K_+^0`. Current
pair first-moment inputs and current pair-BDH-style references do not supply
those two distribution estimates at the active mask-loss scale.

## 2. Why this would advance the main theorem

The active no-twist branch is:

```text
NoTwistColumnProfileCorrelation_356
  -> coefficient top-mass / large-value control
  -> SignedLocalModelInsertion_326
  -> local minor-arc residual eight-slot package.
```

Module 351 decomposed the active anti-diagonal coefficient into:

```text
A_Delta^351(xi)
  =
  E_+^0(xi)^2
  +2E_+^0(xi)K_+^0(xi)
  +RDef_+^0(xi).
```

Module 359 showed that coefficient top-mass can be attacked through:

```text
A_star,|E_+^0|^2(m_{U,V}),
A_star,|E_+^0K_+^0|(m_{U,V}),
A_star,|RDef_+^0|(m_{U,V}).
```

Module 360 handled the rectangle-defect part. This module tests whether the
two pair-residual parts can be closed from present pair information. They
cannot be closed by current inputs, but they can be reduced to sharper
energy and model-top-mass targets.

## 3. Exact assumptions allowed

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Use:

```text
widehat{F}(xi)=E_{a in G_N}F(a)e_N(-xi a),
F_+(xi)=E_{a in G_N}F(a)e_N(xi a)=widehat{F}(-xi).
```

Recall:

```text
P_nu^0(a)
  =
  E_{r in G_N} nu_0(r)nu_0(r+a),

kappa_w^0(a)
  =
  prod_{p>w}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p),

E_pair^0(a)
  =
  P_nu^0(a)-kappa_w^0(a),

E_+^0(xi)
  =
  E_{a in G_N} E_pair^0(a)e_N(xi a),

K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a).
```

For a nonnegative coefficient `c(xi)`, define:

```text
A_star,c(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} c(xi).
```

The active top-mass scale from Module 358 is:

```text
m_{U,V}=ceil(min(I_U/K_U,I_V/K_V)).
```

## 4. Exact assumptions forbidden

This module does not assume:

```text
PairResidualLargeValueTarget_359,
PairResidualFourierEnergyTarget_361,
PairModelMinorTopMassTarget_361,
PairResidualCriteria_351 as proved estimates,
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
RectangleDefectCoefficientCriterion_351 as a proved estimate,
AntiDiagonalPairPairRows_350,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
WeightedProfileSecondMomentCriterion_356,
NoTwistProductProfileCriterion_355,
NoTwistWeightedMassCriterion_354,
MaskBudgetCriteria_352,
HigherOrderBlockCoefficientRows_353,
WeightedSubsetModelDiscrepancyCriterion_346,
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

Forbidden shortcuts:

```text
first-moment pair HL => pair-residual top mass,
ordinary pair-BDH => masked no-twist coefficient top mass,
pair residual energy => mixed E_+K_+ control without K_+ top-mass control,
zero-mode pair calibration => nonzero minor-frequency distribution.
```

## 5. Proof attempt

### A. Pair-residual square top mass from Fourier energy

For any `m>=0`:

```text
A_star,|E_+^0|^2(m)
  <=
  sum_{xi in Minor_0(R,eta)} |E_+^0(xi)|^2
  <=
  sum_{xi in G_N} |E_+^0(xi)|^2.
```

By normalized Parseval:

```text
sum_{xi in G_N} |E_+^0(xi)|^2
  =
  E_{a in G_N} |E_pair^0(a)|^2.
```

Therefore:

```text
A_star,|E_+^0|^2(m)
  <=
  E_a |P_nu^0(a)-kappa_w^0(a)|^2.
```

Classification:

```text
PairResidualSquareEnergyBound_361:
  PROVEN.
```

This is a finite Fourier inequality. It does not estimate the pair residual
energy.

It gives the following sufficient criterion:

```text
D^(-1)K_UK_V
  E_a |P_nu^0(a)-kappa_w^0(a)|^2
  =
  o_W(1).
```

Classification:

```text
PairResidualEnergyCriterion_361:
  CONDITIONAL.

PairResidualFourierEnergyTarget_361:
  OPEN.
```

### B. Mixed pair-residual/model top mass

For any `E subset Minor_0(R,eta)` with `#E<=m`, Cauchy gives:

```text
sum_{xi in E} |E_+^0(xi)K_+^0(xi)|
  <=
  (
    sum_{xi in E}|E_+^0(xi)|^2
  )^(1/2)
  (
    sum_{xi in E}|K_+^0(xi)|^2
  )^(1/2).
```

Taking the supremum over `E` gives:

```text
A_star,|E_+^0K_+^0|(m)
  <=
  A_star,|E_+^0|^2(m)^(1/2)
  A_star,|K_+^0|^2(m)^(1/2).
```

Using part A:

```text
A_star,|E_+^0K_+^0|(m)
  <=
  (
    E_a |E_pair^0(a)|^2
  )^(1/2)
  A_star,|K_+^0|^2(m)^(1/2).
```

Classification:

```text
PairResidualMixedModelBound_361:
  PROVEN.
```

Thus the mixed row would follow from:

```text
D^(-1)K_UK_V
  (
    E_a |E_pair^0(a)|^2
  )^(1/2)
  A_star,|K_+^0|^2(m_{U,V})^(1/2)
  =
  o_W(1).
```

Classification:

```text
PairResidualMixedCriterion_361:
  CONDITIONAL.

PairModelMinorTopMassTarget_361:
  OPEN.
```

The exact pair-model coefficient `K_+^0` cannot simply be treated as
harmless. A large pair-residual energy saving is insufficient for the mixed
row unless the model coefficient has compatible minor-frequency top-mass
control at the same `m_{U,V}` scale.

### C. Why first-moment pair information is blocked

First-moment pair Hardy-Littlewood information concerns averages like:

```text
E_a E_pair^0(a)
```

or comparable mean pair-density calibration. The square top-mass route needs
the second moment:

```text
E_a |E_pair^0(a)|^2.
```

These are different strengths. A finite stress witness shows why.

Let `G_N` be cyclic and choose any nonzero frequency `xi_0`. Set:

```text
e(a)=B e_N(-xi_0 a).
```

Then:

```text
E_a e(a)=0,
```

but:

```text
E_a |e(a)|^2=B^2,
```

and:

```text
E_a e(a)e_N(xi_0 a)=B.
```

Thus zero first moment does not prevent a large nonzero Fourier coefficient
or large second energy. This witness is not asserted to be the actual
`E_pair^0`; it proves only that first-moment pair data alone cannot imply
pair-residual large-value control.

Classification:

```text
FirstMomentPairResidualRoute_361:
  FALSE / BLOCKED.
```

### D. Why ordinary pair-BDH-style information is not enough as currently
stated

The pair-residual square target is not just any pair variance statement. It
must be strong enough to absorb the no-twist mask losses:

```text
D^(-1)K_UK_V
  E_a |E_pair^0(a)|^2
  =
  o_W(1).
```

The mixed target additionally requires:

```text
A_star,|K_+^0|^2(m_{U,V})
```

at the same minor-frequency scale. A pair-residual variance estimate alone
does not control the deterministic pair-model Fourier concentration.

Therefore ordinary pair-BDH language, unless upgraded to the exact
same-family residual energy scale and combined with the pair-model minor
top-mass row, does not close the Module 359 pair-residual large-value target.

Classification:

```text
CurrentPairResidualLargeValueClosure_361:
  FALSE / BLOCKED.
```

## 6. Places where current tools fail

Current tools fail at two precise rows:

```text
PairResidualFourierEnergyTarget_361:
  E_a |P_nu^0(a)-kappa_w^0(a)|^2
    =
    o_W(D/(K_UK_V)).

PairModelMinorTopMassTarget_361:
  A_star,|K_+^0|^2(m_{U,V})
    small enough to combine with the pair-residual energy.
```

The first is a same-family pair-residual second-moment theorem at the
mask-loss scale. The second is a deterministic local-model Fourier
distribution theorem on the minor-frequency set. Current first-moment pair
inputs, unweighted coefficient identities, Parseval ceilings, and endpoint
equivalence language do not prove either row.

## 7. New lemmas proved

The module proves two finite bounds:

```text
PairResidualSquareEnergyBound_361:
  PROVEN.

PairResidualMixedModelBound_361:
  PROVEN.
```

They are Fourier/Cauchy inequalities. They can feed later estimates, but
they are not prime-distribution theorems.

## 8. Dependency reduced or removed

This module replaces the broad dependency:

```text
PairResidualLargeValueTarget_359
```

by:

```text
PairResidualFourierEnergyTarget_361,
PairModelMinorTopMassTarget_361.
```

It also separates the square residual row from the mixed model row. This is
important because the square row could in principle be attacked by pair
residual variance, while the mixed row also needs exact model-coefficient
distribution on minor frequencies.

The next narrower target should be:

```text
PairModelMinorTopMassStress_362(P_minor^0).
```

This questions whether the deterministic exact pair-model coefficient
`K_+^0` is actually harmless on the declared minor arcs, or whether treating
it as harmless hides another major/minor local-model transfer assumption.

## 9. Red-team audit

Selector check:

```text
All statements remain inside P_minor^0. No actual sharp moving-selector
statement is proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, tail, or empty-interval statement is used.
```

Local-factor check:

```text
The exact pair model kappa_w^0 is retained. No rectangle factor is replaced
by a pair product, and no pair-model Fourier coefficient is discarded.
```

Limit-order check:

```text
The bounds are finite cyclic inequalities. No N/w/D/R/eta/cutoff limit is
exchanged.
```

Uniformity check:

```text
The criteria name the required uniform estimates but prove no W-uniform
prime-distribution estimate.
```

Endpoint-circularity check:

```text
The proof does not assume PhaseKernelBound_273^0, NarrowMinorArc_3^B,
ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short, or AU^3.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
PairResidualLargeValueStress_361(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualSquareEnergyBound_361:
  PROVEN.

PairResidualMixedModelBound_361:
  PROVEN.

PairResidualEnergyCriterion_361:
  CONDITIONAL.

PairResidualMixedCriterion_361:
  CONDITIONAL.

FirstMomentPairResidualRoute_361:
  FALSE / BLOCKED.

CurrentPairResidualLargeValueClosure_361:
  FALSE / BLOCKED.

PairResidualFourierEnergyTarget_361:
  OPEN.

PairModelMinorTopMassTarget_361:
  OPEN.
```

The proof attack does not close the pair-residual top-mass row. It reduces
the square row to pair-residual Fourier energy and the mixed row to a
combination of pair-residual energy with exact pair-model minor-frequency
top-mass control.

## Edge cases

Empty masks:

```text
If one mask is empty, the no-twist product contribution is zero. The
pair-residual top-mass row is then irrelevant for that mask pair.
```

Zero frequency:

```text
Mean pair calibration controls zero-mode behavior. The active target is on
Minor_0(R,eta) subset {xi != 0}.
```

Tiny `m_{U,V}`:

```text
If `m_{U,V}` is bounded, pointwise bounds for `E_+^0` and `K_+^0` might
suffice. Current inputs do not prove the required pointwise smallness at the
active scale.
```

Model coefficient concentration:

```text
Even if the pair residual energy is small, the mixed row can fail under the
current proof data if `K_+^0` concentrates on the same minor frequencies.
This is a proof-data obstruction, not a claim that such concentration occurs.
```

## Project-map location

```text
PairRectangleDefectSplit_351
  -> CoefficientLargeValueDistributionAudit_359
  -> RectangleDefectLargeValueStress_360
  -> PairResidualLargeValueStress_361
  -> PairModelMinorTopMassStress_362.
```

This module attacks the pair-residual branch of the large-value split. It
narrows that branch to pair-residual Fourier energy and exact pair-model
minor top-mass.

## What remains open

Still open:

```text
PairModelMinorTopMassStress_362(P_minor^0),
PairResidualFourierEnergyTarget_361,
PairModelMinorTopMassTarget_361,
AntiDiagonalRectangleVarianceTarget_360,
RectangleDefectLargeValueTarget_359,
PairResidualLargeValueTarget_359,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as an estimate,
NoTwistColumnProfileCorrelation_356(P_minor^0),
WeightedProfileSecondMomentCriterion_356 as an estimate,
NoTwistProductProfileCriterion_355,
NoTwistWeightedMassCriterion_354,
MaskBudgetCriteria_352,
HigherOrderBlockCoefficientRows_353,
PairResidualCriteria_351,
RectangleDefectCoefficientCriterion_351,
AntiDiagonalPairPairRows_350,
AntiDiagonalPairPairDiscrepancyCriterion_349,
MinimalFullyCoupledQuadrupleRows_349,
FullyCoupledSubsetDiscrepancyRows_348,
WeightedSubsetModelDiscrepancyCriterion_346,
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

## Red flags / forbidden upgrades

- Do not cite the square-energy bound as pair-residual smallness.
- Do not cite the mixed bound as model-coefficient top-mass control.
- Do not treat first-moment pair calibration as residual variance.
- Do not treat ordinary pair-BDH language as enough unless it supplies the
  exact same-family residual energy scale and the model top-mass row.
- Do not use endpoint-strength pair variance as an assumption in a proof
  advertised as proving the endpoint.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
