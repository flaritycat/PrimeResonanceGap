# Long-term project plan

Created: 2026-05-14

Planning status: `STRUCTURAL / EXTRACTION`

This document gives the working schedule for continuing the Prime Gap
Resonance Project after Module 187. It is an operating plan, not a proof
ledger. It may organize attempts, reductions, and conditional routes, but it
does not upgrade any theorem status.

## 1. Non-negotiable guardrails

The project continues under the global status ledger:

- the original positive existence problem is `OPEN`;
- the all-alpha no-positive-limit theorem is `OPEN`;
- the metric theorem `A_alpha(x) -> 1` for Lebesgue-a.e. irrational alpha is
  `PROVEN according to project ledger`;
- the finite-type no-positive-limit theorem is `CONDITIONAL`;
- `RBDH_pair_short`, `CPC_3^sharp`, `AU^3`, and the `s=2` endpoint are `OPEN`.

Every module must preserve selector discipline, gap-object discipline, exact
local-model discipline, and the forbidden-upgrade list.

## 2. Iteration counters

A solving iteration means a substantive project advance: a new module, a
committed analytic reduction, a proof attempt with a resolved outcome, a
correction that changes the proof map, or a governance update that changes the
future working protocol.

Current anchor:

```text
Latest completed module: 269
Post-Reflective_1 solving count: 88
Long-term-plan count: 82
```

This adoption document is checkpoint `P0`. The 9- and 15-iteration cadences
begin with the next substantive continuation after this document.

If future work proceeds one module per solving iteration, the expected
checkpoint modules are:

```text
First plan update:       Module 196 (completed)
First plan challenge:    Module 202 (completed)
Second plan update:      Module 205 (completed)
Third plan update:       Module 214 (completed)
Second plan challenge:   Module 217 (completed)
Reflective_2 log:        Module 221 (completed)
Reflective_3 log:        Module 261 (completed)
Next reflective log:     Module 301
Fourth plan update:      Module 223 (completed)
Fifth plan update:       Module 232 (completed)
Third plan challenge:    Module 232 (completed)
Sixth plan update:       Module 241 (completed)
Fourth plan challenge:   Module 247 (completed)
Seventh plan update:     Module 250 (completed)
Eighth plan update:      Module 259 (completed)
Fifth plan challenge:    Module 262 (completed)
Ninth plan update:       Module 268 (completed)
Tenth plan update:       Module 277
Sixth plan challenge:    Module 277
```

These module numbers are bookkeeping estimates. If an iteration is not a
module, the counters still advance by iteration count rather than by module
number.

## 3. Cadence rules

Plan update cadence:

- every 9th solving iteration after this document, update this plan;
- record what changed in the project map;
- revise the next 9-iteration target window;
- adjust the counters above.

Plan challenge cadence:

- every 15th solving iteration after this document, question the plan;
- explicitly ask whether the current branch is still the best use of effort;
- identify any assumptions that have become too strong, too vague, or too
  convenient;
- decide whether to continue, narrow, branch, or abandon the current route.

Reflection cadence:

- continue the existing `Reflective_N.md` cadence every 40 solving iterations
  after `Reflective_1.md`;
- a reflection may include a plan update or challenge if the counters coincide,
  but it does not replace them unless it explicitly performs those tasks.

When cadences coincide, perform all due actions in the same iteration. For
example, iteration 45 after this document requires both a 9-iteration plan
update and a 15-iteration plan challenge.

## 4. Long-term route

The present analytic branch is the residual derivative cube endpoint. The work
from Modules 179-187 has clarified the endpoint into four live packages:

```text
major arcs
  -> projected local model
  -> collision control
  -> W-limit and boundary transfer

minor arcs
  -> large-spectrum control
  -> fourth-moment decay

selector transfer
  -> frozen/smoothed/model selector estimates
  -> actual sharp moving selector only with all transfer packages

endpoint equivalence
  -> RBDH_pair_short / CPC_3^sharp / AU^3 remains open
```

The first priority is not to announce a proof. The first priority is to turn
each informal obstruction into an explicit lemma, conditional criterion, or
false route.

## 5. Phase schedule

### Phase A: Collision load and major-arc envelope

Target window: iterations 1-9 after this document.

Purpose: finish the correction started in Module 187 and decide whether major
arc collision control can be reduced to manageable divisor-moment estimates.

Expected modules:

- Module 188: overflow estimate for large total collision load; completed as a
  conditional criterion;
- Module 189: exponential-moment criterion for beta-load sums; completed as a
  conditional joint-divisibility criterion;
- Module 190: kernel absolute-mass and range audit for major projection;
  completed as a conditional kernel/range package;
- Module 191: W-limit order and generic tail uniformity; completed as a
  conditional W-admissibility contract;
- Module 192: averaged collision-defect bound under the qualified envelope;
  completed as a conditional composition lemma;
- Module 193: generic projected model neutrality after collision removal;
  completed as a conditional projected model-neutrality package;
- Module 194: projected local-model matching dependency list; completed as a
  structural dependency list for `ProjectedLocalMatch_3^major`;
- Module 195: audit of Modules 183-194 for hidden upgrades; completed as a
  structural safety audit;
- Module 196: first 9-iteration plan update; completed as a structural
  transition from major-arc dependency mapping to minor-arc large-spectrum
  work.

Success criterion: either a credible conditional major-arc collision package is
isolated, or the route is marked too expensive and the next plan redirects.

### Phase B: Minor arcs and large-spectrum control

Target window: iterations 10-18 after this document.

Purpose: convert the minor-arc fourth-moment target from Module 180 into
checkable large-spectrum estimates.

Expected modules:

- Module 197: formulate a minor-arc density/energy criterion for `B_d`;
  completed as a conditional restriction-envelope criterion;
- Module 198: compare ordinary pair-BDH with the residual fourth-moment target;
  completed as a blocked-shortcut comparison: ordinary pair-BDH controls the
  wrong object unless pair-margin absorption and adaptive residual minor-arc
  restriction are added;
- Module 199: audit rectangle-BDH and first-moment Hardy-Littlewood
  insufficiency;
  completed as a blocked-shortcut audit: mean rectangle-HL and ordinary
  rectangle-BDH do not supply residual adaptive minor-arc control unless
  upgraded by named residual, margin, adaptive, and variance-strength packages;
- Module 200: test whether a dyadic derivative `U^2` package gives the needed
  decay;
  completed as a structural extraction: dyadic derivative `U^2` is exactly the
  same minor-arc fourth moment after applying `Pi_minor`, so it needs a new
  projected derivative input rather than endpoint-equivalence language;
- Module 201: build the minor-arc spectral large-spectrum obstruction map;
  completed as a structural obstruction tree: failure of minor-arc decay must
  pass through low-level leakage, dyadic count/energy failure, bad-shift
  concentration, persistent minor-frequency concentration, or transverse
  incidence concentration;
- Module 202: perform the first 15-iteration plan challenge; completed with a
  narrowed continuation verdict for Phase B through Module 205;
- Module 203: refine the conditional minor-arc criterion after the challenge;
  completed as `NarrowMinorArc_3^B`, a conditional package separating
  low-level leakage, bad-shift moments, persistent-frequency multiplicities,
  and transverse incidence risk;
- Module 204: audit boundary, W-range, and selector compatibility for minor
  arcs;
  completed as `MinorArcTransfer_3^B`, a conditional transfer-compatibility
  package separating model minor-arc cancellation from boundary, W-limit,
  prime-power, threshold, dyadic-range, and sharp-selector transfer;
- Module 205: perform the second 9-iteration plan update;
  completed with the verdict that Phase B has produced useful named open
  dependencies but should now pause rather than keep renaming the missing
  transverse and transfer estimates.

Success criterion: a named open estimate replaces the vague phrase
"minor-arc cancellation", or a conditional route is rejected as insufficient.

### Phase C: Projected local model matching

Target window: iterations 19-27 after this document.

Purpose: state the exact local model needed on major arcs and separate formal
Euler-factor algebra from actual selector transfer.

Expected work:

- Module 206: state the exact projected major-arc target for the residual
  derivative product, including Fourier projection, dyadic domains, and
  zero-mode convention;
  completed as `ProjectedMajorTarget_3^B`, with the Fourier target,
  physical projected cube, `Omega_w^proj` model object, and boundary-error
  slots separated from the still-open matching and neutrality estimates;
- Module 207: define the exact major-arc local model, including the required
  `Omega_w` factor and its relation to `kappa_w`, `Sigma_w`, and
  higher-shift local factors;
  completed as the exact `Theta_{w,S}^proj` Euler-factor dictionary and
  `Omega_w^proj` residual inclusion-exclusion model, with explicit
  lower-dimensional marginals and the warning that `Sigma_w(d,h)` is not
  pointwise `kappa_w(d)^2`;
- Module 208: stratify major-arc collision hyperplanes for the projected
  residual cube and separate structural collisions from analytic error terms;
  completed by reducing the 28 labeled pair collisions to a 19-form
  projected affine list, while separating structural zero strata, large-prime
  congruence strata, boundary/kernel-tail strata, W-residue strata, and
  prime-power strata;
- Module 209: formulate the W-admissible projected local-model theorem with
  all limit orders, uniformity ranges, and denominator restrictions;
  completed as `WProjectedLocalMatch_3^major(P_adm)`, a conditional theorem
  schema with the fixed-`w`, `N -> infinity`, then `w -> infinity` limit
  order and explicit residual-HL, structural, collision, boundary, W-residue,
  prime-power, projection-boundary, and selector error slots;
- Module 210: audit cyclic-to-interval boundary transfer for the projected
  major-arc model;
  completed as `CycIntTransfer_3^major(P_adm)`, a conditional package tracking
  actual and model boundary errors, wraparound, kernel tails, cutoff mismatch,
  normalization transfer, zero-mode leakage, and W-residue boundary
  compatibility;
- Module 211: audit prime-power and small-prime removal for the projected
  major-arc model;
  completed as `PPSPTransfer_3^major(P_adm)`, a conditional package separating
  exact small-prime W-absorption, projected prime-power cube removal,
  model-side prime-power exclusion, boundary/W-residue interaction, and
  fixed-`w` uniformity;
- Module 212: check compatibility between pair, rectangle, and projected cube
  local models, with no pointwise replacement of `Sigma_w(d,h)` by
  `kappa_w(d)^2`;
  completed as `LocalModelCompat_3^major(P_adm)`, a structural ledger of exact
  pair, rectangle, full-cube, and residual projected face identities, together
  with the named averaged compatibility errors needed for any non-exact model
  replacement;
- Module 213: state the selector-class transfer line for projected major arcs,
  separating model, smoothed, frozen, and actual sharp moving selectors;
  completed as `MajorSelectorTransfer_3^P(P_adm;s_0 -> s_*)`, a conditional
  adjacent-selector transfer chain measured after forming `B_d` and applying
  the projected major-arc operator, with boundary, transition, moving-window,
  prefix, denominator, tail, projection, W-residue, prime-power, and centering
  errors separated;
- Module 214: perform the third 9-iteration plan update.
  completed with the verdict that Phase C clarified the projected major-arc
  dependency graph but did not prove the endpoint, and that Phase D should
  now audit selector and boundary transfer globally rather than add more
  major-arc package names.

Success criterion: the major-arc branch becomes a clean dependency diagram
rather than a blended proof narrative.

### Phase D: Selector and boundary transfer

Target window: iterations 28-36 after this document.

Purpose: prevent model estimates from silently becoming sharp moving-selector
estimates.

Expected work:

- Module 215: build a selector inventory for Modules 156-213, recording every
  theorem's selector class and the norm in which transfer would be required;
  completed as `SelectorInventory_156_213`, a structural audit ledger marking
  selector classes as explicit, inferred, ambiguous, or non-selector-bearing,
  and separating actual sharp moving-selector transfer from model, W-tricked,
  cyclic, smoothed, frozen, Bernoulli, and finite-stage statements;
- Module 216: state a global boundary / prefix / transition / denominator /
  tail transfer matrix for the actual sharp moving selector;
  completed as `SharpSelectorTransferMatrix_3`, a structural matrix separating
  boundary, prefix, transition, moving-window, denominator, tail, projection,
  W-residue, prime-power, centering, Bernoulli/finite-stage extraction, and
  core residual fourth-moment selector rows by their relation to the endpoint;
- Module 217: perform the second 15-iteration plan challenge and decide
  whether Phase D should continue, narrow, or stop;
  completed with the verdict to continue Phase D but narrow it sharply:
  generic `CoreSel` rows are not acceptable side packages unless localized,
  and the next modules should isolate major/minor projection compatibility,
  frozen-to-moving threshold transfer, and deterministic extraction;
- Module 218: audit compatibility between major-arc and minor-arc
  selector-transfer packages, especially projection and denominator changes;
  completed as `MajorMinorSelCompat_3(P_adm)`, a conditional compatibility
  package separating projection partition defect, arc-boundary stability,
  denominator compatibility, zero-mode/centering compatibility,
  selector-chain compatibility, boundary accounting, and prime-power /
  W-residue compatibility;
- Module 219: state the frozen-to-moving dyadic threshold transfer obstruction
  in the residual derivative fourth-moment normalization;
  completed as `FrozenMovingObstruction_3^Pi`, a structural extraction showing
  that the `fr -> mv` row requires moving-threshold residual layer cubes,
  amplitude/normalization drift, dyadic endpoint and prefix control,
  denominator/projection compatibility, and centering control, and is mixed or
  potentially endpoint-strength unless `MoveLayerCube_3^Pi` is proved;
- Module 220: state the Bernoulli or finite-stage deterministic-extraction
  requirement for selector statements used in the endpoint branch;
  completed as `DetExtract_3^Pi(s -> mv)`, a structural extraction package
  separating parameter-grid compatibility, Bernoulli exceptional-set
  summability, Bernoulli-to-actual coupling, finite-stage convergence,
  diagonal stability, major/minor and frozen/moving compatibility, and
  alpha-exception accounting in the residual fourth-moment norms;
- Module 221: create `Reflective_2.md`, the required 40-iteration memory log
  after `Reflective_1.md`, and record corrections from Modules 179-220;
  completed as a structural memory log reviewing the residual cube,
  major/minor, projected local model, selector-transfer, frozen-to-moving, and
  deterministic-extraction branches, while preserving all open endpoint
  statuses and setting the next reflection expectation around Module 261;
- Module 222: consolidate the selector-transfer dependency graph after the
  reflection;
  completed as `SelectorTransferGraph_3^consol`, a structural consolidation
  of the Module 216 matrix with Modules 218-220, classifying rows as local,
  mixed, endpoint-strength, or blocked-as-shortcut, merging duplicate row
  names, and identifying a genuinely supported boundary/prefix residual
  fourth-moment row as the smallest honest next analytic target;
- Module 223: perform the fourth 9-iteration plan update.
  completed with the verdict that Phase D clarified selector-transfer
  dependencies but did not prove transfer, and that the next window should
  first test one genuinely supported boundary/prefix residual fourth-moment
  row before auditing endpoint-equivalence arrows.

Success criterion: every future endpoint statement has an explicit selector
line and cannot accidentally jump selector class.

### Phase E: Boundary-row test and endpoint equivalence audit

Target window: iterations 37-45 after this document.

Purpose: test whether the cleanest local selector-transfer row is genuinely
smaller than the endpoint, then return to the compressed endpoint class and
label every equivalence arrow with its side dependencies.

Expected work:

- Module 224: fix one boundary/prefix test row, preferably projected-major and
  selector-fixed, with one projection, one edge, one dyadic `D` range, fixed
  W-limit order, no moving threshold, no Bernoulli extraction, and no
  major/minor partition change;
  completed as `BdPrefRow_224^P(s0,D0;N,w,rho0)`, a conditional fixed
  projected-major cyclic-to-interval row with `Pi=P_M`, selector class `s0`
  held fixed, one dyadic shell `D0<|d|<=2D0`, and exact support defined after
  the eight residual vertices are formed;
- Module 225: expand that row into its residual fourth-moment cube and list
  the exact envelopes needed to make it `o(1)`;
  completed as a conditional envelope ledger reducing
  `BdPrefRow_224^P=o_W(1)` to `AbsMajorant_225`,
  `KernelAbsTail_225`, boundary-marked tuple estimates
  `BoundaryTupleHL_225(S,lambda)`, model-mass bounds
  `BoundaryModelMass_225(S,lambda)`, W/prime-power boundary control, and
  `NormRow_224^P=o_W(1)`;
- Module 226: decide whether the fixed boundary/prefix row is plausibly local,
  conditional, or blocked as endpoint-strength under the available envelopes;
  completed with verdict `LocalBdPkg_226 => BdPrefRow_224^P=o_W(1)`, so the
  row is conditional local only under genuine weighted boundary-support
  saving, mixed if additional transfer rows enter, and endpoint-strength if
  approached by assuming unlocalized projected residual fourth-moment control;
- Module 227: build the endpoint-equivalence arrow inventory from the residual
  cube branch back to `RBDH_pair_short`, `CPC_3^sharp`, `SPAC_2^sharp`,
  `SU2Pair_2^sharp`, `DyadicDerivativeU^2`, and `AU^3`;
  completed as `EndpointArrowInventory_227`, a structural map separating
  Fourier/derivative arrows, residual-to-CPC arrows, CPC/SPAC/SU2Pair arrows,
  CPC/RBDH arrows, and major/minor recomposition arrows, with side-package,
  selector, and `LocalBdPkg_226` boundary locations recorded;
- Module 228: audit the arrows that are exact algebra or structural
  extraction, separating them from analytic estimates;
  completed as `StructuralArrowAudit_228`, isolating the structural identities
  `ResCube_3^sharp <-> DyadicDerivativeU^2`,
  `DyadicDerivativeU^2 <-> AU^3`,
  `SPAC_2^sharp <-> SU2Pair_2^sharp`, and the exact sharp
  major/minor Fourier split, while deferring ResCube/CPC, CPC/SPAC, and
  CPC/RBDH analytic arrows to Module 229;
- Module 229: audit the arrows that require analytic side packages: local
  models, covariance calibration, pair-margin absorption, boundary transfer,
  collision control, W-limit order, prime-power transfer, and range coverage;
  completed as `AnalyticArrowAudit_229`, classifying the ResCube/CPC,
  CPC/SPAC, CPC/RBDH, projected major-arc, and minor-arc arrows as
  conditional on named side packages, with `LocalBdPkg_226` retained only as
  one fixed boundary/prefix row and not as full boundary transfer;
- Module 230: attach selector-transfer requirements to every endpoint arrow
  using `SelectorTransferGraph_3^consol`;
  completed as `EndpointSelectorAttach_230`, attaching selector source/target
  classes, transfer chains, required residual fourth-moment norms, active
  graph rows, and local/mixed/endpoint-strength classifications to the
  endpoint arrows;
- Module 231: produce a consolidated endpoint dependency table with each arrow
  labeled by the allowed status labels;
  completed as `EndpointDependencyTable_231`, merging the structural,
  analytic, selector-transfer, and fixed boundary-row audits into one table
  with endpoint objects kept `OPEN`, analytic bridges kept `CONDITIONAL`, and
  shortcut implications kept `FALSE / BLOCKED`;
- Module 232: perform the fifth plan update and third plan challenge in the
  same iteration;
  completed as `PlanUpdate_5_Challenge_3_232`, with the decision to stop
  expanding the endpoint-equivalence map for now and attempt the fixed
  boundary/model-mass row `BoundaryModelMass_225(S,lambda)` next.

Success criterion: the project has one honest local-row verdict and a current
endpoint dependency graph with no unlabeled arrows.

### Phase F1: Fixed boundary/model-mass attack

Target window: iterations 46-54 after this document.

Purpose: stop adding global endpoint-equivalence labels and attempt one
smaller row from `LocalBdPkg_226`.

Challenge verdict from Module 232:

```text
The endpoint-equivalence audit is now useful as a guardrail, but continuing
the same audit would mostly polish formalism. The next branch should attack
one fixed boundary/model-mass row or mark it blocked.
```

Expected work:

- Module 233: formulate and test a boundary model-mass volume criterion for
  `BoundaryModelMass_225(S,lambda)`;
  completed as `BoundaryModelVolume_233(S,lambda)`, a conditional model-side
  criterion reducing `BoundaryModelMass_225(S,lambda)` to boundary-volume
  saving, absolute kernel budget, exact local-factor envelopes, and localized
  bad-factor mass, without proving the tuple row or the endpoint;
- Module 234: audit `BoundaryTupleHL_225(S,lambda)` and decide whether it is
  a local weighted tuple input or endpoint-strength in disguise;
  completed as `BoundaryTupleAudit_234(S,lambda)`, separating the exact
  empty-subset row from the nonempty rows and reducing the latter to
  `BoundaryIntervalHL_234(S,lambda)`, with W-residue, prime-power,
  diagonal, and range errors classified as mixed unless they are handled
  inside the fixed boundary interval theorem;
- Module 235: isolate `KernelAbsTail_225(P_M,T0)` and the absolute kernel-mass
  budget needed by the fixed row;
  completed as `KernelTailBudget_235(P_M,T0;s0,D0,rho0)`, separating
  `A_W(M)=O_W(1)` and `Tail_W(T0)=o_W(1)` from the stronger
  `TailCube_225(T0)=o_W(1)` requirement, and showing that the latter also
  needs tail residual-product envelopes or tail tuple rows;
- Module 236: audit `WPPBoundary_225`, separating W-residue boundary failures
  from prime-power boundary artifacts;
  completed as `WPPBoundaryAudit_236(s0,D0,rho0)`, splitting the fixed-row
  W/prime-power boundary package into `WResBoundary_236`,
  `PPBoundary_236`, and either disjoint accounting or `WPPOverlap_236`, with
  positive tuple routes recorded and endpoint-strength shortcuts blocked;
- Module 237: audit `NormRow_224^P` and possible zero-mode leakage for the
  fixed cyclic-to-interval row;
  completed as `NormZeroAudit_237(s0,D0,rho0)`, separating exact
  normalization, small normalization drift, centering consistency, and
  truncated zero-mode leakage, with endpoint-strength envelopes blocked;
- Module 238: compose the fixed-row subpackages and identify the first true
  bottleneck;
  completed as `FixedRowPkg_238(s0,D0,rho0)`, composing Modules 233-237 and
  identifying `FixedSupportTupleHL_238`, led by nonempty
  `BoundaryIntervalHL_234(S,lambda)`, as the first genuine analytic
  bottleneck;
- Module 239: attempt a model-class proof or blocked verdict for the easiest
  boundary subrow under bounded local-factor hypotheses;
  completed as `EasyModelSubrow_239(lambda)`, closing the `S=emptyset`
  boundary/model/tail/convention subrow under explicit kernel-volume and
  convention hypotheses, while blocking any extension to nonempty actual
  weighted tuple rows without `FixedSupportTupleHL_238`;
- Module 240: decide whether `LocalBdPkg_226` remains a plausible local route
  or should be marked mixed/endpoint-strength for practical purposes;
  completed as `LocalBdPkgPracticalVerdict_240`, extracting the corrected
  reading that `LocalBdPkg_226` remains usable only as an expanded
  conditional package, with the `S=emptyset` / model / convention subrow
  separated from the active nonempty `FixedSupportTupleHL_238` bottleneck;
- Module 241: perform the sixth plan update;
  completed as `PlanUpdate_6_241`, closing Phase F1 as a narrow success:
  one empty/model/convention subrow was reduced to concrete local conditions,
  while the nonempty `FixedSupportTupleHL_238` bottleneck remains open and
  becomes the focus of a one-row prototype window.

Success criterion: at least one subrow of `LocalBdPkg_226` is either reduced
to checkable local conditions or marked blocked/endpoint-strength with a
precise reason.

Failure criterion: the window only renames boundary rows without producing a
smaller proof obligation than the projected residual endpoint.

### Phase F2: One-row nonempty fixed-support prototype

Target window: iterations 55-63 after this document.

Purpose: test whether the first nonempty row inside `FixedSupportTupleHL_238`
is genuinely smaller than the projected residual endpoint.

Decision from Module 241:

```text
Continue the boundary branch only as a one-row prototype test.
Do not continue expanding LocalBdPkg_226 as a generic package.
```

Expected work:

- Module 242: fix the one-point prototype row
  `BoundaryIntervalHL_234({sigma0},lambda0)`, including the choice of
  `sigma0`, `lambda0`, same-vertex versus off-vertex cases, boundary interval
  geometry, and exact `Theta_{w,{sigma0}}^proj` local factor;
  completed as `OnePointBIHL_242(s0,D0,rho0)`, choosing the active
  same-vertex prototype
  `BoundaryIntervalHL_234({(00,0)},(00,0))`, fixing the two boundary
  intervals, exact one-point model term, averaged error `BIHLErr_242`, and
  side-error slots without proving the row or any off-vertex case;
- Module 243: derive the exact one-point local model and boundary interval
  main term, including W-residue, diagonal, and range synchronization;
  completed as `OnePointLocalModel_243`, deriving the normalized W-tail
  singleton factor `Theta_{w,{(00,0)}}^proj=1`, reducing the model main term
  to `ell_r`, and isolating the open `|W_M|`-averaged boundary mean error
  `BIHLErr_243` plus side-error slots;
- Module 244: reduce the prototype to a W-admissible one-point boundary
  prime-mean estimate, separating model, W-tricked, smoothed, and frozen
  selector classes;
  completed as `OnePointMeanPkg_244(s0,D0,rho0)`, reducing the active
  prototype to `OPMeanErr_244(s0,D0,rho0)=o_W(1)`, with separate model,
  W-tricked, smoothed, and frozen branches and no free selector transfer;
- Module 245: audit the strength required after the `|W_M(t)|` average:
  supremum versus averaged error, kernel absolute mass, and boundary interval
  length;
  completed as `KernelAvgStrength_245(s0,D0,rho0)`, giving direct weighted,
  uniform pointwise, boundary-length, relative-PNT, and Holder sufficient
  routes for `OPMeanErr_244=o_W(1)` and recording that any route must beat
  absolute kernel mass growth without changing selector class or projection;
- Module 246: audit W-residue, prime-power, range, normalization, and
  zero-mode side rows for the one-point prototype;
  completed as `OnePointSideRows_246(s0,D0,rho0)`, a conditional side-row
  package for `CutOne_242`, `RangeOne_242`, `WResOne_242`, `PPOne_242`, and
  `NormZeroOne_242`, classifying each as zero by convention, local, mixed,
  endpoint-strength, or open and composing it with `KernelAvgStrength_245`
  without proving the prototype;
- Module 247: perform the fourth 15-iteration plan challenge;
  completed as `PlanChallenge_4_247`, with the verdict to continue Phase F2
  only through Modules 248-249 in narrowed proof-or-blocked mode, because the
  one-point prototype has exposed a smaller diagnostic target but not a proved
  smaller theorem;
- Module 248: compare the one-point prototype against available
  first-moment tools, W-tricked prime number theorem input, short-interval
  limitations, and ordinary pair-BDH shortcuts;
  completed as `ToolCompare_248(s0,D0,rho0)`, with ordinary first-moment HL,
  full-interval W-tricked PNT, and ordinary pair-BDH blocked as shortcuts,
  exact model normalization limited to the model branch, and short-interval
  W-PNT, boundary-length, Holder, prime-power, W-residue, cutoff, range,
  normalization, and zero-mode routes kept conditional only in the fixed
  `|W_M|`-weighted row;
- Module 249: give a proof-or-blocked verdict for the one-point prototype:
  conditional local, mixed, endpoint-strength, or false/blocked as a
  shortcut;
  completed as `OnePointVerdict_249(s0,D0,rho0)`, with
  `FixedRowOnePointPkg_249 => OnePointBIHL_242` as the conditional local
  route, transfer routes marked mixed, endpoint assumptions marked
  endpoint-strength, and ordinary first-moment HL, full-interval PNT,
  full-interval W-tricked PNT, ordinary pair-BDH, and rectangle-BDH blocked
  as shortcuts;
- Module 250: perform the seventh plan update and decide whether to attempt
  a two-point fixed-support row, redirect to minor arcs, or stop the boundary
  branch.
  completed as `PlanUpdate_7_250`, with the decision not to escalate
  immediately to two-point fixed-support rows and instead test
  `FixedRowOnePointPkg_249` through deterministic boundary-length,
  kernel-mass / Holder, short-interval W-PNT, and side-row feasibility gates.

Success criterion: the project either obtains a precise conditional local
criterion for `BoundaryIntervalHL_234({sigma0},lambda0)` that is smaller than
the endpoint, or marks the prototype mixed/endpoint-strength with a precise
reason.

Failure criterion: the project again only renames tuple rows without testing
one concrete nonempty row.

### Phase G: Fixed-row package feasibility gates

Target window: iterations 64-72 after this document.

Purpose: test whether the conditional package from Module 249 has any
plausible fixed-row local proof route before attempting harder tuple rows.

Decision from Module 250:

```text
Do not attempt a two-point fixed-support row yet.
First test FixedRowOnePointPkg_249 itself.
```

Expected work:

- Module 251: deterministic boundary-length feasibility for `BLength_245`;
  completed as `BoundaryLengthGate_251`, deriving the conditional deterministic
  bound `BLength_245 <= A_W(M)GeomModel_251` and showing that the
  boundary-length majorant route is local only when
  `(C_mean_245+1)A_W(M)GeomModel_251 + MassErr_245=o_W(1)`;
- Module 252: kernel absolute-mass and Holder feasibility for `A_W(M)`,
  `K_q(M)`, and `P_M`;
  completed as `KernelHolderGate_252`, separating the boundary-mass kernel
  condition from the Holder condition and marking projection smoothing or
  kernel replacement as mixed unless a transfer row returns to the fixed
  `P_M`;
- Module 253: short-interval W-PNT range audit for `WOneBoundaryPNT_244`;
  completed as `WShortRangeGate_253`, reducing the W branch to the fixed-row
  condition
  `eps_WPNT_253 BLength_245 + WPNTError_253 + BadRangeMass_253=o_W(1)`,
  and blocking full-interval W-PNT as a shortcut when active boundary
  intervals fall below range or residue/cutoff/limit-order compatibility is
  missing;
- Module 254: exact side-row convention audit for `CutOne_242`,
  `RangeOne_242`, `WResOne_242`, `PPOne_242`, and `NormZeroOne_242`;
  completed as `SideConventionGate_254`, separating pointwise exactness
  checks `CutExact_254`, `RangeExact_254`, `WResExact_254`, `PPExact_254`,
  and `NormZeroExact_254` from the corresponding fixed-row weighted defect
  estimates, and blocking exactness claims obtained by changing row or using
  endpoint-strength estimates;
- Module 255: assemble a feasibility verdict for
  `FixedRowOnePointPkg_249`;
  completed as `FixedRowFeasGate_255`, assembling
  `MeanFeasGate_255 + SideConventionGate_254` into a conditional implication
  to `FixedRowOnePointPkg_249` and recording that the one-point row is a valid
  conditional route but remains unproved outside exact model conventions;
- Module 256: two-point escalation gate after the one-point feasibility
  verdict;
  completed as `TwoPointEscGate_256`, selecting the same-slot derivative pair
  `S={(00,0),(00,1)}` with boundary label `(00,0)`, recording
  `Theta_{w,S}^proj=kappa_w(d)`, and allowing escalation only as a diagnostic
  that carries pair boundary mean, pair side rows, kernel discipline, and
  unresolved one-point gates explicitly;
- Module 257: minor-arc reentry gate, comparing the boundary obstruction with
  `NarrowMinorArc_3^B` and `MinorArcTransfer_3^B`;
  completed as `BoundaryMinorReentry_257`, classifying boundary/minor-arc
  routing and recording that minor-arc packages do not automatically prove
  boundary gates and boundary gates do not prove minor-arc cancellation unless
  named localized transfer rows are supplied;
- Module 258: projected-major reentry gate, comparing the boundary
  obstruction with `ProjectedMajorTarget_3^B` and
  `WProjectedLocalMatch_3^major`;
  completed as `BoundaryMajorReentry_258`, classifying fixed boundary gates
  as possible local or mixed slices of `CycIntTransfer_3^major` while blocking
  their use as proofs of `WProjectedLocalMatch_3^major`,
  `ProjectedModelNeutrality_3^major`, or `ProjectedMajorTarget_3^B`;
- Module 259: perform the eighth plan update and choose the next branch;
  completed as `PlanUpdate_8_259`, closing Phase G as a diagnostic window,
  blocking blind escalation to larger boundary tuple rows, and selecting
  Phase H as a projected model-neutrality feasibility window.

Success criterion: either a concrete fixed-row route to
`FixedRowOnePointPkg_249` survives the feasibility gates, or the boundary
branch is stopped with a precise reason.

Failure criterion: Phase G merely renames `KernelAvgStrength_245` or the side
rows without testing boundary length, kernel mass, short-interval range, and
exact conventions.

### Phase H: Projected model-neutrality feasibility window

Target window: iterations 73-81 after this document.

Purpose: test a non-boundary projected-major bottleneck after the boundary
branch has been classified as transfer-only. The first target is the
model-side neutrality row:

```text
ProjectedModelNeutrality_3^major(P_adm):
  NeutralErr_major^P=o_W(1).
```

Decision from Module 259:

```text
Close Phase G as a useful diagnostic window.
Do not continue blind boundary tuple expansion.
Begin with projected model neutrality before attempting full
WProjectedLocalMatch_3^major or returning to minor transverse incidence.
```

Expected work:

- Module 260: formulate `ProjectedModelNeutralityGate_260(P_adm)`, fixing the
  exact model-neutrality object, admissibility scope, and sufficient
  local-factor, kernel, collision, denominator, and W-limit rows;
  completed as a conditional gate reducing
  `ProjectedModelNeutrality_3^major(P_adm)` to exact model discipline,
  generic W-tail cancellation, a signed or absolute kernel budget,
  collision-defect control, denominator/W-limit/projection uniformity, and
  model-domain conventions;
- Module 261: create `Reflective_3.md`, the required 40-iteration memory log
  after `Reflective_1`, reviewing Modules 221-260 and checking for weakened
  claims or hidden upgrades;
  completed as a structural memory log recording the boundary-row,
  endpoint-arrow, one-point/two-point, reentry, and Phase H model-neutrality
  corrections while preserving all open endpoint statuses;
- Module 262: perform the fifth 15-iteration plan challenge, deciding whether
  the model-neutrality branch remains preferable to minor transverse
  incidence or a localized boundary-transfer slice;
  completed as `PlanChallenge_5_262`, continuing Phase H only in narrowed
  proof-or-blocked mode through the signed inclusion-exclusion, collision,
  kernel, W/denominator/projection uniformity, and verdict tests;
- Module 263: expand `NeutralErr_major^P` into the signed
  inclusion-exclusion subset average and identify which subset sizes and face
  factors can cancel structurally and which require averaged compatibility;
  completed as `SignedSubsetExpansion_263(P_adm)`, an exact structural
  expansion into subset layers that isolates `Kbar_P Omega_w^gen`,
  `CollSigned_263`, exact lower-face identities, and the open averaged
  compatibility row `AvgFaceCompat_263(P_adm)`;
- Module 264: audit collision and diagonal strata inside projected
  model-neutrality, separating exact local-model collisions from removable
  collision-defect routes;
  completed as `CollStrataAudit_264(P_adm)`, splitting the collision row into
  the absolute route `AbsCollStrataGate_264 => CollNeutral_260` and the
  signed full-cover route `SignedCoverGate_264 => CollSigned_263=o_W(1)`,
  while recording that the signed route is not the absolute defect row;
- Module 265: audit kernel signed-cancellation versus absolute-mass
  requirements for model neutrality, including the risk that replacing `W_M`
  by `|W_M|` loses the only available cancellation;
  completed as `KernelBudgetAudit_265(P_adm)`, splitting Phase H into the
  absolute fork `KernelAbsBudget_265 + AbsCollStrataGate_264` and the signed
  fork `KernelSignedBudget_265 + SignedCoverGate_264`, with signed estimates
  barred from proving absolute rows;
- Module 266: audit W-limit, denominator, CRT range, projection-boundary, and
  dyadic uniformity requirements for model neutrality over `P_adm`;
  completed as `UniformityLedger_266(P_adm)`, requiring same-family W-limit,
  denominator/CRT, projection-boundary, kernel-truncation, cutoff,
  W-residue, dyadic, selector, and supremum-closure rows before either Phase H
  fork can be used over `P_adm`;
- Module 267: give a proof-or-blocked verdict for projected model neutrality:
  conditional local/model-side, mixed, endpoint-strength, or false/blocked as
  a shortcut;
  completed as `ProjectedModelNeutralityVerdict_267(P_adm)`, keeping the
  absolute fork as the conditional route to the literal
  `ProjectedModelNeutralityGate_260` and correcting the signed fork into a
  same-family exact-model route rather than a proof of `CollNeutral_260`;
- Module 268: perform the ninth plan update and choose whether to continue
  major matching, return to minor arcs, or isolate a boundary-transfer slice;
  completed as `PlanUpdate_9_268`, pausing Phase H as a conditional
  dependency map and selecting Phase I, a minor-arc transverse-incidence
  feasibility window.

Success criterion: either `ProjectedModelNeutrality_3^major` is reduced to
checkable model-side rows smaller than the projected major endpoint, or it is
marked mixed/endpoint-strength/blocked with a precise reason.

Failure criterion: Phase H merely renames `WProjectedLocalMatch_3^major` or
`ProjectedMajorTarget_3^B` without testing the model-side local-factor,
kernel, collision, denominator, and W-limit requirements.

Maintenance steering note for any Phase H revisit:

```text
1. SharpGenericTail:
   prove or reject a sharper finite-difference bound for Omega_w^gen before
   relying on generic W-tail savings.

2. MinimalAdmissibleFamily:
   define a concrete P_adm^0 with all parameters, cutoff conventions,
   denominator ranges, W-residue conventions, selector class, projection
   family, and limiting order.

3. CollNeutral:
   decide whether CollNeutral_260 can be obtained from finite-prime collision
   load, CRT range estimates, structural diagonal stratification, kernel
   budget, and dyadic averaging alone, or whether it is endpoint-strength.

4. Fork viability:
   only after the first three checks decide whether the absolute or signed
   Phase H fork remains viable.
```

This note does not reopen Phase H as the active branch. Module 268 selected
Phase I, but the note records the smallest safe Phase H targets if the branch
is revisited.

### Phase I: Minor-arc transverse-incidence feasibility window

Target window: iterations 82-90 after this document.

Purpose: return to the minor-arc branch after the Phase H verdict and test
the unresolved transverse incidence term in `NarrowMinorArc_3^B` directly.
The goal is not to prove the residual cube endpoint. The goal is to decide
whether the transverse term can be converted into a smaller, non-tautological
incidence, restriction, inverse, or correlation row.

Decision from Module 268:

```text
Pause Phase H as a conditional dependency map.
Do not continue directly to full projected-major matching.
Begin Phase I with the transverse set I_trans(lambda).
```

Expected work:

- Module 269: completed as `TransIncCore_269`, the exact weighted
  shift-frequency graph left after bad-shift and persistent-frequency
  removals; no transverse bound was proved;
- Module 270: audit bad-shift and persistent-frequency removals, deciding
  what remains after `E_d(lambda)<=mu(lambda)` and
  `N_xi(lambda)<=K(lambda)`;
- Module 271: expand a transverse large Fourier coefficient of `B_d` into
  the underlying shifted `f`-correlations and record the exact phase
  equations generated by two or more transverse incidences;
- Module 272: compare available tools against the transverse object:
  large sieve, additive energy, ordinary pair-BDH, rectangle-BDH,
  first-moment HL, and generic finite-complexity HL;
- Module 273: formulate a non-tautological transverse incidence gate, with a
  candidate `Gamma_trans(lambda;D,R,eta,w)` and explicit non-endpoint
  criteria;
- Module 274: audit W-limit, threshold-buffer, prime-power, major/minor
  arc-boundary, and selector-transfer compatibility for the transverse gate;
- Module 275: test whether low-dimensional degeneracies in the transverse
  equations reduce to bad-shift, persistent-frequency, major-arc leakage, or
  boundary rows already named;
- Module 276: give a proof-or-blocked verdict for the transverse incidence
  gate: local/model-side, mixed, endpoint-strength, or false / blocked as a
  shortcut;
- Module 277: perform the tenth plan update and the sixth plan challenge,
  since the long-term-plan count will reach 90.

Success criterion: produce a named transverse-incidence row that is
demonstrably smaller than `M_minor=o(1)`, or classify the transverse route as
mixed, endpoint-strength, or blocked with a precise reason.

Failure criterion: Phase I merely renames `Gamma_trans` without unpacking the
incidences, phase equations, thresholds, transfer rows, and forbidden
shortcuts.

## 6. How each future iteration should start

At the start of each substantive continuation, check:

```text
latest module number
post-Reflective_1 solving count
long-term-plan count
whether iteration is divisible by 9
whether iteration is divisible by 15
whether the 40-iteration reflection cadence is due
```

Then choose the next module from the current phase unless there is a clear
mathematical reason to deviate. If deviating, record the reason in the module
or in this plan.

## 7. How to question the plan

A 15-iteration challenge must answer:

- What assumption am I relying on because it is convenient rather than proven?
- Which route would I abandon if I had to remove one conditional estimate?
- Is the current work moving toward the original problem, or only polishing an
  endpoint formalism?
- Did any module since the last challenge weaken an earlier claim?
- What would convince me that the current phase should stop?

The answer may keep the plan, revise it, or reject it. The important part is
that the challenge is written down before momentum turns into folklore.

## 8. Immediate next action

Module 256 completed the two-point diagnostic escalation gate:

```text
TwoPointEscGate_256
  => BoundaryIntervalHL_234({(00,0),(00,1)},(00,0)),

Theta_{w,{(00,0),(00,1)}}^proj=kappa_w(d).
```

The verdict is conditional and diagnostic only:

```text
The two-point row introduces a real pair local factor but also inherits the
unresolved one-point mean, kernel, range, and side-row gates.
```

Module 257 completed the reentry comparison:

```text
BoundaryMinorReentry_257
  compares fixed boundary gates with
  NarrowMinorArc_3^B and MinorArcTransfer_3^B.

Verdict:
  minor-arc packages and boundary gates control different objects unless an
  explicit localized trace/side-transfer row is supplied.
```

Module 258 completed the projected-major reentry comparison:

```text
BoundaryMajorReentry_258
  compares fixed boundary gates with
  ProjectedMajorTarget_3^B, WProjectedLocalMatch_3^major, and
  MajorAnalyticPkg_229.

Verdict:
  boundary gates can enter the projected-major branch only as local or mixed
  slices of CycIntTransfer_3^major. They do not prove projected local-model
  matching, model neutrality, or the major target.
```

Module 259 completed the eighth plan update:

```text
PlanUpdate_8_259
  closes Phase G as a diagnostic window
  and selects Phase H:
    projected model-neutrality feasibility.
```

Module 260 completed the projected model-neutrality gate:

```text
ProjectedModelNeutralityGate_260(P_adm)
  => ProjectedModelNeutrality_3^major(P_adm)
```

only conditionally, under exact model discipline, generic W-tail cancellation,
kernel budget, collision-defect control, denominator/W-limit/projection
uniformity, and model-domain convention rows.

Module 261 completed the reflection cadence:

```text
Reflective_3.md
  reviews Modules 221-260
  and records corrections without proving any endpoint.
```

Module 262 completed the fifth plan challenge:

```text
PlanChallenge_5_262
  keeps Phase H alive only in narrowed proof-or-blocked mode
  through model-neutrality subrow tests.
```

Module 263 completed the signed expansion:

```text
SignedSubsetExpansion_263(P_adm)
  expands NeutralErr_major^P into exact subset layers,
  isolates Kbar_P Omega_w^gen and CollSigned_263,
  and names AvgFaceCompat_263(P_adm) as still open.
```

Module 264 completed the collision-strata audit:

```text
CollStrataAudit_264(P_adm)
  separates structural zero and projected diagonal strata from
  large-prime congruence collisions,
  and splits the collision row into absolute and signed routes.
```

Module 265 completed the kernel-budget audit:

```text
KernelBudgetAudit_265(P_adm)
  splits Phase H into an absolute |W_M| fork
  and a same-family signed W_M fork,
  without transferring signed cancellation to absolute rows.
```

Module 266 completed the uniformity audit:

```text
UniformityLedger_266(P_adm)
  requires W-limit, denominator/CRT, projection, kernel,
  cutoff, W-residue, dyadic, selector, and supremum closure
  in the same admissible family.
```

Module 267 completed the proof-or-blocked verdict:

```text
ProjectedModelNeutralityVerdict_267(P_adm)
  absolute route:
    AbsPMNGate_267
      => ProjectedModelNeutralityGate_260
      => ProjectedModelNeutrality_3^major;

  signed exact-model route:
    SignedExactNeutralGate_267
      => ExactModelNeutral_260
      => ProjectedModelNeutrality_3^major,
    but not CollNeutral_260.
```

Module 268 completed the ninth plan update:

```text
PlanUpdate_9_268
  pauses Phase H as a conditional dependency map
  and selects Phase I:
    minor-arc transverse-incidence feasibility.
```

Module 268 selected:

```text
Module 269: extract the exact transverse-incidence object inside
NarrowMinorArc_3^B.
```

Module 269 completed:

```text
TransIncCore_269
  = the weighted shift-frequency graph I_trans_s(lambda)
    after bad-shift and persistent-frequency removals.
```

Its future analytic target is:

```text
TransIncBound_269(Gamma_trans;P_minor):
  Eng_trans_269(lambda;s,D,R,eta,w)
    <= Gamma_trans(lambda;D,R,eta,w;s)

  and

  sum_lambda lambda^2 Gamma_trans(lambda;D,R,eta,w;s)=o(1).
```

The status remains `STRUCTURAL / EXTRACTION`; no transverse bound,
`NarrowMinorArc_3^B`, or selector transfer was proved.

Continue with:

```text
Module 270:
  audit bad-shift and persistent-frequency removals against the row-energy
  ceiling E_{d,s}(lambda)<=mu(lambda), the column-multiplicity ceiling
  N_{xi,s}(lambda)<=K(lambda), and the lambda-summed target.
```

Module 270 should decide whether any plausible threshold regime leaves a
smaller transverse problem, before asking for a new incidence theorem. It
should preserve these statuses:

```text
NarrowMinorArc_3^B,
TransIncBound_269,
MinorArcTransfer_3^B,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ResCube_3^sharp,
selector transfer,
CPC_3^sharp,
RBDH_pair_short,
AU^3
remain unproved.
```
