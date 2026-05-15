# Module 327: Full-cover cluster audit for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 326 showed that signed inclusion-exclusion kills proper-support terms
inside the exact same signed average, but it leaves the top eight-label
Mobius coefficient. This module classifies the full-cover collision clusters
that may survive in that coefficient.

Define:

```text
FullCoverClusterAudit_327(P_minor^0).
```

Verdict:

```text
FullCoverClusterAudit_327(P_minor^0):
  STRUCTURAL / EXTRACTION.

FullCoverSupportCriterion_327:
  STRUCTURAL / EXTRACTION.

OnePrimeFullCoverCatalog_327:
  STRUCTURAL / EXTRACTION.

MultiPrimeCoverProductCatalog_327:
  STRUCTURAL / EXTRACTION.

StructuralFullCoverClusterCatalog_327:
  STRUCTURAL / EXTRACTION.

FullCoverLoadEnvelope_327:
  STRUCTURAL / EXTRACTION.

FullCoverLoadSmallness_327:
  OPEN.

FullCoverRankUniformity_327:
  OPEN.

KernelWeightedCoverRows_327:
  OPEN.

CurrentFullCoverClosure_327:
  FALSE / BLOCKED.

FullCoverLoadCriterion_328(P_minor^0):
  OPEN next target.
```

The audit identifies which collision/load structures are not removed by the
proper-support cancellation from Module 326. It does not estimate their
weighted contribution.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no full-cover smallness, no collision smallness, no
residual eight-slot cancellation, no signed minor-kernel gain, no admissible
`Phi`, no threshold closure, no column barrier, no `PhaseKernelBound_273^0`,
no residual cube endpoint, no selector transfer, and no statement about the
original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use:

```text
Lambda_8={1,2,3,4,5,6,7,8},

L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

For labels `i<j`, write:

```text
Delta_{ij}=L_i-L_j.
```

For a prime `p>w`, define the finite-prime collision graph:

```text
G_p^8(d_1,d_2,x,y,h,k)
```

on vertex set `Lambda_8`, with edge `ij` when:

```text
p | Delta_{ij}.
```

Its active support is:

```text
Supp_p
  =
  { i in Lambda_8 : i is incident to at least one edge of G_p^8 }.
```

For a structural equality or congruence constraint `C`, define:

```text
Supp(C)
  =
  { labels appearing in a nontrivial collision pair forced by C }.
```

A family of constraints or prime-collision graphs:

```text
F={C_a}
```

is a full-cover family if:

```text
union_a Supp(C_a)=Lambda_8.
```

It is a proper-support family if the union is a proper subset of `Lambda_8`.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
the eight-slot identity from Module 323,
the collision catalog from Module 324,
the generic/collision split from Module 325,
and the signed inclusion-exclusion support audit from Module 326.
```

It does not assume:

```text
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
LocalModelInsertion_325,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
MajorLocalModelTransfer_317,
AntiDiagonalTwoShiftKernelGain_312,
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Full-cover support criterion

Module 326 gives:

```text
Delta_8 H = m_{Lambda_8}(H).
```

Hence a collision/load term can survive the signed subset sum only if its
total label support is all of `Lambda_8`.

Therefore:

```text
proper-support family:
  union_a Supp(C_a) subsetneq Lambda_8
  => killed by Delta_8 in the exact same signed average;

full-cover family:
  union_a Supp(C_a)=Lambda_8
  => not killed by support alone.
```

Classification:

```text
FullCoverSupportCriterion_327:
  STRUCTURAL / EXTRACTION.
```

This is a support test. It is not an estimate for the full-cover rows.

### B. One-prime full-cover events

A one-prime full-cover event occurs when, for some `p>w`:

```text
Supp_p=Lambda_8.
```

Equivalently, the collision graph `G_p^8` has no isolated vertex. Minimal
edge support can be as small as four pair-collision edges, for example a
perfect matching modulo `p`, but larger graphs and larger residue classes are
also possible.

Examples of one-prime full-cover shapes include:

```text
four disjoint pair collisions modulo p,
two components of size four,
one component of size eight,
any graph on the eight labels with no isolated vertex.
```

Classification:

```text
OnePrimeFullCoverCatalog_327:
  STRUCTURAL / EXTRACTION.
```

This catalog does not say such events are rare after the actual kernel,
threshold masks, dyadic averaging, and W-limit are restored.

### C. Products of proper-support events

Even when every individual collision event has proper support, a product can
survive if the supports cover all labels. For example:

```text
Supp(C_1)={1,2,3,4},
Supp(C_2)={5,6,7,8}
```

is a full-cover product. Similarly, four pair supports:

```text
{1,2}, {3,4}, {5,6}, {7,8}
```

form a full-cover family.

Thus:

```text
proper-support cancellation is not multiplicative after products are formed.
```

The surviving multi-prime or multi-constraint rows are precisely the cover
families:

```text
F={C_a}: union_a Supp(C_a)=Lambda_8.
```

Classification:

```text
MultiPrimeCoverProductCatalog_327:
  STRUCTURAL / EXTRACTION.
```

This is the first place where the optimistic reading of Module 326 must be
questioned: signed inclusion-exclusion kills isolated proper-support terms,
but products of them can be top-support terms.

### D. Structural full-cover clusters

Module 324 identified structural rows:

```text
h=0, h=d_1, h=-d_1,
k=0, k=d_2, k=-d_2,
```

and sixteen cross-block equations:

```text
x-y=-a d_1-b h+c d_2+e k.
```

Some individual structural rows have proper support. For example, `h=0`
collides labels in the first block, while `k=0` collides labels in the
second block. Their intersection can cover all eight labels.

More generally, a structural cluster:

```text
Z_F = intersection_{C in F} C
```

is full-cover if:

```text
union_{C in F} Supp(C)=Lambda_8.
```

Classification:

```text
StructuralFullCoverClusterCatalog_327:
  STRUCTURAL / EXTRACTION.
```

Structural full-cover does not mean small. It can have dependent equations,
lower-than-expected rank, or large interaction with `K_{U,V}^0(d_1,d_2;h+k)`.

### E. Full-cover load envelope

Define a diagnostic prime-collision edge load:

```text
b_p^8(d_1,d_2,x,y,h,k)
  =
  sum_{1<=i<j<=8, p | Delta_{ij}} 1/p.
```

For a finite ordered family of primes `P_*=(p_1,...,p_m)`, define:

```text
Supp(P_*)
  =
  union_{a=1}^m Supp_{p_a}.
```

A full-cover load envelope is:

```text
CoverLoad_{w,8}^{minor}
  =
  sum_{1<=m<=8}
    sum_{p_1,...,p_m>w
         Supp(p_1,...,p_m)=Lambda_8}
      prod_{a=1}^m b_{p_a}^8(d_1,d_2,x,y,h,k),
```

with repeated primes either disallowed or merged in any future precise
criterion. This is an envelope, not the exact Mobius coefficient.

The edge-cover lower bound is:

```text
pure pair-edge full cover requires at least four pair supports.
```

This suggests that a future full-cover row should be at least fourth-order in
pair-collision load on genuinely generic tuples. The suggestion is not a
proof, because structural dependencies, one-prime large components, overflow,
and kernel weights may change the effective size.

Classification:

```text
FullCoverLoadEnvelope_327:
  STRUCTURAL / EXTRACTION.
```

The envelope is a proposed measuring device for the next module, not a
smallness theorem.

### F. Required analytic rows

A usable full-cover estimate must control rows such as:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    |K_{U,V}^0(d_1,d_2;h+k)|
    CoverLoad_{w,8}^{minor}(d_1,d_2,x,y,h,k)
  = o_W(1),
```

or an exact signed analogue in the same row. The signed analogue must keep
the same masks, cutoff, dyadic range, W-residue convention, minor-arc
convention, and limiting order.

Classification:

```text
FullCoverLoadSmallness_327:
  OPEN.

KernelWeightedCoverRows_327:
  OPEN.
```

The structural equations also need a rank/uniformity row:

```text
FullCoverRankUniformity_327:
  OPEN.
```

because codimension counting can fail if equations are dependent, wrap around
`G_N`, or align with the kernel variable `h+k`.

### G. Current closure verdict

The current ledger has:

```text
proper-support cancellation,
the full-cover support criterion,
catalogs of one-prime and multi-event cover families,
and a diagnostic cover-load envelope.
```

It does not have:

```text
kernel-weighted cover-load smallness,
rank/uniformity estimates for structural full-cover clusters,
overflow control,
data-dependent kernel-selection uniformity,
or signed local-model insertion.
```

Therefore:

```text
CurrentFullCoverClosure_327:
  FALSE / BLOCKED.
```

The next useful step is not to assert that full-cover clusters are negligible,
but to formulate a precise cover-load criterion and test whether current
inputs can satisfy it.

## 6. Edge cases and exclusions

- A full-cover family need not be connected. A perfect matching covers all
  eight labels but has four components.
- A connected collision graph is sufficient for full cover, but not necessary.
- One-prime full-cover events are not the same as products of several
  proper-support prime events; they need different local estimates.
- Products of proper-support events can survive signed inclusion-exclusion.
- Structural full-cover clusters may have dependent equations, so naive
  codimension multiplication is not reliable.
- The full-cover load envelope is not the exact signed local coefficient.
- The data-dependent masks `U,V` remain part of the row.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- The full gap is not a clipped gap, a tail row, or a model gap.
- A structural reduction is not an analytic proof.
- A conditional theorem is not a theorem.
- No endpoint object may be used as an assumption in a module meant to prove
  that endpoint.

## 7. Project-map location

This module lies on the Phase K minor-arc branch:

```text
WeightedPairAutocorrelationExpansion_312
  -> MinorKernelRowSplit_314
  -> SignedMinorKernelCombinationVerdict_318
  -> AntiDiagonalNewInputInventory_319
  -> SizeSensitiveMinorKernelCriterion_320
  -> DataDependentFiberGainAudit_321
  -> PlanUpdate_15_Challenge_9_322
  -> ResidualEightSlotMinorExpansion_323
  -> CollisionDiagonalStrataAudit_324
  -> GenericCollisionLocalModelSplit_325
  -> SignedInclusionExclusionMinorAudit_326
  -> FullCoverClusterAudit_327
  -> FullCoverLoadCriterion_328.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. FullCoverLoadCriterion_328(P_minor^0):
     turn CoverLoad_{w,8}^{minor} into a precise criterion with no hidden
     endpoint assumptions and test the available load moments against the
     kernel and threshold losses.

2. FullCoverRankUniformity_327:
     decide whether structural full-cover clusters have enough uniform rank
     after dyadic ranges, wraparound, and the h+k kernel variable are included.

3. KernelWeightedCoverRows_327:
     prove or reject kernel-weighted smallness for one-prime and multi-prime
     cover families.

4. SignedLocalModelInsertion_326:
     prove or reject the exact local-model insertion theorem for the signed
     eight-slot minor row with data-dependent masks.
```

## 9. Forbidden upgrades

This module does not prove:

```text
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
LocalModelInsertion_325,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
AntiDiagonalTwoShiftKernelGain_312,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

Do not cite `FullCoverClusterAudit_327` as proof that full-cover clusters are
small. It is a classification and criterion-preparation module only.
