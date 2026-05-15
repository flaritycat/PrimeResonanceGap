# Module 359: Coefficient large-value distribution attack

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Module 358 proved that cap-and-total profile data reduce sharply to a
coefficient top-mass functional. This module attacks the next question:

```text
CoefficientLargeValueDistributionAudit_359(P_minor^0).
```

The target is to decide whether current coefficient-side information proves
the large-value/top-mass input needed for:

```text
CoefficientTopMassProfileCriterion_356(P_minor^0).
```

Verdict:

```text
CoefficientLargeValueDistributionAudit_359(P_minor^0):
  STRUCTURAL / EXTRACTION.

LayerCakeTopMassIdentity_359:
  PROVEN.

SubadditiveCoefficientTopMassSplit_359:
  PROVEN.

CurrentCoefficientLargeValueClosure_359:
  FALSE / BLOCKED.

PairResidualLargeValueTarget_359:
  OPEN.

RectangleDefectLargeValueTarget_359:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful conclusion is that the coefficient top-mass problem has an exact
large-value formulation and an exact subadditive split into pair-residual and
rectangle-defect large-value targets. Current identities, first-moment local
model inputs, and Parseval/logarithmic envelopes do not prove the needed
distribution estimate.

## 2. Why this would advance the main theorem

The active local branch is:

```text
NoTwistColumnProfileCorrelation_356
  -> SignedLocalModelInsertion_326
  -> local minor-arc residual eight-slot package
  -> residual derivative cube endpoint branch.
```

The no-twist row is hard because it has no shift oscillation. Module 358
proved that column caps and total incidences alone force one to face:

```text
A_star(m),
```

the mass of the largest `m` coefficient frequencies.

If this module proved the needed large-value distribution for the active
coefficient, it would supply a genuine new input toward the no-twist
profile-correlation row. It does not. Instead it replaces the vague target
"prove coefficient distribution" by an exact layer-cake condition and splits
that condition across the exact Module 351 pair/rectangle decomposition.

## 3. Exact assumptions allowed

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

where the active coefficient may be:

```text
A_Delta^350(xi),
E_+^0(xi)^2,
E_+^0(xi)K_+^0(xi),
RDef_+^0(xi),
```

as in Modules 350-351.

For `m>=0`, define:

```text
A_star(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} a(xi).
```

Define the large-value counting function:

```text
N_A(T)
  =
  # { xi in Minor_0(R,eta): a(xi)>T },
  T>=0.
```

The Module 358 profile-size parameter is:

```text
r_{U,V}=min(I_U/K_U,I_V/K_V),
m_{U,V}=ceil(r_{U,V}),
```

with the convention that an empty mask gives zero contribution.

## 4. Exact assumptions forbidden

This module does not assume:

```text
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
WeightedProfileSecondMomentCriterion_356,
NoTwistProductProfileCriterion_355,
NoTwistWeightedMassCriterion_354,
MaskBudgetCriteria_352,
AntiDiagonalPairPairRows_350,
PairResidualCriteria_351,
RectangleDefectCoefficientCriterion_351,
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
first-moment pair HL => coefficient large-value control,
first-moment rectangle HL => rectangle-defect large-value control,
ordinary pair-BDH => masked coefficient top-mass control,
Parseval/logarithmic envelopes => top-mass smallness at active mask scale.
```

## 5. Proof attempt

### A. Exact layer-cake identity for top mass

Let `Omega` be a finite set and `a:Omega -> [0,infty)`. For:

```text
N_a(T)=#{xi in Omega: a(xi)>T},
```

and integer `m>=0`, one has:

```text
A_star(m)
  =
  int_0^infty min(N_a(T),m) dT.
```

Proof:

Let the values of `a` be rearranged in nonincreasing order:

```text
a_1 >= a_2 >= ... >= a_M >= 0,
```

where `M=#Omega`. Then:

```text
A_star(m)=sum_{j=1}^{min(m,M)} a_j.
```

For every `T>=0`,

```text
min(N_a(T),m)
  =
  sum_{j=1}^{min(m,M)} 1_{a_j>T}.
```

Integrating and using the elementary identity:

```text
int_0^infty 1_{a_j>T} dT = a_j
```

gives:

```text
int_0^infty min(N_a(T),m)dT
  =
  sum_{j=1}^{min(m,M)} a_j
  =
  A_star(m).
```

Classification:

```text
LayerCakeTopMassIdentity_359:
  PROVEN.
```

Consequently, the exact coefficient large-value target required by Module
358 is:

```text
D^(-1)K_UK_V
  int_0^infty min(N_A(T),m_{U,V}) dT
+
sum_xi a(xi)o_abs(xi)
  =
  o_W(1).
```

This is an equivalence for the top-mass term, not an estimate.

### B. Moment consequences and their sharpness

For `q>1`, Markov and layer-cake give:

```text
A_star(m) <= m^(1-1/q)||A||_{q,minor}.
```

This is sharp at the finite level. If `a` is constant of size `B` on exactly
`m` points and zero elsewhere, then:

```text
A_star(m)=mB,
||A||_{q,minor}=m^(1/q)B,
```

so equality holds in the displayed bound.

Thus an `L^q` route must prove the exact scale:

```text
||A||_{q,minor}
  =
  o_W(D/(K_UK_V m_{U,V}^{1-1/q})).
```

Current project inputs do not contain such a same-family coefficient
large-value or high-moment theorem for `A_Delta^350`, its pair-residual
pieces, or the rectangle-defect piece.

### C. Subadditive split across the exact coefficient decomposition

For nonnegative functions `a_1,...,a_s` on the same finite set:

```text
a <= a_1+...+a_s
```

implies:

```text
A_star,a(m)
  <=
  A_star,a_1(m)+...+A_star,a_s(m).
```

Proof:

For any `E` with `#E<=m`,

```text
sum_{xi in E} a(xi)
  <=
  sum_{j=1}^s sum_{xi in E} a_j(xi)
  <=
  sum_{j=1}^s A_star,a_j(m).
```

Take the supremum over `E`.

Classification:

```text
SubadditiveCoefficientTopMassSplit_359:
  PROVEN.
```

Apply this to the Module 351 identity:

```text
A_Delta^351(xi)
  =
  E_+^0(xi)^2
  +2E_+^0(xi)K_+^0(xi)
  +RDef_+^0(xi).
```

Then:

```text
A_star,|A_Delta^351|(m)
  <=
  A_star,|E_+^0|^2(m)
  +2 A_star,|E_+^0K_+^0|(m)
  +A_star,|RDef_+^0|(m).
```

Therefore coefficient top-mass can be proved by the following three
same-family targets, plus diagonal-overlap control:

```text
D^(-1)K_UK_V A_star,|E_+^0|^2(m_{U,V}) = o_W(1),

D^(-1)K_UK_V A_star,|E_+^0K_+^0|(m_{U,V}) = o_W(1),

D^(-1)K_UK_V A_star,|RDef_+^0|(m_{U,V}) = o_W(1).
```

This is a real dependency split. It shows that the large-value problem is not
a single amorphous coefficient estimate; it divides into pair-residual
large values and rectangle-defect large values.

### D. Why current coefficient identities do not close the target

Module 350 gives:

```text
A_Delta^350(xi)=|widehat{nu_0}(xi)|^4-C_w^0(xi).
```

Module 351 gives:

```text
A_Delta^351(xi)
  =
  E_+^0(xi)^2
  +2E_+^0(xi)K_+^0(xi)
  +RDef_+^0(xi).
```

These are identities. They do not bound:

```text
int_0^infty min(N_A(T),m_{U,V})dT.
```

The logarithmic envelope from Module 297 gives pointwise polynomial-log
ceilings for the prime-only model coefficients. Such ceilings imply only:

```text
A_star(m_{U,V})
  <=
  m_{U,V} ||A||_{infty,minor}.
```

At the no-twist scale this becomes:

```text
D^(-1)K_UK_V m_{U,V} ||A||_{infty,minor},
```

which is not known to be `o_W(1)` under the active threshold schedules.

Total-mass information would give:

```text
A_star(m_{U,V}) <= ||A||_{1,minor},
```

but the current ledger does not prove an `L^1` coefficient bound strong
enough to absorb `K_UK_V/D`, and such a bound would ignore the small-set
nature of top mass.

First-moment pair or rectangle Hardy-Littlewood inputs control average local
densities. They do not control the sorted frequency mass of:

```text
E_+^0(xi)^2,
E_+^0(xi)K_+^0(xi),
RDef_+^0(xi),
```

against data-dependent threshold masks.

Classification:

```text
CurrentCoefficientLargeValueClosure_359:
  FALSE / BLOCKED.
```

### E. Exact smaller targets after the split

The pair-residual large-value targets are:

```text
PairResidualSquareTopMass_359:
  A_star,|E_+^0|^2(m_{U,V})
  =
  o_W(D/(K_UK_V)).

PairResidualLinearModelTopMass_359:
  A_star,|E_+^0K_+^0|(m_{U,V})
  =
  o_W(D/(K_UK_V)).
```

Classification:

```text
PairResidualLargeValueTarget_359:
  OPEN.
```

The rectangle-defect large-value target is:

```text
RectangleDefectLargeValueTarget_359:
  A_star,|RDef_+^0|(m_{U,V})
  =
  o_W(D/(K_UK_V)).
```

Classification:

```text
RectangleDefectLargeValueTarget_359:
  OPEN.
```

The diagonal-overlap target remains:

```text
DiagonalOverlapLargeValueTarget_359:
  sum_xi |A(xi)|o_abs(xi)=o_W(1).
```

Classification:

```text
DiagonalOverlapLargeValueTarget_359:
  OPEN.
```

The next attack should not return to generic coefficient language. It should
test one of these smaller rows directly. The cleanest next target is:

```text
RectangleDefectLargeValueStress_360(P_minor^0),
```

because it asks whether the exact local rectangle defect has any exploitable
structure beyond the pair-residual rows, while preserving the rule that
`Sigma_w(d,h)` and higher local factors may not be replaced by pair products.

## 6. Places where current tools fail

Current tools fail at three precise points.

First, they do not give a strong enough distribution theorem:

```text
N_A(T)
```

for the active coefficient family.

Second, they do not prove high-moment estimates at the scale:

```text
||A||_{q,minor}
  =
  o_W(D/(K_UK_V m_{U,V}^{1-1/q})).
```

Third, they do not control the diagonal-overlap term:

```text
sum_xi |A(xi)|o_abs(xi).
```

Pair-BDH, first-moment pair HL, first-moment rectangle HL, and current
Parseval/logarithmic envelopes do not fill these gaps. Using them as if they
did would assume the kind of endpoint-strength frequency distribution this
branch is trying to prove.

## 7. New lemma proved

Two finite lemmas are proved:

```text
LayerCakeTopMassIdentity_359:
  PROVEN.

SubadditiveCoefficientTopMassSplit_359:
  PROVEN.
```

They are finite rearrangement facts. They may be used as local algebraic
tools in later modules, but they are not prime-distribution estimates.

## 8. Dependency reduced or removed

The dependency:

```text
CoefficientLargeValueDistributionAudit_359
```

is reduced to:

```text
1. pair-residual square top mass,
2. pair-residual times exact pair-model top mass,
3. rectangle-defect top mass,
4. diagonal-overlap large-value control.
```

This removes the ambiguity in the phrase "coefficient-side distribution".
The next module can attack a named row rather than the entire coefficient at
once.

## 9. Red-team audit

Selector check:

```text
All statements remain inside P_minor^0. No actual sharp moving-selector
statement is proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, or tail average is used.
```

Local-factor check:

```text
The exact pair and rectangle distinction is preserved. The rectangle-defect
row is kept as RDef_+^0. No pointwise replacement of a rectangle local model
by pair products is made.
```

Limit-order check:

```text
The finite lemmas are pointwise in the local parameters. No N, w, D, R, eta,
cutoff, or W-limit exchange is performed.
```

Uniformity check:

```text
The reductions identify uniform targets but prove no W-uniform prime
estimate for those targets.
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
CoefficientLargeValueDistributionAudit_359(P_minor^0):
  STRUCTURAL / EXTRACTION.

LayerCakeTopMassIdentity_359:
  PROVEN.

SubadditiveCoefficientTopMassSplit_359:
  PROVEN.

CurrentCoefficientLargeValueClosure_359:
  FALSE / BLOCKED.

PairResidualLargeValueTarget_359:
  OPEN.

RectangleDefectLargeValueTarget_359:
  OPEN.

DiagonalOverlapLargeValueTarget_359:
  OPEN.
```

The proof attack does not close the coefficient top-mass row. It proves the
exact distribution formulation and the exact coefficient split that any
future proof must satisfy.

## Edge cases

Empty masks:

```text
If one mask is empty, the no-twist product and diagonal overlap vanish. The
large-value target is then irrelevant for that mask pair.
```

Zero or tiny `m_{U,V}`:

```text
If `m_{U,V}=0`, the top-mass term is zero. If `m_{U,V}` is bounded, pointwise
coefficient smallness may suffice, but the current threshold schedules do not
force this uniformly.
```

Fractional profile scale:

```text
Module 358 used a continuous top-mass functional before passing to
ceil(r_{U,V}). This module states the layer-cake identity for integer m.
The continuous version follows by adding the appropriate fractional next
coefficient.
```

Signed cancellation:

```text
This module attacks an absolute top-mass route. A signed theorem could bypass
some absolute top-mass terms only if proved in the exact same projection,
cutoff, W-residue, dyadic shell, selector class, and limiting family.
```

## Project-map location

```text
NoTwistColumnProfileCorrelationAudit_356
  -> SignedInsertionRouteDecision_357
  -> CoefficientTopMassFeasibility_358
  -> CoefficientLargeValueDistributionAudit_359
  -> RectangleDefectLargeValueStress_360.
```

This module is a proof attack on the first new-input route after the
signed-insertion block. It narrows the branch but does not close it.

## What remains open

Still open:

```text
RectangleDefectLargeValueStress_360(P_minor^0),
PairResidualLargeValueTarget_359,
RectangleDefectLargeValueTarget_359,
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

- Do not cite the layer-cake identity as coefficient smallness.
- Do not cite the subadditive split as pair-residual or rectangle-defect
  control.
- Do not replace the rectangle local factor by a product of pair factors.
- Do not treat first-moment local densities as sorted-frequency estimates.
- Do not use an endpoint-strength large-value theorem as an assumption in a
  proof advertised as proving that endpoint.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
