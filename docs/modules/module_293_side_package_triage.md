# Module 293: Side-package triage inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the side-package triage selected by Module 292.

Define:

```text
SidePkgTriage_293(P_minor^0).
```

The claim advanced is only a classification:

```text
SidePkg_291 is not a single proof target.
It splits into convention rows, proof-hygiene rows, threshold/low-level rows,
degeneracy rows, and adaptive-core rows.
```

The triage verdict is:

```text
SidePkgReady_293:
  OPEN.
```

The first narrow side target selected for the next module is:

```text
LowLevelBudgetTriage_294(P_minor^0).
```

This module does not prove the low-level row. It only selects it as the next
smallest row to classify.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a triage module. It proves no `SidePkg_291`, no
`SideRowsP0Ready_283`, no `DegRowsP0Small_282`, no
`ThresholdBudgetP0Closure_284(q,r)`, no `AdaptiveShellGainP0_285`, and no
endpoint theorem.

## 3. Definitions and variables

Work inside the Module 278 local family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
lambda in Lambda_0,
sigma in Lambda_0,
J=J_trans_0(lambda;sigma),
beta_0(d,xi)=widehat{B_d^0}(xi),
Xi_273^0(lambda;sigma)=sum_{(d,xi) in J}|beta_0(d,xi)|.
```

From Module 292:

```text
SidePkg_291
  =
  ThresholdBudgetP0Closure_284(q,r)
  + SideRowsP0Ready_283
  + DegRowsP0Small_282.
```

Expand the visible rows as:

```text
SideRowsP0Ready_283
  =
  WUniformP0_283
  + ThresholdBudgetP0_283
  + LowLevelCutoffP0_283
  + DyadicUniformityP0_283
  + ShellSelectionP0_283
```

inside the nonzero local rows of `P_minor^0`, with internal convention rows
kept separate.

The threshold closure from Module 284 is:

```text
ThresholdBudgetP0Closure_284(q,r)
  =
  LowLevelBudgetP0_284
  + ShiftRemovalBudget_284(q)
  + FreqRemovalBudget_284(r)
  + min(
      RowShellBudget_284,
      ColumnShellBudget_284,
      SigmaColumnShellBudget_284
    ).
```

The degeneracy package from Module 282 contains:

```text
DegRowsP0Small_282
  =
  ShiftDiag_282 small
  + FreqDiag_282 small
  + RepeatEdge_282 absorbed
  + MajorDiffBound_282
  + PhysDiagLocal_282.
```

The deg-free remainder:

```text
DegFreePhaseGate_282
```

is not treated as a side row in this module; it is a core shell estimate.

## 4. Assumptions

This module assumes only Modules 278-292 and the active status ledger.

It does not assume:

```text
SidePkg_291,
SidePkgReady_293,
LowLevelBudgetTriage_294,
ThresholdBudgetP0Closure_284(q,r),
ThresholdBudgetP0_283,
LowLevelBudgetP0_284,
LowLevelCutoffP0_283,
WUniformP0_283,
DyadicUniformityP0_283,
SideRowsP0Ready_283,
ShellSelectionP0_283,
DegRowsP0Small_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransIncBound_269,
MinorArcTransfer_3^B,
NarrowMinorArc_3^B,
selector transfer,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Triage classes

The side package splits into five classes:

```text
Class 1: internal convention rows
  BoundaryConventionP0_283,
  ResidueConventionP0_283,
  SelectorConventionP0_283,
  BoundaryCutoff_282,
  WPP_282,
  Selector_282.

Class 2: proof-hygiene uniformity rows
  WUniformP0_283,
  DyadicUniformityP0_283.

Class 3: threshold and low-level rows
  ThresholdBudgetP0Closure_284(q,r),
  ThresholdBudgetP0_283,
  LowLevelCutoffP0_283,
  LowLevelBudgetP0_284,
  ShiftRemovalBudget_284(q),
  FreqRemovalBudget_284(r),
  RowShellBudget_284,
  ColumnShellBudget_284,
  SigmaColumnShellBudget_284.

Class 4: degeneracy rows
  ShiftDiag_282,
  FreqDiag_282,
  RepeatEdge_282,
  MajorDiffBound_282,
  PhysDiagLocal_282.

Class 5: adaptive-core rows
  ShellSelectionP0_283,
  DegFreePhaseGate_282,
  AdaptiveShellGainP0_285,
  PhaseKernelBound_273^0.
```

This split is the main output of the module.

### B. Convention rows are local only

Inside `P_minor^0`, the following rows are convention-zero:

```text
BoundaryConventionP0_283,
ResidueConventionP0_283,
SelectorConventionP0_283,
BoundaryCutoff_282,
WPP_282,
Selector_282.
```

They are useful because they keep the local model clean. They do not prove
interval transfer, residue averaging, prime-power restoration, or actual
sharp moving-selector transfer.

Classification:

```text
ConventionRowsP0_293:
  STRUCTURAL / EXTRACTION locally;

ConventionRowsExport_293:
  OPEN outside P_minor^0.
```

These rows are not selected as the next proof target because they are already
classified locally and are not enough to advance the side package.

### C. Uniformity rows are proof-hygiene rows

The rows:

```text
WUniformP0_283,
DyadicUniformityP0_283
```

are essential for any future theorem, but they cannot be proved in isolation
without a theorem whose constants, losses, and parameter ranges can be tested.

Classification:

```text
UniformityRowsP0_293:
  OPEN;
  not selected as first target without a candidate estimate.
```

They should be checked whenever a future estimate is proposed.

### D. Shell selection is not a side row after Phase K

Module 283 listed:

```text
ShellSelectionP0_283
```

inside the side package. Phase K has now tested the visible versions of that
row:

```text
DirectShellCrossTermGain_287,
SelectionComplexityGain_288,
WeightedRCSubgraphGain_289.
```

Module 290 recorded that the current Phase K package does not close
`AdaptiveShellGainP0_285`.

Therefore `ShellSelectionP0_283` should no longer be treated as an ordinary
side row. It is the adaptive-shell core itself.

Classification:

```text
ShellSelectionAsSideRow_293:
  FALSE / BLOCKED.

ShellSelectionP0_283:
  OPEN as an adaptive-core row.
```

The side-package branch must not hide an adaptive-shell gain attempt inside
the word "side".

### E. Deg-free is not a side row

The row:

```text
DegFreePhaseGate_282
```

is the nondegenerate shell phase problem left after routed degeneracies. It
is not side bookkeeping. It is a core phase-kernel estimate and is therefore
not selected as the first side-package target.

Classification:

```text
DegFreeAsSideRow_293:
  FALSE / BLOCKED.

DegFreePhaseGate_282:
  OPEN as a core phase row.
```

### F. Degeneracy rows remain side-adjacent but mixed

The rows:

```text
ShiftDiag_282,
FreqDiag_282,
RepeatEdge_282
```

are tied to the same threshold schedules and lambda-summed row/column budgets
as Module 284.

The rows:

```text
MajorDiffBound_282,
PhysDiagLocal_282
```

are more analytic. Major-like differences between minor frequencies may
re-enter major-arc control, and physical diagonals require same-family
shifted-correlation estimates.

Classification:

```text
DegRowsP0Small_282:
  OPEN.

ShiftFreqDiagTriage_293:
  tied to threshold-budget triage.

MajorPhysDiagTriage_293:
  OPEN, but not first target because it is closer to phase-kernel strength.
```

This does not demote these rows. It only orders the next work.

### G. Threshold closure is too broad for one module

The row:

```text
ThresholdBudgetP0Closure_284(q,r)
```

combines at least:

```text
LowLevelBudgetP0_284,
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284.
```

Trying to prove the whole threshold closure in one step would likely repeat
the Module 284 audit. The next target should be narrower.

Classification:

```text
ThresholdBudgetP0Closure_284(q,r):
  OPEN;
  too broad as the immediate next proof target.
```

### H. First narrow side target: low-level leakage

The narrowest visible row is:

```text
LowLevelBudgetP0_284
```

which corresponds to:

```text
LowLevelCutoffP0_283.
```

It asks whether coefficients below:

```text
lambda_min=A_N^0 N^{-kappa_lambda}
```

can be shown negligible in the local transverse target, uniformly over
`P_minor^0`, without assuming the adaptive shell estimate.

This row is selected first because:

```text
1. It is smaller than PhaseKernelBound_273^0.
2. It is not a selector-transfer theorem.
3. It is local to P_minor^0.
4. It is needed by every threshold schedule.
5. If it is blocked, the threshold package is blocked before moment choices.
```

Classification:

```text
LowLevelBudgetTriage_294(P_minor^0):
  OPEN;
  selected as the next target.
```

No low-level estimate is proved here.

### I. Final triage verdict

The side package should now be read as:

```text
SidePkgReady_293
  =
  LowLevelBudgetP0_284
  + ThresholdMomentAndShellBudgets_293
  + ShiftFreqDiagBudget_293
  + MajorPhysDiagRows_293
  + WDyadicUniformityCheck_293
```

with:

```text
ShellSelectionP0_283
  removed from side-only bookkeeping and returned to the adaptive-core row.

DegFreePhaseGate_282
  kept as a core phase row.

Convention rows
  local-only inside P_minor^0.
```

Therefore:

```text
SidePkgTriage_293(P_minor^0):
  STRUCTURAL / EXTRACTION.

SidePkgReady_293:
  OPEN.

LowLevelBudgetTriage_294(P_minor^0):
  OPEN and selected next.
```

## 6. Edge cases

- A convention-zero row inside `P_minor^0` is not a transfer theorem.
- A proof-hygiene row such as W-uniformity cannot be certified before there
  is an estimate to audit.
- `ShellSelectionP0_283` cannot be used as a side row to bypass the Phase K
  adaptive-shell block.
- `DegFreePhaseGate_282` is a core phase estimate, not a side-package
  bookkeeping row.
- Low-level leakage below `lambda_min` is not negligible by definition.
- Proving a low-level row would not prove threshold closure, degeneracy
  smallness, adaptive-shell gain, or `PhaseKernelBound_273^0`.
- If low-level triage requires `PhaseKernelBound_273^0`,
  `TransIncBound_269`, or `NarrowMinorArc_3^B`, it must be marked blocked.

## 7. Where it fits in the project map

```text
Module 282
  -> degeneracy rows inside P_minor^0

Module 283
  -> side rows inside P_minor^0

Module 284
  -> threshold-budget barriers

Module 292
  -> side-package branch selected

Module 293
  -> side package split; low-level triage selected
```

The next useful step is:

```text
Module 294:
  perform LowLevelBudgetTriage_294(P_minor^0), deciding whether the
  below-lambda_min contribution has a non-endpoint local route or is already
  endpoint-strength.
```

## 8. What remains open

This module does not prove:

- `SidePkg_291`;
- `SidePkgReady_293`;
- `LowLevelBudgetTriage_294`;
- `LowLevelBudgetP0_284`;
- `LowLevelCutoffP0_283`;
- `ThresholdBudgetP0Closure_284(q,r)`;
- `ThresholdBudgetP0_283`;
- `ShiftRemovalBudget_284(q)`;
- `FreqRemovalBudget_284(r)`;
- `RowShellBudget_284`;
- `ColumnShellBudget_284`;
- `SigmaColumnShellBudget_284`;
- `WUniformP0_283`;
- `DyadicUniformityP0_283`;
- `SideRowsP0Ready_283`;
- `ShellSelectionP0_283`;
- `DegRowsP0Small_282`;
- `MajorDiffBound_282`;
- `PhysDiagLocal_282`;
- `DegFreePhaseGate_282`;
- `AdaptiveShellGainP0_285`;
- `PhaseKernelBound_273^0`;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- `MinorArcTransfer_3^B`;
- `NarrowMinorArc_3^B`;
- selector transfer to the actual sharp moving selector;
- `ProjectedModelNeutrality_3^major`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not claim the side package from this triage.
- Do not treat `ShellSelectionP0_283` as a harmless side row after Phase K.
- Do not treat `DegFreePhaseGate_282` as side bookkeeping.
- Do not export local convention rows to the actual sharp moving selector.
- Do not call low-level leakage negligible by definition.
- Do not prove low-level leakage by assuming `PhaseKernelBound_273^0`,
  `TransIncBound_269`, `NarrowMinorArc_3^B`, or endpoint objects.
- Do not change the original, all-alpha, finite-type, RBDH, CPC, AU^3, or
  `ResCube_3^sharp` statuses.
