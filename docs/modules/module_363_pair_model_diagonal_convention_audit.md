# Module 363: Pair-model diagonal convention audit

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Module 362 showed that the exact pair-model coefficient

```text
K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a)
```

cannot be treated as harmless on minor arcs until the denominator expansion,
tail, and pair diagonal are specified. This module attacks the diagonal part:

```text
PairModelDiagonalConventionGate_362(P_minor^0).
```

Define:

```text
PairModelDiagonalConventionAudit_363(P_minor^0).
```

Verdict:

```text
PairModelDiagonalConventionAudit_363(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairDiagonalDivergenceLemma_363:
  PROVEN.

OffDiagonalPairFactorConvergenceLemma_363:
  PROVEN.

FiniteTruncatedDiagonalFourierLemma_363:
  PROVEN.

PairMixedDiagonalAbsorptionCriterion_363:
  CONDITIONAL.

OffDiagonalPairModelConvention_363:
  STRUCTURAL / EXTRACTION.

UnqualifiedPairDiagonalConvention_363:
  FALSE / BLOCKED.

PairModelDiagonalConventionGate_362:
  CONDITIONAL.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful extraction is that the diagonal `a=0` cannot remain inside the
unqualified infinite Euler product for `kappa_w^0`. It must be removed,
finitely truncated, renormalized with an explicit re-insertion term, or routed
to a separate diagonal row. The safest convention for the active minor-arc
top-mass branch is to use an off-diagonal pair model and carry any finite
diagonal atom as a named error row.

This is not a proof of `PairModelMinorTopMassTarget_361`.

## 2. Why this would advance the main theorem

The active branch contains the mixed coefficient row:

```text
A_star,|E_+^0 K_+^0|(m_{U,V}),
```

where:

```text
E_+^0(xi)
  =
  E_{a in G_N} (P_nu^0(a)-kappa_w^0(a))e_N(xi a),

K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a).
```

If `kappa_w^0(0)` is left undefined or silently replaced by a finite value,
then the object being estimated is not well-defined. If a finite diagonal
atom is retained, it contributes the same amount to every frequency, including
all minor frequencies. Therefore the diagonal must be handled before any
minor-frequency top-mass estimate for `K_+^0` can be cited.

This module reduces the diagonal question to a finite absorption criterion.
It also blocks the shortcut:

```text
the pair diagonal is harmless because xi is minor.
```

Minor-arc exclusion does not remove a point mass at `a=0`.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Use:

```text
e_N(t)=exp(2 pi i t/N),
F_+(xi)=E_{a in G_N}F(a)e_N(xi a).
```

The displayed pair factor from Modules 351 and 362 is:

```text
kappa_w^0(a)
  =
  prod_{p>w}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p).
```

For a finite high-prime cutoff `z>w`, define the truncated local factor:

```text
kappa_{w,z}^0(a)
  =
  prod_{w<p<=z}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p).
```

Its diagonal mass is:

```text
B_{w,z}
  =
  kappa_{w,z}^0(0)
  =
  prod_{w<p<=z} (1-1/p)^(-1).
```

Define the diagonal atom:

```text
D_{w,z}^0(a)=B_{w,z} 1_{a=0 in G_N},
```

and the truncated off-diagonal part:

```text
kappa_{w,z}^{0,off}(a)
  =
  kappa_{w,z}^0(a)-D_{w,z}^0(a).
```

Then:

```text
K_{+,z}^0(xi)
  =
  E_a kappa_{w,z}^0(a)e_N(xi a),

K_{+,z}^{0,off}(xi)
  =
  E_a kappa_{w,z}^{0,off}(a)e_N(xi a),

D_{+,z}^0(xi)
  =
  E_a D_{w,z}^0(a)e_N(xi a).
```

For a nonnegative coefficient `c(xi)`, use:

```text
A_star,c(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} c(xi).
```

The active top-mass scale is:

```text
m_{U,V}=ceil(min(I_U/K_U,I_V/K_V)).
```

## 4. Assumptions

This module assumes:

```text
Modules 278, 350, 351, 361, and 362,
finite cyclic Fourier algebra,
the displayed Euler product definitions,
and the active status ledger.
```

It also uses the elementary facts:

```text
sum_p 1/p diverges,
sum_p 1/p^2 converges.
```

It does not assume:

```text
PairModelMinorTopMassTarget_361,
PairModelRamanujanTailTarget_362,
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
kappa_w^0(0) is a finite unqualified Euler product,
a diagonal atom is major-arc supported,
minor-frequency restriction removes the pair diagonal,
renormalizing the diagonal changes nothing,
finite truncation may be sent to infinity without a tail row.
```

## 5. Proof / disproof / reduction

### A. The unqualified diagonal Euler product diverges

At `a=0`, the set `{0,a} mod p` has one element for every prime `p`. Hence
the displayed pair factor becomes:

```text
kappa_w^0(0)
  =
  prod_{p>w} (1-1/p)^(-1).
```

For a finite cutoff `z`, this is:

```text
B_{w,z}
  =
  prod_{w<p<=z} (1-1/p)^(-1).
```

Taking logarithms:

```text
log B_{w,z}
  =
  sum_{w<p<=z} -log(1-1/p)
  >=
  sum_{w<p<=z} 1/p.
```

Since `sum_p 1/p` diverges, `B_{w,z}` diverges as `z->infty`. Therefore the
infinite diagonal value `kappa_w^0(0)` is not finite.

Classification:

```text
PairDiagonalDivergenceLemma_363:
  PROVEN.
```

Consequence:

```text
UnqualifiedPairDiagonalConvention_363:
  FALSE / BLOCKED.
```

The infinite pair factor cannot be used on all of `G_N` unless the diagonal
is removed, truncated, renormalized with an explicit compensating term, or
routed separately.

### B. The off-diagonal Euler product is finite for a fixed nonzero shift

Let `a` be a fixed nonzero integer shift after the declared representative
convention. If `p|a`, then:

```text
(1-1/p)^(-2)(1-#({0,a} mod p)/p)
  =
  (1-1/p)^(-1).
```

Only finitely many primes divide `a`.

If `p` does not divide `a`, then `{0,a} mod p` has two elements and:

```text
(1-1/p)^(-2)(1-2/p)
  =
  p(p-2)/(p-1)^2
  =
  1 - 1/(p-1)^2.
```

The product over primes not dividing `a` converges absolutely because:

```text
sum_{p>w} 1/(p-1)^2 < infinity.
```

Thus the off-diagonal local factor is finite after an integer-shift
representative is fixed.

Classification:

```text
OffDiagonalPairFactorConvergenceLemma_363:
  PROVEN.
```

This lemma is local to a fixed nonzero integer shift convention. It does not
prove that the cyclic `G_N` coefficient has a completed range-transfer
theorem.

### C. A finite diagonal atom leaks into every minor frequency

For the finite diagonal atom:

```text
D_{w,z}^0(a)=B_{w,z} 1_{a=0},
```

one has for every `xi in G_N`:

```text
D_{+,z}^0(xi)
  =
  E_{a in G_N} D_{w,z}^0(a)e_N(xi a)
  =
  B_{w,z}/N.
```

Therefore, for every `m>=0`:

```text
A_star,|D_{+,z}^0|^2(m)
  =
  min(m,#Minor_0(R,eta)) B_{w,z}^2/N^2.
```

Also, if:

```text
K_{+,z}^0=K_{+,z}^{0,off}+D_{+,z}^0,
```

then:

```text
A_star,|K_{+,z}^0|^2(m)
  <=
  2 A_star,|K_{+,z}^{0,off}|^2(m)
  + 2 min(m,#Minor_0(R,eta)) B_{w,z}^2/N^2.
```

Classification:

```text
FiniteTruncatedDiagonalFourierLemma_363:
  PROVEN.
```

This is a finite Fourier calculation. It does not estimate
`K_{+,z}^{0,off}`.

### D. Mixed pair-residual row with a finite diagonal atom

Let:

```text
E_pair^0(a)=P_nu^0(a)-kappa_w^0(a)
```

be replaced, under the finite cutoff convention, by the corresponding
finite-cutoff residual:

```text
E_{pair,z}^0(a)=P_nu^0(a)-kappa_{w,z}^{0,off}(a)-D_{w,z}^0(a).
```

For any `E subset Minor_0(R,eta)` with `#E<=m`, Cauchy and Parseval give:

```text
sum_{xi in E}
  |E_{+,z}^0(xi)D_{+,z}^0(xi)|
  <=
  (B_{w,z}/N)
  m^(1/2)
  (
    sum_{xi in G_N} |E_{+,z}^0(xi)|^2
  )^(1/2)
```

and hence:

```text
sum_{xi in E}
  |E_{+,z}^0(xi)D_{+,z}^0(xi)|
  <=
  (B_{w,z}/N)
  m^(1/2)
  (
    E_{a in G_N}|E_{pair,z}^0(a)|^2
  )^(1/2).
```

Thus the diagonal part of the mixed Module 361 row is absorbed if:

```text
D^(-1)K_UK_V
  (B_{w,z}/N)
  m_{U,V}^{1/2}
  (
    E_a |E_{pair,z}^0(a)|^2
  )^(1/2)
  =
  o_W(1),
```

with the same limiting order and the same admissible family.

Classification:

```text
PairMixedDiagonalAbsorptionCriterion_363:
  CONDITIONAL.
```

The displayed criterion is not proved here. It names the exact finite
diagonal row that must be checked if a truncated diagonal atom is retained.

### E. Decision among the available conventions

The possible conventions have different mathematical costs.

Removed diagonal:

```text
kappa_w^{0,off}(0)=0,
kappa_w^{0,off}(a)=kappa_w^0(a) for a != 0.
```

This is the cleanest coefficient for minor-frequency top-mass work, but it
is valid only if the physical row also excludes or separately routes the pair
diagonal. It is not a free deletion.

Renormalized diagonal:

```text
kappa_w^0(0) is replaced by a finite chosen value.
```

This changes the local model by a point mass. It is acceptable only if the
chosen point mass is named and its transform is inserted back into every row
that uses `K_+^0`.

Finite truncation:

```text
kappa_{w,z}^0(0)=B_{w,z}.
```

This is well-defined for fixed `z`, but sending `z->infty` is not harmless.
The diagonal atom is uniform over frequency with size `B_{w,z}/N`, so the
limit requires the absorption criterion above and a declared limiting order.

Separate diagonal row:

```text
K_{+,z}^0
  =
  K_{+,z}^{0,off}
  + D_{+,z}^0.
```

This is the safest active convention. The off-diagonal model is attacked by
denominator expansion and tail estimates; the diagonal atom is carried by
the finite row supplied in part D.

Classification:

```text
OffDiagonalPairModelConvention_363:
  STRUCTURAL / EXTRACTION.

PairModelDiagonalConventionGate_362:
  CONDITIONAL.
```

The gate is conditional because future uses of `K_+^0` must either:

```text
use the off-diagonal convention and prove the diagonal row is absent,
or use a finite truncation and prove PairMixedDiagonalAbsorptionCriterion_363.
```

## 6. Edge cases

### Zero frequency

The zero frequency is removed from the major/minor split, but the diagonal
atom contributes to every nonzero frequency as well. Removing `xi=0` does not
remove the diagonal atom.

### Cyclic representative convention

The off-diagonal convergence lemma is stated for a fixed nonzero integer
shift. In `G_N`, a residue class needs a representative convention before
integer divisibility by primes `p>w` is meaningful. This is a range-transfer
issue and remains separate from the diagonal calculation.

### Large finite cutoff

For fixed `z`, the diagonal atom is finite. If `z` grows with `N`, the row
must track `B_{w,z}/N` against `m_{U,V}`, `D`, `K_U`, `K_V`, and the
pair-residual energy in the declared limit order.

### Physical pair diagonal

The physical quantity `P_nu^0(0)=E_r nu_0(r)^2` is also a diagonal object.
This module does not identify it with a chosen finite Euler-product diagonal
or prove its absorption. That identification would be a separate local-model
calibration row.

### W-primes and excluded small primes

All products here run over `p>w`. The W-residue and small-prime removal
conventions are inherited from `P_minor^0`; this module does not change them.

## 7. Project-map location

```text
PairResidualLargeValueStress_361
  -> PairModelMinorTopMassStress_362
  -> PairModelDiagonalConventionAudit_363
  -> PairModelOffDiagonalRamanujanTailAudit_364.
```

The module clears one definitional obstruction: the diagonal cannot remain
inside the unqualified infinite pair Euler product. It does not prove minor
top-mass for the off-diagonal model.

## 8. What remains open

Still open:

```text
PairModelOffDiagonalRamanujanTailAudit_364(P_minor^0),
PairModelRamanujanTailTarget_362,
PairModelMinorTopMassTarget_361,
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

The diagonal convention is now reduced to a named conditional row, not
closed as an analytic estimate.

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
The exact pair local factor is not replaced by a pointwise product shortcut.
The diagonal value is separated precisely because the unqualified local
factor diverges at a=0.
```

Limit-order check:

```text
Finite truncation is kept finite. No z->infty, N->infty, or w->infty limit is
exchanged.
```

Uniformity check:

```text
The diagonal absorption criterion names the required same-family bound but
does not prove it.
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
PairModelDiagonalConventionAudit_363(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairDiagonalDivergenceLemma_363:
  PROVEN.

OffDiagonalPairFactorConvergenceLemma_363:
  PROVEN.

FiniteTruncatedDiagonalFourierLemma_363:
  PROVEN.

PairMixedDiagonalAbsorptionCriterion_363:
  CONDITIONAL.

OffDiagonalPairModelConvention_363:
  STRUCTURAL / EXTRACTION.

UnqualifiedPairDiagonalConvention_363:
  FALSE / BLOCKED.

PairModelDiagonalConventionGate_362:
  CONDITIONAL.
```

Do not cite this module as proving that `K_+^0` is minor-small. It proves
that the diagonal must be separated and gives the finite Fourier cost of doing
so.

## Red flags / forbidden upgrades

- Do not use `kappa_w^0(0)` as an unqualified finite Euler product.
- Do not delete the pair diagonal unless the physical row also excludes it or
  a separate diagonal row is proved.
- Do not treat the diagonal atom as major-arc supported.
- Do not send a finite diagonal cutoff `z` to infinity without a tail and
  absorption argument.
- Do not claim `PairModelMinorTopMassTarget_361`, `ResCube_3^sharp`, or the
  original selected-average problem is solved.
