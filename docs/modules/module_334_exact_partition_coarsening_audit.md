# Module 334: Exact partition coarsening audit for one-prime rows

## 1. Precise theorem / claim being advanced

Modules 331-333 audited equality envelopes, kernel fibers, and dyadic shift
residue counts for one-prime partition classes. This module audits the gap
between an equality envelope and an exact partition event.

Define:

```text
ExactPartitionCoarseningAudit_334(P_minor^0).
```

Verdict:

```text
ExactPartitionCoarseningAudit_334(P_minor^0):
  STRUCTURAL / EXTRACTION.

PartitionLatticeMobiusIdentity_334:
  STRUCTURAL / EXTRACTION.

EqualityEnvelopeDomination_334:
  STRUCTURAL / EXTRACTION.

CoarseningWeightedCriterion_334:
  CONDITIONAL.

ExactWeightedPartitionRows_334:
  OPEN.

CoarseningWeightedUniformityRows_334:
  OPEN.

CoarseningSignCancellationRoute_334:
  FALSE / BLOCKED.

SameWeightEnvelopeShortcut_334:
  FALSE / BLOCKED.

CurrentExactPartitionClosure_334:
  FALSE / BLOCKED.

MultiPrimeCRTMaskAudit_335(P_minor^0):
  OPEN next target.
```

The audit records the exact finite partition-lattice identity. It does not
prove that the equality-envelope rows, or their coarsenings, are small in the
kernel-weighted cover moment.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The identities below are finite combinatorics of partitions of at most eight
labels. The analytic weighted rows remain open.

This module proves no exact partition count, no weighted equality-envelope
estimate, no mask residue uniformity, no kernel residue uniformity, no
multi-prime CRT product estimate, no finite-prime tail removal, no signed
local-model insertion, no threshold closure, no `PhaseKernelBound_273^0`, no
residual cube endpoint, no selector transfer, and no statement about the
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

Let `T subset Lambda_8`. Let `Part(T)` be the partition lattice of `T`.
Write:

```text
pi <= sigma
```

when `pi` refines `sigma`, so `sigma` is a coarsening of `pi`.

For one prime `p>w`, let:

```text
Pi_p|_T
```

be the actual partition of `T` induced by the congruence relation:

```text
i ~ j  iff  L_i=L_j mod p.
```

For `pi in Part(T)`, define:

```text
Exact_pi(p):
  Pi_p|_T = pi.
```

Define the equality envelope:

```text
Eq_pi(p):
  all labels in every block of pi are equal mod p.
```

Equivalently:

```text
Eq_pi(p) = { pi <= Pi_p|_T }.
```

For threshold-localized masks `U,V`, define the exact weighted row:

```text
C_exact^{334}(pi;p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      1_{Exact_pi(p)}.
```

Define the equality-envelope weighted row:

```text
C_eq^{334}(pi;p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      1_{Eq_pi(p)}.
```

These are local one-prime rows. They are not multi-prime cover estimates.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 329-333,
finite partition-lattice Mobius inversion,
and the exact one-prime partition definitions above.
```

It does not assume:

```text
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
CoarseningWeightedCriterion_334 as a proved estimate,
MultiPrimeCRTMaskAudit_335,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333 as a proved estimate,
KernelResidueMassCriterion_332 as a proved estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
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
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Partition-lattice Mobius identity

The equality envelope is the disjoint union of exact coarsenings:

```text
1_{Eq_pi(p)}
  =
  sum_{sigma in Part(T): pi <= sigma}
    1_{Exact_sigma(p)}.
```

By Mobius inversion on the partition lattice:

```text
1_{Exact_pi(p)}
  =
  sum_{sigma in Part(T): pi <= sigma}
    mob(pi,sigma) 1_{Eq_sigma(p)}.
```

The coefficient is:

```text
mob(pi,sigma)
  =
  prod_{B in sigma}
    (-1)^(m_B-1)(m_B-1)!,
```

where `m_B` is the number of `pi`-blocks contained in the block `B` of
`sigma`.

Classification:

```text
PartitionLatticeMobiusIdentity_334:
  STRUCTURAL / EXTRACTION.
```

This identity is exact and finite. It is not a weighted estimate.

### B. Equality-envelope domination

For nonnegative weights:

```text
1_{Exact_pi(p)} <= 1_{Eq_pi(p)}.
```

Therefore:

```text
C_exact^{334}(pi;p;U,V)
  <=
  C_eq^{334}(pi;p;U,V).
```

Classification:

```text
EqualityEnvelopeDomination_334:
  STRUCTURAL / EXTRACTION.
```

This domination can be useful for absolute upper bounds. It can also be much
too crude. If `pi` is the discrete partition into singletons, `Eq_pi(p)` is
the whole space, while `Exact_pi(p)` is the event that all labels are
distinct modulo `p`.

### C. Coarsening weighted criterion

The exact weighted row can be bounded by coarser equality envelopes:

```text
C_exact^{334}(pi;p;U,V)
  <=
  sum_{sigma: pi <= sigma}
    |mob(pi,sigma)| C_eq^{334}(sigma;p;U,V).
```

A sufficient same-family criterion is:

```text
CoarseningWeightedCriterion_334:

For every one-prime partition pi that appears in the sharp cover functional,
every coarsening sigma >= pi has a kernel-weighted equality-envelope estimate
with its own correct structural rank, kernel-fiber row, dyadic projection row,
mask row, and finite-prime error budget.
```

Classification:

```text
CoarseningWeightedCriterion_334:
  CONDITIONAL.
```

This criterion is not proved here.

### D. Why same-weight envelope shortcuts fail

Module 329 showed that the pointwise prime-local Mobius weight depends on the
largest collision block:

```text
mu_p(T) <= C_8 p^(-(1+|T|-b_max(T,p))).
```

Passing from an exact partition `pi` to a coarsening `sigma` can increase
`b_max`. Larger blocks can have larger pointwise weights.

Example: for `T={1,2,3}`, the exact partition with `{1,2}` colliding and
`3` singleton is represented by a pair block plus singleton. Its pointwise
Mobius size is of order `p^(-2)`. The coarsening where `{1,2,3}` all collide
has pointwise size of order `p^(-1)`.

Thus one may not bound the pair-plus-singleton exact row by its equality
envelope while keeping the pair-plus-singleton weight if the envelope includes
the triple collision. Coarsenings must be charged with their own weights and
their own counting rows.

Classification:

```text
SameWeightEnvelopeShortcut_334:
  FALSE / BLOCKED.
```

### E. Why signed coarsening cancellation is unavailable

The partition-lattice identity has signs:

```text
mob(pi,sigma).
```

But the Module 330 cover-moment envelope and the Module 331-333 rows are
absolute:

```text
|K_{U,V}^0(d_1,d_2;h+k)|,
positive prime-local weights,
and nonnegative partition indicators.
```

Therefore the signed cancellation in:

```text
1_{Exact_pi} = sum_sigma mob(pi,sigma)1_{Eq_sigma}
```

does not by itself reduce the absolute weighted row. To use cancellation, the
project would need a signed same-family row before absolute values are taken,
with the same local model, masks, cutoff, and limiting order.

Classification:

```text
CoarseningSignCancellationRoute_334:
  FALSE / BLOCKED.
```

This does not rule out a future signed row. It only blocks using the lattice
signs inside the current absolute cover-moment envelope.

### F. Interaction with previous micro-rows

For each equality envelope `Eq_sigma(p)`, Modules 331-333 provide only
structural diagnostics:

```text
Module 331:
  equality matrix and rank split;

Module 332:
  kernel-fiber criterion and kernel-residue obstruction;

Module 333:
  unweighted fixed-prime dyadic residue count.
```

To turn the coarsening criterion into an estimate, every coarsening must pass
the open rows:

```text
KernelResidueMassCriterion_332 as an estimate,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333,
and exact W-limit bookkeeping.
```

The number of coarsenings is bounded by a Bell number for at most eight
labels, so the combinatorial count is finite. The obstruction is analytic,
not combinatorial size.

### G. Current closure verdict

The current ledger now has:

```text
the exact partition-lattice Mobius identity,
equality-envelope domination,
and a conditional coarsening criterion.
```

It does not have:

```text
weighted equality-envelope estimates for every coarsening,
same-family signed cancellation before absolute values,
coarsening-sensitive prime-local weights in the cover moment,
mask residue uniformity,
kernel residue uniformity,
weighted dyadic projection uniformity,
multi-prime CRT/mask compatibility,
or finite-prime tail control.
```

Therefore:

```text
CurrentExactPartitionClosure_334:
  FALSE / BLOCKED.
```

The next target is the multi-prime CRT/mask audit: even if every one-prime
coarsening row were available, the Module 330 full-cover families multiply
several primes and require same-family compatibility across primes under the
same kernel and masks.

## 6. Edge cases and exclusions

- The discrete partition has equality envelope equal to the whole space; it
  is a poor substitute for the exact all-distinct event.
- Coarsening can increase collision block size and therefore change the
  correct prime-local Mobius weight.
- Signed Mobius cancellation on the partition lattice is not available inside
  an absolute-value cover-moment envelope.
- Exact inequalities between distinct blocks are not free; they are handled
  by coarsening inversion or by separate exact partition estimates.
- The number of coarsenings is finite, but each coarsening needs the same
  kernel, dyadic, mask, finite-prime, and W-limit discipline.
- A one-prime coarsening audit does not prove multi-prime CRT uniformity.
- The masks `U,V` and shell membership remain data-dependent.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A partition-lattice identity is not an analytic proof.

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
  -> PartitionClassCountingAudit_331
  -> KernelFiberPartitionAudit_332
  -> DyadicResidueUniformityAudit_333
  -> ExactPartitionCoarseningAudit_334
  -> MultiPrimeCRTMaskAudit_335.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. MultiPrimeCRTMaskAudit_335(P_minor^0):
     decide whether one-prime equality/coarsening rows can be combined across
     several primes under the same kernel, dyadic, and mask weights.

2. ExactWeightedPartitionRows_334:
     prove or reject direct same-family estimates for exact partition events.

3. CoarseningWeightedUniformityRows_334:
     prove or reject equality-envelope estimates for every coarsening with
     its own correct weight and structural rank.

4. WeightedDyadicProjectionRow_333 and KernelResidueMassCriterion_332:
     supply the missing weighted residue rows needed by every coarsening.

5. FinitePrimeTailRows_330:
     prove or reject the finite-prime cutoff and tail control needed for the
     cover moment.
```

The current cadence after completing this module is:

```text
Latest completed module: 334
Post-Reflective_1 solving count: 153
Long-term-plan count: 147

147 is not divisible by 9, so no plan update is due in this module.
147 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
CoarseningWeightedCriterion_334 as an estimate,
MultiPrimeCRTMaskAudit_335,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333 as an estimate,
KernelResidueMassCriterion_332 as an estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as an estimate,
PrimeMobiusSmallness_329,
KernelWeightedMobiusCoverRows_329,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as an estimate,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
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

Do not cite `PartitionLatticeMobiusIdentity_334` or
`EqualityEnvelopeDomination_334` as a weighted partition estimate. They are
finite combinatorial reductions only.
