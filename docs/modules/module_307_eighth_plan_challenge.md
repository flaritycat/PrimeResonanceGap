# Module 307: Eighth plan challenge after fixed-fiber blockage

## 1. Precise theorem / claim being advanced

This module performs the eighth scheduled 15-iteration plan challenge.

Define:

```text
PlanChallenge_8_307.
```

The challenge question is:

```text
After Modules 303-306, should the project keep pushing the q=2 row-square
branch, isolate the size-sensitive fixed-fiber criterion, return to the
threshold-window column side, or redirect Phase K elsewhere?
```

Verdict:

```text
PlanChallenge_8_307:
  STRUCTURAL / EXTRACTION.

ChallengeDecision_307:
  STRUCTURAL / EXTRACTION.

RowSquareContinue_307:
  FALSE / BLOCKED as the next move under the current toolkit.

ColumnBarrierMomentAudit_308(P_minor^0):
  OPEN next target.
```

Decision:

```text
Pause direct row-square continuation.
Do not move to selection transfer.
Do not promote SizeSensitiveClosure_306 into an assumed input.
Next audit the column-multiplicity side of the Module 284 threshold barriers.
```

This module is a steering challenge only. It proves no row barrier, no column
barrier, no threshold closure, no adaptive-shell gain, no minor-arc endpoint,
and no theorem about the original selected-average problem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a cadence checkpoint and branch-selection module. It records which
branch is most honest to test next, given the current ledger. It does not
prove that the row-square target is impossible.

## 3. Cadence counters

The cadence counters before this module are:

```text
Latest completed module: 306
Post-Reflective_1 solving count: 125
Long-term-plan count: 119
```

This module advances them to:

```text
Latest completed module: 307
Post-Reflective_1 solving count: 126
Long-term-plan count: 120
```

The cadence arithmetic is:

```text
120 is divisible by 15,
120 is not divisible by 9,
126 is not the next reflection threshold.
```

Therefore:

```text
eighth plan challenge is due,
fourteenth plan update remains due at long-term-plan count 126,
next reflective log remains expected around Module 341.
```

## 4. Definitions and variables

Work inside the local family:

```text
P_minor^0.
```

Use the Module 284 threshold objects. For `lambda_j in Lambda_0`, define:

```text
Spec_{d,0}^minor(lambda_j)
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j },

E_{d,0}(lambda_j)
  =
  sum_{xi in Spec_{d,0}^minor(lambda_j)}
    |beta_0(d,xi)|^2,

N_{xi,0}(lambda_j)
  =
  # { d:D<|d|<=2D,
      xi in Spec_{d,0}^minor(lambda_j) }.
```

The row moments are:

```text
ShiftMomentP0_284(q;lambda_j)
  =
  D^(-1) sum_{D<|d|<=2D}
    E_{d,0}(lambda_j)^q.
```

The column multiplicity moments are:

```text
MultMomentP0_284(r;lambda_j)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)}
    N_{xi,0}(lambda_j)^r.
```

The two column barriers from Module 284 are:

```text
ColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^((r-1)/r)
    MultMomentP0_284(r;lambda_j)^(1/r),

SigmaColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    ((A_N^0)^2 MultMomentP0_284(r;lambda_j))^(1/r)
    (m_minor^0 H_j/D)^((r-1)/r).
```

The next target selected here is:

```text
ColumnBarrierMomentAudit_308(P_minor^0):
  audit whether current same-family pointwise, counting, Parseval, low-level,
  and vacuous-removal inputs force either column barrier to be o_W(1).
```

## 5. Assumptions

This module assumes Modules 278-306 and the active status ledger.

It does not assume:

```text
ColumnBarrierMomentAudit_308(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
SizeSensitiveClosure_306,
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
AdaptiveShellGainP0_285,
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

## 6. Challenge analysis

### A. What Modules 303-306 taught

The row branch has produced useful status discipline:

```text
Module 303:
  q=2 row-square moment is an exact same-shift restricted-kernel problem over
  data-dependent fibers S_{d,j}.

Module 304:
  fixed-fiber benchmarking was selected before a direct same-shift attack.

Module 305:
  prescribed fibers U_d remove data-dependent selection, but current
  Parseval, Bessel, and full-frequency diagnostics still give only
  ceiling-scale bounds.

Module 306:
  selection transfer is blocked as the next move because there is no
  fixed-fiber gain to transfer; the size-sensitive route is only a criterion.
```

This means the immediate missing object is not merely a transfer theorem. The
analytic gain is already absent in the easier prescribed-fiber benchmark.

### B. Candidate branches

The visible options are:

```text
Option A:
  keep pushing SameShiftSquareKernelGain_303(P_minor^0) directly.

Option B:
  isolate SizeSensitiveClosure_306 as the next proof target.

Option C:
  attempt selection transfer from prescribed fibers to S_{d,j}.

Option D:
  return to the threshold-window column side and audit
  MultMomentP0_284(r;lambda_j), ColumnBarrierP0_284(r), and
  SigmaColumnBarrierP0_284(r).

Option E:
  pause Phase K entirely and redirect away from threshold windows.
```

Option A is not selected. It is still open, but Modules 303-306 show that a
direct same-shift row-square attack currently risks repeating endpoint-scale
kernel statements with new notation.

Option B is not selected now. `SizeSensitiveClosure_306` is a real smaller
criterion, but the ledger has not yet supplied a concrete prescribed-fiber
size/energy theorem or a declared class of useful fibers with summable losses.

Option C is blocked. Transferring a gain that has not been proved would only
move a ceiling to a data-dependent ceiling.

Option E is premature. The threshold-window package needs both row and column
information, and the column side has not yet received the same current-tools
moment audit that Modules 300-306 gave to the row side.

Option D is selected.

### C. Why the column audit is the best next test

Module 299 says useful threshold windows require:

```text
RowBarrierP0_284(q)=o_W(1)
```

and at least one of:

```text
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1).
```

The row side is now blocked under the present toolkit, but that blockage is
more informative if the column side is also audited carefully. A column audit
can answer:

```text
1. Does pure multiplicity counting already fail at the same scale?

2. Does the local low-level fourth-moment tail help column multiplicities, or
   only row energy leakage?

3. Do maximal local thresholds create a useful column schedule, or only the
   same vacuous removal phenomenon as Module 298?

4. Is the sigma-shell column variant genuinely smaller under current inputs,
   or just a relabeled ceiling?
```

If the column side also returns only ceilings, then the next plan update
should consider leaving threshold windows unless a new analytic input appears.

If the column side has a nontrivial route, it still will not close the
threshold package without the row side; it would only identify which half of
the package is not currently the bottleneck.

## 7. Edge cases

If `Lambda_0` is empty, the local threshold sums are empty. That is a local
vacuity, not threshold closure in the useful regime.

If maximal thresholds force all bad sets empty, this reproduces Module 298's
vacuous-removal phenomenon and must not be counted as barrier smallness.

If `m_minor^0` or `H_j` is chosen after inspecting the coefficients, the next
module must state that dependency. Hidden adaptivity cannot be used as a
fixed schedule.

If a column bound uses only the total count

```text
sum_xi N_{xi,0}(lambda_j),
```

it must be checked after the `r`-moment and lambda weights are restored. A
first-moment count is not automatically an `r`-moment barrier.

If the column audit finds a conditional route, it remains inside `P_minor^0`
until transfer rows are supplied. It does not reach the actual sharp moving
selector.

## 8. Project-map location

The local threshold branch now reads:

```text
Module 299:
  threshold windows require row/column barrier smallness plus schedule and
  uniformity rows.

Module 300:
  current row-barrier energy route gives only a ceiling.

Modules 302-303:
  row distribution and q=2 row-square routes are exact but open.

Modules 305-306:
  fixed-fiber row-square benchmarking still gives only ceilings, so selection
  transfer is not the next missing input.

Module 307:
  pause direct row-square continuation and audit the column barriers next.
```

The selected next map is:

```text
ColumnBarrierMomentAudit_308(P_minor^0)
  -> if blocked, record symmetric threshold-window blockage;
  -> if conditional, isolate the exact non-row column input;
  -> if a genuine local column gain is proved, keep it local and still leave
     row and transfer rows open.
```

## 9. What remains open

Still open:

```text
ColumnBarrierMomentAudit_308(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
SizeSensitiveClosure_306,
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
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

## 10. Forbidden upgrades

Do not cite `PlanChallenge_8_307` as an estimate.

Do not cite `RowSquareContinue_307` as a theorem that row-square estimates are
impossible. It is only a next-step blockage under the current toolkit.

Do not treat `SizeSensitiveSubcriterion_306` as a proved size-sensitive
closure.

Do not treat a column first-moment count as an `r`-moment barrier without the
lambda weights and full Module 284 normalization.

Do not prove either column barrier by assuming:

```text
ThresholdWindowClosure_299(q,r),
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move any local `P_minor^0` conclusion to the actual sharp moving
selector without transfer rows.

## 11. Next target

The next target is:

```text
Module 308:
  ColumnBarrierMomentAudit_308(P_minor^0).
```

It should be a proof-or-blocked audit of the Module 284 column multiplicity
moments and column barriers using only current same-family local inputs.
