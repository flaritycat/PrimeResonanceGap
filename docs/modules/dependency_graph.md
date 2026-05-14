# Dependency Graph

This graph is a status map, not a proof. Solid arrows mean "would require" or
"feeds into if established." Dashed arrows mark structural/equivalence
relationships that must not be read as analytic closure.

```mermaid
flowchart TD
  Original["Original selected-average problem<br/>OPEN"]
  SharpSel["Actual sharp moving selector transfer<br/>OPEN"]
  FiniteType["Finite-type branch<br/>CONDITIONAL"]
  Metric["Metric a.e. branch<br/>PROVEN a.e.; not all-alpha"]
  Obstruction["Obstruction branches<br/>STRUCTURAL / CONDITIONAL"]

  ResCube["Residual derivative cube endpoint<br/>OPEN"]
  MajorTarget["ProjectedMajorTarget_3^B<br/>OPEN"]
  MinorTarget["MinorTarget_3^B / NarrowMinorArc_3^B<br/>OPEN / CONDITIONAL"]
  TransInc["TransIncCore_269 / TransIncBound_269<br/>definition STRUCTURAL; bound OPEN"]
  ThresholdAudit["ThresholdRemovalAudit_270 / ThresholdOnlyClosure_270<br/>audit STRUCTURAL; closure OPEN"]
  PhaseExpansion["TransPhaseExpansion_271 / PhaseIncidenceGate_271<br/>identity STRUCTURAL; gate OPEN"]
  ToolCompat["PhaseToolCompatAudit_272 / AvailableToolClosure_272<br/>audit STRUCTURAL; closure OPEN"]
  TransGate["TransverseIncidenceGate_273 / PhaseKernelBound_273<br/>gate STRUCTURAL; kernel bound OPEN"]
  TransGateCompat["TransGateCompatAudit_274 / TransGateSideRows_274<br/>audit STRUCTURAL; side rows OPEN"]
  DegAudit["TransDegeneracyAudit_275 / DegFreePhaseGate_275<br/>routing STRUCTURAL; remainder OPEN"]
  TransVerdict["TransverseGateVerdict_276 / TransverseGateProofPkg_276<br/>verdict STRUCTURAL; proof package OPEN"]
  MinTransFamily["MinimalTransverseFamily_278(P_minor^0)<br/>definition STRUCTURAL"]
  XiExpansion["XiDualPhaseExpansion_279(P_minor^0)<br/>identity STRUCTURAL"]
  FixedShellAudit["FixedSetShellAudit_280<br/>audit STRUCTURAL; automatic transfer BLOCKED"]
  FixedShellTransfer["UniformFiber / SelectionTransfer / DirectShell<br/>OPEN routes"]
  LSBesselBench["LSBesselBenchmark_281<br/>benchmark STRUCTURAL; adaptive gain OPEN"]
  DegRowsP0["DegRowsP0Audit_282(P_minor^0)<br/>audit STRUCTURAL; smallness OPEN"]
  SideRowsP0["SideRowsP0Audit_283(P_minor^0)<br/>audit STRUCTURAL; ready package OPEN"]
  ThresholdP0["ThresholdBudgetP0Audit_284<br/>audit STRUCTURAL; closure OPEN"]
  AdaptiveShellP0["AdaptiveShellVerdict_285<br/>current tools BLOCKED; gain OPEN"]
  PlanUpdate11["PlanUpdate_11_286<br/>Phase K selected"]
  DirectTTStar["DirectShellTTStarAudit_287<br/>audit STRUCTURAL; cross gain OPEN"]
  SelectionComplexity["SelectionComplexityAudit_288<br/>audit STRUCTURAL; complexity gain OPEN"]
  UniformFiberStress["UniformFiberStress_289<br/>audit STRUCTURAL; row/column-only gain BLOCKED"]
  WeightedRCSubgraph["WeightedRCSubgraphGain_289<br/>OPEN"]
  AdaptiveVerdict290["PhaseKAdaptiveShellVerdict_290<br/>current closure BLOCKED"]
  PhaseKCleanup291["PhaseKStatusCleanup_291<br/>same-tools continuation BLOCKED"]
  PlanChallenge7["PlanChallenge_7_292<br/>selects side-package triage"]
  SidePkgTriage293["SidePkgTriage_293<br/>triage STRUCTURAL; ready package OPEN"]
  LowLevelTriage294["LowLevelBudgetTriage_294<br/>triage STRUCTURAL; budget OPEN"]
  PlanUpdate12["PlanUpdate_12_295<br/>plan update STRUCTURAL"]
  LowLevelBarrier296["LowLevelCountingBarrierAudit_296<br/>audit STRUCTURAL; pure counting BLOCKED"]
  E2Tail297["E2MinorEnergyTailAudit_297<br/>audit STRUCTURAL; local tail PROVEN"]
  ShiftFreq298["ShiftFreqRemovalAudit_298<br/>audit STRUCTURAL; vacuous removal not closure"]
  ThresholdWindow299["ThresholdWindowCompatibilityAudit_299<br/>audit STRUCTURAL; barriers OPEN"]
  RowBarrier300["RowBarrierMomentAudit_300<br/>audit STRUCTURAL; current route BLOCKED"]
  Reflective4["Reflective_4<br/>memory log STRUCTURAL"]
  RowMoment302["RowMomentDistributionAudit_302<br/>audit STRUCTURAL; Markov/circular routes BLOCKED"]
  RowSquare303["RowSquareMomentExpansion_303<br/>identity STRUCTURAL; shortcuts BLOCKED"]
  PlanUpdate13["PlanUpdate_13_304<br/>plan update STRUCTURAL"]
  FixedFiber305["FixedFiberRowSquareBenchmark_305<br/>benchmark STRUCTURAL; current tools BLOCKED"]
  FixedFiber306["FixedFiberBlockedVerdict_306<br/>verdict STRUCTURAL; selection next BLOCKED"]
  PlanChallenge8["PlanChallenge_8_307<br/>challenge STRUCTURAL; row-square next move BLOCKED"]
  ColumnBarrier308["ColumnBarrierMomentAudit_308<br/>audit STRUCTURAL; current route BLOCKED"]
  ColumnDist309["ColumnMultiplicityDistributionAudit_309<br/>audit STRUCTURAL; first-moment route BLOCKED"]
  ColumnPair310["ColumnPairMultiplicityExpansion_310<br/>expansion STRUCTURAL; off-diagonal OPEN"]
  WPair311["WeightedColumnPairEnergyAudit_311<br/>audit STRUCTURAL; current route BLOCKED"]
  AutoCorr312["WeightedPairAutocorrelationExpansion_312<br/>identity STRUCTURAL; current tools BLOCKED"]
  AntiDiag312["AntiDiagonalTwoShiftKernelGain_312<br/>OPEN"]
  PlanUpdate14["PlanUpdate_14_313<br/>completed; selects row split"]
  MinorKernel314["MinorKernelRowSplit_314<br/>split STRUCTURAL; controls OPEN"]
  ZeroAudit315["ZeroModeProductAudit_315<br/>audit STRUCTURAL; standalone control BLOCKED"]
  CenteredFull316["CenteredFullAntiDiagonalAudit_316<br/>next target OPEN"]
  PhaseKernel0["PhaseKernelBound_273^0 over P_minor^0<br/>OPEN"]
  SelectorTransfer["Selector transfer packages<br/>OPEN / MIXED"]
  BoundaryTransfer["Boundary, W, prime-power transfer<br/>OPEN / CONDITIONAL"]

  WLocal["WProjectedLocalMatch_3^major<br/>CONDITIONAL schema"]
  ModelNeutral["ProjectedModelNeutrality_3^major<br/>OPEN"]
  PMNGate["ProjectedModelNeutralityGate_260<br/>CONDITIONAL gate"]
  GenericTail["GenericTail_260 / SharpGenericTail<br/>OPEN subtarget"]
  KernelAbs["KernelAbsBudget_265<br/>OPEN"]
  KernelSigned["KernelSignedBudget_265<br/>OPEN"]
  CollNeutral["CollNeutral_260<br/>OPEN"]
  Uniformity["UniformityLedger_266<br/>OPEN"]

  EndpointClass["Endpoint equivalence class<br/>RBDH / CPC / SPAC / SU2 / U2 / AU3<br/>OPEN"]

  SharpSel --> Original
  FiniteType --> Original
  Obstruction --> Original
  ResCube --> Original
  Metric -. "does not imply all-alpha" .-> Original

  MajorTarget --> ResCube
  MinorTarget --> ResCube
  TransInc --> MinorTarget
  ThresholdAudit --> TransInc
  PhaseExpansion --> TransInc
  ToolCompat --> PhaseExpansion
  TransGate --> TransInc
  PhaseExpansion --> TransGate
  ToolCompat --> TransGate
  TransGateCompat --> TransGate
  SelectorTransfer --> TransGateCompat
  BoundaryTransfer --> TransGateCompat
  DegAudit --> TransGate
  DegAudit --> PhaseExpansion
  TransVerdict --> TransGate
  TransVerdict --> TransGateCompat
  TransVerdict --> DegAudit
  PhaseKernel0 --> TransGate
  MinTransFamily --> XiExpansion
  XiExpansion --> PhaseKernel0
  XiExpansion --> FixedShellAudit
  FixedShellAudit --> FixedShellTransfer
  FixedShellTransfer --> PhaseKernel0
  LSBesselBench --> FixedShellTransfer
  DegRowsP0 --> PhaseKernel0
  SideRowsP0 --> PhaseKernel0
  ThresholdP0 --> SideRowsP0
  ThresholdP0 --> PhaseKernel0
  AdaptiveShellP0 --> PhaseKernel0
  AdaptiveShellP0 --> FixedShellTransfer
  AdaptiveShellP0 --> PlanUpdate11
  PlanUpdate11 --> DirectTTStar
  DirectTTStar --> AdaptiveShellP0
  DirectTTStar --> PhaseKernel0
  DirectTTStar --> SelectionComplexity
  SelectionComplexity --> UniformFiberStress
  SelectionComplexity --> AdaptiveShellP0
  UniformFiberStress --> WeightedRCSubgraph
  WeightedRCSubgraph --> AdaptiveShellP0
  UniformFiberStress --> AdaptiveVerdict290
  UniformFiberStress --> AdaptiveShellP0
  AdaptiveVerdict290 --> AdaptiveShellP0
  AdaptiveVerdict290 --> PhaseKCleanup291
  PhaseKCleanup291 --> PlanChallenge7
  PlanChallenge7 --> SidePkgTriage293
  SidePkgTriage293 --> LowLevelTriage294
  SidePkgTriage293 --> AdaptiveShellP0
  LowLevelTriage294 --> AdaptiveShellP0
  LowLevelTriage294 --> PlanUpdate12
  PlanUpdate12 --> LowLevelBarrier296
  LowLevelBarrier296 --> E2Tail297
  LowLevelBarrier296 --> ThresholdP0
  E2Tail297 --> ThresholdP0
  E2Tail297 --> ShiftFreq298
  ShiftFreq298 --> ThresholdP0
  ShiftFreq298 --> ThresholdWindow299
  ThresholdWindow299 --> ThresholdP0
  ThresholdWindow299 --> RowBarrier300
  RowBarrier300 --> ThresholdP0
  RowBarrier300 --> Reflective4
  Reflective4 --> RowMoment302
  RowMoment302 --> RowSquare303
  RowSquare303 --> PlanUpdate13
  PlanUpdate13 --> FixedFiber305
  FixedFiber305 --> FixedFiber306
  FixedFiber306 --> PlanChallenge8
  PlanChallenge8 --> ColumnBarrier308
  ColumnBarrier308 --> ColumnDist309
  ColumnDist309 --> ColumnPair310
  ColumnPair310 --> WPair311
  WPair311 --> AutoCorr312
  AutoCorr312 --> AntiDiag312
  AntiDiag312 --> ThresholdP0
  AutoCorr312 --> PlanUpdate14
  PlanUpdate14 --> MinorKernel314
  MinorKernel314 --> AntiDiag312
  MinorKernel314 --> ZeroAudit315
  ZeroAudit315 --> CenteredFull316
  CenteredFull316 --> AntiDiag312
  WPair311 --> ThresholdP0
  ColumnPair310 --> ThresholdP0
  ColumnDist309 --> ThresholdP0
  ColumnBarrier308 --> ThresholdP0
  MinTransFamily --> TransGateCompat
  MinTransFamily --> TransVerdict
  SelectorTransfer --> ResCube
  BoundaryTransfer --> ResCube
  EndpointClass -. "structural/equivalence map, not proof" .-> ResCube

  WLocal --> MajorTarget
  ModelNeutral --> MajorTarget

  PMNGate --> ModelNeutral
  GenericTail --> PMNGate
  KernelAbs --> PMNGate
  KernelSigned --> PMNGate
  CollNeutral --> PMNGate
  Uniformity --> PMNGate

  BoundaryTransfer --> WLocal
  SelectorTransfer --> WLocal
  SelectorTransfer --> MinorTarget
```

## Reading Discipline

- The graph does not license using an endpoint object as an input to prove
  that same endpoint.
- The signed Phase H fork may target exact-model neutrality, but it does not
  prove the absolute row `CollNeutral_260`.
- The actual selected-average problem still needs the actual sharp moving
  selector and full gap discipline; model/frozen/smoothed rows are not enough.
- Phase J now has `P_minor^0`; that definition is a convention package, not a
  proof of `PhaseKernelBound_273^0`.
- `XiDualPhaseExpansion_279` is an identity ledger. It does not transfer
  fixed frequency-set estimates to data-dependent shells.
- `FixedSetShellAudit_280` blocks automatic transfer; the open routes still
  require uniform adaptive-fiber, selection-transfer, or direct-shell input.
- `LSBesselBenchmark_281` records that current non-endpoint Bessel bounds
  reproduce row/column ceilings, not adaptive shell closure.
- `DegRowsP0Audit_282` removes some degeneracies only inside the minimal
  model by convention; it does not prove row/column, major-difference,
  physical-diagonal, or deg-free smallness.
- `SideRowsP0Audit_283` removes boundary, fixed-residue, prime-only, and
  selector-change rows only inside the minimal model by convention; it does
  not prove W-uniformity, threshold-budget, low-level cutoff, dyadic
  uniformity, or adaptive shell-selection rows.
- `ThresholdBudgetP0Audit_284` names the threshold budgets and optimized
  barriers required inside `P_minor^0`; these barriers are diagnostics, not
  estimates.
- `AdaptiveShellVerdict_285` marks the current Phase J tool package as
  blocked for `PhaseKernelBound_273^0`; it does not disprove the local target
  or any endpoint.
- `PlanUpdate_11_286` pauses Phase J and starts Phase K as adaptive-shell
  gain triage. The first Phase K test is the direct-shell `TT*` cross-term
  audit, not a claimed gain.
- `DirectShellTTStarAudit_287` isolates `DirectShellCrossTermGain_287` as
  open; Cauchy/Bessel, fixed-set, full-orthogonality, and endpoint-derived
  closures remain blocked.
- `SelectionComplexityAudit_288` records that raw union selection,
  fixed-threshold-to-fixed-fiber transfer, and favorable phase selection do
  not supply `SelectionComplexityGain_288`; row/column graph entropy is only a
  diagnostic until a uniform theorem is proved.
- `UniformFiberStress_289` blocks row/column-only uniform-fiber gain; a
  useful uniform route would need `WeightedRCSubgraphGain_289` or another
  same-family residual-structure theorem.
- `PhaseKAdaptiveShellVerdict_290` records that the current Phase K package
  does not prove `AdaptiveShellGainP0_285`; the local target and all endpoint
  objects remain open.
- `PhaseKStatusCleanup_291` blocks continuing Phase K without a new input and
  prepares `ChallengePacket_291` for the seventh plan challenge.
- `PlanChallenge_7_292` selects side-package triage as the next branch; this
  is not a proof of the side package or adaptive shell gain.
- `SidePkgTriage_293` splits the side package and returns shell selection and
  deg-free phase rows to the adaptive core; the next narrow side target is
  low-level leakage.
- `LowLevelBudgetTriage_294` classifies the below-`lambda_min` row and gives
  deterministic counting barriers, but it does not prove
  `LowLevelBudgetP0_284`, `LowLevelCutoffP0_283`, or any threshold closure.
- `PlanUpdate_12_295` keeps the side-package branch narrow and selects
  `LowLevelCountingBarrierAudit_296`; that next target is still open and must
  test the exact reconstruction formula and target weights.
- `LowLevelCountingBarrierAudit_296` blocks pure counting under the current
  declarations and extracts the open second-energy tail target
  `LowLevelEnergyTailTarget_296`.
- `E2MinorEnergyTailAudit_297` proves the local fourth-moment low-level tail
  inside `P_minor^0` only. It does not prove the shift/frequency removal
  budgets or the threshold package.
- `ShiftFreqRemovalAudit_298` proves only vacuous actual bad-set removal
  inside `P_minor^0`; maximal thresholds are not a usable threshold closure.
  The next live question is threshold-window compatibility.
- `ThresholdWindowCompatibilityAudit_299` reduces useful threshold-window
  closure to optimized barrier smallness plus admissible threshold scheduling.
  The current trivial caps do not prove those barriers.
- `RowBarrierMomentAudit_300` shows that the current energy-only row route
  gives only a polylogarithmic ceiling. The row barrier remains open and now
  needs a genuine row-energy distribution or high-moment gain.
- `Reflective_4` is a memory log for Modules 261-300. It records no theorem
  upgrade and points the next mathematical work to `RowMomentDistributionAudit_302`.
- `RowMomentDistributionAudit_302` is a structural audit: layer-cake is a
  criterion, current Markov tails are blocked at the Module 300 ceiling, and
  the fourth-moment route is circular without an independent theorem.
- `RowSquareMomentExpansion_303` is an identity ledger. It expands the q=2
  row-square object into exact same-shift restricted kernels over
  data-dependent fibers, blocks full-frequency/fixed-fiber/endpoint shortcuts,
  and leaves `SameShiftSquareKernelGain_303` open.
- `PlanUpdate_13_304` selects `FixedFiberRowSquareBenchmark_305` before a
  direct attack on the data-dependent same-shift row-square kernel.
- `FixedFiberRowSquareBenchmark_305` shows that prescribed fibers remove the
  selection issue but current tools still recover ceiling-scale row-square
  bounds. The fixed-fiber branch now needs a blocked verdict or a genuinely
  smaller size-sensitive criterion.
- `FixedFiberBlockedVerdict_306` blocks selection transfer as the immediate
  next step and sends the row-square branch to `PlanChallenge_8_307`.
- `PlanChallenge_8_307` pauses direct row-square continuation under the
  current toolkit and selects `ColumnBarrierMomentAudit_308`; this is a
  steering decision, not a column estimate.
- `ColumnBarrierMomentAudit_308` extracts first-incidence column ceilings and
  blocks the current column-barrier route; it does not prove either Module
  284 column barrier.
- `ColumnMultiplicityDistributionAudit_309` gives an exact layer-cake
  formulation but blocks first-moment tails as a gain route; the next concrete
  test is the `r=2` same-frequency shift-pair expansion.
- `ColumnPairMultiplicityExpansion_310` expands the `r=2` column moment and
  isolates the off-diagonal same-frequency pair row; the weighted
  coefficient-pair route is still only a criterion.
- `WeightedColumnPairEnergyAudit_311` records that energy-square and
  fourth-power Cauchy estimates return ceiling-scale weighted pair bounds
  under current inputs. It blocks current tools as weighted pair closure and
  sends the next step to the exact weighted pair autocorrelation expansion.
- `WeightedPairAutocorrelationExpansion_312` is an exact identity ledger: it
  rewrites `WPair(d_1,d_2)` as an anti-diagonal two-shift autocorrelation
  kernel with the minor cutoff. Full-frequency and minor-kernel
  decompositions are diagnostics only; the open analytic row is
  `AntiDiagonalTwoShiftKernelGain_312`.
- `PlanUpdate_14_313` blocks direct attack on the bundled anti-diagonal
  target as the next move and selects `MinorKernelRowSplit_314`; that split
  must classify full-frequency, zero-mode, and major-correction rows before
  any weighted pair gain is claimed.
- `MinorKernelRowSplit_314` gives the exact full/zero/major partition of
  `WOff_311`, but independent row smallness is blocked under current tools.
  The next local audit is the zero-mode product row.
- `ZeroModeProductAudit_315` shows that the zero row is not killed by the
  minor convention and not controlled by current tools, but it can be removed
  as an explicit correction by using centered products. The next audit is the
  centered full anti-diagonal row.
