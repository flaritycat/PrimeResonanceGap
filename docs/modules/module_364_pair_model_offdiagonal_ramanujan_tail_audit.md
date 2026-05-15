# Module 364: Pair-model off-diagonal Ramanujan tail audit

## 1. Target claim

Chosen attack mode:

```text
E. Residual obstruction route with a counter-route audit.
```

Modules 362 and 363 reduced the exact pair-model top-mass problem to two
separate questions:

```text
diagonal convention,
off-diagonal denominator expansion and tail.
```

Module 363 showed that the diagonal `a=0` cannot remain inside the
unqualified infinite Euler product. This module attacks the remaining
off-diagonal branch:

```text
PairModelRamanujanTailTarget_362(P_minor^0).
```

Define:

```text
PairModelOffDiagonalRamanujanTailAudit_364(P_minor^0).
```

Verdict:

```text
PairModelOffDiagonalRamanujanTailAudit_364(P_minor^0):
  STRUCTURAL / EXTRACTION.

FinitePairRamanujanExpansion_364:
  PROVEN.

LowDenominatorRamanujanLeakage_364:
  CONDITIONAL.

ReducedCharacterAbsoluteTail_364:
  FALSE / BLOCKED.

RamanujanSquareCoefficientTail_364:
  PROVEN.

FiniteCyclicRamanujanLargeSieveTarget_364:
  OPEN.

PairModelRamanujanTailTarget_362:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful progress is an exact finite Ramanujan expansion for the truncated
pair local factor. The obstruction is equally important: the naive absolute
tail over reduced characters is divergent, so the high-denominator tail
cannot be removed by triangle inequality. The square coefficient tail is
summable, which points to a finite-cyclic large-sieve or almost-orthogonality
target, but that target is not proved here.

## 2. Why this would advance the main theorem

The active no-twist branch includes:

```text
PairResidualLargeValueStress_361
  -> PairModelMinorTopMassTarget_361
  -> mixed coefficient row |E_+^0 K_+^0|
  -> coefficient top-mass / no-twist profile correlation
  -> SignedLocalModelInsertion_326.
```

Module 362 proved that low-denominator terms leak weakly into minor arcs if a
finite denominator expansion is supplied. Module 364 supplies the exact
Ramanujan expansion for the finite off-diagonal pair model. It also explains
why that alone does not close the top-mass target: the high-denominator tail
needs cancellation or square-summability, not absolute summation.

This is a genuine narrowing of the obstruction. The next useful analytic row
is no longer "find an expansion"; it is:

```text
prove finite-cyclic high-denominator almost-orthogonality for the
Ramanujan tail in the declared P_minor^0 range.
```

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Use the representative convention:

```text
a in G_N is represented by 0<=a<N
```

whenever an expression such as `p|a` or `e_q(ra)` is used. This is a
finite-cyclic convention, not a transfer theorem from integer shifts.

For `z>w`, let:

```text
P(w,z)=prod_{w<p<=z} p.
```

For squarefree `q`, define:

```text
q|P(w,z)
```

to mean that every prime divisor of `q` lies in `(w,z]`.

The finite truncated pair factor is:

```text
kappa_{w,z}^0(a)
  =
  prod_{w<p<=z}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p).
```

The Ramanujan sum is:

```text
c_q(a)
  =
  sum_{r in (Z/qZ)^*} e_q(ra),

e_q(t)=exp(2 pi i t/q).
```

For squarefree `q`, use:

```text
lambda_q=mu(q)^2/phi(q)^2.
```

For a cutoff `Q`, define the low- and high-denominator pieces:

```text
H_{Q,z}(a)
  =
  sum_{q|P(w,z), q<=Q}
    lambda_q c_q(a),

T_{Q,z}(a)
  =
  sum_{q|P(w,z), q>Q}
    lambda_q c_q(a).
```

Thus:

```text
kappa_{w,z}^0(a)=H_{Q,z}(a)+T_{Q,z}(a).
```

If the diagonal is removed as in Module 363, then an additional finite atom
must be subtracted:

```text
kappa_{w,z}^{0,off}(a)
  =
  kappa_{w,z}^0(a)-kappa_{w,z}^0(0)1_{a=0}.
```

This module audits the Ramanujan expansion and tail before any final diagonal
absorption is applied.

For any function `F` on representatives `0<=a<N`, write:

```text
F_+(xi)=E_{a in G_N}F(a)e_N(xi a).
```

## 4. Assumptions

This module assumes:

```text
Modules 278, 351, 361, 362, and 363,
finite cyclic Fourier algebra,
elementary properties of Ramanujan sums,
and the active status ledger.
```

It uses only elementary convergence facts:

```text
sum_p 1/p diverges,
sum_n n^(-3/2) converges,
and phi(q)>=q^(1/2) for squarefree q with all prime factors at least 3.
```

It does not assume:

```text
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
absolute convergence of the reduced-character Ramanujan tail,
finite-cyclic almost-orthogonality for free,
integer-shift Ramanujan expansions transfer automatically to G_N,
the diagonal subtraction has no Fourier cost.
```

## 5. Proof / disproof / reduction

### A. Exact finite Ramanujan expansion

For a prime `p>w`, the prime-level Ramanujan sum is:

```text
c_p(a)
  =
  p-1,  if p|a,
  -1,   if p does not divide a.
```

Therefore:

```text
1 + c_p(a)/(p-1)^2
```

equals:

```text
1 + 1/(p-1)
  =
  p/(p-1)
  =
  (1-1/p)^(-1),
```

when `p|a`, and equals:

```text
1 - 1/(p-1)^2
  =
  p(p-2)/(p-1)^2
  =
  (1-1/p)^(-2)(1-2/p),
```

when `p` does not divide `a`.

These are exactly the two local factors of `kappa_{w,z}^0(a)` according as
`#{0,a mod p}=1` or `2`. Hence:

```text
kappa_{w,z}^0(a)
  =
  prod_{w<p<=z}
    (1 + c_p(a)/(p-1)^2).
```

For squarefree coprime moduli, Ramanujan sums multiply:

```text
c_q(a)=prod_{p|q} c_p(a).
```

Expanding the finite Euler product gives:

```text
kappa_{w,z}^0(a)
  =
  sum_{q|P(w,z)}
    mu(q)^2/phi(q)^2 c_q(a).
```

Equivalently:

```text
kappa_{w,z}^0(a)
  =
  sum_{q|P(w,z)}
  sum_{r in (Z/qZ)^*}
    mu(q)^2/phi(q)^2 e_q(ra).
```

Classification:

```text
FinitePairRamanujanExpansion_364:
  PROVEN.
```

This is a finite identity after the representative convention is declared.
It does not prove a high-denominator tail bound.

### B. Low-denominator leakage after inserting the exact coefficients

Apply Module 362's low-denominator leakage lemma to:

```text
gamma_{q,r}=mu(q)^2/phi(q)^2
```

for:

```text
q|P(w,z), q<=Q<=R, r in (Z/qZ)^*.
```

For every:

```text
xi in Minor_0(R,eta),
```

one obtains:

```text
|H_{Q,z,+}(xi)|
  <=
  (1/(2N eta))
  sum_{q|P(w,z), q<=Q}
    q/phi(q).
```

Thus the low-denominator part is minor-small if the declared range supplies:

```text
(1/(N eta))
sum_{q|P(w,z), q<=Q}
  q/phi(q)
  =
  o(1).
```

Classification:

```text
LowDenominatorRamanujanLeakage_364:
  CONDITIONAL.
```

This is conditional because the active constants in `P_minor^0` do not by
themselves specify a range relation between `Q`, `R`, `N`, and `eta` strong
enough to close the displayed bound uniformly.

### C. The reduced-character absolute high-denominator tail diverges

The absolute reduced-character mass above `Q` is:

```text
A_{Q,z}
  =
  sum_{q|P(w,z), q>Q}
    phi(q) mu(q)^2/phi(q)^2
  =
  sum_{q|P(w,z), q>Q}
    mu(q)^2/phi(q).
```

For every fixed `Q`, the prime terms alone give:

```text
A_{Q,z}
  >=
  sum_{Q<p<=z, p>w}
    1/(p-1).
```

Since:

```text
sum_p 1/p diverges,
```

the right side diverges as `z->infty`. Therefore there is no uniform
absolute reduced-character tail bound.

Classification:

```text
ReducedCharacterAbsoluteTail_364:
  FALSE / BLOCKED.
```

This blocks the naive route:

```text
bound T_{Q,z,+} by summing absolute values of all reduced-character
coefficients.
```

The tail must use cancellation or square-summability.

### D. The square coefficient tail is summable

The square coefficient mass over reduced characters is:

```text
S_Q
  =
  sum_{q>Q, p|q => p>w}
    phi(q) (mu(q)^2/phi(q)^2)^2
  =
  sum_{q>Q, p|q => p>w}
    mu(q)^2/phi(q)^3.
```

Since every prime divisor of such `q` is at least `3`, and `q` is squarefree:

```text
phi(q)=prod_{p|q}(p-1) >= prod_{p|q} p^(1/2)=q^(1/2).
```

Therefore:

```text
S_Q
  <=
  sum_{q>Q} q^(-3/2)
  =
  O(Q^(-1/2)).
```

In particular:

```text
S_Q -> 0 as Q->infty.
```

Classification:

```text
RamanujanSquareCoefficientTail_364:
  PROVEN.
```

This is coefficient-square decay only. It is not yet a finite-cyclic Fourier
tail bound for `T_{Q,z,+}`.

### E. The remaining finite-cyclic tail target

The previous two parts show the exact shape of the remaining target. A future
row must prove a bound of the following kind, with all parameters inside the
same `P_minor^0` family:

```text
FiniteCyclicRamanujanLargeSieveTarget_364:
  prove that for admissible Q=Q(N,w,R,eta) and z=z(N,w),

  sup_{E subset Minor_0(R,eta), #E<=m_{U,V}}
    sum_{xi in E} |T_{Q,z,+}(xi)|^2

  is small enough for PairModelMinorTopMassTarget_361,

  after adding the diagonal row from Module 363.
```

A plausible sufficient route would combine the square coefficient tail:

```text
sum_{q>Q} mu(q)^2/phi(q)^3 -> 0
```

with a finite-cyclic large-sieve or almost-orthogonality estimate for the
phases:

```text
e_q(ra)e_N(xi a).
```

But the project does not currently contain that estimate with the required
range, representative convention, denominator cutoff, minor-frequency
restriction, and diagonal routing.

Classification:

```text
FiniteCyclicRamanujanLargeSieveTarget_364:
  OPEN.

PairModelRamanujanTailTarget_362:
  OPEN.
```

## 6. Edge cases

### Diagonal value

The expansion includes `a=0` and reproduces the finite diagonal value:

```text
kappa_{w,z}^0(0)
  =
  sum_{q|P(w,z)} mu(q)^2/phi(q)^2 phi(q)
  =
  sum_{q|P(w,z)} mu(q)^2/phi(q).
```

This diverges as `z->infty`, as Module 363 already recorded. Therefore the
off-diagonal convention still requires diagonal subtraction or a separate
diagonal row.

### Cyclic representatives

The expression `e_q(ra)` is evaluated on representatives `0<=a<N`. It is not
automatically a character of `G_N` unless the denominator is compatible with
`N`. Any future large-sieve row must keep this representative convention
visible.

### Denominators above the major cutoff

The minor-arc definition excludes rationals only up to denominator `R`.
Therefore Module 362's geometric leakage argument applies directly only for
`q<=Q<=R`. Denominators above `R` are precisely the high-denominator tail.

### Absolute versus square tail

The absolute reduced-character tail diverges, while the square coefficient
tail converges. Replacing one by the other requires an orthogonality input,
not a notation change.

### Prime powers

The expansion is squarefree because Ramanujan sums multiply over distinct
prime factors in the finite Euler product. It does not insert prime powers
into the W-prime model or prove prime-power transfer.

## 7. Project-map location

```text
PairModelMinorTopMassStress_362
  -> PairModelDiagonalConventionAudit_363
  -> PairModelOffDiagonalRamanujanTailAudit_364
  -> FiniteCyclicRamanujanLargeSieveAudit_365.
```

The module supplies the exact finite Ramanujan expansion and identifies the
tail route that remains viable. It also blocks the absolute-tail shortcut.

## 8. What remains open

Still open:

```text
FiniteCyclicRamanujanLargeSieveAudit_365(P_minor^0),
FiniteCyclicRamanujanLargeSieveTarget_364,
PairModelRamanujanTailTarget_362,
PairModelMinorTopMassTarget_361,
PairMixedDiagonalAbsorptionCriterion_363,
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
The exact pair factor is expanded prime by prime. Sigma_w(d,h) is not
replaced by kappa_w(d)^2, and the rectangle factor is not touched.
```

Limit-order check:

```text
The expansion is finite at cutoff z. The module does not send z, Q, N, or w
through an unproved exchange of limits.
```

Uniformity check:

```text
The low-denominator and high-denominator conclusions are stated with their
missing uniform range requirements. No uniform tail theorem is claimed.
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
PairModelOffDiagonalRamanujanTailAudit_364(P_minor^0):
  STRUCTURAL / EXTRACTION.

FinitePairRamanujanExpansion_364:
  PROVEN.

LowDenominatorRamanujanLeakage_364:
  CONDITIONAL.

ReducedCharacterAbsoluteTail_364:
  FALSE / BLOCKED.

RamanujanSquareCoefficientTail_364:
  PROVEN.

FiniteCyclicRamanujanLargeSieveTarget_364:
  OPEN.

PairModelRamanujanTailTarget_362:
  OPEN.
```

Do not cite this module as proving `PairModelMinorTopMassTarget_361`. It
proves the exact finite expansion and a square-coefficient tail, while showing
that the absolute reduced-character tail route is blocked.

## Red flags / forbidden upgrades

- Do not use absolute summation of reduced-character coefficients for the
  high-denominator tail.
- Do not treat coefficient-square summability as finite-cyclic
  almost-orthogonality.
- Do not ignore the diagonal subtraction from Module 363.
- Do not transfer representative-based integer divisibility to `G_N` without
  a declared range convention.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
