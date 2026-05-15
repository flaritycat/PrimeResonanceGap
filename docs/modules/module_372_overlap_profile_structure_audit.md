# Module 372: Overlap-profile structure audit

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Best-module selection:

```text
The best current module is OverlapProfileStructureAudit_372(P_minor^0).
```

Reason:

```text
Module 371 reduced the diagonal-overlap row to the exact overlap profile
l_{U,V}(xi). The next useful attack is to decide whether the actual
threshold-mask origin of l_{U,V} gives more than the abstract cap-and-total
top-mass obstruction, or whether the project needs a new coefficient-weighted
overlap theorem.
```

Define:

```text
OverlapProfileStructureAudit_372(P_minor^0).
```

Verdict:

```text
OverlapProfileStructureAudit_372(P_minor^0):
  STRUCTURAL / EXTRACTION.

ThresholdAmplitudeDomination_372:
  PROVEN.

SameSourceOverlapReduction_372:
  PROVEN.

WeightedMixedAmplitudeCriterion_372:
  CONDITIONAL.

WeightedColumnMultiplicityCriterion_372:
  CONDITIONAL.

UnweightedEnergyOverlapClosure_372:
  FALSE / BLOCKED.

CurrentOverlapProfileStructureClosure_372:
  FALSE / BLOCKED.

WeightedMixedAmplitudeTarget_372:
  OPEN.

WeightedColumnMultiplicityTarget_372:
  OPEN.

OverlapProfileAntiConcentrationTarget_371:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful conclusion is that the threshold origin of the overlap profile
does give two sharper formulations:

```text
1. a coefficient-weighted mixed-amplitude row;
2. in the same-source case, a coefficient-weighted column-multiplicity row.
```

Neither row is proved by the current ledger. The diagonal-overlap branch is
therefore not closed, but the missing input is now smaller and more concrete
than a generic anti-concentration statement.

## 2. Why this would advance the main theorem

The active branch is:

```text
NoTwistColumnProfileCorrelation_356
  -> coefficient top-mass / large-value control
  -> SignedLocalModelInsertion_326
  -> local minor-arc residual eight-slot package.
```

Module 371 showed that:

```text
sum_xi |A(xi)|o_abs(xi)
  =
  D^(-1)sum_xi |A(xi)|l_{U,V}(xi)
```

and that cap-and-total data reduce this to:

```text
D^(-1)K_O A_star(m_O).
```

This module asks whether the actual origin of `l_{U,V}` as an overlap of
threshold masks supplies a better proof route. The answer is partly yes:
threshold amplitudes give exact domination inequalities. But those
inequalities require coefficient-weighted mixed amplitude or weighted column
multiplicity estimates that are not in the ledger.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0},
mathcal D={d:D<|d|<=2D}.
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

Let `U,V` be admissible threshold masks with:

```text
|U(d,xi)|<=1,
|V(d,xi)|<=1.
```

The diagonal-overlap profile from Module 371 is:

```text
l_{U,V}(xi)
  =
  sum_{d in mathcal D}|U(d,xi)V(d,xi)|,

o_abs(xi)=D^(-1)l_{U,V}(xi).
```

For threshold-source functions `b_U,b_V` and levels `sigma_U,sigma_V>0`,
write the lower-threshold support condition as:

```text
|U(d,xi)| <= 1_{|b_U(d,xi)|>=sigma_U},
|V(d,xi)| <= 1_{|b_V(d,xi)|>=sigma_V}.
```

In the ordinary residual-derivative threshold case:

```text
b_U(d,xi)=beta_0(d,xi),
b_V(d,xi)=beta_0(d,xi),
```

possibly with different threshold levels or dyadic shell restrictions.

For `p,q>0`, define the coefficient-weighted mixed-amplitude row:

```text
MixAmp_A^{p,q}(b_U,b_V;sigma_U,sigma_V)
  =
  D^(-1)sigma_U^(-p)sigma_V^(-q)
  sum_{d in mathcal D}
  sum_{xi in Minor_0(R,eta)}
    a(xi)|b_U(d,xi)|^p|b_V(d,xi)|^q.
```

For a same-source lower threshold `b` at level `sigma`, define:

```text
N_b(xi;sigma)
  =
  # { d in mathcal D: |b(d,xi)|>=sigma }.
```

The coefficient-weighted column-multiplicity row is:

```text
ColAmp_A(b;sigma)
  =
  D^(-1)sum_xi a(xi)N_b(xi;sigma).
```

## 4. Assumptions

This module assumes:

```text
Modules 350-371,
the P_minor^0 threshold-mask conventions,
finite rearrangement algebra,
and the active status ledger.
```

It does not assume:

```text
WeightedMixedAmplitudeTarget_372,
WeightedColumnMultiplicityTarget_372,
OverlapProfileAntiConcentrationTarget_371,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
NoTwistProductProfileCriterion_355,
NoTwistWeightedMassCriterion_354,
ColumnMultiplicityGainTarget_308,
ColumnTailGainTarget_309,
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
unweighted beta_0 energy implies coefficient-weighted overlap,
column multiplicity tails imply coefficient-weighted column multiplicity
  without a correlation theorem,
same-source shell disjointness covers all admissible mask pairs,
the diagonal-overlap row is automatic because it has only one shift variable,
model-selector statements imply actual sharp moving-selector statements.
```

## 5. Proof / disproof / reduction

### A. Threshold-amplitude domination

Assume:

```text
|U(d,xi)| <= 1_{|b_U(d,xi)|>=sigma_U},
|V(d,xi)| <= 1_{|b_V(d,xi)|>=sigma_V}.
```

For any `p,q>0`:

```text
1_{|b_U|>=sigma_U}1_{|b_V|>=sigma_V}
  <=
  (|b_U|/sigma_U)^p(|b_V|/sigma_V)^q.
```

Therefore:

```text
|U(d,xi)V(d,xi)|
  <=
  sigma_U^(-p)sigma_V^(-q)
  |b_U(d,xi)|^p|b_V(d,xi)|^q.
```

Multiplying by `a(xi)`, summing over `(d,xi)`, and normalizing by `D` gives:

```text
sum_xi a(xi)o_abs(xi)
  =
  D^(-1)sum_{d,xi}a(xi)|U(d,xi)V(d,xi)|
  <=
  MixAmp_A^{p,q}(b_U,b_V;sigma_U,sigma_V).
```

Classification:

```text
ThresholdAmplitudeDomination_372:
  PROVEN.
```

This is an exact finite domination inequality. It uses the threshold origin
of the masks and is stronger than forgetting the amplitudes completely. It
does not estimate the mixed-amplitude row.

### B. Same-source overlap reduction

Suppose both masks come from the same source `b` with lower thresholds:

```text
|U(d,xi)| <= 1_{|b(d,xi)|>=sigma_U},
|V(d,xi)| <= 1_{|b(d,xi)|>=sigma_V}.
```

Let:

```text
sigma_* = max(sigma_U,sigma_V).
```

Then:

```text
|U(d,xi)V(d,xi)|
  <=
  1_{|b(d,xi)|>=sigma_*}.
```

Thus:

```text
l_{U,V}(xi)
  <=
  N_b(xi;sigma_*),
```

and:

```text
sum_xi a(xi)o_abs(xi)
  <=
  D^(-1)sum_xi a(xi)N_b(xi;sigma_*)
  =
  ColAmp_A(b;sigma_*).
```

If the two masks are half-open dyadic shells for the same source and the
shell intervals are disjoint, then:

```text
U(d,xi)V(d,xi)=0
```

for every `(d,xi)`, and the diagonal-overlap row is zero for that pair of
shells.

Classification:

```text
SameSourceOverlapReduction_372:
  PROVEN.
```

This is useful only for mask pairs that genuinely come from the same
threshold source and compatible shell convention. Mixed-source masks still
require the mixed-amplitude row from part A.

### C. Conditional weighted amplitude and column criteria

By part A, diagonal-overlap control follows from:

```text
MixAmp_A^{p,q}(b_U,b_V;sigma_U,sigma_V)=o_W(1)
```

for some fixed exponents `p,q>0`, uniformly in the same family and limiting
order.

Classification:

```text
WeightedMixedAmplitudeCriterion_372:
  CONDITIONAL.
```

In the same-source lower-threshold case, part B gives the sufficient row:

```text
ColAmp_A(b;sigma_*)=o_W(1).
```

Classification:

```text
WeightedColumnMultiplicityCriterion_372:
  CONDITIONAL.
```

These are smaller than the generic overlap anti-concentration target because
they retain the threshold amplitude or same-source column multiplicity. They
are not currently proved.

### D. Cauchy variants and why they do not close with current inputs

For `p=q=1`, Cauchy gives:

```text
sum_{d,xi} a(xi)|b_U(d,xi)b_V(d,xi)|
  <=
  (
    sum_{d,xi} a(xi)|b_U(d,xi)|^2
  )^(1/2)
  (
    sum_{d,xi} a(xi)|b_V(d,xi)|^2
  )^(1/2).
```

Thus a sufficient row is:

```text
D^(-1)(sigma_U sigma_V)^(-1)
  (
    WEng_A(b_U)
  )^(1/2)
  (
    WEng_A(b_V)
  )^(1/2)
  =
  o_W(1),
```

where:

```text
WEng_A(b)
  =
  sum_{d in mathcal D}
  sum_{xi in Minor_0(R,eta)}
    a(xi)|b(d,xi)|^2.
```

The current ledger has unweighted energy controls such as:

```text
D^(-1)sum_{d,xi}|beta_0(d,xi)|^2
  =
  E2_minor^0(D;R,eta),
```

and low-level fourth-moment tail controls from Module 297. It does not prove
the coefficient-weighted energy:

```text
D^(-1)WEng_A(beta_0)=o_W(sigma_U sigma_V)
```

or any comparable estimate at the active threshold levels.

Using a coefficient sup norm gives only:

```text
sum_xi a(xi)o_abs(xi)
  <=
  ||A||_{infty,minor}
  D^(-1)sum_{d,xi}|U(d,xi)V(d,xi)|.
```

This returns to the unweighted diagonal-overlap ceiling from Module 355 and
is not known to be `o_W(1)` in the active range.

Classification:

```text
UnweightedEnergyOverlapClosure_372:
  FALSE / BLOCKED.
```

The obstacle is not algebraic ignorance of the masks. It is the missing
coefficient-weighted correlation between the active coefficient `A(xi)` and
the actual threshold amplitudes or column multiplicities.

### E. Current structure verdict

The actual threshold structure gives:

```text
ThresholdAmplitudeDomination_372,
SameSourceOverlapReduction_372,
WeightedMixedAmplitudeCriterion_372,
WeightedColumnMultiplicityCriterion_372.
```

The ledger does not give:

```text
MixAmp_A^{p,q}(b_U,b_V;sigma_U,sigma_V)=o_W(1),
ColAmp_A(b;sigma)=o_W(1),
D^(-1)WEng_A(beta_0)=o_W(sigma_U sigma_V),
or coefficient-weighted column tail decay for N_b(xi;sigma).
```

Therefore:

```text
CurrentOverlapProfileStructureClosure_372:
  FALSE / BLOCKED.

WeightedMixedAmplitudeTarget_372:
  OPEN.

WeightedColumnMultiplicityTarget_372:
  OPEN.

OverlapProfileAntiConcentrationTarget_371:
  OPEN.
```

The best next attack is to choose the smallest of these new targets. The
same-source column row is most concrete when both masks arise from the same
`beta_0` threshold family:

```text
WeightedColumnMultiplicityTarget_372(beta_0;sigma):
  D^(-1)sum_xi |A(xi)|N_{beta_0}(xi;sigma)=o_W(1).
```

This target should be audited before returning to broader mixed-source
overlap language.

## 6. Edge cases

### Disjoint dyadic shells

If `U` and `V` are half-open dyadic shells of the same source and their shell
intervals do not intersect, then `l_{U,V}=0`. This is a real simplification
for those shell pairs only. It does not handle mixed-source masks or nested
threshold masks.

### Nested thresholds

If one same-source threshold is stronger than the other, the overlap is
bounded by the stronger threshold column multiplicity. This may reduce
`K_O` and `I_O`, but coefficient-weighted control of the surviving columns
is still required.

### Fractional masks

The domination inequalities use only `|U|,|V|<=1` and support containment.
They remain valid for fractional masks.

### Zero threshold source

If `b_U` or `b_V` vanishes on a row, the mixed-amplitude bound gives zero on
that row. This is local bookkeeping, not uniform closure.

### Coefficient-free overlap

Unweighted overlap estimates may be useful for bookkeeping, but the target is
coefficient-weighted. Dropping `a(xi)` is harmless only if a strong enough
coefficient norm is separately proved.

## 7. Project-map location

```text
DiagonalOverlapLargeValueStress_371
  -> OverlapProfileStructureAudit_372
  -> WeightedColumnMultiplicityTarget_372
  -> NoTwistColumnProfileCorrelation_356.
```

The branch now has three levels:

```text
abstract overlap top mass:
  D^(-1)K_O A_star(m_O);

threshold-amplitude row:
  MixAmp_A^{p,q};

same-source column row:
  D^(-1)sum_xi |A(xi)|N_{beta_0}(xi;sigma).
```

The third row is the most concrete next target when the masks have the same
`beta_0` source.

## 8. What remains open

Still open:

```text
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
Latest completed module: 372
Post-Reflective_1 solving count: 191
Long-term-plan count: 185

185 is not divisible by 9, so no plan update is due in this module.
185 is not divisible by 15, so no plan challenge is due in this module.
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
No pair, rectangle, or two-rectangle local factor is replaced. This module
concerns only threshold-mask overlap profiles.
```

Limit-order check:

```text
The proved rows are finite inequalities at fixed local parameters. No
N/w/D/R/eta limit is exchanged.
```

Uniformity check:

```text
The open weighted targets are required in the same coefficient, mask,
threshold, dyadic shell, W-residue, and limiting family. They are not assumed.
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
OverlapProfileStructureAudit_372(P_minor^0):
  STRUCTURAL / EXTRACTION.

ThresholdAmplitudeDomination_372:
  PROVEN.

SameSourceOverlapReduction_372:
  PROVEN.

WeightedMixedAmplitudeCriterion_372:
  CONDITIONAL.

WeightedColumnMultiplicityCriterion_372:
  CONDITIONAL.

UnweightedEnergyOverlapClosure_372:
  FALSE / BLOCKED.

CurrentOverlapProfileStructureClosure_372:
  FALSE / BLOCKED.

WeightedMixedAmplitudeTarget_372:
  OPEN.

WeightedColumnMultiplicityTarget_372:
  OPEN.

OverlapProfileAntiConcentrationTarget_371:
  OPEN.
```

Do not cite this module as proving diagonal-overlap control. It proves only
finite domination and same-source reduction lemmas, and it identifies the
new coefficient-weighted rows that remain open.

## Red flags / forbidden upgrades

- Do not treat unweighted `E2_minor^0` as coefficient-weighted overlap
  control.
- Do not assume the active coefficient is anti-correlated with threshold
  columns.
- Do not apply same-source shell simplifications to mixed-source mask pairs.
- Do not convert `WeightedMixedAmplitudeCriterion_372` or
  `WeightedColumnMultiplicityCriterion_372` into a theorem without the
  required same-family estimate.
- Keep the original selected-average problem, residual cube endpoint,
  `CPC_3^sharp`, `RBDH_pair_short`, and `AU^3` at their active open statuses.
