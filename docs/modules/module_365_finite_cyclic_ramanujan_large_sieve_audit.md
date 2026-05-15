# Module 365: Finite-cyclic Ramanujan large-sieve audit

## 1. Target claim

Chosen attack mode:

```text
E. Residual obstruction route with a sharper equivalent formulation.
```

Module 364 proved the exact finite Ramanujan expansion for the truncated pair
model and showed that the high-denominator tail cannot be controlled by the
absolute reduced-character mass. It also proved square-coefficient summability
and left the finite-cyclic large-sieve conversion open.

This module attacks:

```text
FiniteCyclicRamanujanLargeSieveTarget_364(P_minor^0).
```

Define:

```text
FiniteCyclicRamanujanLargeSieveAudit_365(P_minor^0).
```

Verdict:

```text
FiniteCyclicRamanujanLargeSieveAudit_365(P_minor^0):
  STRUCTURAL / EXTRACTION.

FiniteDirichletKernelRowSum_365:
  PROVEN.

RamanujanTailPointwiseBound_365:
  PROVEN.

RamanujanTailTopMassCriterion_365:
  CONDITIONAL.

SquareTailAloneClosure_365:
  FALSE / BLOCKED.

CurrentFiniteCyclicLargeSieveClosure_365:
  FALSE / BLOCKED.

FiniteCyclicRamanujanLargeSieveTarget_364:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful progress is a finite-cyclic kernel bound:

```text
sup_xi |T_{Q,z,+}(xi)|
  <=
  C U_{Q,z}
  + C (log(2N)/N) V_{Q,z},
```

where:

```text
U_{Q,z}
  =
  sum_{q|P(w,z), q>Q} mu(q)^2/phi(q)^2,

V_{Q,z}
  =
  sum_{q|P(w,z), q>Q} mu(q)^2 q/phi(q)^2.
```

This turns the large-sieve target into a concrete range condition. The
current ledger does not yet declare `Q,z` so that the bound is small at the
active top-mass scale and with the Module 363 diagonal row included.

## 2. Why this would advance the main theorem

The active path is:

```text
PairModelMinorTopMassTarget_361
  -> mixed coefficient row |E_+^0 K_+^0|
  -> CoefficientTopMassProfileCriterion_356
  -> NoTwistColumnProfileCorrelation_356
  -> SignedLocalModelInsertion_326.
```

Modules 362-364 reduced the pair-model top-mass problem to:

```text
low denominator leakage,
high denominator tail,
diagonal routing.
```

This module gives a concrete finite-cyclic estimate for the high-denominator
tail. It does not close the branch because it introduces the range term
`(log(2N)/N)V_{Q,z}` and because the diagonal row from Module 363 still must
be assembled with the same cutoffs.

The gain is diagnostic: the next question is not whether the Ramanujan tail
has square coefficients, but whether the declared cutoff range makes the
finite-cyclic kernel term small.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Use representatives:

```text
0<=a<N
```

when evaluating `e_q(ra)`.

For `theta in R/Z`, define the normalized finite Dirichlet average:

```text
A_N(theta)
  =
  E_{0<=a<N} exp(2 pi i a theta).
```

Then:

```text
|A_N(theta)|
  <=
  min(1, 1/(2N ||theta||_{R/Z})).
```

For `z>w`, let:

```text
P(w,z)=prod_{w<p<=z} p.
```

For squarefree `q|P(w,z)`, define:

```text
lambda_q=mu(q)^2/phi(q)^2.
```

For a cutoff `Q`, the Module 364 high-denominator tail is:

```text
T_{Q,z}(a)
  =
  sum_{q|P(w,z), q>Q}
  sum_{r in (Z/qZ)^*}
    lambda_q e_q(ra).
```

Its finite-cyclic transform is:

```text
T_{Q,z,+}(xi)
  =
  E_{a in G_N} T_{Q,z}(a)e_N(xi a).
```

Equivalently:

```text
T_{Q,z,+}(xi)
  =
  sum_{q|P(w,z), q>Q}
  sum_{r in (Z/qZ)^*}
    lambda_q A_N(r/q+xi/N).
```

Define:

```text
U_{Q,z}
  =
  sum_{q|P(w,z), q>Q}
    mu(q)^2/phi(q)^2,

V_{Q,z}
  =
  sum_{q|P(w,z), q>Q}
    mu(q)^2 q/phi(q)^2.
```

For a nonnegative coefficient `c(xi)`, define:

```text
A_star,c(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} c(xi).
```

The active top-mass scale remains:

```text
m_{U,V}=ceil(min(I_U/K_U,I_V/K_V)).
```

## 4. Assumptions

This module assumes:

```text
Modules 278, 361, 362, 363, and 364,
finite cyclic Fourier algebra,
the finite Ramanujan expansion of Module 364,
and the active status ledger.
```

It does not assume:

```text
FiniteCyclicRamanujanLargeSieveTarget_364,
PairModelMinorTopMassTarget_361,
PairModelRamanujanTailTarget_362,
PairMixedDiagonalAbsorptionCriterion_363,
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
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
square coefficient summability automatically implies finite-cyclic tail
smallness,
the denominators q have free spacing relative to N,
the cutoff z can be sent to infinity without tracking V_{Q,z},
the diagonal row from Module 363 has disappeared.
```

## 5. Proof / disproof / reduction

### A. Finite Dirichlet kernel row sum

For every integer `q>=1` and every `t in R/Z`:

```text
sum_{r in Z/qZ}
  |A_N(t+r/q)|
  <=
  C (1 + (q/N) log(2N)).
```

Proof:

The points `t+r/q` are spaced by `1/q` on `R/Z`. After choosing the closest
point to `0`, their distances from `0` are bounded below, up to absolute
constants, by:

```text
k/q,  1<=k<=q/2,
```

with at most two points at each distance level. Hence:

```text
sum_{r mod q} |A_N(t+r/q)|
  <=
  C + C sum_{1<=k<=q/2} min(1, q/(N k)).
```

If `q<=N`, the last sum is:

```text
<= C + C (q/N) sum_{1<=k<=q/2} 1/k
<= C (1 + (q/N) log(2N)).
```

If `q>N`, split at `k<=q/N`. The contribution below the split is
`O(q/N)`, and the contribution above it is:

```text
<=
  C (q/N) sum_{q/N<k<=q/2} 1/k
  <=
  C (q/N) log(2N).
```

This proves the bound. Restricting to reduced residues only decreases the
left side.

Classification:

```text
FiniteDirichletKernelRowSum_365:
  PROVEN.
```

### B. Pointwise finite-cyclic Ramanujan tail bound

Using the Module 364 formula:

```text
T_{Q,z,+}(xi)
  =
  sum_{q|P(w,z), q>Q}
  sum_{r in (Z/qZ)^*}
    lambda_q A_N(r/q+xi/N),
```

and applying the row-sum bound with `t=xi/N`, one obtains:

```text
|T_{Q,z,+}(xi)|
  <=
  C sum_{q|P(w,z), q>Q}
    lambda_q (1 + (q/N) log(2N)).
```

Therefore, uniformly in `xi`:

```text
|T_{Q,z,+}(xi)|
  <=
  C U_{Q,z}
  + C (log(2N)/N) V_{Q,z}.
```

Classification:

```text
RamanujanTailPointwiseBound_365:
  PROVEN.
```

This is a finite-cyclic estimate with the representative convention visible.
It is not an endpoint theorem until the cutoff ranges make the right side
small and the diagonal row is added.

### C. Top-mass consequence

For every `m>=0`:

```text
A_star,|T_{Q,z,+}|^2(m)
  <=
  m (
    C U_{Q,z}
    + C (log(2N)/N) V_{Q,z}
  )^2.
```

Thus the high-denominator tail is harmless for Module 361's mixed row if:

```text
D^(-1)K_UK_V
  (
    E_a |E_pair^0(a)|^2
  )^(1/2)
  m_{U,V}^{1/2}
  (
    U_{Q,z}
    + (log(2N)/N) V_{Q,z}
  )
  =
  o_W(1),
```

after replacing `E_pair^0` by the exact residual belonging to the same
off-diagonal/diagonal convention.

Classification:

```text
RamanujanTailTopMassCriterion_365:
  CONDITIONAL.
```

The condition is useful because it is explicit, but it is not verified in
the active ledger.

### D. Why square coefficient summability alone does not close the tail

Module 364 proved:

```text
sum_{q>Q}
  mu(q)^2/phi(q)^3
  -> 0.
```

This is the square mass of reduced-character coefficients:

```text
sum_{q>Q}
sum_{r in (Z/qZ)^*}
  lambda_q^2.
```

However, to turn this into a bound for `T_{Q,z,+}` one also needs an
operator norm for the matrix:

```text
(q,r) -> A_N(r/q+xi/N).
```

The row-sum proof shows that this operator norm carries a range term involving

```text
V_{Q,z}
  =
  sum_{q|P(w,z), q>Q} mu(q)^2 q/phi(q)^2.
```

The current ledger has not declared a cutoff range forcing:

```text
(log(2N)/N)V_{Q,z}=o(1)
```

at the same time as the low-denominator and diagonal rows. Therefore the
square coefficient tail does not by itself prove the finite-cyclic tail
estimate.

Classification:

```text
SquareTailAloneClosure_365:
  FALSE / BLOCKED.
```

### E. Current closure verdict

The current branch now has a clean sufficient package:

```text
LowDenominatorRamanujanLeakage_364,
RamanujanTailTopMassCriterion_365,
PairMixedDiagonalAbsorptionCriterion_363,
same-family pair-residual energy.
```

But the package is not currently proved. The finite-cyclic tail estimate is
conditional on range data for `Q,z,N` and on using the same diagonal
convention throughout.

Classification:

```text
CurrentFiniteCyclicLargeSieveClosure_365:
  FALSE / BLOCKED.

FiniteCyclicRamanujanLargeSieveTarget_364:
  OPEN.
```

## 6. Edge cases

### Reduced residues

The row-sum is proved over all residues modulo `q`; reduced residues are a
subset. No coprimality cancellation is used.

### Very large denominators

For `q>N`, the row-sum grows like `(q/N)log(2N)`. This is exactly the range
loss recorded in `V_{Q,z}`. Ignoring it would reintroduce the blocked
absolute-tail shortcut in a disguised form.

### Denominator compatibility with N

The functions `e_q(ra)` are evaluated on representatives `0<=a<N`; they are
not characters of `G_N` unless extra compatibility is imposed. The bound uses
finite averages directly and does not assert character orthogonality on
`G_N`.

### Diagonal subtraction

This module estimates the Ramanujan tail before final diagonal routing. Any
use in the pair model must add the Module 363 diagonal convention and its
absorption row.

### Minor arcs

The pointwise bound is uniform in all `xi`, so it does not use the minor-arc
exclusion. The low-denominator part still needs the minor-arc leakage
argument from Modules 362 and 364.

## 7. Project-map location

```text
PairModelMinorTopMassStress_362
  -> PairModelDiagonalConventionAudit_363
  -> PairModelOffDiagonalRamanujanTailAudit_364
  -> FiniteCyclicRamanujanLargeSieveAudit_365
  -> PairModelRangeAssemblyAudit_366.
```

This module turns the high-denominator tail problem into an explicit
finite-cyclic range criterion. It does not close the parent pair-model
top-mass target.

## 8. What remains open

Still open:

```text
PairModelRangeAssemblyAudit_366(P_minor^0),
FiniteCyclicRamanujanLargeSieveTarget_364,
PairModelRamanujanTailTarget_362,
PairModelMinorTopMassTarget_361,
PairMixedDiagonalAbsorptionCriterion_363,
LowDenominatorRamanujanLeakage_364,
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
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
The exact pair Ramanujan expansion from Module 364 is used. No rectangle
local factor is replaced, and Sigma_w(d,h) is not treated as kappa_w(d)^2.
```

Limit-order check:

```text
The estimate is finite in N,Q,z. No cutoff is sent to infinity without the
range term V_{Q,z}.
```

Uniformity check:

```text
The criterion states the exact uniform bound required but does not verify it
for the whole active family.
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
FiniteCyclicRamanujanLargeSieveAudit_365(P_minor^0):
  STRUCTURAL / EXTRACTION.

FiniteDirichletKernelRowSum_365:
  PROVEN.

RamanujanTailPointwiseBound_365:
  PROVEN.

RamanujanTailTopMassCriterion_365:
  CONDITIONAL.

SquareTailAloneClosure_365:
  FALSE / BLOCKED.

CurrentFiniteCyclicLargeSieveClosure_365:
  FALSE / BLOCKED.

FiniteCyclicRamanujanLargeSieveTarget_364:
  OPEN.
```

Do not cite this module as proving `PairModelMinorTopMassTarget_361`. It
proves a finite-cyclic tail bound and identifies the missing range assembly.

## Red flags / forbidden upgrades

- Do not treat square coefficient summability as a completed large-sieve
  theorem.
- Do not ignore the `(log(2N)/N)V_{Q,z}` range term.
- Do not send `z` to infinity before proving the finite-cyclic range bound.
- Do not use this tail estimate without the diagonal convention from
  Module 363.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
