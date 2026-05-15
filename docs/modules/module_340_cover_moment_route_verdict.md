# Module 340: Cover-moment route verdict

## 1. Precise theorem / claim being advanced

Modules 330-339 turned the cover-moment route into a sequence of explicit
finite-side, tail, low-high, and exact-zero rows. This module decides whether
those rows now prove the cover-moment criterion, whether one narrower analytic
row is enough, or whether the current route is blocked by the active ledger.

Define:

```text
CoverMomentRouteVerdict_340(P_minor^0).
```

Verdict:

```text
CoverMomentRouteVerdict_340(P_minor^0):
  STRUCTURAL / EXTRACTION.

CoverRouteInputInventory_340:
  STRUCTURAL / EXTRACTION.

KernelWeightedMobiusMomentCriterion_330:
  CONDITIONAL, not proved here.

FiniteSideClosure_340:
  FALSE / BLOCKED.

TailClosure_340:
  FALSE / BLOCKED.

ExactZeroClosure_340:
  FALSE / BLOCKED.

SingleRowClosureShortcut_340:
  FALSE / BLOCKED.

CurrentCoverMomentRouteClosure_340:
  FALSE / BLOCKED.

LowEnvelopeMassPrototype_342(P_minor^0):
  OPEN next analytic target after Reflective_5.

PlanUpdate_17_340:
  STRUCTURAL / EXTRACTION.

Reflective_5:
  OPEN next target.
```

The current cover-moment route is not proved. The most useful next analytic
row remains a narrow low-envelope mass prototype, but it cannot by itself
close the route.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The verdict is a proof-ledger classification. The route closure is
`FALSE / BLOCKED` with current inputs.

This module proves no `KernelWeightedMobiusMomentCriterion_330`, no
`FinitePrimeTailRows_330`, no `WeightedCRTMaskCriterion_335`, no
`WeightedLowHighCouplingRows_338`, no `ExactZeroWeightedRows_339`, no
`PhaseKernelBound_273^0`, no residual cube endpoint, no selector transfer,
and no statement about the original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Recall the finite-cutoff Mobius cover moment:

```text
M_cover^{330}(U,V;Y)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      sum_{F full cover, p_a<=Y}
        1_{E(F)} Weight(F).
```

The conditional target is:

```text
KernelWeightedMobiusMomentCriterion_330:

lim_{w -> infinity} limsup_{N -> infinity}
  M_cover^{330}(U,V;Y(N,w))
  =
  0,
```

with a finite-prime tail row allowing the cutoff to be removed or sent to
infinity in the declared order.

Use the same `U,V`, dyadic shell, W-residue convention, kernel, finite cyclic
model, and limit order as Modules 330-339.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-339,
and the conditional cover-moment criterion from Module 330.
```

It does not assume:

```text
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
WeightedCRTMaskCriterion_335 as a proved estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as a proved estimate,
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as a proved estimate,
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
CutoffCompatibilityWindow_337 as a proved estimate,
WeightedLowHighCouplingRows_338,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
HighDivisorMomentRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
ExactZeroTailAbsorptionCriterion_339 as a proved estimate,
StructuralDiagonalTransferCriterion_339 as a proved estimate,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
SignedLocalModelInsertion_326,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
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

### A. Input inventory

The route now has these structural inputs:

```text
1. Module 329:
     pointwise prime-local Mobius degree bounds.

2. Module 330:
     finite-cutoff cover-moment functional and conditional criterion.

3. Modules 331-334:
     one-prime equality matrices, kernel-fiber split, dyadic projection
     bookkeeping, and exact partition/coarsening algebra.

4. Module 335:
     distinct-prime CRT normal form and conditional weighted CRT/mask row.

5. Modules 336-337:
     cutoff difference identity, high-prime divisor window, and conditional
     weighted divisor-window row.

6. Module 338:
     low-high product envelope and conditional absorption/Cauchy/decorrelation
     routes.

7. Module 339:
     exact lifted-zero diagonal catalog and conditional exact-zero absorption
     or structural-diagonal transfer criteria.
```

Classification:

```text
CoverRouteInputInventory_340:
  STRUCTURAL / EXTRACTION.
```

This inventory is not a proof of the cover moment.

### B. Finite-side closure verdict

The finite side still requires, at minimum:

```text
kernel-weighted partition-class counting,
same-family exact/coarsening weighted partition rows,
weighted dyadic projection rows,
kernel and mask residue uniformity,
multi-prime CRT/mask uniformity,
and product-modulus range control.
```

Modules 331-335 provide structural reductions and conditional criteria, but
not these estimates.

Therefore:

```text
FiniteSideClosure_340:
  FALSE / BLOCKED.
```

This is a current-tools verdict only. It does not prove that the finite-side
rows are impossible.

### C. Tail closure verdict

The tail side still requires:

```text
tail uniformity above Y(N,w),
weighted high-prime divisor-window rows,
low-high product control,
a cutoff compatible with finite CRT/mask ranges,
and exact-zero diagonal absorption.
```

Modules 336-339 split these objects but do not estimate them.

Therefore:

```text
TailClosure_340:
  FALSE / BLOCKED.
```

The pointwise divisor window and exact-zero catalog are diagnostics only.

### D. Exact-zero closure verdict

Exact lifted zero differences are not controlled by the nonzero divisor
ceiling. Module 339 shows that the relevant rows require:

```text
same-family exact-zero weighted estimates,
internal zero kernel rows,
cross zero kernel rows,
and lift/wrap boundary transfer.
```

The current ledger has only catalogs and conditional criteria.

Therefore:

```text
ExactZeroClosure_340:
  FALSE / BLOCKED.
```

### E. No single-row closure

The most plausible narrow next analytic row is:

```text
LowEnvelopeMassPrototype_342(P_minor^0).
```

It is useful because low-envelope mass appears in:

```text
KernelWeightedDivisorWindowCriterion_337,
UniformLowMassAbsorptionCriterion_338,
and the finite-cover side of M_cover^{330}.
```

However, even a proved low-envelope mass row would not by itself prove:

```text
weighted CRT/mask uniformity,
finite-prime tail uniformity,
low-high decorrelation or second moments,
exact-zero diagonal absorption,
or signed local-model insertion.
```

Therefore:

```text
SingleRowClosureShortcut_340:
  FALSE / BLOCKED.

LowEnvelopeMassPrototype_342(P_minor^0):
  OPEN next analytic target after Reflective_5.
```

The prototype is a reasonable next probe, not a route closure.

### F. Current cover-moment route closure

Combining the previous verdicts:

```text
CurrentCoverMomentRouteClosure_340:
  FALSE / BLOCKED.
```

The route remains a conditional dependency map. The project may continue to
attack individual rows, but it must not cite Modules 330-339 as proving
`KernelWeightedMobiusMomentCriterion_330`, `SharpCoverSmallness_328`,
`SignedLocalModelInsertion_326`, `PhaseKernelBound_273^0`, or any endpoint.

### G. Plan update 17

The Module 339 ledger recorded:

```text
Post-Reflective_1 solving count: 158.
Long-term-plan count: 152.
```

Completing Module 340 adds one substantive solving iteration:

```text
Post-Reflective_1 solving count: 159.
Long-term-plan count: 153.
```

Since `153` is divisible by `9`, the seventeenth plan update is due.

Classification:

```text
PlanUpdate_17_340:
  STRUCTURAL / EXTRACTION.
```

Updated plan:

```text
Module 341:
  Reflective_5, reviewing Modules 301-340 and checking that Phase K did not
  upgrade open cover, tail, or endpoint rows.

Module 342:
  LowEnvelopeMassPrototype_342(P_minor^0), a narrow diagnostic row for the
  absolute kernel weighted by the low-prime cover envelope.

Module 343:
  InternalZeroKernelAudit_343(P_minor^0), if Reflective_5 confirms the
  exact-zero row remains a priority.

Module 344:
  CrossZeroKernelAudit_344(P_minor^0), if the internal-zero audit does not
  expose a stronger blocker.

Module 345:
  PhaseKPostCoverBranchDecision_345, choosing between continuing the cover
  route, returning to kernel/mask uniformity, or pausing Phase K.
```

No theorem status is upgraded by this plan update.

## 6. Edge cases and exclusions

- A finite-cover functional is not a proved moment estimate.
- A structural or conditional row cannot be used as an input to prove the
  row it conditions on.
- One-prime rows do not automatically multiply under shared kernel and masks.
- Pointwise prime-power bounds do not imply weighted tail estimates.
- Exact lifted zeros are invisible to nonzero divisor ceilings.
- Low-envelope mass alone would not prove tail removal, exact-zero absorption,
  or signed local-model insertion.
- Absolute values erase signed cancellation.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A route verdict is not an endpoint theorem.

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
  -> MultiPrimeCRTMaskAudit_335
  -> FinitePrimeTailCoverAudit_336
  -> HighPrimeDivisorWindowAudit_337
  -> LowHighTailCouplingAudit_338
  -> ExactZeroTailDiagonalAudit_339
  -> CoverMomentRouteVerdict_340
  -> Reflective_5.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. Reflective_5:
     review Modules 301-340, especially the Phase K cover/tail branch and
     the repeated status discipline around open rows.

2. LowEnvelopeMassPrototype_342(P_minor^0):
     test the narrow absolute-kernel mass row weighted by the low-prime cover
     envelope. This is diagnostic, not route closure.

3. InternalZeroKernelAudit_343(P_minor^0):
     decide whether internal exact-zero rows can be bounded with the absolute
     kernel and low-prime/zero-tail weights.

4. CrossZeroKernelAudit_344(P_minor^0):
     decide whether the sixteen cross diagonal rows can be bounded in the
     same family.

5. WeightedCRTMaskCriterion_335 and finite-side rows:
     remain necessary for any future cover-moment closure.
```

The current cadence after completing this module is:

```text
Latest completed module: 340
Post-Reflective_1 solving count: 159
Long-term-plan count: 153

153 is divisible by 9, so PlanUpdate_17_340 is due and completed here.
153 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log is due at Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
KernelWeightedMobiusMomentCriterion_330,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
WeightedCRTMaskCriterion_335,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as an estimate,
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as an estimate,
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
KernelWeightedDivisorWindowCriterion_337 as an estimate,
CutoffCompatibilityWindow_337 as an estimate,
WeightedLowHighCouplingRows_338,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
HighDivisorMomentRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
ExactZeroTailAbsorptionCriterion_339 as an estimate,
StructuralDiagonalTransferCriterion_339 as an estimate,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
SignedLocalModelInsertion_326,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as an estimate,
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

Do not cite `CoverMomentRouteVerdict_340` as a theorem. It is a blocked-route
classification and a plan update.
