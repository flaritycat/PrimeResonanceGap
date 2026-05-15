# Module 348: Minimal active pair discrepancy audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 347 isolated the two-sided active subset discrepancies and selected
the four minimal active pair subsets:

```text
{3,7}, {3,8}, {4,7}, {4,8}.
```

This module audits those pairs and the larger class they reveal. The question
is whether the minimal pairs require a new pair local-model theorem, or
whether the nonzero minor-kernel average already kills them inside the local
cyclic model.

Define:

```text
MinimalActivePairDiscrepancyAudit_348(P_minor^0).
```

Verdict:

```text
MinimalActivePairDiscrepancyAudit_348(P_minor^0):
  STRUCTURAL / EXTRACTION.

MinimalActivePairDiscrepancyZero_348(P_minor^0):
  PROVEN inside P_minor^0.

NonFullyCoupledSubsetDiscrepancyZero_348(P_minor^0):
  PROVEN inside P_minor^0.

FullyCoupledSubsetCatalog_348:
  STRUCTURAL / EXTRACTION.

FullyCoupledSubsetDiscrepancyRows_348:
  OPEN.

AllTwoSidedActiveRowsClose_348:
  FALSE / BLOCKED.

MinimalFullyCoupledQuadrupleAudit_349(P_minor^0):
  OPEN next target.
```

The main local result is:

```text
Err_S(U,V)=0
```

inside `P_minor^0` for every subset `S` that does not meet all four slot
groups:

```text
{1,2}, {3,4}, {5,6}, {7,8}.
```

Thus the four minimal active pair discrepancies are exact local zeros. The
first potentially nonzero subset discrepancies must be fully coupled
quadruple-or-larger rows.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves two exact local zero statements inside `P_minor^0`. It
proves no `FullyCoupledSubsetDiscrepancyRows_348`, no
`SignedLocalModelInsertion_326`, no `LocalModelInsertion_325`, no
`DataDependentKernelSelectionRows_325`, no `PhaseKernelBound_273^0`, no
residual cube endpoint, no selector transfer, and no statement about the
original selected-average problem.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the eight slots:

```text
L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k,
z=(x,y,h,k,d_1,d_2),
t=h+k,
Lambda_8={1,2,3,4,5,6,7,8}.
```

Split the slots into four two-element groups:

```text
X_*={1,2},   H_*={3,4},
Y_*={5,6},   K_*={7,8}.
```

Here `H_*` is the first-block group containing `h`, and `K_*` is the
second-block group containing `k`. The groups `X_*` and `Y_*` are the
corresponding pre-shift groups.

For `S subset Lambda_8`, inherit:

```text
Nu_S^{348}(z)
  =
  prod_{i in S} nu_0(L_i(z)),

Theta_{w,S}^{8,min}(z)
  =
  prod_{p>w}
    (1-1/p)^(-|S|)
    (1-r_p(S;z)/p).
```

For threshold-localized masks:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

The discrepancy row is:

```text
Err_S^{348}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      (Nu_S^{348}(z)-Theta_{w,S}^{8,min}(z)).
```

Call `S` fully coupled if:

```text
S cap X_* != emptyset,
S cap H_* != emptyset,
S cap Y_* != emptyset,
S cap K_* != emptyset.
```

Otherwise call `S` non-fully-coupled.

There are:

```text
(2^2-1)^4 = 81
```

fully coupled subsets, and:

```text
256-81 = 175
```

non-fully-coupled subsets.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-347,
the nonzero minor-frequency support of K_{U,V}^0,
and the convention that U(d,xi), V(d,xi) do not depend on x,y,h,k.
```

It does not assume:

```text
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
TwoSidedActiveSubsetDiscrepancyRows_347,
FullyCoupledSubsetDiscrepancyRows_348,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
KernelWeightedMobiusMomentCriterion_330,
WeightedCRTMaskCriterion_335,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

## 5. Proof / disproof / reduction

### A. Coordinate decoupling for an active pair

Fix an active pair:

```text
a in H_*,
b in K_*.
```

Set:

```text
u=L_a,
v=L_b.
```

For fixed `d_1,d_2`, the map:

```text
(x,y,h,k) -> (u,v,h,k)
```

is a bijection of `G_N^4`. In these coordinates:

```text
K_{U,V}^0(d_1,d_2;h+k)
```

is still only a function of `h+k`, while the selected active pair slots are
functions of `u,v` alone. For example:

```text
L_3=u,       L_4=u-d_1      if a=3,
L_4=u,       L_3=u+d_1      if a=4,

L_7=v,       L_8=v-d_2      if b=7,
L_8=v,       L_7=v+d_2      if b=8.
```

Therefore, for `S={a,b}`:

```text
Nu_S^{348}(z)-Theta_{w,S}^{8,min}(z)
```

is independent of both `h` and `k`. Since the kernel is supported on
nonzero frequencies:

```text
E_{h,k} K_{U,V}^0(d_1,d_2;h+k)=0.
```

Thus:

```text
Err_{a,b}^{348}(U,V)=0
```

for all four minimal active pairs.

Classification:

```text
MinimalActivePairDiscrepancyZero_348(P_minor^0):
  PROVEN inside P_minor^0.
```

This is a cyclic nonzero-kernel zero, not a pair Hardy-Littlewood theorem.

### B. Non-fully-coupled subsets are also kernel-invisible

Let `S` be non-fully-coupled.

If `S` misses `H_*` or `K_*`, then Module 347 already gives:

```text
Err_S^{348}(U,V)=0.
```

It remains to consider the case:

```text
S cap H_* != emptyset,
S cap K_* != emptyset.
```

Choose `a in S cap H_*` and `b in S cap K_*`, and again use:

```text
u=L_a, v=L_b.
```

In these coordinates, slots in `H_*` and `K_*` depend only on `u,v` and
fixed shifts. Slots in `X_*` depend on `u-h` and fixed shifts. Slots in
`Y_*` depend on `v-k` and fixed shifts.

If:

```text
S cap X_* = emptyset,
```

then both `Nu_S^{348}` and `Theta_{w,S}^{8,min}` are independent of `h`.
The average over `h` kills every nonzero-frequency term in the kernel.

If:

```text
S cap Y_* = emptyset,
```

then both factors are independent of `k`, and the average over `k` kills the
kernel.

Therefore:

```text
Err_S^{348}(U,V)=0
```

for every non-fully-coupled subset.

Classification:

```text
NonFullyCoupledSubsetDiscrepancyZero_348(P_minor^0):
  PROVEN inside P_minor^0.
```

This extends the one-sided zero of Module 347 but remains internal to the
full cyclic nonzero-frequency model.

### C. Fully coupled subset catalog

The only subset discrepancies not killed by the previous argument are those
meeting all four groups:

```text
X_*, H_*, Y_*, K_*.
```

There are `81` such subsets. The smallest have size four:

```text
{i,j,m,n}
with
i in X_*,
j in H_*,
m in Y_*,
n in K_*.
```

There are:

```text
2^4=16
```

minimal fully coupled quadruples.

Classification:

```text
FullyCoupledSubsetCatalog_348:
  STRUCTURAL / EXTRACTION.
```

### D. Why the fully coupled rows remain open

For a fully coupled subset, after choosing `u=L_a` and `v=L_b` with
`a in H_*`, `b in K_*`, the row still contains at least one factor depending
on `u-h` and at least one factor depending on `v-k`. The nonzero kernel
average:

```text
K_{U,V}^0(d_1,d_2;h+k)
```

can then interact with both variables. The preceding one-variable averaging
argument no longer applies.

The required row remains:

```text
Err_S^{348}(U,V)=o_W(1)
```

for every fully coupled `S`, with the same data-dependent threshold masks and
same limiting order.

Classification:

```text
FullyCoupledSubsetDiscrepancyRows_348:
  OPEN.

AllTwoSidedActiveRowsClose_348:
  FALSE / BLOCKED.
```

The current module kills many subset rows exactly but does not prove signed
local-model insertion.

### E. Next smaller target

The next target should audit the 16 minimal fully coupled quadruples:

```text
MinimalFullyCoupledQuadrupleAudit_349(P_minor^0).
```

This is the first place where the physical product can genuinely couple the
two kernel directions after the obvious cyclic nonzero-frequency cancellations
have been removed.

## 6. Edge cases and exclusions

### Zero frequency

All exact zeros in this module require the kernel to be supported on
`xi != 0`. They do not apply to zero-frequency or full-kernel rows.

### Mask dependence

The argument allows `U(d,xi)` and `V(d,xi)`. It does not allow masks depending
on `x,y,h,k` unless the independence proof is re-established.

### Boundary cuts and lift restrictions

The proof is a full cyclic average in `P_minor^0`. Boundary restrictions,
lift-window cuts, W-limit transfer, selector transfer, or noncyclic
truncation can break the cancellation.

### Pair local model

The minimal active pair rows vanish before any pair local-model theorem is
needed. This does not prove pair model insertion in any weighted nonzero row.

### Fully coupled rows

No fully coupled subset discrepancy is estimated here. In particular, the 16
minimal fully coupled quadruples remain open.

### Selector and endpoint transfer

This module stays inside `P_minor^0`. It does not transfer to the actual
sharp moving selector, full gap averages, the residual cube endpoint, or the
original selected-average problem.

## 7. Where it fits in the project map

```text
Phase K
  -> ResidualEightSlotMinorExpansion_323
  -> CollisionDiagonalStrataAudit_324
  -> GenericCollisionLocalModelSplit_325
  -> SignedInclusionExclusionMinorAudit_326
  -> FullCoverClusterAudit_327
  -> FullCoverLoadCriterion_328
  -> PrimePartitionMobiusAudit_329
  -> PrimePartitionCoverMomentCriterion_330
  -> PartitionClassCountingAudit_331
  -> KernelFiberPartitionAudit_332
  -> DyadicResidueUniformityAudit_333
  -> ExactPartitionCoarseningAudit_334
  -> MultiPrimeCRTMaskAudit_335
  -> FinitePrimeTailCoverAudit_336
  -> HighPrimeDivisorWindowAudit_337
  -> LowHighTailCouplingAudit_338
  -> ExactZeroTailDiagonalAudit_339
  -> CoverMomentRouteVerdict_340
  -> Reflective_5
  -> LowEnvelopeMassPrototype_342
  -> InternalZeroKernelAudit_343
  -> CrossZeroKernelAudit_344
  -> PhaseKPostCoverBranchDecision_345
  -> SignedLocalModelInsertionFeasibility_346
  -> SubsetModelDiscrepancyAudit_347
  -> MinimalActivePairDiscrepancyAudit_348.
```

This module sharpens the signed insertion obstruction by removing all
non-fully-coupled subset rows inside the local cyclic model. It does not
prove `SignedLocalModelInsertion_326`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

Still open:

```text
MinimalFullyCoupledQuadrupleAudit_349(P_minor^0),
FullyCoupledSubsetDiscrepancyRows_348,
TwoSidedActiveSubsetDiscrepancyRows_347 beyond the local zeros,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
KernelWeightedMobiusMomentCriterion_330,
WeightedCRTMaskCriterion_335,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the all-alpha theorem,
the finite-type theorem unconditionally,
and the original selected-average problem.
```

Next target:

```text
MinimalFullyCoupledQuadrupleAudit_349(P_minor^0).
```

## Red flags / forbidden upgrades

Do not cite `MinimalActivePairDiscrepancyZero_348` or
`NonFullyCoupledSubsetDiscrepancyZero_348` outside the full cyclic
nonzero-frequency `P_minor^0` average.

Do not cite these local zeros as signed local-model insertion.

Do not treat fully coupled subset discrepancies as controlled by this
argument.

Do not use pair Hardy-Littlewood, pair-BDH, proper-support signed
cancellation, or generic local density as a substitute for fully coupled
subset discrepancy estimates.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this local zero statement to the actual sharp moving selector
or to the original selected-average problem.
