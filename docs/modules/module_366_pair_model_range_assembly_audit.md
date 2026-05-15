# Module 366: Pair-model range assembly audit

## 1. Target claim

Chosen attack mode:

```text
E. Residual obstruction route with a conditional closure test.
```

Best-module selection:

```text
The best current target is Module 366, not a new global branch.
```

Reason:

```text
Modules 362-365 have isolated the pair-model coefficient obstruction into
low-denominator leakage, diagonal routing, finite Ramanujan expansion, and a
finite-cyclic range term. The next useful question is whether these pieces
can be assembled under any honest admissible range, or whether the pair-model
minor top-mass route remains endpoint-strength.
```

This module attacks:

```text
PairModelRangeAssemblyAudit_366(P_minor^0).
```

Verdict:

```text
PairModelRangeAssemblyAudit_366(P_minor^0):
  STRUCTURAL / EXTRACTION.

PolynomialRRangeOffDiagonalPairModelBound_366:
  CONDITIONAL.

FiniteTruncationAllDenominatorsLeakage_366:
  PROVEN.

UniformOffDiagonalTruncationTail_366:
  PROVEN.
  Scope: PolyR_rho.

DiagonalRemovedFiniteModelBound_366:
  PROVEN.
  Scope: PolyR_rho.

CurrentPminor0UniformRangeClosure_366:
  FALSE / BLOCKED.

PairModelMinorTopMassTarget_361:
  CONDITIONAL.
  Note: not proved in full P_minor^0.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful progress is that the off-diagonal pair model is minor-small if the
major denominator range is polynomially large:

```text
R >= N^rho
```

for some fixed `rho>0`, while `N eta >= N^delta_eta`. This is not part of
the declared minimal family `P_minor^0`, which only gives:

```text
2 <= R <= N^delta_R.
```

Thus the result is a conditional subfamily theorem, not a closure of the
parent target.

## 2. Why this would advance the main theorem

The active no-twist branch requires control of:

```text
A_star,|E_+^0 K_+^0|(m_{U,V}).
```

Module 361 reduced this mixed row to pair-residual energy plus top-mass
control of the exact pair-model coefficient. Modules 362-365 then reduced
the model coefficient to:

```text
low denominator leakage,
diagonal routing,
Ramanujan truncation,
finite-cyclic range control.
```

This module shows that these pieces really can bound the off-diagonal model
under a stronger denominator-range hypothesis. It also shows why the current
minimal family is still too broad: if `R` is bounded or grows too slowly,
the truncation cannot both approximate the infinite off-diagonal Euler
product and stay inside the declared major-denominator set.

Therefore the branch advances from:

```text
unknown pair-model coefficient behavior
```

to:

```text
conditional off-diagonal model smallness under polynomial R-range,
with diagonal and pair-residual rows still separate.
```

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

for divisibility statements.

For `z>w`, set:

```text
P(w,z)=prod_{w<p<=z} p.
```

The finite pair factor is:

```text
kappa_{w,z}^0(a)
  =
  prod_{w<p<=z}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p).
```

The diagonal atom is:

```text
B_{w,z}=kappa_{w,z}^0(0),
D_{w,z}^0(a)=B_{w,z}1_{a=0}.
```

The finite off-diagonal model is:

```text
kappa_{w,z}^{0,off}(a)
  =
  kappa_{w,z}^0(a)-D_{w,z}^0(a).
```

The infinite off-diagonal pair model is:

```text
kappa_w^{0,off}(0)=0,

kappa_w^{0,off}(a)
  =
  prod_{p>w}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p),
  for 1<=a<N.
```

The corresponding transforms are:

```text
K_{w,z,+}^{0,off}(xi)
  =
  E_{a in G_N} kappa_{w,z}^{0,off}(a)e_N(xi a),

K_{w,+}^{0,off}(xi)
  =
  E_{a in G_N} kappa_w^{0,off}(a)e_N(xi a).
```

The polynomial major-denominator range hypothesis is:

```text
PolyR_rho:
  there exists fixed rho>0 such that R>=N^rho
  for all sufficiently large N in the tested subfamily.
```

It is compatible with `P_minor^0` only if:

```text
0<rho<=delta_R.
```

The lower eta condition already built into `P_minor^0` is:

```text
N eta >= N^delta_eta.
```

## 4. Assumptions

This module assumes:

```text
Modules 278, 361, 362, 363, 364, and 365,
finite cyclic Fourier algebra,
the finite Ramanujan expansion from Module 364,
and the active status ledger.
```

For the conditional subfamily result it additionally assumes:

```text
PolyR_rho for some fixed 0<rho<=delta_R.
```

It does not assume:

```text
PairModelMinorTopMassTarget_361 in full P_minor^0,
PairResidualFourierEnergyTarget_361,
PairMixedDiagonalAbsorptionCriterion_363,
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
R automatically grows polynomially,
the diagonal atom is absent without a convention,
finite truncation is the same as the infinite Euler product,
off-diagonal pair-model smallness proves pair-residual energy,
conditional subfamily control proves full P_minor^0 control.
```

## 5. Proof / disproof / reduction

### A. Choice of truncation under polynomial R-range

Assume `PolyR_rho`. Choose:

```text
z_N=(rho/4) log N
```

rounded to a real cutoff for primes. For large `N`, `z_N>w`.

By Chebyshev's bound `theta(x)=sum_{p<=x} log p = O(x)`, after decreasing
the constant `rho/4` if needed, one has:

```text
P(w,z_N) <= N^(rho/2) <= R.
```

Thus every squarefree denominator:

```text
q|P(w,z_N)
```

satisfies:

```text
q<=R.
```

This is the decisive point: after truncating at `z_N`, all Ramanujan
denominators are low denominators relative to the declared major-arc range.

### B. Finite truncation all-denominators leakage

Module 364 gives:

```text
kappa_{w,z_N}^0(a)
  =
  sum_{q|P(w,z_N)}
  sum_{r in (Z/qZ)^*}
    mu(q)^2/phi(q)^2 e_q(ra).
```

Since all `q|P(w,z_N)` satisfy `q<=R`, Module 362's low-denominator leakage
lemma applies to every term. For `xi in Minor_0(R,eta)`:

```text
|K_{w,z_N,+}^0(xi)|
  <=
  (1/(2N eta))
  sum_{q|P(w,z_N)}
    q/phi(q).
```

The `q=1` term is constant in `a` and has zero transform at every nonzero
minor frequency, so including it in the displayed upper bound is harmless.

The sum factors:

```text
S(z_N)
  =
  sum_{q|P(w,z_N)} q/phi(q)
  =
  prod_{w<p<=z_N} (1+p/(p-1)).
```

For `p>w`, the factor is bounded by an absolute constant, so:

```text
S(z_N)
  <=
  exp(C pi(z_N))
  <=
  exp(C z_N/log z_N)
  =
  N^o(1).
```

Since:

```text
N eta >= N^delta_eta,
```

it follows that:

```text
sup_{xi in Minor_0(R,eta)} |K_{w,z_N,+}^0(xi)|=o(1).
```

Classification:

```text
FiniteTruncationAllDenominatorsLeakage_366:
  PROVEN.
  Scope: PolyR_rho.
```

### C. Diagonal-removed finite model bound

For the finite diagonal atom:

```text
D_{w,z_N,+}^0(xi)=B_{w,z_N}/N.
```

Also:

```text
B_{w,z_N}
  =
  prod_{w<p<=z_N} (1-1/p)^(-1)
  <=
  prod_{w<p<=z_N} p
  =
  P(w,z_N)
  <=
  R
  <=
  N^delta_R.
```

Since `delta_R<1/100`, this gives:

```text
B_{w,z_N}/N=o(1).
```

Therefore:

```text
sup_{xi in Minor_0(R,eta)}
  |K_{w,z_N,+}^{0,off}(xi)|
  <=
  sup_{xi in Minor_0(R,eta)} |K_{w,z_N,+}^0(xi)|
  + B_{w,z_N}/N
  =
  o(1).
```

Classification:

```text
DiagonalRemovedFiniteModelBound_366:
  PROVEN.
  Scope: PolyR_rho.
```

This proves finite truncated off-diagonal model smallness, not physical
diagonal absorption.

### D. Uniform off-diagonal truncation tail

For `1<=a<N`, compare the infinite off-diagonal factor with its truncation.
The omitted primes `p>z_N` contribute:

```text
(1-1/p)^(-1)
```

if `p|a`, and:

```text
1 - 1/(p-1)^2
```

if `p` does not divide `a`.

Thus the logarithm of the omitted tail differs from `0` by:

```text
O(
  sum_{p>z_N, p|a} 1/p
  +
  sum_{p>z_N} 1/p^2
).
```

The second sum is:

```text
O(1/z_N).
```

For the divisor sum, split primes into dyadic intervals:

```text
2^j z_N < p <= 2^(j+1) z_N.
```

The number of prime divisors of `a` in this interval is at most:

```text
log N / log(2^j z_N),
```

because their product divides `a<N`. Hence:

```text
sum_{p>z_N, p|a} 1/p
  <=
  sum_{j>=0}
    (1/(2^j z_N))
    (log N / log(2^j z_N))
  <=
  C_rho / log z_N,
```

using `z_N=(rho/4)log N`.

Therefore:

```text
sup_{1<=a<N}
  |kappa_w^{0,off}(a)-kappa_{w,z_N}^{0,off}(a)|
  =
  O_w(1/log z_N)
  =
  o(1).
```

Since normalized Fourier transform is bounded by the physical sup norm:

```text
sup_xi
  |K_{w,+}^{0,off}(xi)-K_{w,z_N,+}^{0,off}(xi)|
  =
  o(1).
```

Classification:

```text
UniformOffDiagonalTruncationTail_366:
  PROVEN.
  Scope: PolyR_rho.
```

### E. Conditional off-diagonal pair-model minor bound

Combining parts C and D gives:

```text
sup_{xi in Minor_0(R,eta)}
  |K_{w,+}^{0,off}(xi)|
  =
  o(1)
```

under `PolyR_rho`.

Consequently, for every `m<=#Minor_0(R,eta)`:

```text
A_star,|K_{w,+}^{0,off}|^2(m)
  <=
  m
  (
    sup_{xi in Minor_0(R,eta)}
      |K_{w,+}^{0,off}(xi)|
  )^2.
```

Thus the off-diagonal pair-model top-mass row is reduced to the usual
threshold scale requirement:

```text
m_{U,V}^{1/2}
sup_{xi in Minor_0(R,eta)} |K_{w,+}^{0,off}(xi)|
```

being small enough in Module 361's mixed criterion, together with same-family
pair-residual energy.

Classification:

```text
PolynomialRRangeOffDiagonalPairModelBound_366:
  CONDITIONAL.
```

The condition is not the finite Fourier argument; that part is proved. The
condition is the extra subfamily hypothesis `PolyR_rho`, the diagonal
convention, and the remaining mixed-row assembly with pair residual energy.

### F. Why full P_minor^0 is not closed

The declared minimal family allows:

```text
2 <= R <= N^delta_R.
```

It does not require:

```text
R>=N^rho.
```

If `R` is bounded or grows too slowly, then a truncation with all denominators
inside the major-denominator set cannot also satisfy `z_N >= c log N`.
Without `z_N >= c log N`, the uniform off-diagonal truncation tail above is
not small by the displayed divisor-sum argument.

Thus:

```text
CurrentPminor0UniformRangeClosure_366:
  FALSE / BLOCKED.
```

The parent target remains:

```text
PairModelMinorTopMassTarget_361:
  CONDITIONAL.
  Note: not proved in full P_minor^0.
```

## 6. Edge cases

### Bounded R

If `R` is bounded, every truncation with `P(w,z)<=R` has bounded `z`. It
cannot approximate the infinite off-diagonal Euler product uniformly over
`1<=a<N`.

### Slowly growing R

If `R` grows but does not permit `z_N >= c log N` with `P(w,z_N)<=R`, then
the dyadic divisor-tail estimate does not give `o(1)`. A different
non-uniform or averaged tail theorem would be required.

### Diagonal convention

The module proves an off-diagonal model estimate. It does not prove that the
physical pair diagonal is absent, renormalized correctly, or absorbed in the
mixed row.

### Threshold top-mass scale

The pointwise off-diagonal bound must still be strong enough after the factor
`m_{U,V}^{1/2}` in the mixed criterion. This is a threshold-schedule issue,
not solved by the pointwise statement alone.

### Fixed w

All estimates are for fixed `w` while `N->infty`. A later `w->infty` passage
requires the project limit order and uniformity ledger.

## 7. Project-map location

```text
PairModelMinorTopMassStress_362
  -> PairModelDiagonalConventionAudit_363
  -> PairModelOffDiagonalRamanujanTailAudit_364
  -> FiniteCyclicRamanujanLargeSieveAudit_365
  -> PairModelRangeAssemblyAudit_366
  -> PairModelMinorTopMassVerdict_367.
```

This module is the best current attack because it assembles the last four
modules and distinguishes an actually provable conditional subfamily result
from a full `P_minor^0` theorem.

## 8. What remains open

Still open:

```text
PairModelMinorTopMassVerdict_367(P_minor^0),
full P_minor^0 pair-model minor top-mass without PolyR_rho,
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
All statements remain inside the model family P_minor^0 or the explicitly
named polynomial-R subfamily. No actual sharp moving-selector statement is
proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, dyadic tail, or empty-interval statement is used.
```

Local-factor check:

```text
The exact pair local factor is kept. The diagonal is removed only by an
explicit off-diagonal convention, and no rectangle local factor is replaced.
```

Limit-order check:

```text
The proof chooses z_N proportional to log N only under PolyR_rho. It does not
assert this choice is available in full P_minor^0.
```

Uniformity check:

```text
The off-diagonal truncation tail is uniform in 1<=a<N under the polynomial
R-range. The remaining diagonal and pair-residual rows are not proved.
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
PairModelRangeAssemblyAudit_366(P_minor^0):
  STRUCTURAL / EXTRACTION.

PolynomialRRangeOffDiagonalPairModelBound_366:
  CONDITIONAL.

FiniteTruncationAllDenominatorsLeakage_366:
  PROVEN.
  Scope: PolyR_rho.

UniformOffDiagonalTruncationTail_366:
  PROVEN.
  Scope: PolyR_rho.

DiagonalRemovedFiniteModelBound_366:
  PROVEN.
  Scope: PolyR_rho.

CurrentPminor0UniformRangeClosure_366:
  FALSE / BLOCKED.

PairModelMinorTopMassTarget_361:
  CONDITIONAL.
  Note: not proved in full P_minor^0.
```

Do not cite this module as a full proof of `PairModelMinorTopMassTarget_361`.
It proves an off-diagonal conditional subfamily result and identifies exactly
where full `P_minor^0` still lacks range information.

## Red flags / forbidden upgrades

- Do not assume `R>=N^rho` inside full `P_minor^0`.
- Do not treat off-diagonal pair-model smallness as diagonal absorption.
- Do not treat pair-model smallness as pair-residual energy control.
- Do not move this model-side statement to the actual sharp selector.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
