# Module 360: Rectangle-defect large-value stress test

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Module 359 split the coefficient top-mass problem into pair-residual,
rectangle-defect, and diagonal-overlap targets. This module attacks the
rectangle-defect target:

```text
RectangleDefectLargeValueTarget_359(P_minor^0).
```

Define:

```text
RectangleDefectLargeValueStress_360(P_minor^0).
```

Verdict:

```text
RectangleDefectLargeValueStress_360(P_minor^0):
  STRUCTURAL / EXTRACTION.

RectangleAntiDiagonalCompression_360:
  PROVEN.

RectangleTopMassVarianceCriterion_360:
  CONDITIONAL.

FirstMomentRectangleDefectRoute_360:
  FALSE / BLOCKED.

CurrentRectangleDefectLargeValueClosure_360:
  FALSE / BLOCKED.

AntiDiagonalRectangleVarianceTarget_360:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful extraction is that the rectangle-defect coefficient is exactly the
Fourier transform of an anti-diagonal rectangle-defect profile. Therefore a
non-endpoint proof of its top-mass smallness would need a same-family
variance estimate for that anti-diagonal profile. First-moment rectangle
information only sees the zero Fourier mode and does not control this
variance.

## 2. Why this would advance the main theorem

The active branch is:

```text
NoTwistColumnProfileCorrelation_356
  -> coefficient top-mass / large-value control
  -> SignedLocalModelInsertion_326
  -> local minor-arc residual eight-slot package.
```

Module 351 showed that even if the pair residual were controlled, the exact
rectangle product defect remains:

```text
RectDef_w^0(a,b)
  =
  kappa_w^0(a)kappa_w^0(b)-R_w^0(a,b).
```

Module 359 then identified:

```text
A_star,|RDef_+^0|(m_{U,V})
  =
  o_W(D/(K_UK_V))
```

as one of the concrete large-value targets needed for coefficient top mass.
If this module proved that estimate, it would remove the rectangle-defect
part of the no-twist coefficient obstruction. It does not. Instead it
identifies the exact variance row that would be needed.

## 3. Exact assumptions allowed

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Use the normalized Fourier convention:

```text
widehat{F}(xi)=E_{t in G_N}F(t)e_N(-xi t),
F_+(xi)=E_{t in G_N}F(t)e_N(xi t)=widehat{F}(-xi).
```

Recall the exact objects from Modules 350-351:

```text
kappa_w^0(a)
  =
  prod_{p>w}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p),

Theta_w^4(a,b;q)
  =
  prod_{p>w}
    (1-1/p)^(-4)
    (1-#({0,a,q,q+b} mod p)/p),

R_w^0(a,b)
  =
  E_{q in G_N} Theta_w^4(a,b;q),

RectDef_w^0(a,b)
  =
  kappa_w^0(a)kappa_w^0(b)-R_w^0(a,b),

RDef_+^0(xi)
  =
  E_{a,b in G_N}
    RectDef_w^0(a,b)e_N(xi(a+b)).
```

For a nonnegative coefficient `c(xi)`, write:

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
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
RectangleDefectCoefficientCriterion_351 as a proved estimate,
PairResidualCriteria_351 as proved estimates,
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
first-moment rectangle HL => rectangle-defect top mass,
mean rectangle control => anti-diagonal rectangle variance,
pair model product kappa_w^0(a)kappa_w^0(b) replaces R_w^0(a,b),
zero-mode calibration controls nonzero minor frequencies.
```

## 5. Proof attempt

### A. Exact anti-diagonal compression

Define the anti-diagonal rectangle-defect profile:

```text
RDag_w^0(t)
  =
  E_{a in G_N} RectDef_w^0(a,t-a).
```

Then:

```text
RDef_+^0(xi)
  =
  E_{t in G_N} RDag_w^0(t)e_N(xi t)
  =
  widehat{RDag_w^0}(-xi).
```

Proof:

Starting from the definition:

```text
RDef_+^0(xi)
  =
  E_{a,b} RectDef_w^0(a,b)e_N(xi(a+b)).
```

Set:

```text
t=a+b.
```

For each `t`, the cyclic change of variables `b=t-a` gives:

```text
E_{a,b} RectDef_w^0(a,b)e_N(xi(a+b))
  =
  E_t e_N(xi t) E_a RectDef_w^0(a,t-a)
  =
  E_t RDag_w^0(t)e_N(xi t).
```

By the Fourier convention this is `widehat{RDag_w^0}(-xi)`.

Classification:

```text
RectangleAntiDiagonalCompression_360:
  PROVEN.
```

This is exact finite cyclic algebra. It does not estimate the defect.

### B. Top-mass from anti-diagonal variance

For `m>=0`, Cauchy and Parseval give:

```text
A_star,|RDef_+^0|(m)
  <=
  m^(1/2)
  (
    sum_{xi in Minor_0(R,eta)} |RDef_+^0(xi)|^2
  )^(1/2)
```

and:

```text
sum_{xi in Minor_0(R,eta)} |RDef_+^0(xi)|^2
  <=
  sum_{xi in G_N} |widehat{RDag_w^0}(xi)|^2
  =
  E_{t in G_N} |RDag_w^0(t)|^2.
```

Therefore:

```text
A_star,|RDef_+^0|(m)
  <=
  m^(1/2)
  (
    E_t |RDag_w^0(t)|^2
  )^(1/2).
```

This gives the following sufficient criterion for the rectangle-defect
top-mass row:

```text
D^(-1)K_UK_V m_{U,V}^{1/2}
  (
    E_t |RDag_w^0(t)|^2
  )^(1/2)
  =
  o_W(1).
```

Equivalently, it would be enough to prove:

```text
E_t |RDag_w^0(t)|^2
  =
  o_W(D^2/(K_U^2 K_V^2 m_{U,V})).
```

Classification:

```text
RectangleTopMassVarianceCriterion_360:
  CONDITIONAL.

AntiDiagonalRectangleVarianceTarget_360:
  OPEN.
```

The implication is proved. The variance estimate is not.

### C. Why first-moment rectangle information is blocked

The first moment of the anti-diagonal profile is:

```text
E_t RDag_w^0(t)
  =
  E_{a,b} RectDef_w^0(a,b).
```

It controls only the zero Fourier mode:

```text
RDef_+^0(0).
```

The active no-twist obstruction uses nonzero minor frequencies. A zero-mode
or first-moment statement does not control:

```text
sum_{xi in Minor_0(R,eta)} |RDef_+^0(xi)|^2
```

or any top-mass functional on nonzero frequencies.

Finite stress witness:

Let `G_N` be any cyclic group and fix a nonzero frequency `xi_0`. For any
`B>0`, define an abstract anti-diagonal profile:

```text
h(t)=B e_N(-xi_0 t).
```

Then:

```text
E_t h(t)=0,
```

but:

```text
E_t h(t)e_N(xi_0 t)=B.
```

Thus an abstract profile may have zero first moment and a large nonzero
Fourier coefficient. This witness is not asserted to be the actual
`RDag_w^0`; it proves only that first-moment data alone cannot imply
rectangle-defect top-mass control.

Classification:

```text
FirstMomentRectangleDefectRoute_360:
  FALSE / BLOCKED.
```

### D. Why the current rectangle-defect route does not close

The exact identity:

```text
RDef_+^0(xi)=K_+^0(xi)^2-C_w^0(xi)
```

does not estimate `RDef_+^0(xi)`. It says the rectangle-defect coefficient is
the difference between:

```text
the anti-diagonal product of exact pair factors,
```

and:

```text
the exact anti-diagonal transform of the four-point rectangle factor.
```

First-moment rectangle Hardy-Littlewood controls average local densities, not
the anti-diagonal variance:

```text
E_t |RDag_w^0(t)|^2.
```

Pair information controls `kappa_w^0` or pair residuals. It does not justify
discarding:

```text
R_w^0(a,b)
  =
  E_q Theta_w^4(a,b;q)
```

or replacing it by:

```text
kappa_w^0(a)kappa_w^0(b).
```

Consequently the rectangle-defect large-value row remains open.

Classification:

```text
CurrentRectangleDefectLargeValueClosure_360:
  FALSE / BLOCKED.
```

## 6. Places where current tools fail

Current tools fail at the variance row:

```text
AntiDiagonalRectangleVarianceTarget_360:
  E_t |RDag_w^0(t)|^2
    =
    o_W(D^2/(K_U^2 K_V^2 m_{U,V})).
```

The available inputs do not prove this because:

```text
first-moment rectangle inputs see only E_t RDag_w^0(t),
pair inputs do not control the four-point rectangle factor,
pointwise/logarithmic envelopes give only sup-norm ceilings,
and total-mass estimates do not exploit top-mass scale.
```

This is not a disproof of the variance target. It is a proof that current
first-moment and pair-product shortcuts do not supply it.

## 7. New lemma proved

The new finite identity is:

```text
RectangleAntiDiagonalCompression_360:
  PROVEN.
```

It proves:

```text
RDef_+^0(xi)=widehat{RDag_w^0}(-xi).
```

The module also proves the finite implication:

```text
A_star,|RDef_+^0|(m)
  <=
  m^(1/2)(E_t |RDag_w^0(t)|^2)^(1/2).
```

The implication is exact finite Fourier algebra, but the needed variance
smallness remains open.

## 8. Dependency reduced or removed

This module replaces:

```text
RectangleDefectLargeValueTarget_359
```

by the sharper row:

```text
AntiDiagonalRectangleVarianceTarget_360.
```

It removes the misleading hope that a first-moment rectangle local model
estimate could close the rectangle-defect top-mass row. The next proof
attempt should not appeal to mean rectangle HL. It must either prove the
anti-diagonal variance row or move to another part of the Module 359 split.

Since the rectangle-defect route has now exposed a variance-strength row, the
next narrower coefficient-distribution target should be:

```text
PairResidualLargeValueStress_361(P_minor^0).
```

This deliberately questions the earlier temptation to keep pushing
rectangle-factor algebra: without a new variance theorem, more algebraic
rewriting of `R_w^0` risks becoming endpoint-renaming.

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
The exact rectangle factor R_w^0(a,b)=E_q Theta_w^4(a,b;q) is retained.
No replacement by kappa_w^0(a)kappa_w^0(b) is made.
```

Limit-order check:

```text
The compression and variance criterion are finite cyclic statements. No
N/w/D/R/eta/cutoff limit is exchanged.
```

Uniformity check:

```text
The criterion names the required uniform variance estimate but does not
prove it.
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
RectangleDefectLargeValueStress_360(P_minor^0):
  STRUCTURAL / EXTRACTION.

RectangleAntiDiagonalCompression_360:
  PROVEN.

RectangleTopMassVarianceCriterion_360:
  CONDITIONAL.

FirstMomentRectangleDefectRoute_360:
  FALSE / BLOCKED.

CurrentRectangleDefectLargeValueClosure_360:
  FALSE / BLOCKED.

AntiDiagonalRectangleVarianceTarget_360:
  OPEN.
```

The proof attack does not close the rectangle-defect top-mass row. It proves
the exact anti-diagonal compression and identifies the variance-strength row
that would be needed.

## Edge cases

Empty masks:

```text
If one mask is empty, the no-twist product contribution is zero. The
rectangle-defect top-mass row is then irrelevant for that mask pair.
```

Zero frequency:

```text
The first moment controls only xi=0. The active minor-frequency target has
xi != 0, so zero-mode calibration is not enough.
```

Tiny `m_{U,V}`:

```text
If `m_{U,V}` is bounded and a pointwise bound for `RDef_+^0` is strong
enough, a sup-norm route may suffice. Current tools do not prove such a
bound at the active scale.
```

Abstract stress witness:

```text
The witness h(t)=B e_N(-xi_0 t) is only a logical stress test for
first-moment data. It is not claimed to arise from the actual local
rectangle factor.
```

## Project-map location

```text
PairRectangleDefectSplit_351
  -> CoefficientLargeValueDistributionAudit_359
  -> RectangleDefectLargeValueStress_360
  -> PairResidualLargeValueStress_361.
```

This module attacks the rectangle-defect branch of the large-value split. It
narrows that branch to an anti-diagonal variance target.

## What remains open

Still open:

```text
PairResidualLargeValueStress_361(P_minor^0),
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

- Do not cite anti-diagonal compression as variance smallness.
- Do not cite the variance criterion as a proved rectangle estimate.
- Do not replace the exact rectangle factor by a pair-product model.
- Do not treat zero-mode or first-moment rectangle information as nonzero
  minor-frequency control.
- Do not use endpoint-strength rectangle variance as an assumption in a proof
  advertised as proving the endpoint.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
