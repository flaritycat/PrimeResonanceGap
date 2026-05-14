# Theorem Status Index

This is the compact live status index for the active proof ledger. It is a
navigation aid, not a proof. When this file conflicts with
`docs/status/global_status.md`, treat `global_status.md` and the latest
module as authoritative and update this index.

Allowed statuses remain:

```text
PROVEN
CONDITIONAL
STRUCTURAL / EXTRACTION
HEURISTIC
OPEN
FALSE / BLOCKED
```

| Object | Status | Dependencies / blockers | Last relevant module | Can be used as input? |
|---|---|---|---|---|
| Original selected-average problem: existence of irrational `alpha` with `A_alpha(x)->L0>1` | OPEN | Actual sharp selector, full gap object, endpoint/obstruction branches | `global_status.md` | No |
| Metric theorem `A_alpha(x)->1` a.e. | PROVEN according to project ledger | Lebesgue-a.e. only; does not imply all-alpha theorem | `global_status.md` | Yes, only in metric/a.e. contexts |
| Finite-type theorem | CONDITIONAL | Finite-type hypotheses and side packages | `global_status.md`, Paper II | Only under stated hypotheses |
| `s=2` rational-major endpoint | OPEN | Exact local models, side packages, transfer, endpoint estimates | `module_178_residual_cube.md` onward | No |
| Residual derivative cube target `ResCube_3^sharp` | OPEN | Major target, minor target, selector, boundary/W/prime-power transfer | `module_178_residual_cube.md`, `module_179_fourier_major_minor.md` | No |
| `RBDH_pair_short(Hcal)` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `CPC_3^sharp(Hcal)` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `SPAC_2^sharp` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `SU2Pair_2^sharp` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `DyadicDerivativeU^2` | OPEN | Structurally equivalent target; analytic estimate still missing | `module_228_structural_arrow_audit.md` | Only as structural target label |
| `AU^3` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `WProjectedLocalMatch_3^major` | CONDITIONAL | Residual subset-HL, boundary, W-residue, prime-power, projection, denominator, selector rows | `module_209_w_admissible_projected_local_model.md` | Only as a conditional schema |
| `ProjectedMajorTarget_3^B` | OPEN | `WProjectedLocalMatch_3^major` plus projected model neutrality | `module_206_exact_projected_major_arc_target.md` | No |
| `NarrowMinorArc_3^B` | CONDITIONAL | Low-level leakage, bad-shift energy, persistent-frequency energy, transverse incidence energy, transfer rows | `module_203_refined_minor_arc_criterion.md`, `module_269_transverse_incidence_object.md` | Only if every input row is supplied |
| `TransIncCore_269` | STRUCTURAL / EXTRACTION | Definition of the transverse weighted shift-frequency graph; no decay estimate | `module_269_transverse_incidence_object.md` | Only as an object definition |
| `TransIncBound_269` | OPEN | Non-tautological `Gamma_trans`, threshold compatibility, same selector/model class, dyadic/W-limit discipline | `module_269_transverse_incidence_object.md` | No |
| `ThresholdRemovalAudit_270` | STRUCTURAL / EXTRACTION | Threshold-only diagnostic; derives tension between removal thresholds and trivial transverse ceilings | `module_270_threshold_removal_audit.md` | Only as an audit formula |
| `ThresholdOnlyClosure_270` | OPEN | External `ShiftMoment_{q,s}` and `MultMoment_{r,s}` estimates plus compatible lambda-summed threshold window | `module_270_threshold_removal_audit.md` | No |
| `TransPhaseExpansion_271` | STRUCTURAL / EXTRACTION | Exact expansion of transverse coefficients into shifted `f_s`-correlation kernels | `module_271_transverse_phase_equations.md` | Only as an algebraic identity |
| `PhaseIncidenceGate_271` | OPEN | Same-family estimates for restricted minor-arc phase kernels, same-frequency pairs, same-shift pairs, and rectangles | `module_271_transverse_phase_equations.md` | No |
| `PhaseToolCompatAudit_272` | STRUCTURAL / EXTRACTION | Compatibility matrix for large sieve, additive energy, pair-BDH, rectangle-BDH, first-moment HL, and finite-complexity HL | `module_272_phase_tool_compatibility.md` | Only as an audit |
| `AvailableToolClosure_272` | OPEN | Would require an exact same-family restricted weighted phase-kernel estimate from existing tools | `module_272_phase_tool_compatibility.md` | No |
| `TransverseIncidenceGate_273` | STRUCTURAL / EXTRACTION | Candidate `Gamma_trans^273` from dyadic base-tail shells and graph-restriction input `X_273`; sufficient only if all inputs are proved | `module_273_transverse_incidence_gate.md` | Only as a conditional gate |
| `PhaseKernelBound_273` | OPEN | Same-family bound for the shell graph-restriction functional `Xi_273` with restricted kernels and weighted residual coefficients | `module_273_transverse_incidence_gate.md` | No |
| `TransGateCompatAudit_274` | STRUCTURAL / EXTRACTION | Compatibility audit for W-limit, threshold, arc-boundary, prime-power, cutoff, selector, and dyadic side rows | `module_274_transverse_gate_compatibility.md` | Only as an audit |
| `TransGateSideRows_274` | OPEN | `WLimitCompat`, threshold buffers, arc-boundary, prime-power/W-residue, cutoff/truncation, selector transfer, dyadic uniformity | `module_274_transverse_gate_compatibility.md` | No |
| `TransDegeneracyAudit_275` | STRUCTURAL / EXTRACTION | Routes low-dimensional transverse degeneracies to named open rows and isolates the genuine transverse remainder | `module_275_transverse_degeneracy_classification.md` | Only as a routing audit |
| `DegFreePhaseGate_275` | OPEN | Same-family phase-kernel estimate on the complement of routed degeneracy classes, strong enough for `Gamma_trans^273` | `module_275_transverse_degeneracy_classification.md` | No |
| `TransverseGateVerdict_276` | STRUCTURAL / EXTRACTION | Proof-or-blocked verdict: Phase I transverse route is mixed/conditional; direct shortcuts blocked | `module_276_transverse_gate_verdict.md` | Only as a verdict |
| `TransverseGateProofPkg_276` | OPEN | `PhaseKernelBound_273`, `TransGateSideRows_274`, routed degeneracy rows, `DegFreePhaseGate_275`, and lambda-summed `Gamma_trans^273` | `module_276_transverse_gate_verdict.md` | No |
| `PlanUpdate_10_277` | STRUCTURAL / EXTRACTION | Governance update pausing broad Phase I and selecting Phase J | `module_277_tenth_plan_update_sixth_challenge.md` | Only as schedule/steering |
| `PlanChallenge_6_277` | STRUCTURAL / EXTRACTION | Challenge verdict: broad transverse architecture must shrink to a minimal declared family before further proof-package testing | `module_277_tenth_plan_update_sixth_challenge.md` | Only as steering |
| `MinimalTransverseFamily_278(P_minor^0)` | STRUCTURAL / EXTRACTION | Local W-cyclic prime-only model family fixing selector/model class, Fourier group, W-order, dyadic ranges, thresholds, shell convention, residue/cutoff conventions, limiting order | `module_278_minimal_transverse_family.md` | Only as a convention package |
| `XiDualPhaseExpansion_279(P_minor^0)` | STRUCTURAL / EXTRACTION | Exact linear dual form, `TT*` square, fourth-power phase kernel, and data-dependent shell ledger for `Xi_273^0` | `module_279_xi_dual_phase_expansion.md` | Only as an identity ledger |
| `PhaseKernelBound_273^0` | OPEN | Same-family bound for `Xi_273^0` over data-dependent base-tail shells inside `P_minor^0` | `module_278_minimal_transverse_family.md` | No |
| `FixedSetShellAudit_280(P_minor^0)` | STRUCTURAL / EXTRACTION | Audits fixed-set estimates versus data-dependent shells and blocks automatic transfer | `module_280_fixed_set_shell_transfer.md` | Only as an audit |
| `FixedSetShellTransfer_280` | OPEN | Requires `UniformFiberBound_280`, `SelectionTransfer_280`, or `DirectShellBound_280`; fixed-set-only estimates do not suffice | `module_280_fixed_set_shell_transfer.md` | No |
| `UniformFiberBound_280 / SelectionTransfer_280 / DirectShellBound_280` | OPEN | Uniform adaptive-fiber bound, selection theorem, or direct shell estimate for `X_J(omega)` inside `P_minor^0` | `module_280_fixed_set_shell_transfer.md` | No |
| `LSBesselBenchmark_281(P_minor^0)` | STRUCTURAL / EXTRACTION | Benchmarks row, column, global Cauchy/Bessel, fixed-set large-sieve, selection, and direct-shell routes | `module_281_large_sieve_bessel_benchmark.md` | Only as a benchmark |
| `LargeSieveBesselClosure_281 / AdaptiveBesselGain_281` | OPEN | Would require adaptive-fiber, selection-transfer, or direct-shell gain beyond row/column ceilings | `module_281_large_sieve_bessel_benchmark.md` | No |
| `DegRowsP0Audit_282(P_minor^0)` | STRUCTURAL / EXTRACTION | Classifies routed degeneracy rows inside `P_minor^0`; internal model-zero rows are not transfer theorems | `module_282_pminor0_degeneracy_audit.md` | Only as an audit |
| `DegRowsP0Small_282 / MajorDiffBound_282 / PhysDiagLocal_282 / DegFreePhaseGate_282` | OPEN | Lambda-summed row/column smallness, major-difference control, physical-diagonal local row, and deg-free shell phase estimate | `module_282_pminor0_degeneracy_audit.md` | No |
| `SideRowsP0Audit_283(P_minor^0)` | STRUCTURAL / EXTRACTION | Classifies local side rows inside `P_minor^0`; internal convention zeros are not export theorems | `module_283_pminor0_side_rows.md` | Only as an audit |
| `SideRowsP0Ready_283` | OPEN | Requires W-uniformity, threshold budget, low-level cutoff, dyadic uniformity, and adaptive shell selection inside `P_minor^0` | `module_283_pminor0_side_rows.md` | No |
| `WUniformP0_283 / ThresholdBudgetP0_283 / LowLevelCutoffP0_283 / DyadicUniformityP0_283 / ShellSelectionP0_283` | OPEN | Local Phase J side rows needed before `PhaseKernelBound_273^0` can be used | `module_283_pminor0_side_rows.md` | No |
| `ThresholdBudgetP0Audit_284(P_minor^0)` | STRUCTURAL / EXTRACTION | Names row, column, shell-counting, removal, optimized-barrier, and low-level threshold budget tests | `module_284_pminor0_threshold_budget.md` | Only as an audit |
| `ThresholdBudgetP0Closure_284(q,r)` | OPEN | Requires `LowLevelBudgetP0_284`, removal budgets, and row/column/shell-counting budgets to be `o_W(1)` in the same threshold schedule | `module_284_pminor0_threshold_budget.md` | No |
| `RowBarrierP0_284 / ColumnBarrierP0_284 / SigmaColumnBarrierP0_284` | OPEN | Optimized threshold barriers are diagnostics; moment estimates and W-uniformity missing | `module_284_pminor0_threshold_budget.md` | No |
| `AdaptiveShellVerdict_285(P_minor^0)` | STRUCTURAL / EXTRACTION | Proof-or-blocked verdict for the current Phase J adaptive-shell package | `module_285_adaptive_shell_verdict.md` | Only as a verdict |
| `CurrentToolsCloseP0_285` | FALSE / BLOCKED | Existing fixed-set, Bessel, threshold, side-row, and degeneracy tools do not prove `PhaseKernelBound_273^0` | `module_285_adaptive_shell_verdict.md` | No |
| `AdaptiveShellGainP0_285` | OPEN | Would require a new same-family uniform-fiber, selection-transfer, or direct-shell theorem with compatible side and threshold losses | `module_285_adaptive_shell_verdict.md` | No |
| `PlanUpdate_11_286` | STRUCTURAL / EXTRACTION | Eleventh plan update: Phase J paused as current-tool blocked; Phase K selected | `module_286_eleventh_plan_update.md` | Only as steering |
| `PhaseK_AdaptiveShellTriage` | STRUCTURAL / EXTRACTION | Working phase for testing possible new adaptive-shell inputs after the Phase J block | `module_286_eleventh_plan_update.md` | Only as schedule/steering |
| `DirectShellTTStarAudit_287(P_minor^0)` | STRUCTURAL / EXTRACTION | Audits direct-shell `TT*` cross terms and blocks Cauchy/Bessel, fixed-set, full-orthogonality, and endpoint-derived shortcuts | `module_287_direct_shell_ttstar_audit.md` | Only as an audit |
| `DirectShellCrossTermGain_287` | OPEN | Uniform gain for fully transverse `TT*` cross terms with adversarial `omega` and data-dependent `J` missing | `module_287_direct_shell_ttstar_audit.md` | No |
| `DirectShellTTStarClosure_287` | OPEN | Would require cross-term gain plus row/column phase, major-difference, physical-diagonal, side, and threshold rows | `module_287_direct_shell_ttstar_audit.md` | No |
| `SelectionComplexityAudit_288(P_minor^0)` | STRUCTURAL / EXTRACTION | Audits entropy, row/column graph complexity, fixed thresholds, and adversarial phases for adaptive shell fibers | `module_288_selection_complexity_audit.md` | Only as an audit |
| `SelectionComplexityGain_288` | OPEN | No entropy, stopping-time, sparse-domination, VC, or chaining theorem supplied for `S_d(J)` | `module_288_selection_complexity_audit.md` | No |
| Raw union selection / fixed-threshold-to-fixed-fiber shortcuts | FALSE / BLOCKED | Selection family too large; fixed thresholds do not make shell fibers predetermined | `module_288_selection_complexity_audit.md` | No |
| `UniformFiberStress_289(P_minor^0)` | STRUCTURAL / EXTRACTION | Stress-tests uniform-fiber route over row/column-admissible shells | `module_289_uniform_fiber_stress.md` | Only as an audit |
| `RowColumnOnlyUniformFiberGain_289` | FALSE / BLOCKED | Row/column data alone cannot produce a gain beyond deterministic ceilings | `module_289_uniform_fiber_stress.md` | No |
| `WeightedRCSubgraphGain_289(P_minor^0)` | OPEN | Requires structured residual Fourier control of weighted row/column subgraphs with compatible losses | `module_289_uniform_fiber_stress.md` | No |
| `PhaseKAdaptiveShellVerdict_290(P_minor^0)` | STRUCTURAL / EXTRACTION | Gives the Phase K proof-or-blocked verdict for the adaptive-shell gain attempt | `module_290_phase_k_adaptive_shell_verdict.md` | Only as a verdict |
| `PhaseKCurrentClosure_290` | FALSE / BLOCKED | Current Phase K direct-shell, selection, and uniform-fiber tests do not prove `AdaptiveShellGainP0_285` | `module_290_phase_k_adaptive_shell_verdict.md` | No |
| `PhaseKStatusCleanup_291(P_minor^0)` | STRUCTURAL / EXTRACTION | Cleans Phase K status map and prepares the Module 292 challenge packet | `module_291_phase_k_status_cleanup.md` | Only as steering |
| `ContinuePhaseKWithoutNewInput_291` | FALSE / BLOCKED | Repeating the same Phase K route tests without a new theorem cannot close `AdaptiveShellGainP0_285` | `module_291_phase_k_status_cleanup.md` | No |
| `ChallengePacket_291` | STRUCTURAL / EXTRACTION | Decision packet for the seventh plan challenge | `module_291_phase_k_status_cleanup.md` | Only as steering |
| `ProjectedModelNeutralityGate_260(P_adm)` | CONDITIONAL | Exact model discipline, generic tail, kernel route, collision route, uniformity, model-domain conventions | `module_260_projected_model_neutrality_gate.md`, `module_267_projected_model_neutrality_verdict.md` | Only if every row is supplied |
| `CollNeutral_260(P_adm)` | OPEN | Absolute collision-defect control with `|W_M|` and same-family uniformity | `module_264_collision_diagonal_strata.md` | No |
| `AbsCollStrataGate_264` | OPEN | Structural strata, nonstructural load, overflow, finite-prime-set CRT, absolute kernel weight | `module_264_collision_diagonal_strata.md` | No |
| `SignedCoverGate_264` | OPEN | Exact signed averaging, structural signed rows, proper-support cancellation, full-cover clusters | `module_264_collision_diagonal_strata.md` | No; not an absolute row |
| `KernelAbsBudget_265` | OPEN | `A_W(M)eps_gen`, structural/collision load, overflow, tail and range budgets | `module_265_kernel_absolute_vs_signed.md` | No |
| `KernelSignedBudget_265` | OPEN | Exact signed `W_M`, generic signed row, signed structural/full-cover cluster rows | `module_265_kernel_absolute_vs_signed.md` | No; not an absolute row |
| `UniformityLedger_266` | OPEN | W-limit, denominator/CRT, projection, kernel tail, cutoff, W-residue, dyadic, selector, supremum closure rows | `module_266_uniformity_admissible_family.md` | No |

## Guardrail Notes

- Equivalence classes and structural decompositions are not proofs.
- A conditional gate is not an established theorem.
- Model, smoothed, frozen, or cyclic estimates do not reach the actual sharp
  moving selector without named transfer rows.
- `Sigma_w(d,h)` is not pointwise `kappa_w(d)^2`.
- No endpoint-strength object may be assumed in a module whose purpose is to
  prove or reduce that endpoint.
