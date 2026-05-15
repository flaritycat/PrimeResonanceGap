# Module 358: Proof attack on coefficient top-mass feasibility

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route.
```

The target is the coefficient top-mass route isolated in Module 356 and
selected by Module 357:

```text
CoefficientTopMassProfileCriterion_356(P_minor^0).
```

The proof-attack claim is:

```text
CapTotalTopMassClosure_358(P_minor^0):
  FALSE / BLOCKED.
```

More precisely, the cap-and-total information currently available for the
threshold column profiles cannot by itself imply the coefficient top-mass
smallness needed for the no-twist profile-correlation row. A separate
same-family large-value distribution theorem for the active coefficient is
required.

The module also proves a finite combinatorial lemma:

```text
FiniteTopMassExtremalLemma_358:
  PROVEN.
```

This lemma is local and combinatorial. It is not a theorem about primes, the
actual selector, the residual cube endpoint, or the original selected-average
problem.

## 2. Why this would advance the main theorem

The current Phase K branch is trying to insert the local model into the
minor-arc residual eight-slot row. Modules 346-357 reduced part of that
problem to masked anti-diagonal coefficient rows. The no-twist mask is the
hardest offset because it has no useful oscillation in the shift variable.

Module 356 showed that the no-twist row would follow from a same-family
coefficient-weighted column-profile correlation estimate, and that one
possible route is coefficient top-mass control.

If this module had proved top-mass smallness, it would have supplied a real
new input toward:

```text
NoTwistColumnProfileCorrelation_356
  -> SignedLocalModelInsertion_326
  -> local minor-arc obstruction package
  -> residual derivative cube endpoint branch.
```

Instead it proves that the current cap-and-total threshold data are too weak
to supply that input. This is still progress: it removes a tempting but
circular proof route and sharpens the next analytic target to a genuine
large-value theorem for the coefficient.

## 3. Exact assumptions allowed

Work inside the local model family:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
mathcal D={d:D<|d|<=2D},
Minor_0(R,eta) subset G_N \ {0}.
```

Let the active coefficient be:

```text
a(xi)=|A(xi)| >= 0,
xi in Minor_0(R,eta),
```

where `A` may be one of the same-family coefficients from Modules 350-351,
for example:

```text
A_Delta^350(xi),
E_+^0(xi)^2,
E_+^0(xi)K_+^0(xi),
RDef_+^0(xi).
```

Let the threshold column profiles be:

```text
n_U(xi)=sum_{d in mathcal D} |U(d,xi)|,
n_V(xi)=sum_{d in mathcal D} |V(d,xi)|,

u_abs(xi)=D^(-1)n_U(xi),
v_abs(xi)=D^(-1)n_V(xi),

o_abs(xi)=D^(-1)sum_d |U(d,xi)V(d,xi)|.
```

The current threshold ledger supplies only cap-and-total information of the
form:

```text
0 <= n_U(xi) <= K_U,
0 <= n_V(xi) <= K_V,

I_U=sum_xi n_U(xi),
I_V=sum_xi n_V(xi),

K_U <= K_0(lambda_U),
K_V <= K_0(lambda_V),

I_U <= D sigma_U^(-2) E2_minor^0(D;R,eta),
I_V <= D sigma_V^(-2) E2_minor^0(D;R,eta).
```

For `m>=0`, define the discrete top-mass functional:

```text
A_star(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} a(xi).
```

Also define the continuous top-mass functional:

```text
A_star^cont(r)
  =
  sup {
    sum_xi a(xi)c(xi):
      0 <= c(xi) <= 1,
      sum_xi c(xi) <= r
  }.
```

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

The argument also forbids the following proof shortcut:

```text
"Because threshold masks have bounded total mass and bounded columns,
their coefficient-weighted product is automatically small."
```

That shortcut is false at the profile level unless a coefficient top-mass or
large-value estimate is supplied.

## 5. Proof attempt

### A. The finite extremal lemma

Let `Omega` be a finite set, let `a:Omega -> [0,infty)`, and let:

```text
0 <= p(xi) <= 1,
0 <= q(xi) <= 1,
P=sum_xi p(xi),
Q=sum_xi q(xi),
r=min(P,Q).
```

Then:

```text
sum_xi a(xi)p(xi)q(xi)
  <=
  A_star^cont(r)
  <=
  A_star(ceil(r)).
```

Proof:

Set:

```text
c(xi)=p(xi)q(xi).
```

Then:

```text
0 <= c(xi) <= 1,
c(xi) <= p(xi),
c(xi) <= q(xi).
```

Therefore:

```text
sum_xi c(xi)
  <=
  min(sum_xi p(xi), sum_xi q(xi))
  =
  r.
```

By the definition of `A_star^cont(r)`,

```text
sum_xi a(xi)p(xi)q(xi)
  =
  sum_xi a(xi)c(xi)
  <=
  A_star^cont(r).
```

The second inequality follows because the maximum of the linear functional
`sum a(xi)c(xi)` over the polytope:

```text
0 <= c(xi) <= 1,
sum_xi c(xi) <= r
```

is obtained by placing mass on the largest values of `a`. Its value is the
sum of the largest `floor(r)` values plus at most one fractional next value,
which is bounded by the sum of the largest `ceil(r)` values. Hence:

```text
A_star^cont(r) <= A_star(ceil(r)).
```

This proves the lemma.

Sharpness:

If `r` is an integer and `E` is a set of `r` frequencies on which the top
mass is attained, then choosing:

```text
p=1_E,
q=1_E
```

gives:

```text
sum_xi a(xi)p(xi)q(xi)=A_star(r).
```

Thus the lemma cannot be improved using only the pointwise caps and the two
total masses. Any improvement must use additional structure of `a`, `U`, `V`,
or their coupling.

Classification:

```text
FiniteTopMassExtremalLemma_358:
  PROVEN.
```

### B. Application to the no-twist profile product

Apply the lemma with:

```text
Omega=Minor_0(R,eta),
p(xi)=n_U(xi)/K_U,
q(xi)=n_V(xi)/K_V.
```

For empty masks or zero caps the product row is zero, so assume here that
`K_U,K_V>0`.

Then:

```text
P=I_U/K_U,
Q=I_V/K_V,
r_{U,V}=min(I_U/K_U,I_V/K_V).
```

The no-twist off-diagonal product term satisfies:

```text
D sum_xi a(xi)u_abs(xi)v_abs(xi)
  =
  D^(-1) sum_xi a(xi)n_U(xi)n_V(xi)
```

and hence:

```text
D sum_xi a(xi)u_abs(xi)v_abs(xi)
  <=
  D^(-1)K_UK_V A_star^cont(r_{U,V})
  <=
  D^(-1)K_UK_V A_star(ceil(r_{U,V})).
```

This gives a correct version of the top-mass sufficient criterion:

```text
D^(-1)K_UK_V A_star(ceil(r_{U,V}))
+
sum_xi a(xi)o_abs(xi)
  =
  o_W(1)
```

where:

```text
r_{U,V}=min(I_U/K_U,I_V/K_V).
```

The criterion is not yet an estimate. It is a sharp finite reduction from
cap-and-total profile data to coefficient top mass.

### C. Why cap-and-total closure is blocked

The lemma is sharp at the profile level. Therefore a proof using only:

```text
0 <= n_U <= K_U,
0 <= n_V <= K_V,
sum n_U=I_U,
sum n_V=I_V
```

cannot replace `A_star(ceil(r_{U,V}))` by a smaller quantity.

Indeed, if a set `E` of size `m <= floor(r_{U,V})` carries large coefficient
mass, then the profile-level choice:

```text
n_U=K_U 1_E,
n_V=K_V 1_E
```

with harmless leftover mass placed away from the top coefficients, when
needed, obeys the same cap constraints and realizes:

```text
D^(-1)sum_xi a(xi)n_U(xi)n_V(xi)
  >=
  D^(-1)K_UK_V sum_{xi in E}a(xi).
```

Thus the cap-and-total method can be small only if the active coefficient has
small top mass on all sets of the relevant size, or if one proves a separate
overlap/correlation theorem tying the actual masks away from the large
coefficient frequencies.

Classification:

```text
CapTotalTopMassClosure_358(P_minor^0):
  FALSE / BLOCKED.
```

This is a blockage proof for the proof route, not a disproof of the desired
coefficient top-mass theorem.

### D. Lorentz and large-value routes that remain viable

For `1<q<infinity`, Holder gives:

```text
A_star(m) <= m^(1-1/q)||A||_{q,minor}.
```

So the top-mass route would follow from:

```text
D^(-1)K_UK_V ceil(r_{U,V})^(1-1/q)||A||_{q,minor}
+
sum_xi a(xi)o_abs(xi)
  =
  o_W(1).
```

Equivalently, one may prove a large-value distribution bound for:

```text
N_A(T)=#{xi in Minor_0(R,eta): a(xi)>T}
```

strong enough to control the integral of the decreasing rearrangement of
`a` over the first `ceil(r_{U,V})` frequencies.

Classification:

```text
LorentzTopMassRoute_358:
  CONDITIONAL.

CoefficientLargeValueDistributionTarget_358:
  OPEN.
```

These routes are genuine possible attacks. They are not supplied by the
current coefficient identities.

## 6. Places where current tools fail

Current coefficient identities give exact decompositions such as:

```text
A_Delta^350(xi)=|widehat{nu_0}(xi)|^4-C_w^0(xi),

A_Delta^351(xi)
  =
  E_+^0(xi)^2
  +2E_+^0(xi)K_+^0(xi)
  +RDef_+^0(xi).
```

They do not give sorted-frequency mass bounds for:

```text
A_star(m).
```

The known threshold information supplies row/column caps and first-incidence
totals. By the finite extremal lemma, that information is exactly the data
for which top-mass concentration is the sharp obstruction.

Ordinary pair estimates and first-moment pair or rectangle Hardy-Littlewood
inputs also fail here because they control mean local density or shift-side
pair residuals, not the decreasing rearrangement of the minor-frequency
coefficient against data-dependent threshold profiles.

The sup-norm route gives only:

```text
D^(-1)K_UK_V A_star(ceil(r_{U,V}))
  <=
  D^(-1)K_UK_V ceil(r_{U,V}) ||A||_{infty,minor}.
```

Under the current threshold schedules this is not known to be `o_W(1)`.

The total-mass route gives only:

```text
A_star(m) <= ||A||_{1,minor},
```

which ignores the small-set nature of the obstruction and is too crude
unless an already very strong coefficient estimate is proved.

## 7. New lemma proved

The new lemma is:

```text
FiniteTopMassExtremalLemma_358:
  PROVEN.
```

It proves that the no-twist product row admits the sharp finite reduction:

```text
D sum_xi a(xi)u_abs(xi)v_abs(xi)
  <=
  D^(-1)K_UK_V A_star^cont(r_{U,V})
  <=
  D^(-1)K_UK_V A_star(ceil(r_{U,V})).
```

It also proves sharpness at the profile level. Therefore any proof route
which uses only column caps and column totals cannot beat the top-mass
functional.

## 8. Dependency reduced or removed

This module removes the vague dependency:

```text
"threshold mask regularity might be enough for no-twist correlation."
```

and replaces it with the precise dependency:

```text
Either prove coefficient top-mass / large-value control for A,
or prove a new same-family coefficient-mask overlap theorem.
```

The next clean attack target is:

```text
CoefficientLargeValueDistributionAudit_359(P_minor^0).
```

That target should ask whether the active coefficients from Modules 350-351
have any same-family large-value distribution strong enough to make:

```text
A_star(ceil(r_{U,V})) = o_W(D/(K_UK_V)).
```

The diagonal-overlap term remains separate:

```text
sum_xi a(xi)o_abs(xi).
```

It must be controlled or bypassed by a signed theorem in the same family.

## 9. Red-team audit

Selector check:

```text
This module stays inside P_minor^0. It proves no statement for the actual
sharp moving selector chi_alpha(p).
```

Gap-object check:

```text
No full-gap, clipped-gap, or tail statement is used or proved.
```

Local-factor check:

```text
No local Euler factor is simplified. No replacement of Sigma_w(d,h) by
kappa_w(d)^2 occurs.
```

Limit-order check:

```text
The finite extremal lemma is pointwise in the declared local parameters.
It does not exchange N, w, D, R, eta, cutoff, or W limits.
```

Uniformity check:

```text
The lemma is uniform as finite algebra, but it supplies no uniform prime
estimate for A_star(m), no W-uniformity row, and no dyadic transfer row.
```

Endpoint-circularity check:

```text
The proof does not assume PhaseKernelBound_273^0, NarrowMinorArc_3^B,
ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short, or AU^3.
```

No official theorem status is changed by this module.

## 10. Final classification

```text
CoefficientTopMassFeasibility_358(P_minor^0):
  STRUCTURAL / EXTRACTION.

FiniteTopMassExtremalLemma_358:
  PROVEN.

CapTotalTopMassClosure_358(P_minor^0):
  FALSE / BLOCKED.

LorentzTopMassRoute_358:
  CONDITIONAL.

CoefficientLargeValueDistributionTarget_358:
  OPEN.

CoefficientTopMassProfileCriterion_356:
  OPEN.
```

The proof attack does not close the no-twist row. It proves that the current
cap-and-total profile information cannot close it, and it identifies the
next required analytic object: a same-family large-value or top-mass theorem
for the active coefficient, together with control of the diagonal-overlap
term.

## Edge cases

Empty masks:

```text
If one mask is empty, the product row is zero. This gives no information
about the general mask family.
```

Tiny `r_{U,V}`:

```text
If `r_{U,V}` is bounded and the coefficient is pointwise tiny, a sup-norm
route may suffice. The current ledger does not prove that uniformly for the
active coefficient family.
```

Fractional profile mass:

```text
The continuous top-mass functional A_star^cont(r) handles non-integer
I_U/K_U and I_V/K_V. The discrete bound with ceil(r) is a safe consequence,
not a new analytic estimate.
```

Actual mask realizability:

```text
The sharpness example is a profile-level obstruction. It proves that
cap-and-total data alone cannot imply more. It does not assert that every
extremal profile is realized by the actual threshold masks.
```

## Project-map location

```text
NoTwistColumnProfileCorrelationAudit_356
  -> SignedInsertionRouteDecision_357
  -> CoefficientTopMassFeasibility_358
  -> CoefficientLargeValueDistributionAudit_359.
```

This module attacks the first genuinely new input selected after the
signed-insertion route decision. It narrows that input to coefficient
large-value distribution and overlap control.

## What remains open

Still open:

```text
CoefficientLargeValueDistributionAudit_359(P_minor^0),
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

- Do not read `FiniteTopMassExtremalLemma_358` as a prime estimate.
- Do not use the profile-level sharpness example as a counterexample to the
  actual threshold masks.
- Do not claim the no-twist row is false; only the cap-and-total proof route
  is blocked.
- Do not convert the Lorentz criterion into a coefficient distribution
  theorem.
- Do not upgrade any model-local statement here to the actual sharp moving
  selector.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
