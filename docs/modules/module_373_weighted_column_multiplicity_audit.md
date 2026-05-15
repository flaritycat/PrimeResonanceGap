# Module 373: Weighted column-multiplicity audit

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Best-module selection:

```text
The best current module is WeightedColumnMultiplicityAudit_373(P_minor^0).
```

Reason:

```text
Module 372 reduced the same-source diagonal-overlap branch to the
coefficient-weighted column multiplicity row

  D^(-1) sum_xi |A(xi)|N_{beta_0}(xi;sigma)=o_W(1).

This is now the smallest concrete target on the diagonal-overlap branch.
The next useful attack is to test whether it follows from existing
coefficient norms, column-tail information, threshold amplitudes, or the
pair/rectangle coefficient split.
```

Define:

```text
WeightedColumnMultiplicityAudit_373(P_minor^0).
```

Verdict:

```text
WeightedColumnMultiplicityAudit_373(P_minor^0):
  STRUCTURAL / EXTRACTION.

WeightedColumnIncidenceIdentity_373:
  PROVEN.

WeightedColumnLayerCakeIdentity_373:
  PROVEN.

WeightedColumnSubadditiveSplit_373:
  PROVEN.

WeightedBetaEnergyCriterion_373:
  CONDITIONAL.

HolderColumnMomentCriterion_373:
  CONDITIONAL.

TopMassColumnTailCriterion_373:
  CONDITIONAL.

SupNormFirstIncidenceRoute_373:
  FALSE / BLOCKED.

ExistingPairRectangleSplitClosure_373:
  FALSE / BLOCKED.

CurrentWeightedColumnMultiplicityClosure_373:
  FALSE / BLOCKED.

WeightedBetaEnergyTarget_373:
  OPEN.

WeightedColumnMultiplicityTarget_372:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful conclusion is that the weighted column row has exact incidence,
layer-cake, and coefficient-split formulations. None of the present inputs
make these formulations small. The next smaller target is the
coefficient-weighted beta-energy row:

```text
D^(-1)sigma^(-2)
  sum_{d,xi}|A(xi)||beta_0(d,xi)|^2=o_W(1).
```

## 2. Why this would advance the main theorem

The active branch is:

```text
NoTwistColumnProfileCorrelation_356
  -> diagonal-overlap control
  -> SignedLocalModelInsertion_326
  -> local minor-arc residual eight-slot package.
```

Module 371 reduced the diagonal-overlap row to:

```text
D^(-1)sum_xi |A(xi)|l_{U,V}(xi)=o_W(1).
```

Module 372 showed that, for same-source threshold masks from `beta_0`, this
is implied by:

```text
WeightedColumnMultiplicityTarget_372(beta_0;sigma):
  D^(-1)sum_xi |A(xi)|N_{beta_0}(xi;sigma)=o_W(1).
```

If this module proved that row from current tools, the same-source
diagonal-overlap obstruction would be removed. It does not. Instead, it
shows that current tools reduce the problem either to a new weighted
beta-energy theorem, a coefficient top-mass theorem along column tails, or a
new joint coefficient-column moment theorem.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0},
mathcal D={d:D<|d|<=2D},
S_D=#mathcal D.
```

Use:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

Let:

```text
a(xi)=|A(xi)| >= 0,
xi in Minor_0(R,eta),
```

where `A` is one of the active same-family coefficients:

```text
A_Delta^350(xi),
E_+^0(xi)^2,
E_+^0(xi)K_+^0(xi),
RDef_+^0(xi).
```

For a threshold `sigma>0`, define:

```text
N_sigma(xi)
  =
  N_{beta_0}(xi;sigma)
  =
  # { d in mathcal D:
      |beta_0(d,xi)|>=sigma }.
```

Define the weighted column multiplicity:

```text
WCol_A(sigma)
  =
  D^(-1)sum_{xi in Minor_0(R,eta)}
    a(xi)N_sigma(xi).
```

Define the first incidence count:

```text
I_sigma
  =
  sum_xi N_sigma(xi)
  =
  # { (d,xi):
      xi in Minor_0(R,eta),
      |beta_0(d,xi)|>=sigma }.
```

Define the coefficient-weighted beta-energy:

```text
WBetaEng_A
  =
  sum_{d in mathcal D}
  sum_{xi in Minor_0(R,eta)}
    a(xi)|beta_0(d,xi)|^2.
```

Define the weighted column-tail mass:

```text
WColTail_A(T;sigma)
  =
  sum_{xi in Minor_0(R,eta):
        N_sigma(xi)>=T}
    a(xi),
  1<=T<=S_D.
```

Also recall:

```text
A_star(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E}a(xi).
```

## 4. Assumptions

This module assumes:

```text
Modules 308-312 and 350-372,
finite rearrangement algebra,
finite cyclic Fourier algebra,
and the active status ledger.
```

It does not assume:

```text
WeightedBetaEnergyTarget_373,
WeightedColumnMultiplicityTarget_372,
WeightedMixedAmplitudeTarget_372,
OverlapProfileAntiConcentrationTarget_371,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
ColumnMultiplicityGainTarget_308,
ColumnTailGainTarget_309,
WeightedColumnPairEnergyTarget_310,
WeightedColumnSecondMomentTarget_311,
AntiDiagonalTwoShiftKernelGain_312,
PairResidualFourierEnergyTarget_361,
SameFamilyPairBDHVarianceTarget_368,
AntiDiagonalRectangleVarianceTarget_360,
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
the finite-type theorem unconditionally,
or the original selected-average problem.
```

Forbidden shortcuts:

```text
unweighted column multiplicity tails imply coefficient-weighted tails,
unweighted E2_minor^0 controls WBetaEng_A,
the pair/rectangle coefficient split is itself a bound,
ordinary first-moment incidence controls data-dependent coefficient overlap,
same-source threshold reduction proves diagonal-overlap control automatically.
```

## 5. Proof / disproof / reduction

### A. Weighted column incidence identity

By definition:

```text
WCol_A(sigma)
  =
  D^(-1)sum_xi a(xi)N_sigma(xi)
```

and:

```text
N_sigma(xi)
  =
  sum_{d in mathcal D}
    1_{|beta_0(d,xi)|>=sigma}.
```

Therefore:

```text
WCol_A(sigma)
  =
  D^(-1)
  sum_{d in mathcal D}
  sum_{xi in Minor_0(R,eta)}
    a(xi)1_{|beta_0(d,xi)|>=sigma}.
```

Classification:

```text
WeightedColumnIncidenceIdentity_373:
  PROVEN.
```

This is the exact weighted incidence row. It is not an estimate.

### B. Weighted column layer-cake identity

For every integer `n>=0`:

```text
n=sum_{T=1}^{S_D}1_{n>=T}
```

when `0<=n<=S_D`. Hence:

```text
N_sigma(xi)
  =
  sum_{T=1}^{S_D}1_{N_sigma(xi)>=T}.
```

Multiplying by `a(xi)` and summing:

```text
WCol_A(sigma)
  =
  D^(-1)
  sum_{T=1}^{S_D} WColTail_A(T;sigma).
```

Classification:

```text
WeightedColumnLayerCakeIdentity_373:
  PROVEN.
```

Unweighted column-tail data give only:

```text
WColTail_A(T;sigma)
  <=
  A_star(ColTail_sigma(T)),
```

where:

```text
ColTail_sigma(T)
  =
  # { xi:N_sigma(xi)>=T }.
```

Using the first-moment tail:

```text
ColTail_sigma(T) <= min(m_minor^0,I_sigma/T)
```

therefore gives the conditional criterion:

```text
D^(-1)
sum_{T=1}^{S_D}
  A_star(min(m_minor^0,ceil(I_sigma/T)))
  =
  o_W(1).
```

Classification:

```text
TopMassColumnTailCriterion_373:
  CONDITIONAL.
```

This criterion keeps the coefficient top mass. It is not proved by the
current coefficient distribution ledger.

### C. Threshold-amplitude route

On the threshold set:

```text
1_{|beta_0(d,xi)|>=sigma}
  <=
  sigma^(-2)|beta_0(d,xi)|^2.
```

Thus:

```text
WCol_A(sigma)
  <=
  D^(-1)sigma^(-2) WBetaEng_A.
```

Consequently, `WeightedColumnMultiplicityTarget_372` follows from:

```text
D^(-1)sigma^(-2) WBetaEng_A=o_W(1).
```

Classification:

```text
WeightedBetaEnergyCriterion_373:
  CONDITIONAL.

WeightedBetaEnergyTarget_373:
  OPEN.
```

The current ledger has the unweighted estimate:

```text
D^(-1)sum_{d,xi}|beta_0(d,xi)|^2
  =
  E2_minor^0(D;R,eta),
```

but it does not have the coefficient-weighted estimate `WBetaEng_A`.

### D. Holder column-moment route

Let `q>1` and `q'=q/(q-1)`. Holder gives:

```text
sum_xi a(xi)N_sigma(xi)
  <=
  ||A||_{q,minor}
  (
    sum_xi N_sigma(xi)^(q')
  )^(1/q').
```

Thus:

```text
WCol_A(sigma)
  <=
  D^(-1)||A||_{q,minor}
  (
    sum_xi N_sigma(xi)^(q')
  )^(1/q').
```

The route closes only if the coefficient norm and the same-threshold column
moment satisfy:

```text
D^(-1)||A||_{q,minor}
  (
    sum_xi N_sigma(xi)^(q')
  )^(1/q')
  =
  o_W(1).
```

Classification:

```text
HolderColumnMomentCriterion_373:
  CONDITIONAL.
```

Modules 308-309 show that first-moment column information alone collapses to
ceiling-scale bounds for the column moments. They do not prove the required
weighted Holder row.

### E. Why sup norm plus first incidence is blocked

The most direct route gives:

```text
WCol_A(sigma)
  <=
  ||A||_{infty,minor}D^(-1)I_sigma.
```

First incidence gives:

```text
I_sigma
  <=
  sigma^(-2)
  sum_{d,xi in Minor_0(R,eta)}
    |beta_0(d,xi)|^2
  =
  D sigma^(-2)E2_minor^0(D;R,eta).
```

Hence:

```text
WCol_A(sigma)
  <=
  ||A||_{infty,minor}
  sigma^(-2)E2_minor^0(D;R,eta).
```

The active ledger does not prove this is `o_W(1)` for the active coefficient,
threshold schedule, dyadic shell, minor-frequency set, and limiting order.

Moreover, this route ignores coefficient concentration: it treats the large
columns as if they were automatically disjoint from the large values of
`A`. That anti-correlation is precisely the missing same-family input.

Classification:

```text
SupNormFirstIncidenceRoute_373:
  FALSE / BLOCKED.
```

### F. Pair/rectangle coefficient split

Module 351 gives the exact active coefficient split:

```text
A_Delta^351(xi)
  =
  E_+^0(xi)^2
  +2E_+^0(xi)K_+^0(xi)
  +RDef_+^0(xi).
```

Therefore:

```text
|A_Delta^351(xi)|
  <=
  |E_+^0(xi)|^2
  +2|E_+^0(xi)K_+^0(xi)|
  +|RDef_+^0(xi)|.
```

Multiplying by `N_sigma(xi)`, summing, and normalizing gives:

```text
WCol_{A_Delta}(sigma)
  <=
  WCol_{|E_+^0|^2}(sigma)
  +2WCol_{|E_+^0K_+^0|}(sigma)
  +WCol_{|RDef_+^0|}(sigma).
```

Classification:

```text
WeightedColumnSubadditiveSplit_373:
  PROVEN.
```

This is a real reduction, but not a closure. It creates three same-family
weighted column targets:

```text
PairResidualSquareWeightedColumnTarget_373,
PairResidualModelWeightedColumnTarget_373,
RectangleDefectWeightedColumnTarget_373.
```

The current ledger has not proved any of them. Modules 360-370 explain that
the corresponding unweighted large-value branches already require
variance-strength inputs. Adding `N_sigma(xi)` as a data-dependent weight
does not make them easier under current tools.

Classification:

```text
ExistingPairRectangleSplitClosure_373:
  FALSE / BLOCKED.
```

### G. Current weighted column verdict

The current ledger has:

```text
WeightedColumnIncidenceIdentity_373,
WeightedColumnLayerCakeIdentity_373,
WeightedColumnSubadditiveSplit_373,
WeightedBetaEnergyCriterion_373,
HolderColumnMomentCriterion_373,
TopMassColumnTailCriterion_373.
```

It does not have:

```text
WeightedBetaEnergyTarget_373,
TopMassColumnTailCriterion_373 as an estimate,
the Holder column-moment input,
PairResidualSquareWeightedColumnTarget_373,
PairResidualModelWeightedColumnTarget_373,
RectangleDefectWeightedColumnTarget_373.
```

Therefore:

```text
CurrentWeightedColumnMultiplicityClosure_373:
  FALSE / BLOCKED.

WeightedColumnMultiplicityTarget_372:
  OPEN.
```

The best next attack is:

```text
WeightedBetaEnergyAudit_374(P_minor^0),
```

because it is the smallest amplitude-preserving sufficient row:

```text
D^(-1)sigma^(-2)
  sum_{d,xi}|A(xi)||beta_0(d,xi)|^2=o_W(1).
```

## 6. Edge cases

### Empty threshold set

If `sigma>A_N^0`, then `N_sigma=0` and `WCol_A(sigma)=0`. This is a
bookkeeping case, not a proof for the active threshold grid.

### Zero coefficient

If `A` vanishes on the support of `N_sigma`, then the weighted row is zero.
The project does not currently prove such support separation for the active
coefficients.

### Low threshold levels

For small `sigma`, first incidence may be large. Module 297's low-level
fourth-moment tail applies below `lambda_min`; it does not provide high-level
column anti-correlation against `A`.

### High threshold levels

For high `sigma`, the unweighted incidence can be smaller, but the target
requires coefficient-weighted incidence. Concentration of `A` on the
remaining high columns is not ruled out by current inputs.

### Coefficient decomposition

The pair/rectangle split may be used only as a subadditive reduction. It does
not authorize dropping the rectangle-defect row or replacing exact local
factors by averaged substitutes.

## 7. Project-map location

```text
OverlapProfileStructureAudit_372
  -> WeightedColumnMultiplicityAudit_373
  -> WeightedBetaEnergyAudit_374
  -> diagonal-overlap branch of NoTwistColumnProfileCorrelation_356.
```

This module narrows:

```text
OverlapProfileAntiConcentrationTarget_371
```

to the more concrete amplitude-preserving target:

```text
WeightedBetaEnergyTarget_373.
```

It does not prove the diagonal-overlap branch.

## 8. What remains open

Still open:

```text
WeightedBetaEnergyTarget_373,
WeightedColumnMultiplicityTarget_372,
WeightedMixedAmplitudeTarget_372,
OverlapProfileAntiConcentrationTarget_371,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as an estimate,
NoTwistColumnProfileCorrelation_356(P_minor^0),
PairResidualFourierEnergyTarget_361,
SameFamilyPairVarianceNewInput_370,
SameFamilyPairBDHVarianceTarget_368,
AntiDiagonalRectangleVarianceTarget_360,
RectangleDefectLargeValueTarget_359,
PairResidualLargeValueTarget_359,
NoTwistWeightedMassCriterion_354,
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
Latest completed module: 373
Post-Reflective_1 solving count: 192
Long-term-plan count: 186

186 is not divisible by 9, so no plan update is due in this module.
186 is not divisible by 15, so no plan challenge is due in this module.
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
No full-gap, clipped-gap, tail, or empty-interval statement is used.
```

Local-factor check:

```text
The pair/rectangle coefficient split is used only subadditively. No exact
local factor is replaced by an averaged substitute.
```

Limit-order check:

```text
The proved identities are finite equalities or inequalities at fixed local
parameters. No N/w/D/R/eta limit is exchanged.
```

Uniformity check:

```text
The open weighted targets are required in the same coefficient, threshold,
dyadic shell, W-residue, and limiting family. They are not assumed.
```

Endpoint-circularity check:

```text
The proof does not assume SignedLocalModelInsertion_326, LocalModelInsertion_325,
PhaseKernelBound_273^0, NarrowMinorArc_3^B, ResCube_3^sharp, CPC_3^sharp,
RBDH_pair_short, AU^3, selector transfer, or full-gap transfer.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
WeightedColumnMultiplicityAudit_373(P_minor^0):
  STRUCTURAL / EXTRACTION.

WeightedColumnIncidenceIdentity_373:
  PROVEN.

WeightedColumnLayerCakeIdentity_373:
  PROVEN.

WeightedColumnSubadditiveSplit_373:
  PROVEN.

WeightedBetaEnergyCriterion_373:
  CONDITIONAL.

HolderColumnMomentCriterion_373:
  CONDITIONAL.

TopMassColumnTailCriterion_373:
  CONDITIONAL.

SupNormFirstIncidenceRoute_373:
  FALSE / BLOCKED.

ExistingPairRectangleSplitClosure_373:
  FALSE / BLOCKED.

CurrentWeightedColumnMultiplicityClosure_373:
  FALSE / BLOCKED.

WeightedBetaEnergyTarget_373:
  OPEN.

WeightedColumnMultiplicityTarget_372:
  OPEN.
```

Do not cite this module as proving weighted column multiplicity. It proves
finite identities and reductions, and it identifies the weighted beta-energy
row as the next smaller target.

## Red flags / forbidden upgrades

- Do not treat unweighted `E2_minor^0` as `WBetaEng_A`.
- Do not treat first-moment column tails as coefficient-weighted tails.
- Do not claim the pair/rectangle coefficient split estimates its rows.
- Do not use `WeightedBetaEnergyCriterion_373` as a theorem unless
  `WeightedBetaEnergyTarget_373` is proved in the same family.
- Keep the original selected-average problem, residual cube endpoint,
  `CPC_3^sharp`, `RBDH_pair_short`, and `AU^3` at their active open statuses.
