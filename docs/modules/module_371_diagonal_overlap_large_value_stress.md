# Module 371: Diagonal-overlap large-value stress test

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Best-module selection:

```text
The best current module is DiagonalOverlapLargeValueStress_371(P_minor^0).
```

Reason:

```text
Module 359 split the no-twist coefficient obstruction into pair-residual
large values, rectangle-defect large values, and diagonal-overlap large
values. Modules 360-370 stressed the rectangle-defect and pair-residual
branches to variance-strength obstructions. The diagonal-overlap row is now
the least directly tested branch of that split.
```

Define:

```text
DiagonalOverlapLargeValueStress_371(P_minor^0).
```

Verdict:

```text
DiagonalOverlapLargeValueStress_371(P_minor^0):
  STRUCTURAL / EXTRACTION.

DiagonalOverlapProfileIdentity_371:
  PROVEN.

DiagonalOverlapTopMassExtremalLemma_371:
  PROVEN.

DiagonalOverlapTopMassCriterion_371:
  CONDITIONAL.

FirstIncidenceDiagonalOverlapRoute_371:
  FALSE / BLOCKED.

CurrentDiagonalOverlapClosure_371:
  FALSE / BLOCKED.

OverlapProfileAntiConcentrationTarget_371:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful extraction is that the diagonal-overlap row is exactly a
one-profile coefficient top-mass problem. It is easier in shape than the
two-shift no-twist product row, because it carries only one overlap cap
instead of the product cap `K_UK_V`. But current first-incidence and
profile-ceiling data still do not prove smallness. A new same-family
anti-concentration or top-mass theorem is still needed.

## 2. Why this would advance the main theorem

The active branch is:

```text
NoTwistColumnProfileCorrelation_356
  -> coefficient top-mass / large-value control
  -> SignedLocalModelInsertion_326
  -> local minor-arc residual eight-slot package.
```

Module 356 separated the no-twist profile row into:

```text
D sum_xi |A(xi)|u_abs(xi)v_abs(xi)
+
sum_xi |A(xi)|o_abs(xi).
```

Module 358 reduced the first term to coefficient top mass against two column
profiles. Module 359 then kept the diagonal term as a separate row:

```text
DiagonalOverlapLargeValueTarget_359:
  sum_xi |A(xi)|o_abs(xi)=o_W(1).
```

If this module proved that target from existing threshold information, it
would remove the last untested piece of the Module 359 split. It does not.
Instead it proves the exact finite top-mass reduction for the overlap profile
and shows why current first-incidence ceilings cannot by themselves give the
needed `o_W(1)` estimate.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0},
mathcal D={d:D<|d|<=2D}.
```

Let `U,V` be admissible threshold masks with:

```text
|U(d,xi)|<=1,
|V(d,xi)|<=1.
```

Let:

```text
a(xi)=|A(xi)| >= 0,
xi in Minor_0(R,eta),
```

where `A` may be one of the same-family coefficients from Modules 350-351:

```text
A_Delta^350(xi),
E_+^0(xi)^2,
E_+^0(xi)K_+^0(xi),
RDef_+^0(xi).
```

Recall:

```text
n_U(xi)=sum_{d in mathcal D}|U(d,xi)|,
n_V(xi)=sum_{d in mathcal D}|V(d,xi)|,

u_abs(xi)=D^(-1)n_U(xi),
v_abs(xi)=D^(-1)n_V(xi),

o_abs(xi)=D^(-1)sum_{d in mathcal D}|U(d,xi)V(d,xi)|.
```

Define the exact diagonal-overlap profile:

```text
l_{U,V}(xi)
  =
  sum_{d in mathcal D}|U(d,xi)V(d,xi)|.
```

Then:

```text
o_abs(xi)=D^(-1)l_{U,V}(xi).
```

Set:

```text
I_O=sum_xi l_{U,V}(xi),
K_O=sup_xi l_{U,V}(xi).
```

If `K_O>0`, define:

```text
r_O=I_O/K_O,
m_O=ceil(r_O).
```

If `K_O=0`, set `r_O=m_O=0`.

Use the coefficient top-mass functionals:

```text
A_star(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E}a(xi),

A_star^cont(r)
  =
  sup {
    sum_xi a(xi)c(xi):
      0<=c(xi)<=1,
      sum_xi c(xi)<=r
  }.
```

## 4. Assumptions

This module assumes:

```text
Modules 350-370,
finite cyclic Fourier algebra,
finite rearrangement algebra,
and the active status ledger.
```

It does not assume:

```text
DiagonalOverlapLargeValueTarget_359,
OverlapProfileAntiConcentrationTarget_371,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
WeightedProfileSecondMomentCriterion_356,
NoTwistProductProfileCriterion_355,
NoTwistWeightedMassCriterion_354,
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
first-incidence overlap ceilings imply coefficient-weighted overlap,
the two-shift product top-mass criterion automatically controls diagonal
  overlap,
pair-residual or rectangle-defect variance controls the threshold overlap
  profile,
absolute overlap control follows from signed cancellation,
model-selector statements imply actual sharp moving-selector statements.
```

## 5. Proof / disproof / reduction

### A. Exact diagonal-overlap profile identity

By definition:

```text
sum_xi a(xi)o_abs(xi)
  =
  D^(-1)sum_xi a(xi)l_{U,V}(xi)
```

and:

```text
D^(-1)sum_xi a(xi)l_{U,V}(xi)
  =
  D^(-1)
  sum_{d in mathcal D}
  sum_{xi in Minor_0(R,eta)}
    a(xi)|U(d,xi)V(d,xi)|.
```

Classification:

```text
DiagonalOverlapProfileIdentity_371:
  PROVEN.
```

This is the exact same-shift overlap row. No oscillation in `d`, no signed
cancellation, and no local-model substitution has been introduced.

The overlap profile satisfies:

```text
0 <= l_{U,V}(xi) <= min(n_U(xi),n_V(xi)),
K_O <= min(K_U,K_V),
I_O <= min(I_U,I_V).
```

For shell masks, Module 355 gives the unweighted ceiling:

```text
D^(-1)I_O
  <=
  min(sigma_U^(-2),sigma_V^(-2))E2_minor^0(D;R,eta).
```

This ceiling is unweighted. It does not know where the large values of
`a(xi)` live.

### B. Diagonal-overlap top-mass extremal lemma

Assume first that `K_O>0`. Set:

```text
c(xi)=l_{U,V}(xi)/K_O.
```

Then:

```text
0 <= c(xi) <= 1,
sum_xi c(xi)=I_O/K_O=r_O.
```

Therefore, by the definition of `A_star^cont`:

```text
sum_xi a(xi)l_{U,V}(xi)
  =
  K_O sum_xi a(xi)c(xi)
  <=
  K_O A_star^cont(r_O).
```

Since:

```text
A_star^cont(r_O) <= A_star(ceil(r_O))=A_star(m_O),
```

we get:

```text
sum_xi a(xi)o_abs(xi)
  <=
  D^(-1)K_O A_star^cont(r_O)
  <=
  D^(-1)K_O A_star(m_O).
```

If `K_O=0`, both sides are zero by convention.

Sharpness from cap-and-total data:

Let `E` be a set of top coefficient frequencies with:

```text
#E=m <= floor(I_O/K_O).
```

The abstract overlap profile:

```text
l_{U,V}(xi)=K_O 1_E(xi)
```

with any leftover overlap mass placed away from `E`, obeys the same cap
`K_O` and total `I_O`, and realizes:

```text
D^(-1)sum_xi a(xi)l_{U,V}(xi)
  >=
  D^(-1)K_O sum_{xi in E}a(xi).
```

Thus cap-and-total data alone cannot beat the top-mass expression.

Classification:

```text
DiagonalOverlapTopMassExtremalLemma_371:
  PROVEN.
```

This is a finite extremal lemma. It is not a prime-distribution estimate.

### C. Conditional diagonal top-mass criterion

The diagonal-overlap target follows from:

```text
D^(-1)K_O A_star(m_O)=o_W(1)
```

uniformly over the admissible coefficient family, threshold masks, dyadic
shells, W-residue convention, minor-frequency set, and limiting order.

Equivalently, the target follows if there exists `q>1` such that:

```text
D^(-1)K_O m_O^(1-1/q)||A||_{q,minor}=o_W(1).
```

It also follows from the crude sup route:

```text
||A||_{infty,minor} I_O/D=o_W(1).
```

Classification:

```text
DiagonalOverlapTopMassCriterion_371:
  CONDITIONAL.
```

The criterion is strictly a sufficient condition. The current ledger does
not prove any of these estimates for the active coefficient family and the
active threshold schedules.

### D. Why first incidence alone is blocked

First incidence gives:

```text
I_O/D
  <=
  min(sigma_U^(-2),sigma_V^(-2))E2_minor^0(D;R,eta).
```

Together with a coefficient sup norm, this gives:

```text
sum_xi a(xi)o_abs(xi)
  <=
  ||A||_{infty,minor}
  min(sigma_U^(-2),sigma_V^(-2))E2_minor^0(D;R,eta).
```

The active ledger does not prove that this expression is `o_W(1)` for the
same coefficient, thresholds, dyadic shell, and limit order required by
`P_minor^0`.

More importantly, the sharpness in part B shows that any method using only:

```text
0 <= l_{U,V} <= K_O,
sum l_{U,V}=I_O
```

cannot rule out concentration of the overlap profile on the largest
coefficient frequencies. That is exactly the diagonal-overlap large-value
problem.

Classification:

```text
FirstIncidenceDiagonalOverlapRoute_371:
  FALSE / BLOCKED.
```

The blockage concerns this proof route. It does not disprove the desired
same-family diagonal-overlap theorem.

### E. Current diagonal-overlap verdict

The current ledger now has:

```text
DiagonalOverlapCeiling_355,
CoefficientTopMassProfileCriterion_356 as a conditional criterion,
FiniteTopMassExtremalLemma_358,
LayerCakeTopMassIdentity_359,
DiagonalOverlapProfileIdentity_371,
DiagonalOverlapTopMassExtremalLemma_371.
```

It does not have:

```text
D^(-1)K_O A_star(m_O)=o_W(1),
||A||_{infty,minor}I_O/D=o_W(1),
D^(-1)K_O m_O^(1-1/q)||A||_{q,minor}=o_W(1),
or an anti-concentration theorem separating l_{U,V} from the large values of A.
```

Therefore:

```text
CurrentDiagonalOverlapClosure_371:
  FALSE / BLOCKED.

OverlapProfileAntiConcentrationTarget_371:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
```

The next smaller target is not another first-incidence ceiling. It is a
same-family statement controlling the actual overlap profile:

```text
OverlapProfileAntiConcentrationTarget_371(P_minor^0):
  for the active coefficient family A and admissible threshold masks U,V,

  D^(-1)sum_xi |A(xi)|l_{U,V}(xi)=o_W(1),

  or equivalently a top-mass/Lorentz estimate strong enough to imply it
  through DiagonalOverlapTopMassExtremalLemma_371.
```

This target must be proved in the exact projection, cutoff, W-residue,
dyadic shell, selector class, denominator range, threshold schedule, and
limit order of `P_minor^0`.

## 6. Edge cases

### Empty masks and zero overlap

If `U` or `V` is empty, then `l_{U,V}=0` and the diagonal-overlap row is
zero. If the supports are disjoint for every `d`, the row is also zero. These
are valid edge cases but do not give uniform control over the active mask
family.

### Zero cap

If `K_O=0`, then `I_O=0` and the top-mass criterion is vacuous. The
definition `r_O=m_O=0` is used only to avoid division by zero.

### Fractional overlap profiles

The masks need only satisfy `|U|,|V|<=1`, so `l_{U,V}` may be fractional.
The continuous top-mass functional handles this exactly before passing to
`ceil(r_O)`.

### Small `K_O`

If a future module proves `K_O/D=o_W(1)` together with a usable total
coefficient bound, then diagonal overlap could be easier than the two-shift
product row. The current ledger does not prove such a uniform estimate.

### Signed cancellation

This module treats the absolute row from Module 356. A signed theorem may
bypass the absolute overlap only if it is proved in the same family and does
not assume the endpoint it is meant to support.

## 7. Project-map location

```text
NoTwistColumnProfileCorrelationAudit_356
  -> CoefficientTopMassFeasibility_358
  -> CoefficientLargeValueDistributionAudit_359
  -> DiagonalOverlapLargeValueStress_371
  -> OverlapProfileAntiConcentrationTarget_371.
```

This module finishes the first direct stress test of the three Module 359
branches:

```text
Rectangle-defect branch
  -> AntiDiagonalRectangleVarianceTarget_360.

Pair-residual branch
  -> SameFamilyPairBDHVarianceTarget_368
  -> PairResidualVarianceInputVerdict_370.

Diagonal-overlap branch
  -> OverlapProfileAntiConcentrationTarget_371.
```

The diagonal branch is not resolved. It is now reduced to one exact
overlap-profile top-mass target.

## 8. What remains open

Still open:

```text
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
Latest completed module: 371
Post-Reflective_1 solving count: 190
Long-term-plan count: 184

184 is not divisible by 9, so no plan update is due in this module.
184 is not divisible by 15, so no plan challenge is due in this module.
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
No pair, rectangle, or two-rectangle local factor is simplified. The module
concerns threshold overlap profiles only.
```

Limit-order check:

```text
The proved lemmas are finite inequalities at fixed local parameters. No
N/w/D/R/eta limit is exchanged.
```

Uniformity check:

```text
The open anti-concentration target is explicitly required in the same family
and limit order. It is not assumed.
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
DiagonalOverlapLargeValueStress_371(P_minor^0):
  STRUCTURAL / EXTRACTION.

DiagonalOverlapProfileIdentity_371:
  PROVEN.

DiagonalOverlapTopMassExtremalLemma_371:
  PROVEN.

DiagonalOverlapTopMassCriterion_371:
  CONDITIONAL.

FirstIncidenceDiagonalOverlapRoute_371:
  FALSE / BLOCKED.

CurrentDiagonalOverlapClosure_371:
  FALSE / BLOCKED.

OverlapProfileAntiConcentrationTarget_371:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
```

Do not cite this module as proving diagonal-overlap control. It proves only
the exact overlap-profile identity, the sharp top-mass extremal reduction,
and the blockage of first-incidence-only diagonal control.

## Red flags / forbidden upgrades

- Do not treat `DiagonalOverlapCeiling_355` as coefficient-weighted control.
- Do not treat `l_{U,V}` as spread out unless a same-family anti-concentration
  theorem is proved.
- Do not use product-profile top-mass control as a substitute for diagonal
  overlap unless the diagonal row is included explicitly.
- Do not infer actual sharp moving-selector control from `P_minor^0`.
- Keep the original selected-average problem, residual cube endpoint,
  `CPC_3^sharp`, `RBDH_pair_short`, and `AU^3` at their active open statuses.
