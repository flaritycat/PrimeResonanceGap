# Module 322: Fifteenth plan update and ninth plan challenge after fiber-gain blockage

## 1. Precise theorem / claim being advanced

This module performs the scheduled combined cadence checkpoint after
Modules 313-321. It does not prove a new estimate. It decides which exact
local object should be audited next after Module 321 showed that the current
row caps, column caps, shell heights, energy tails, and selection rules do not
force an admissible `Phi` gain.

Define:

```text
PlanUpdate_15_Challenge_9_322.
```

Verdict:

```text
PlanUpdate_15_Challenge_9_322:
  STRUCTURAL / EXTRACTION.

ChallengeDecision_322:
  STRUCTURAL / EXTRACTION.

PhaseKColumnBranchContinue_322:
  FALSE / BLOCKED as a direct cap-only or fiber-only continuation.

FiberOverlapDirectAttack_322(P_minor^0):
  FALSE / BLOCKED as the next move under current inputs.

ResidualEightSlotMinorPivot_322(P_minor^0):
  STRUCTURAL / EXTRACTION.

ResidualEightSlotMinorExpansion_323(P_minor^0):
  OPEN next target.
```

The decision is:

```text
Pause the cap-only fiber-overlap route.
Do not attack FiberOverlapGainTarget_321 directly with the same inputs.
Do not assume an admissible Phi.
Pivot next to an extraction-only residual eight-slot minor expansion.
```

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module is governance and proof-ledger maintenance. It proves no
threshold closure, no column barrier, no row barrier, no admissible `Phi`, no
signed minor-kernel gain, no residual cube endpoint, and no selector transfer.

## 3. Definitions and variables

Work in the active local family:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

The current exact row is the centered minor-kernel row:

```text
WOff_311
  =
  the off-diagonal weighted same-frequency pair row after the exact
  Module 312 autocorrelation expansion and Module 315 centering.
```

Module 320 introduced cross-shell pieces:

```text
U=J_{j,k},
V=J_{j,l},
k,l>=j,
```

and the conditional majorant criterion:

```text
WOff(U,V) <= Phi_{j;k,l}.
```

The admissible `Phi` would need to pass at least one of:

```text
ColumnBarrier_320(Phi)=o_W(1),
SigmaColumnBarrier_320(Phi)=o_W(1).
```

Module 321 audited the fiber overlaps:

```text
Overlap_N(U,V)=sum_xi N_U(xi)N_V(xi),

Overlap_C(U,V)=sum_xi C_U(xi)C_V(xi),
```

and found that the current deterministic caps still permit complete
same-frequency concentration.

The next proposed object is a residual eight-slot minor expansion:

```text
ResidualEightSlotMinorExpansion_323(P_minor^0):
  expand the centered minor-kernel row in the exact residual variables,
  with the minor cutoff, W-residue convention, dyadic shell weights,
  threshold losses, and off-diagonal shift condition all still visible.
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278-321.

It uses the following facts only as structural inputs:

```text
Module 312 gives the exact anti-diagonal two-shift autocorrelation form.
Module 314 gives the full/zero/major row split.
Module 315 gives the centered rewrite that removes the explicit zero row.
Module 316 blocks current centered full-row closure.
Module 317 blocks current major-correction closure.
Module 318 identifies centered full-minus-major with WOff_311.
Module 319 rejects endpoint assumptions and records residual eight-slot
  minor cancellation as a genuine but open candidate.
Module 320 formulates the conditional Phi criterion.
Module 321 blocks deriving admissible Phi from current fiber caps alone.
```

It does not assume:

```text
ResidualEightSlotMinorExpansion_323(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
PhiCriterion_320(Phi) with a proved Phi,
SignedMinorKernelGain_318(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
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

### A. Cadence check

Before this module the active counters were:

```text
Latest completed module: 321
Post-Reflective_1 solving count: 140
Long-term-plan count: 134
```

After this module they become:

```text
Latest completed module: 322
Post-Reflective_1 solving count: 141
Long-term-plan count: 135
```

The long-term-plan count `135` is divisible by both `9` and `15`, so both the
plan update and plan challenge are due here. This module completes both.

### B. Review of the active branch

The branch since the fourteenth plan update has become very narrow:

```text
Module 313:
  blocks a direct attack on AntiDiagonalTwoShiftKernelGain_312 as the next
  move and selects the exact minor-kernel row split.

Module 314:
  splits WOff_311 into full-frequency, zero-mode, and major-correction rows,
  but independent row smallness is not available.

Module 315:
  shows the zero row is not killed by the minor convention, then replaces the
  explicit zero row by an exact centered rewrite.

Module 316:
  identifies the centered full row as a full nonzero-frequency column second
  moment, still uncontrolled by current tools.

Module 317:
  identifies the major correction as a positive major-frequency pair-energy
  row, still requiring an exact residual eight-slot major model.

Module 318:
  proves that the centered full-minus-major row is exactly WOff_311, so the
  split is diagnostic unless a new same-family signed theorem is supplied.

Module 319:
  filters possible new inputs and keeps only genuine, non-endpoint candidates.

Module 320:
  extracts a size-sensitive Phi criterion but leaves the required Phi open.

Module 321:
  shows the current fiber caps do not force that Phi.
```

Thus the cap-only continuation has run out of force. Repeating it would only
rename the same ceiling.

### C. Challenge question

The checkpoint asks which next move is least circular:

```text
Option A:
  Continue directly through FiberOverlapGainTarget_321.

Option B:
  Assume or search for an admissible Phi without opening the residual
  structure.

Option C:
  Return to the projected-major or residual-cube endpoint map.

Option D:
  Pause the cap-only fiber branch and extract the residual eight-slot minor
  expansion inside P_minor^0.
```

Option A is blocked as the immediate next move because Module 321 shows the
current deterministic constraints still allow complete same-frequency
concentration.

Option B is blocked because an admissible `Phi` is exactly the missing input;
using it now would make the criterion circular.

Option C is blocked as an immediate proof move because the projected-major
and residual-cube endpoint rows remain open and cannot be imported as
hypotheses.

Option D is selected, but only as structural work. It asks for a more exact
expansion of the signed residual expression so that future modules can see
whether the eight residual slots contain a smaller collision/generic split or
only another form of the same endpoint-strength target.

Classification:

```text
ChallengeDecision_322:
  STRUCTURAL / EXTRACTION.

PhaseKColumnBranchContinue_322:
  FALSE / BLOCKED as a direct cap-only or fiber-only continuation.

FiberOverlapDirectAttack_322(P_minor^0):
  FALSE / BLOCKED as the next move under current inputs.

ResidualEightSlotMinorPivot_322(P_minor^0):
  STRUCTURAL / EXTRACTION.
```

### D. The next nine-iteration window

The next plan window should keep the branch small and falsifiable:

```text
Module 323:
  ResidualEightSlotMinorExpansion_323(P_minor^0).
  Expand the centered minor-kernel row into exact eight residual slots.

Module 324:
  Audit collision and diagonal strata in that eight-slot minor row.

Module 325:
  Separate generic local factors from collision defects, without importing
  the major-arc projected model.

Module 326:
  Test whether signed inclusion-exclusion creates a genuinely smaller minor
  cancellation target or only restates WOff_311.

Module 327:
  Compare the residual eight-slot route against ResCube_3^sharp and mark any
  endpoint-strength assumptions explicitly blocked.

Module 328:
  Extract any admissible local cancellation criterion that would imply a
  usable Phi after Module 320 losses.

Module 329:
  Audit current tools against that local cancellation criterion.

Module 330:
  Decide whether a non-endpoint subtarget remains or whether Phase K should
  be paused.

Module 331:
  Perform the sixteenth plan update.
```

This schedule is provisional steering. It supplies no theorem status beyond
the labels stated here.

## 6. Edge cases

If the eight-slot expansion is merely an algebraic restatement of `WOff_311`,
then Module 323 should say so and route the branch toward a pause rather than
pretending to have found a new estimate.

If a collision stratum vanishes by the internal conventions of `P_minor^0`,
that is not a transfer theorem for the actual sharp moving selector.

If a signed cancellation row appears, it must remain in the same projection,
cutoff, denominator, W-residue, dyadic-shell, selector, and limiting family.

If a future criterion controls only a clipped gap, model selector, frozen
selector, or finite-stage measure, it does not control the full selected
average without the named transfer rows.

If a proposed major-arc comparison uses an averaged local factor in place of
the exact local factor, it is a diagnostic, not a proof input.

## 7. Project-map location

The active map now reads:

```text
Weighted column-pair energy
  -> anti-diagonal two-shift autocorrelation
  -> centered minor-kernel row WOff_311
  -> full/zero/major diagnostic split
  -> signed full-minus-major verdict
  -> new-input inventory
  -> Phi criterion
  -> fiber-gain audit
  -> plan update/challenge
  -> residual eight-slot minor expansion next.
```

This is still inside the local `P_minor^0` proof ledger. It does not reach the
actual sharp moving selector or the original selected-average problem.

## 8. What remains open

Still open:

```text
ResidualEightSlotMinorExpansion_323(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
SizeSensitiveMinorKernelCriterion_320 as an estimate,
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `PlanUpdate_15_Challenge_9_322` as an estimate.

Do not cite `ResidualEightSlotMinorPivot_322(P_minor^0)` as residual
eight-slot cancellation.

Do not attack `FiberOverlapGainTarget_321(P_minor^0)` again with only the
row caps, column caps, shell-height restrictions, energy tails, and selection
rules audited in Module 321.

Do not assume an admissible `Phi` inside a module whose purpose is to produce
that `Phi`.

Do not replace the actual sharp moving selector by a model, frozen, smoothed,
or finite-stage selector without a named transfer theorem.

Do not replace the full gap by a clipped gap or tail without a named gap/tail
transfer theorem.

Do not replace an exact local factor by an averaged substitute.

Do not treat a structural reduction as an analytic proof.

Do not use a conditional theorem as an established theorem.

Do not use any endpoint object as an assumption in a module meant to prove or
reduce that same endpoint.

## 10. Next target

The next target is:

```text
Module 323:
  ResidualEightSlotMinorExpansion_323(P_minor^0).
```

It should expand the centered minor-kernel row into exact eight residual
slots, keep all local conventions and losses visible, and decide whether the
expansion exposes a smaller non-endpoint target or simply restates the
signed minor-kernel obstruction.
