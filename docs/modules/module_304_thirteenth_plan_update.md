# Module 304: Thirteenth plan update after row-square expansion

## 1. Precise theorem / claim being advanced

This module performs the thirteenth scheduled 9-iteration plan update.

Define:

```text
PlanUpdate_13_304.
```

The update records the outcome of Modules 296-303 and chooses the next narrow
Phase K target after the q=2 row-square expansion.

Decision:

```text
Do not attack SameShiftSquareKernelGain_303(P_minor^0) directly yet.

Next target:
  FixedFiberRowSquareBenchmark_305(P_minor^0).
```

The next module should test the q=2 row-square kernel under a deliberately
easier hypothesis: replace the data-dependent fibers `S_{d,j}` by a
prescribed family `U_d subset Minor_0(R,eta)` independent of `beta_0`, and
audit what current tools actually prove. If fixed fibers already return only
the Module 300/302 ceiling, then selection transfer cannot be the first
missing input. If fixed fibers give a genuine gain, the next obstruction is
selection transfer from `U_d` to `S_{d,j}`.

This module does not prove any analytic estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a plan update and branch decision. It does not upgrade any open or
conditional result.

## 3. Cadence counters

The cadence counters before this module are:

```text
Latest completed module: 303
Post-Reflective_1 solving count: 122
Long-term-plan count: 116
```

This module advances them to:

```text
Latest completed module: 304
Post-Reflective_1 solving count: 123
Long-term-plan count: 117
```

The cadence arithmetic is:

```text
117 is divisible by 9,
117 is not divisible by 15,
123 is not the next reflection threshold.
```

Therefore:

```text
thirteenth plan update is due,
eighth plan challenge remains due at long-term-plan count 120,
next reflective log remains expected around Module 341.
```

## 4. Assumptions

This module assumes only the ledger through Module 303.

It does not assume:

```text
FixedFiberRowSquareBenchmark_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
PhaseKernelBound_273^0,
PhaseKernelBound_273,
DirectShellCrossTermGain_287,
SelectionTransfer_280,
UniformFiberBound_280,
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

## 5. Plan update

### A. What changed since Module 295

Modules 296-303 narrowed the Phase K side and row branch:

```text
Module 296:
  pure low-level counting is blocked, but the energy-tail criterion is exact.

Module 297:
  the local fourth-moment low-level tail is proved inside P_minor^0 only.

Module 298:
  maximal local thresholds give vacuous bad-set removal, not useful threshold
  closure.

Module 299:
  useful threshold windows require row/column barrier smallness plus
  admissible schedules.

Module 300:
  current energy-only row inputs give only a polylogarithmic ceiling.

Module 301:
  Reflective_4 preserved the open endpoint statuses and redirected to row
  distribution.

Module 302:
  Markov row tails reproduce the Module 300 ceiling, and endpoint fourth
  moments are circular.

Module 303:
  the q=2 row-square moment is an exact same-shift restricted-kernel problem
  over data-dependent fibers S_{d,j}.
```

The local gains are real but narrow:

```text
LowLevelFourthMomentTailP0_297:
  PROVEN inside P_minor^0.

VacuousActualRemovalP0_298:
  PROVEN inside P_minor^0 for maximal local thresholds only.
```

Neither local gain closes the row barrier, threshold window, adaptive shell
gain, minor-arc endpoint, or original problem.

### B. Questioning the current branch

The q=2 row-square branch is attractive because it is smaller than the full
threshold package. But Module 303 also shows a risk:

```text
The object may still be endpoint-strength if the only way to control it is to
prove a restricted same-shift kernel estimate over data-dependent
large-spectrum fibers.
```

So the next step should not merely restate:

```text
SameShiftSquareKernelGain_303 is open.
```

It must test a smaller question. The cleanest smaller question is whether a
fixed-fiber version of the same kernel is already beyond current tools.

### C. Candidate next branches

After Module 303, the visible options are:

```text
Option A:
  Direct proof-or-blocked audit of SameShiftSquareKernelGain_303(P_minor^0).

Option B:
  FixedFiberRowSquareBenchmark_305(P_minor^0).

Option C:
  SelectionTransferForRowSquare_305 from fixed fibers to S_{d,j}.

Option D:
  DiagonalFourthPowerRow_303(lambda_j) audit.

Option E:
  Pause the row-square branch and return to broad threshold-window closure.
```

Option A is too broad as the immediate next module. It risks becoming another
endpoint restatement unless the fixed-fiber and selection components are
separated.

Option C is premature. A transfer theorem is only useful if the fixed-fiber
target is genuinely controlled with acceptable losses.

Option D is too narrow as the first follow-up because the off-diagonal
same-shift row is the genuinely new q=2 obstruction. The diagonal row should
remain tracked, but it is not the only barrier.

Option E is not selected because threshold-window closure already depends on
row-barrier smallness, and Modules 300-303 show the current row input is the
active bottleneck.

Option B is selected because it tests the smallest meaningful distinction:

```text
Is the obstruction already present for fixed frequency fibers, or does it
enter only through the data-dependent selection S_{d,j}?
```

### D. Selected next target

Define:

```text
FixedFiberRowSquareBenchmark_305(P_minor^0).
```

The Module 305 task is:

```text
1. Fix a prescribed family U_d subset Minor_0(R,eta), independent of beta_0.

2. Define

   E_d^U = sum_{xi in U_d}|beta_0(d,xi)|^2

   and

   RowSq^U = D^(-1) sum_d (E_d^U)^2.

3. Expand RowSq^U into the same-shift kernel with K_{U_d}.

4. Audit current tools:
   Parseval,
   pointwise logarithmic envelope,
   full-frequency diagnostics,
   large-sieve/Bessel style bounds,
   and any fixed-set theorem already present in the ledger.

5. Decide whether fixed fibers produce a genuine row-square gain or only the
   Module 300/302 ceiling.
```

Allowed outcomes:

```text
FixedFiberRowSquareBenchmark_305:
  STRUCTURAL / EXTRACTION
  or FALSE / BLOCKED
  or CONDITIONAL.
```

Not allowed:

```text
PROVEN endpoint closure,
RowSquareMomentTarget_302 proved,
RowBarrierP0_284(2)=o_W(1) proved,
or transfer from U_d to S_{d,j} without a named theorem.
```

### E. Next 9-iteration window

The working window through the next plan update is:

```text
Module 305:
  FixedFiberRowSquareBenchmark_305(P_minor^0).

Module 306:
  Either SelectionTransferBarrier_306(P_minor^0) if fixed fibers look useful,
  or FixedFiberBlockedVerdict_306 if fixed fibers already fail.

Module 307:
  PlanChallenge_8_307.

Modules 308-312:
  Follow the Module 307 challenge decision. Candidate branches are the
  diagonal fourth-power row, off-diagonal same-shift kernel gain, or a return
  to threshold-window/column rows if the row-square branch is blocked.

Module 313:
  PlanUpdate_14_313, unless a non-module solving iteration changes the count.
```

The next window must stay narrow. It should not try to prove the residual cube
endpoint through the row-square branch by name alone.

## 6. Edge cases

If the fixed-fiber benchmark uses `U_d=G_N`, then it is only a full-frequency
diagnostic. It does not control the restricted minor-arc large-spectrum
fibers.

If `U_d=emptyset`, the row-square object is zero for that benchmark only.
This is not a useful estimate.

If `U_d` is allowed to depend on `beta_0`, then the benchmark has silently
returned to the Module 303 object and must be relabeled as a selection problem.

If a fixed-fiber estimate has losses depending on `#U_d`, it must be checked
against the lambda-summed row barrier; a pointwise bound with untracked losses
is not progress.

Nothing in this plan update transfers from `P_minor^0` to the actual sharp
moving selector.

## 7. Project-map location

The active row branch is now:

```text
Module 300:
  energy-only row barrier blocked.

Module 302:
  Markov row distribution blocked; endpoint fourth moment circular.

Module 303:
  q=2 row square expanded into data-dependent same-shift kernels.

Module 304:
  choose fixed-fiber benchmark before direct same-shift attack.
```

The planned local fork is:

```text
FixedFiberRowSquareBenchmark_305
  -> if useful, SelectionTransferBarrier_306;
  -> if blocked, row-square branch needs a new same-shift theorem or should
     be paused by PlanChallenge_8_307.
```

## 8. What remains open

Still open:

```text
FixedFiberRowSquareBenchmark_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `PlanUpdate_13_304` as an estimate.

Do not treat fixed-fiber estimates as data-dependent fiber estimates unless a
selection-transfer theorem is proved.

Do not cite `LowLevelFourthMomentTailP0_297` or
`VacuousActualRemovalP0_298` as threshold-window closure.

Do not prove the row-square or row-barrier target by assuming:

```text
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local plan update to the actual sharp moving selector without
transfer rows.

## 10. Next target

The next target is:

```text
Module 305:
  FixedFiberRowSquareBenchmark_305(P_minor^0).
```

It should be a proof-or-blocked benchmark, not a theorem-upgrade module.
