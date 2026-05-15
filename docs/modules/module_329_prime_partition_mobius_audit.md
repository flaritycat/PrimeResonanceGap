# Module 329: Prime-partition Mobius audit for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 328 replaced the crude full-cover edge-load reading with a
prime-local Mobius sharp-cover criterion. This module audits the actual
prime-local Mobius weights:

```text
mu_p(T)=|m_T(delta_{p,.})|.
```

Define:

```text
PrimePartitionMobiusAudit_329(P_minor^0).
```

Verdict:

```text
PrimePartitionMobiusAudit_329(P_minor^0):
  STRUCTURAL / EXTRACTION.

PrimePartitionDefectFormula_329:
  STRUCTURAL / EXTRACTION.

MobiusDegreeBound_329:
  STRUCTURAL / EXTRACTION.

PairBlockWeight_329:
  STRUCTURAL / EXTRACTION.

SingletonAppendagePenalty_329:
  STRUCTURAL / EXTRACTION.

OnePrimeFullCoverPowerTable_329:
  STRUCTURAL / EXTRACTION.

PrimeMobiusSmallness_329:
  OPEN.

PartitionClassCounting_329:
  OPEN.

KernelWeightedMobiusCoverRows_329:
  OPEN.

CurrentPrimeMobiusClosure_329:
  FALSE / BLOCKED.

PrimePartitionCoverMomentCriterion_330(P_minor^0):
  OPEN next target.
```

The audit computes the structural size of a prime-local Mobius coefficient in
terms of the largest collision block inside the relevant label set. It shows
why a one-prime full-cover event can range from order `p^(-1)` to order
`p^(-7)` depending on the partition. No averaged smallness follows.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no kernel-weighted sharp-cover smallness, no full-cover
smallness, no signed local-model insertion, no residual eight-slot
cancellation, no signed minor-kernel gain, no admissible `Phi`, no threshold
closure, no column barrier, no `PhaseKernelBound_273^0`, no residual cube
endpoint, no selector transfer, and no statement about the original
selected-average problem.

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

For a prime `p>w`, let `Pi_p` be the partition of `Lambda_8` into residue
classes modulo `p`:

```text
i ~_p j
  iff
L_i = L_j mod p.
```

For `S subset Lambda_8`, write:

```text
s(S)=|S|,
r_p(S)=number of blocks of Pi_p met by S,
e_p(S)=s(S)-r_p(S).
```

The `p`-local defect ratio from Module 328 is:

```text
1+delta_{p,S}
  =
  theta_{p,S}/theta_{p,s(S)}^{gen}.
```

For a set function `H`, define:

```text
m_T(H)
  =
  sum_{R subset T} (-1)^(|T|-|R|)H(R).
```

The prime-local Mobius weight is:

```text
mu_p(T)=|m_T(delta_{p,.})|.
```

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-328,
finite subset Mobius inversion,
and elementary algebra in the prime-local Euler factor.
```

It does not assume:

```text
PrimeMobiusSmallness_329,
PartitionClassCounting_329,
KernelWeightedMobiusCoverRows_329,
PrimePartitionCoverMomentCriterion_330,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
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

### A. Prime-partition defect formula

By definition:

```text
theta_{p,S}
  =
  (1-1/p)^(-s(S))(1-r_p(S)/p),

theta_{p,s(S)}^{gen}
  =
  (1-1/p)^(-s(S))(1-s(S)/p).
```

Therefore:

```text
1+delta_{p,S}
  =
  (1-r_p(S)/p)/(1-s(S)/p)
  =
  (p-r_p(S))/(p-s(S)).
```

Thus:

```text
delta_{p,S}
  =
  (s(S)-r_p(S))/(p-s(S))
  =
  e_p(S)/(p-s(S)).
```

Classification:

```text
PrimePartitionDefectFormula_329:
  STRUCTURAL / EXTRACTION.
```

This formula is pointwise and local to one prime. It is not a summed
estimate.

### B. Collision excess and singleton appendages

For each block `B` of `Pi_p`, set:

```text
t_B(S)=|S cap B|.
```

Then:

```text
e_p(S)
  =
  sum_{B in Pi_p} max(t_B(S)-1,0).
```

Singleton blocks do not contribute to `e_p(S)`. They can still appear in
`m_T(delta_{p,.})` through the denominator:

```text
1/(p-s(S)).
```

For `p>8`,

```text
1/(p-s(S))
  =
  p^(-1) sum_{a>=0} (s(S)/p)^a.
```

Each extra singleton label not already in a collision-excess monomial costs
at least one additional power of `1/p`.

Classification:

```text
SingletonAppendagePenalty_329:
  STRUCTURAL / EXTRACTION.
```

This corrects a too-rough reading of "full cover": all eight labels may be in
the Mobius support, but singleton appendages can enter only at higher order.

### C. Mobius degree bound

Let `T subset Lambda_8`. Let:

```text
b_max(T,p)
  =
  max_{B in Pi_p} |T cap B|.
```

If `b_max(T,p)<=1`, then no two labels of `T` collide modulo `p`, so:

```text
mu_p(T)=0.
```

If `b_max(T,p)>=2`, the expansion above gives the structural bound:

```text
mu_p(T)
  <=
  C_8 p^(-(1+|T|-b_max(T,p)))
```

for all `p>8`, with `C_8` an absolute constant depending only on eight
labels.

Reason: the collision-excess part can contribute a Mobius monomial supported
inside a single collision block of size at most `b_max(T,p)`. To cover all
labels of `T`, the denominator expansion must supply at least
`|T|-b_max(T,p)` further labels, costing that many extra powers of `1/p`,
in addition to the leading `p^(-1)`.

Classification:

```text
MobiusDegreeBound_329:
  STRUCTURAL / EXTRACTION.
```

This is a pointwise prime-local size bound. It does not count how often such
partitions occur in `(d_1,d_2,x,y,h,k)`, and it does not include the kernel.

### D. Pair-block and small examples

For `T={i,j}`:

```text
mu_p({i,j})
  =
  1_{L_i=L_j mod p}/(p-2).
```

For `T={i,j,k}` with `i,j` in one collision block and `k` singleton:

```text
mu_p(T)
  =
  1/((p-2)(p-3))
```

up to the indicator of that partition pattern. This is order `p^(-2)`.

For `T={i,j,k}` all in one collision block:

```text
mu_p(T)=O(p^(-1)).
```

Classification:

```text
PairBlockWeight_329:
  STRUCTURAL / EXTRACTION.
```

The examples show why active label support and analytic size are different.

### E. One-prime full-cover power table

For `T=Lambda_8`, a single prime can be full cover in many ways. The
Mobius-degree bound gives:

```text
largest collision block size b_max | pointwise order for mu_p(Lambda_8)
-----------------------------------|------------------------------------
8                                  | O(p^(-1))
7                                  | O(p^(-2))
6                                  | O(p^(-3))
5                                  | O(p^(-4))
4                                  | O(p^(-5))
3                                  | O(p^(-6))
2                                  | O(p^(-7))
1                                  | 0
```

Thus a one-prime full-cover graph with no isolated vertices is not a single
analytic size. A perfect matching has `b_max=2` and is much smaller
pointwise than an eight-label block. Conversely, an eight-label block is
pointwise only order `p^(-1)` but should be much rarer as a congruence event;
that rarity is a counting/rank question, not a Mobius algebra fact.

Classification:

```text
OnePrimeFullCoverPowerTable_329:
  STRUCTURAL / EXTRACTION.
```

The table is a pointwise local-factor table. It is not an averaged estimate.

### F. What still needs estimates

To use Module 329 inside the Module 328 criterion, the project still needs:

```text
PartitionClassCounting_329:
  count or bound the frequency of each partition class Pi_p, including
  structural dependencies and wraparound in G_N.

KernelWeightedMobiusCoverRows_329:
  prove the kernel-weighted sum of products of mu_p(T) over full-cover
  families is o_W(1) in the same threshold-localized row.

PrimeMobiusSmallness_329:
  combine pointwise Mobius powers with partition counting, kernel weights,
  dyadic ranges, W-residue conventions, finite-prime tails, and limiting
  order.
```

Classification:

```text
PrimeMobiusSmallness_329:
  OPEN.

PartitionClassCounting_329:
  OPEN.

KernelWeightedMobiusCoverRows_329:
  OPEN.
```

Current first-load, energy-only, and rank-only routes remain blocked by
Module 328.

### G. Current closure verdict

The current ledger now has:

```text
the exact prime-local defect formula,
a singleton-appendage penalty,
a pointwise Mobius-degree bound,
small examples,
and a one-prime full-cover power table.
```

It does not have:

```text
partition-class counting,
kernel-weighted Mobius cover estimates,
finite-prime tail removal,
data-dependent mask uniformity,
or signed local-model insertion.
```

Therefore:

```text
CurrentPrimeMobiusClosure_329:
  FALSE / BLOCKED.
```

The next useful target is a cover-moment criterion that pairs the Mobius
degree table with actual partition-counting and kernel weights.

## 6. Edge cases and exclusions

- A full-cover partition with `b_max=2` can be pointwise high order in
  `1/p`; it is not the same size as an eight-label block.
- An eight-label block has only `O(p^(-1))` Mobius weight pointwise, so its
  usefulness depends on congruence-counting rarity.
- Singleton labels can enter a Mobius coefficient through the denominator,
  but they cost additional powers of `1/p`.
- The bound `C_8 p^{-(1+|T|-b_max)}` is pointwise and local to one prime.
- Products across several primes still need a full-cover family criterion.
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
  -> PrimePartitionMobiusAudit_329
  -> PrimePartitionCoverMomentCriterion_330.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. PrimePartitionCoverMomentCriterion_330(P_minor^0):
     combine the pointwise Mobius-degree table with partition-counting rows,
     kernel weights, and finite-prime tail conventions.

2. PartitionClassCounting_329:
     count the occurrence of each partition class Pi_p under the eight affine
     slots, including structural rank defects.

3. KernelWeightedMobiusCoverRows_329:
     prove or reject the actual full-cover sharp functional after
     threshold-localized kernel weights.

4. SignedLocalModelInsertion_326:
     prove or reject the exact local-model insertion theorem for the signed
     eight-slot minor row with data-dependent masks.
```

## 9. Forbidden upgrades

This module does not prove:

```text
PrimeMobiusSmallness_329,
PartitionClassCounting_329,
KernelWeightedMobiusCoverRows_329,
PrimePartitionCoverMomentCriterion_330,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as an estimate,
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

Do not cite `PrimePartitionMobiusAudit_329` as an averaged collision estimate.
It is a pointwise prime-local Mobius audit only.
