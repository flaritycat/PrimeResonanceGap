# Module 328: Full-cover load criterion for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 327 classified full-cover collision families that survive the signed
support audit. This module turns that classification into a sharper criterion:
the full-cover row should be measured by prime-local Mobius coefficients, not
by the crude edge-load envelope alone.

Define:

```text
FullCoverLoadCriterion_328(P_minor^0).
```

Verdict:

```text
FullCoverLoadCriterion_328(P_minor^0):
  STRUCTURAL / EXTRACTION.

FinitePrimeMobiusExpansion_328:
  STRUCTURAL / EXTRACTION.

SharpCoverFunctional_328:
  STRUCTURAL / EXTRACTION.

KernelWeightedSharpCoverCriterion_328:
  CONDITIONAL.

CrudeCoverLoadAsExactCoefficient_328:
  FALSE / BLOCKED.

FirstLoadCoverRoute_328:
  FALSE / BLOCKED.

EnergyOnlyCoverRoute_328:
  FALSE / BLOCKED.

RankOnlyCoverRoute_328:
  FALSE / BLOCKED.

SharpCoverSmallness_328:
  OPEN.

PrimePartitionMobiusAudit_329(P_minor^0):
  OPEN next target.
```

The main correction is that the Module 327 `CoverLoad_{w,8}^{minor}` is a
diagnostic envelope. It is not the exact top Mobius coefficient of the Euler
factor product. A usable criterion needs the actual prime-partition Mobius
weights and then a kernel-weighted estimate for the resulting sharp cover
functional.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The criterion is conditional as an input: if the kernel-weighted sharp cover
functional is proved small in the same family, then it can feed the
full-cover row. This module does not prove that smallness.

It proves no full-cover smallness, no signed local-model insertion, no
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

Use the eight labels and slots:

```text
Lambda_8={1,2,3,4,5,6,7,8},

L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

For a prime `p>w`, let `Pi_p` be the partition of `Lambda_8` into residue
classes modulo `p`:

```text
i and j lie in the same block of Pi_p
  iff
L_i = L_j mod p.
```

For `S subset Lambda_8`, write:

```text
r_p(S)=number of blocks of Pi_p met by S.
```

The `p`-local collision-sensitive factor is:

```text
theta_{p,S}
  =
  (1-1/p)^(-|S|)(1-r_p(S)/p).
```

The generic `p`-local factor is:

```text
theta_{p,|S|}^{gen}
  =
  (1-1/p)^(-|S|)(1-|S|/p).
```

For finite prime cutoff `Y>w`, define the truncated defect ratio:

```text
1+delta_{p,S}
  =
  theta_{p,S}/theta_{p,|S|}^{gen},

Def_Y(S)
  =
  prod_{w<p<=Y} (1+delta_{p,S}) - 1.
```

The full-cover Mobius coefficient at cutoff `Y` is:

```text
m_{Lambda_8}(Def_Y)
  =
  sum_{S subset Lambda_8} (-1)^(8-|S|) Def_Y(S).
```

Removing the finite cutoff `Y` is part of the future uniformity and tail row,
not a theorem supplied here.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
the eight-slot identity from Module 323,
the collision catalog from Module 324,
the generic/collision split from Module 325,
the signed support audit from Module 326,
and the full-cover cluster catalog from Module 327.
```

It does not assume:

```text
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
PrimePartitionMobiusAudit_329,
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

### A. Finite-prime Mobius expansion

For each prime `p`, expand:

```text
1+delta_{p,S}.
```

For any set function `H`, write:

```text
m_T(H)
  =
  sum_{R subset T} (-1)^(|T|-|R|) H(R).
```

At finite cutoff `Y`, the product expansion gives:

```text
Def_Y(S)
  =
  sum_{empty != P_* subset {p: w<p<=Y}}
    prod_{p in P_*} delta_{p,S}.
```

Applying the top Mobius coefficient:

```text
m_{Lambda_8}(Def_Y)
  =
  sum_{empty != P_*}
    m_{Lambda_8}( prod_{p in P_*} delta_{p,.} ).
```

Each summand can survive only if the combined supports of the prime-local
Mobius pieces cover all eight labels. This is the exact finite-cutoff version
of the Module 327 cover principle.

Classification:

```text
FinitePrimeMobiusExpansion_328:
  STRUCTURAL / EXTRACTION.
```

This expansion is algebra at finite `Y`. It is not a convergence theorem, and
it is not a bound for the kernel-weighted row.

### B. Sharp cover functional

For a prime `p` and nonempty `T subset Lambda_8`, define the prime-local
Mobius weight:

```text
mu_p(T)
  =
  |m_T(delta_{p,.})|.
```

Set:

```text
Supp(p,T)=T.
```

For finite cutoff `Y`, define the sharp cover functional:

```text
SharpCover_{w,8}^{minor}(Y)
  =
  sum_{m>=1}
    sum_{(p_1,T_1),...,(p_m,T_m)}
      1_{union_a T_a = Lambda_8}
      prod_{a=1}^m mu_{p_a}(T_a),
```

where `w<p_a<=Y` and repeated primes/sets are handled by the exact finite
product convention chosen for `Def_Y`.

Then the finite-cutoff top coefficient has the structural envelope:

```text
|m_{Lambda_8}(Def_Y)|
  <=
  SharpCover_{w,8}^{minor}(Y).
```

Classification:

```text
SharpCoverFunctional_328:
  STRUCTURAL / EXTRACTION.
```

The point of this definition is to replace the crude edge-cover load from
Module 327 by the actual prime-partition Mobius weights. It still does not
prove that the sharp cover functional is small.

### C. Kernel-weighted sharp cover criterion

A sufficient same-family criterion for the full-cover local-model row is:

```text
KernelWeightedSharpCoverCriterion_328:

For every admissible threshold-localized mask pair U,V,

lim_{w -> infinity} limsup_{N -> infinity}
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      SharpCover_{w,8}^{minor}(Y(N,w))
  = 0,
```

with the finite prime cutoff `Y(N,w)` removed or absorbed by an explicit
uniform tail row.

If this criterion is proved in the exact same `P_minor^0` family, then it can
feed the full-cover part of the model-side signed row.

Classification:

```text
KernelWeightedSharpCoverCriterion_328:
  CONDITIONAL.

SharpCoverSmallness_328:
  OPEN.
```

The criterion does not insert the model into the physical residual row; that
is still `SignedLocalModelInsertion_326`.

### D. Why the crude cover load is not the exact coefficient

Module 327 defined a diagnostic envelope using edge loads such as:

```text
b_p^8=sum_{i<j, p|Delta_{ij}} 1/p.
```

This records that a prime touches many labels, but it does not compute:

```text
m_T(delta_{p,.}).
```

Different partitions with the same number of collision edges can have
different Mobius weights. A no-isolated-vertex graph modulo `p` is only a
support condition; it is not the exact local Euler-factor coefficient.

Therefore:

```text
CrudeCoverLoadAsExactCoefficient_328:
  FALSE / BLOCKED.
```

The crude envelope may still inspire upper bounds, but it cannot be cited as
the signed full-cover coefficient.

### E. Current first-load route

The first collision load:

```text
B_{w,8}^{minor}
  =
  sum_{i<j} sum_{p>w, p|Delta_{ij}} 1/p
```

controls the presence of at least one collision edge. Full-cover control asks
for a top-support event involving all eight labels through one or more
prime-local Mobius pieces.

Even if a first moment for `B_{w,8}^{minor}` were available, it would not by
itself supply:

```text
D^(-1) sum |K_{U,V}^0| SharpCover_{w,8}^{minor}=o_W(1).
```

The missing parts are:

```text
prime-partition Mobius weights,
cover support rather than edge support,
kernel weighting,
data-dependent masks,
overflow/tail control,
and same-family W-limit uniformity.
```

Thus:

```text
FirstLoadCoverRoute_328:
  FALSE / BLOCKED.
```

### F. Current energy-only route

The Fourier-energy inputs from Modules 297-321 control low-level tails,
row/column ceilings, weighted pair ceilings, and data-dependent fiber
diagnostics. They do not estimate the arithmetic prime-partition Mobius
weights:

```text
mu_p(T)=|m_T(delta_{p,.})|.
```

Nor do they control the kernel-weighted full-cover functional after
threshold masks.

Therefore:

```text
EnergyOnlyCoverRoute_328:
  FALSE / BLOCKED.
```

### G. Current rank-only route

Structural full-cover clusters may have several equations, but rank counting
alone is insufficient. One must also control:

```text
wraparound in G_N,
dyadic ranges for d_1,d_2,
the h+k kernel variable,
threshold-localized masks,
finite-prime residue classes,
and the W-limit order.
```

Thus:

```text
RankOnlyCoverRoute_328:
  FALSE / BLOCKED.
```

Rank information remains necessary, but it is not a proof of the
kernel-weighted cover criterion.

## 6. Edge cases and exclusions

- The finite cutoff `Y` is only a bookkeeping device; removing it requires a
  uniform tail row.
- The sharp cover functional is an upper envelope, not the exact signed
  coefficient.
- The crude Module 327 cover load is not the exact prime-local Mobius
  coefficient.
- A one-prime full-cover partition can be important even when the crude edge
  count is small.
- Products of proper-support prime-local coefficients can cover all labels.
- Absolute values erase signed cancellations; signed rows must remain in the
  exact same average.
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
  -> FullCoverLoadCriterion_328
  -> PrimePartitionMobiusAudit_329.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. PrimePartitionMobiusAudit_329(P_minor^0):
     compute or bound mu_p(T)=|m_T(delta_{p,.})| from the partition Pi_p,
     including one-prime full-cover partitions.

2. SharpCoverSmallness_328:
     prove or reject the kernel-weighted sharp cover criterion with the
     finite-prime tail and W-limit order included.

3. FullCoverRankUniformity_327:
     decide whether structural full-cover clusters have enough uniform rank
     after dyadic ranges, wraparound, and the h+k kernel variable are included.

4. SignedLocalModelInsertion_326:
     prove or reject the exact local-model insertion theorem for the signed
     eight-slot minor row with data-dependent masks.
```

## 9. Forbidden upgrades

This module does not prove:

```text
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as an estimate,
PrimePartitionMobiusAudit_329,
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

Do not cite `FullCoverLoadCriterion_328` as a proved estimate. It is a
criterion and a correction of the crude cover-load bookkeeping only.
