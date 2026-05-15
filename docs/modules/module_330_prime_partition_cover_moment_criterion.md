# Module 330: Prime-partition cover-moment criterion for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 329 computed pointwise prime-local Mobius weights. This module turns
those pointwise weights into the moment criterion that would be needed to use
them in the full-cover row.

Define:

```text
PrimePartitionCoverMomentCriterion_330(P_minor^0).
```

Verdict:

```text
PrimePartitionCoverMomentCriterion_330(P_minor^0):
  STRUCTURAL / EXTRACTION.

MobiusCoverMomentFunctional_330:
  STRUCTURAL / EXTRACTION.

KernelWeightedMobiusMomentCriterion_330:
  CONDITIONAL.

PartitionClassCountingRows_330:
  OPEN.

StructuralRankUniformityRows_330:
  OPEN.

MultiPrimeCoverMomentRows_330:
  OPEN.

FinitePrimeTailRows_330:
  OPEN.

CurrentRankHeuristicClosure_330:
  FALSE / BLOCKED.

CurrentCoverMomentClosure_330:
  FALSE / BLOCKED.

PartitionClassCountingAudit_331(P_minor^0):
  OPEN next target.
```

The criterion says that the pointwise Mobius powers from Module 329 become
useful only after partition classes are counted with the actual kernel,
threshold masks, dyadic ranges, finite-prime tails, and W-limit order. Current
rank heuristics and first-load/energy inputs do not prove that criterion.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The criterion is conditional as an input: if the kernel-weighted Mobius-cover
moment is proved small in the same family, then it can feed the full-cover
model-side row. This module does not prove that smallness.

It proves no partition-counting theorem, no kernel-weighted sharp-cover
smallness, no full-cover smallness, no signed local-model insertion, no
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

For a prime `p>w`, let `Pi_p` be the partition of `Lambda_8` into residue
classes modulo `p`. For `T subset Lambda_8`, define:

```text
b_max(T,p)=max_{B in Pi_p}|T cap B|.
```

Module 329 gives the pointwise bound, for `p>8`,

```text
mu_p(T)
  <=
  C_8 p^(-a_p(T)),

a_p(T)=1+|T|-b_max(T,p),
```

with `mu_p(T)=0` if `b_max(T,p)<=1`.

For a finite cutoff `Y>w`, define a cover family:

```text
F=((p_1,T_1),...,(p_m,T_m)),
```

with:

```text
w<p_a<=Y,
empty != T_a subset Lambda_8,
union_a T_a = Lambda_8.
```

Let:

```text
Weight(F)
  =
  prod_{a=1}^m C_8 p_a^(-a_{p_a}(T_a)).
```

Let `E(F)` be the event that every pair `(p_a,T_a)` has the partition pattern
needed for the corresponding nonzero Mobius coefficient.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-329,
the pointwise Mobius-degree bound from Module 329,
and finite cutoff bookkeeping.
```

It does not assume:

```text
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
PartitionClassCountingAudit_331,
PrimeMobiusSmallness_329,
PartitionClassCounting_329,
KernelWeightedMobiusCoverRows_329,
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

### A. Mobius cover moment functional

Define the finite-cutoff Mobius cover moment:

```text
M_cover^{330}(U,V;Y)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      sum_{F full cover, p_a<=Y}
        1_{E(F)} Weight(F).
```

Classification:

```text
MobiusCoverMomentFunctional_330:
  STRUCTURAL / EXTRACTION.
```

This functional is an envelope for the sharp-cover row after inserting the
Module 329 pointwise Mobius-degree bound. It is not the exact signed
coefficient, and it is not a proved estimate.

### B. Kernel-weighted criterion

A sufficient criterion for the full-cover model-side row is:

```text
KernelWeightedMobiusMomentCriterion_330:

For every admissible threshold-localized mask pair U,V,

lim_{w -> infinity} limsup_{N -> infinity}
  M_cover^{330}(U,V;Y(N,w))
  =
  0,
```

with an explicit finite-prime tail row allowing `Y(N,w)` to be removed or
sent to infinity in the declared order.

Classification:

```text
KernelWeightedMobiusMomentCriterion_330:
  CONDITIONAL.
```

If this criterion is proved in the exact same `P_minor^0` family, then it can
feed `SharpCoverSmallness_328` on the model side. It still does not prove
`SignedLocalModelInsertion_326`.

### C. Partition-class counting row

For a fixed prime `p` and a partition pattern `pi` of a subset `T`, the
required counting row has the schematic form:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    |K_{U,V}^0(d_1,d_2;h+k)|
    1_{Pi_p|_T = pi}
  <= acceptable_count(p,pi;U,V),
```

with the same dyadic ranges, threshold masks, W-residue conventions, and
finite-cyclic wrap rules as the target row.

Classification:

```text
PartitionClassCountingRows_330:
  OPEN.
```

No such kernel-weighted partition count is supplied by Module 329.

### D. Structural rank row

A partition pattern `pi` imposes congruences:

```text
L_i = L_j mod p
```

inside each non-singleton block. A naive rank prediction would count about
one factor `p^(-1)` for each independent congruence. But the actual rank can
drop because of:

```text
internal autocorrelation identities,
cross-block affine dependencies,
the dyadic constraints on d_1,d_2,
wraparound in G_N,
the h+k kernel variable,
and data-dependent threshold masks.
```

Classification:

```text
StructuralRankUniformityRows_330:
  OPEN.

CurrentRankHeuristicClosure_330:
  FALSE / BLOCKED.
```

Rank heuristics are useful for designing the next audit, but they are not a
kernel-weighted estimate.

### E. Multi-prime cover moments

A full cover can be formed by several primes:

```text
union_a T_a = Lambda_8.
```

The needed moment is not a product of independent single-prime estimates
unless a same-family CRT/uniformity theorem proves such factorization after
the kernel and masks are present.

Classification:

```text
MultiPrimeCoverMomentRows_330:
  OPEN.
```

The current ledger has no independence theorem for these full-cover families.

### F. Finite-prime tail row

The finite cutoff `Y` is only a bookkeeping device. A usable row must show
that primes above the cutoff contribute an acceptable error, or it must
choose `Y(N,w)` and prove uniformity in the declared limit order:

```text
N -> infinity first at fixed w,
then w -> infinity.
```

Classification:

```text
FinitePrimeTailRows_330:
  OPEN.
```

This is separate from the pointwise `p`-power table.

### G. Current closure verdict

The current ledger has:

```text
pointwise Mobius-degree bounds,
a finite-cutoff cover-moment functional,
and a conditional kernel-weighted criterion.
```

It does not have:

```text
kernel-weighted partition-class counting,
structural rank uniformity,
multi-prime CRT/uniformity,
finite-prime tail control,
data-dependent mask uniformity,
or signed local-model insertion.
```

Therefore:

```text
CurrentCoverMomentClosure_330:
  FALSE / BLOCKED.
```

The next useful target is the partition-counting audit: before estimating the
whole cover moment, the project must know whether even one prime partition
class can be counted with the actual kernel and threshold masks.

## 6. Edge cases and exclusions

- `M_cover^{330}` is an envelope built from pointwise Mobius-degree bounds,
  not the exact signed coefficient.
- A rank prediction is not a kernel-weighted count.
- Single-prime partition counts do not automatically multiply over several
  primes after the kernel and data-dependent masks are present.
- Tail control in `p` is separate from pointwise powers of `1/p`.
- Structural partition classes may align with the kernel variable `h+k`.
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
  -> PrimePartitionCoverMomentCriterion_330
  -> PartitionClassCountingAudit_331.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. PartitionClassCountingAudit_331(P_minor^0):
     test whether one fixed prime partition class can be counted with the
     actual kernel, threshold masks, dyadic ranges, and W-residue conventions.

2. StructuralRankUniformityRows_330:
     determine the true rank of partition constraints after affine
     dependencies, wraparound, and the h+k kernel variable are included.

3. MultiPrimeCoverMomentRows_330:
     prove or reject the CRT/uniformity needed to combine single-prime
     partition counts into full-cover families.

4. FinitePrimeTailRows_330:
     prove or reject tail control above the cutoff Y(N,w).

5. SignedLocalModelInsertion_326:
     prove or reject the exact local-model insertion theorem for the signed
     eight-slot minor row with data-dependent masks.
```

## 9. Forbidden upgrades

This module does not prove:

```text
KernelWeightedMobiusMomentCriterion_330 as an estimate,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
PartitionClassCountingAudit_331,
PrimeMobiusSmallness_329,
PartitionClassCounting_329,
KernelWeightedMobiusCoverRows_329,
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

Do not cite `PrimePartitionCoverMomentCriterion_330` as a proved moment
estimate. It is a criterion and a routing module only.
