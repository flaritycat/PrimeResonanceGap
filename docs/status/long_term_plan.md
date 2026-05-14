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
Latest completed module: 216
Post-Reflective_1 solving count: 35
Long-term-plan count: 29
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
Second plan challenge:   Module 217
Next reflective log:     Module 221
Fourth plan update:      Module 223
Fifth plan update:       Module 232
Third plan challenge:    Module 232
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
- Module 218: audit compatibility between major-arc and minor-arc
  selector-transfer packages, especially projection and denominator changes;
- Module 219: state the frozen-to-moving dyadic threshold transfer obstruction
  in the residual derivative fourth-moment normalization;
- Module 220: state the Bernoulli or finite-stage deterministic-extraction
  requirement for selector statements used in the endpoint branch;
- Module 221: create `Reflective_2.md`, the required 40-iteration memory log
  after `Reflective_1.md`, and record corrections from Modules 179-220;
- Module 222: consolidate the selector-transfer dependency graph after the
  reflection;
- Module 223: perform the fourth 9-iteration plan update.

Success criterion: every future endpoint statement has an explicit selector
line and cannot accidentally jump selector class.

### Phase E: Endpoint equivalence audit

Target window: iterations 37-45 after this document.

Purpose: return to the compressed endpoint class and test whether the side
packages are truly equivalent or only one-way reductions.

Expected work:

- audit each arrow in the endpoint chain;
- label each arrow as proved in ledger, conditional, structural, or open;
- create `Reflective_2.md` when the 40-iteration reflection cadence is reached;
- perform the fifth plan update and third plan challenge at iteration 45.

Success criterion: the project has a current dependency graph with no
unlabeled arrows.

### Phase F: Decision branch

Target window: after iteration 45.

At this point the project should choose one of three routes:

- close a genuinely isolated conditional package if the missing estimate has
  become plausible;
- retreat to a weaker theorem whose hypotheses are honest and useful;
- mark the endpoint branch blocked and return to the original problem through
  a different obstruction analysis.

The decision must be recorded as a status update before more modules are added.

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

Continue with:

```text
Module 217: Second 15-iteration plan challenge.
```

Expected status: `STRUCTURAL / EXTRACTION`.

Module 216 completed the global selector-transfer matrix:

```text
SharpSelectorTransferMatrix_3.
```

The next module is the scheduled plan challenge at long-term-plan count 30. It
should answer:

```text
Is Phase D identifying genuinely smaller transfer problems,
or only restating the endpoint under selector-transfer names?
Which selector row would be abandoned if one conditional estimate had to be
removed?
Should the project continue Phase D, narrow to a single transfer obstruction,
or redirect toward endpoint equivalence / weaker theorem work?
```

In particular, it must scrutinize the core residual selector rows
`SelErr_4`, `SelErr_4^minor`, and `SelErr_major^P`, since those may be
endpoint-strength unless additional localization is supplied.
