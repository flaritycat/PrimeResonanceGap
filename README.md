# Prime Resonance Gap

This repository is the working proof ledger for the **Prime Gap Resonance
Project**.

The short version:

```text
We are studying whether a carefully chosen irrational alpha can select primes
whose normalized next-prime gaps have average limit L0 > 1.
```

That original problem is still **OPEN**. This repository does not claim a
proof of it. The job of the repo is to keep every reduction, obstruction,
conditional route, and failed shortcut visible enough that the project does
not accidentally turn hope into theorem.

## What Is The Main Question?

For an irrational number `alpha`, select primes `p` for which `alpha p` is
very close to an integer:

```text
chi_alpha(p) = 1_{||alpha p|| < 1/log p}
```

For those selected primes, average the normalized next-prime gap:

```text
g(p)        = (p^+ - p) / log p
D_alpha(x)  = sum_{p <= x} chi_alpha(p)
N_alpha(x)  = sum_{p <= x} chi_alpha(p) g(p)
A_alpha(x)  = N_alpha(x) / D_alpha(x)
```

The original problem asks:

```text
Does there exist an irrational alpha such that
A_alpha(x) -> L0 > 1?
```

Status:

```text
OPEN.
```

## ELI5

Primes have gaps between them. We use a number `alpha` as a filter to pick
some primes. The big question is whether one clever filter can pick primes
whose gaps are, on average, bigger than normal. We do not know yet.

## ELI15

The selector keeps primes `p` where `alpha p` is unusually close to an
integer. For those primes we average `(next prime - p)/log p`, which is the
prime gap normalized by its expected size. The project is trying to understand
whether a special irrational `alpha` can make that selected average converge
to a value bigger than `1`. Most of the repository breaks this into Fourier,
local-model, boundary, and selector-transfer subproblems, while keeping track
of which parts are proved, conditional, or still open.

## ELI25

The analytic core uses residual prime weights. Write `f=nu-1` and

```text
B_d(n)=f(n+d)conj(f(n)).
```

One hard endpoint asks for fourth-moment Fourier decay, schematically:

```text
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1).
```

The project splits this into major arcs, minor arcs, local Euler-factor
models, W-trick uniformity, boundary transfer, prime-power transfer, and
selector transfer. The current frontier is a minor-arc transverse obstruction:
large Fourier coefficients form adaptive shift-frequency shells. We are
testing whether any non-endpoint estimate can control the shell functional
`Xi_273^0` in a fixed minimal model family `P_minor^0`. The current verdict is
that fixed frequency-set estimates do not automatically control these
data-dependent shells, and the remaining local side rows must still be proved
before any Phase J kernel bound can be used. The later Phase K audits narrowed
the threshold-window obstruction: the local low-level fourth-moment tail is
proved inside `P_minor^0`, vacuous removal is only bookkeeping, and the row
barrier remains blocked under the current first-energy, row-distribution,
row-square, and fixed-fiber tests. The latest steering challenge pauses direct
row-square continuation, and the column audit now shows that first-incidence
counting gives only column-barrier ceilings. The distributional audit then
shows that layer-cake with first-moment tails collapses back to the same
ceiling. The concrete `r=2` expansion now isolates the off-diagonal
same-frequency shift-pair row and points to a weighted coefficient-pair energy
audit. That audit shows current Cauchy/Parseval inputs still give only
energy-square ceilings, so the next useful step is an autocorrelation
expansion. None of this proves the endpoint.

## The Whole Project In One Narrative

The project is about a very specific way of asking whether prime gaps can be
biased by an irrational rotation.

Start with all primes. For each prime `p`, the selector
`chi_alpha(p)` asks whether `alpha p` lands very close to an integer. This
creates a thin subsequence of primes depending on `alpha`. On that subsequence
we average the normalized next-prime gap `g(p)`. The original problem asks
whether some irrational `alpha` can make that selected average converge to a
limit bigger than the ordinary value `1`.

The project then separates the problem into layers:

```text
Layer 1: Selected averages
  D_alpha(x), N_alpha(x), A_alpha(x), and the full gap g(p).

Layer 2: Selector and gap transfer
  Can statements in model, frozen, smoothed, cyclic, or W-tricked worlds be
  returned to the actual sharp moving selector and the full gap?

Layer 3: Prime-weight residuals
  Replace prime irregularity by f=nu-1 and shifted products
  B_d(n)=f(n+d)conj(f(n)).

Layer 4: Fourier endpoint engines
  Control major/minor arc fourth moments and residual derivative cubes.

Layer 5: Exact local models and side rows
  Euler factors, collision terms, W-limits, boundary errors, prime powers,
  dyadic ranges, thresholds, and adaptive-shell selection.
```

Each layer can fail independently. A proof at Layer 4 is not a solution of
Layer 1 unless Layers 2 and 5 also transfer correctly. A model estimate is
not an actual-alpha theorem. A clipped-gap theorem is not a full-gap theorem.
An endpoint equivalence is not an endpoint proof.

At the project level, the ledger currently says:

```text
Original selected-average problem:
  OPEN.

Metric almost-everywhere branch:
  PROVEN according to the project ledger, but only for a.e. alpha.

Finite-type branch:
  CONDITIONAL.

s=2 / residual-cube endpoint branch:
  OPEN.

Current local work:
  a minor-arc W-cyclic model laboratory, P_minor^0, used to test whether a
  smaller non-endpoint input can control adaptive Fourier shells.
```

So the current modules are not "the project"; they are the active microscope.
The whole project remains the selected-prime-gap problem above. The active
microscope is examining one local obstruction because it is one of the places
where a future proof would need real analytic strength.

## How The Branches Fit Together

There are five main project branches:

```text
1. Metric branch
   What happens for almost every alpha?
   Current ledger: A_alpha(x)->1 a.e. is PROVEN.

2. Finite-type branch
   What can be said for Diophantine alpha with controlled approximation?
   Current ledger: CONDITIONAL.

3. Major-arc branch
   Can exact local Euler-factor models, collision control, and W-limits be
   matched strongly enough?
   Current ledger: projected major target remains OPEN / CONDITIONAL.

4. Minor-arc branch
   Can residual Fourier mass be controlled at endpoint strength?
   Current ledger: residual cube and transverse shell targets remain OPEN.

5. Transfer branch
   Can model/cyclic/frozen/smoothed statements be moved back to the actual
   sharp moving selector and full gap?
   Current ledger: no automatic transfer.
```

The current Phase K side-package triage belongs to branch 4, with necessary
help from branch 5. It does not settle branches 1, 2, 3, or the original
problem.

## What A Complete Solution Would Need

A positive solution would need all of the following, in the actual target
world:

```text
1. An irrational alpha or a construction mechanism.
2. Control of the selector count D_alpha(x).
3. Control of the selected gap numerator N_alpha(x).
4. Full-gap control, not only clipped or model tail control.
5. Exact transfer from any model estimates to chi_alpha(p).
6. Boundary, W-limit, residue, prime-power, and dyadic uniformity.
7. A final proof that A_alpha(x)->L0 with L0>1.
```

A negative all-alpha theorem would need a different full route:

```text
show that no irrational alpha can have a positive finite limit L0>1,
with the actual selector and full gap still present.
```

That theorem is also open.

## Whole Project Map

The project has three jobs at once:

```text
1. Study the original selected-prime gap problem.
2. Prove whatever can be proved honestly.
3. Keep every unproved endpoint and shortcut clearly labeled.
```

The work is organized as a proof ledger, not as a single linear paper. The
main branches are:

```text
Original selected-average problem
  asks whether some irrational alpha gives A_alpha(x) -> L0 > 1.

Metric branch
  studies typical alpha. The ledger records A_alpha(x) -> 1 for almost every
  alpha as PROVEN.

Finite-type branch
  studies alpha with Diophantine restrictions. This remains CONDITIONAL.

Obstruction branch
  asks what would prevent a positive selected-gap limit. This is structural
  unless a module gives an actual theorem.

s=2 endpoint branch
  compresses one major analytic bottleneck into equivalent endpoint objects
  such as RBDH_pair_short, CPC_3^sharp, DyadicDerivativeU^2, and AU^3.
  The endpoint class remains OPEN.

Selector-transfer branch
  tracks whether estimates in model, smoothed, frozen, cyclic, or W-tricked
  worlds can be transferred to the actual sharp moving selector. These
  transfers are not automatic.
```

## The Proof Architecture

The large strategy is to replace the original selected-gap average by exact
objects that can be attacked analytically, while never forgetting what was
lost in the replacement.

The rough architecture is:

```text
selected prime-gap average
  -> gap and tail decompositions
  -> covariance and local model extraction
  -> residual prime-weight objects f=nu-1
  -> shifted products B_d(n)=f(n+d)conj(f(n))
  -> Fourier fourth moments
  -> major/minor arc split
  -> local model, collision, boundary, W-limit, and selector-transfer rows
```

The current hard endpoint is not the original problem itself. It is a
compressed analytic target that would be one necessary engine in a larger
route:

```text
ResCube_3^sharp
  <-> DyadicDerivativeU^2
  <-> AU^3
  <-> CPC_3^sharp
  <-> RBDH_pair_short
```

This equivalence map is useful, but equivalence is not proof. The whole class
is still open.

## Major Arcs, Minor Arcs, And Transfer

The Fourier target splits into major and minor arcs.

Major arcs:

```text
need exact local Euler-factor models,
collision and diagonal control,
kernel budgets,
W-limit uniformity,
boundary and prime-power transfer,
and selector-class transfer.
```

Minor arcs:

```text
need large-spectrum and fourth-moment control for B_d,
bad-shift and persistent-frequency removals,
transverse incidence or phase-kernel estimates,
and the same transfer discipline.
```

Transfer rows matter because a proof in the wrong world is not a proof of the
original object. For example:

```text
cyclic model != interval model,
W-prime model != actual primes without transfer,
smoothed/frozen selector != sharp moving selector,
clipped gap != full gap,
first-moment local density != fourth-moment Fourier control.
```

## What The Documents Are

The repository has several kinds of files:

```text
source_texts/
  original large artifacts from the project.

docs/paper/
  generated 500-page paper text.

docs/ledger/
  older 250-page project ledger.

docs/modules/
  the active module chain. This is where new proof steering happens.

docs/status/
  global status, theorem status index, forbidden upgrades, and long-term plan.

docs/reviews/
  project-wide review snapshots.

papers/
  paper outlines and theorem inventories.

experiments/
  HEURISTIC probes only. These are not proof inputs.
```

The most important active files are:

```text
docs/status/global_status.md
docs/status/theorem_status_index.md
docs/status/long_term_plan.md
docs/modules/dependency_graph.md
docs/modules/modules_156_178_summary.md
```

## What Would Count As Real Progress?

Real progress is one of:

```text
a proved theorem with exact hypotheses;
a conditional theorem with all dependencies named;
a structural identity that prevents ambiguity;
a blocked shortcut recorded clearly;
a smaller subtarget replacing a vague obstruction;
a status correction that prevents overclaiming.
```

Real progress is not:

```text
renaming an endpoint;
assuming the object we meant to prove;
using a model estimate as a sharp selector estimate;
using first-moment information as a fourth-moment bound;
using equivalence between endpoints as proof of any endpoint.
```

## What Would Solve The Original Problem?

A full solution would need far more than the current Phase J work. It would
need a complete path from the actual sharp moving selector and full gap object
to a proved asymptotic statement for `A_alpha(x)`.

In particular, a positive construction would need:

```text
an irrational alpha or construction mechanism;
control of D_alpha(x) and N_alpha(x);
full gap, not only clipped or model gaps;
transfer from any model/frozen/smoothed estimates to the actual selector;
all boundary, W-limit, prime-power, and local-model errors controlled;
a proof that the final selected average has limit L0 > 1.
```

The project does not currently have that. It has a carefully mapped set of
open analytic engines and transfer barriers.

## What Are We Actually Doing Now?

The current active phase is **Phase K: partition-class counting audit after
the prime-partition cover-moment criterion**.

Current frontier:

```text
Latest module frontier: Module 330
Active phase: Phase K, partition-class counting audit next
Latest project-wide review:
  docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md
```

Recent modules did this:

```text
Module 278:
  fixed a minimal W-cyclic prime-only model family P_minor^0.

Module 279:
  expanded Xi_273^0 exactly into linear, TT*, and fourth-power shell kernels.

Module 280:
  showed that fixed frequency-set estimates do not automatically transfer to
  the data-dependent shell fibers S_d(J) and D_xi(J).

Module 281:
  benchmarked large-sieve/Bessel-type estimates and found that currently
  available non-endpoint versions reproduce row/column ceilings or fixed-set
  diagnostics, not the adaptive shell gain needed for PhaseKernelBound_273^0.

Module 282:
  audited degeneracy rows inside P_minor^0. Boundary/cutoff, WPP, and
  selector degeneracies vanish only by internal model convention; row,
  column, major-difference, physical-diagonal, and deg-free rows remain open.

Module 283:
  audited the minimum side rows still needed inside P_minor^0. Boundary,
  fixed-residue, prime-only, and selector-change rows are conventions only
  in the local model; W-uniformity, threshold budget, low-level cutoff,
  dyadic uniformity, and adaptive shell selection remain open.

Module 284:
  tested the threshold budget against row/column ceilings and the
  lambda-summed target. It named row, column, shell-counting, removal, and
  low-level budget barriers, but left all smallness claims open.

Module 285:
  gave a current-tools verdict for the adaptive shell route. Fixed-set
  estimates still need selection transfer, Bessel gives only row/column
  ceilings, threshold barriers remain open, and `PhaseKernelBound_273^0`
  remains open.

Module 286:
  performed the eleventh plan update. Phase J is paused as blocked by current
  tools, and Phase K begins with adaptive-shell gain triage.

Module 287:
  audited the direct-shell TT* cross terms for X_J(omega). The coefficient
  diagonal gives only energy, Cauchy/Bessel returns row/column ceilings,
  fixed-set and full-orthogonality shortcuts are blocked, and
  DirectShellCrossTermGain_287 remains open.

Module 288:
  audited selection complexity for the adaptive shell fibers S_d(J). Raw
  union bounds are too large, row/column graph entropy is diagnostic only,
  fixed thresholds do not make fibers predetermined, and
  SelectionComplexityGain_288 remains open.

Module 289:
  stress-tested the uniform-fiber route over row/column-admissible shells.
  Row/column-only data reproduce deterministic ceilings rather than a gain;
  WeightedRCSubgraphGain_289 is the remaining open structured target.

Module 290:
  gave the Phase K adaptive-shell gain verdict. Direct-shell,
  selection-transfer, and uniform-fiber routes all remain open at current
  strength, so PhaseKCurrentClosure_290 is FALSE / BLOCKED while
  AdaptiveShellGainP0_285 remains open.

Module 291:
  cleaned up the Phase K status map and prepared ChallengePacket_291 for the
  seventh plan challenge. Continuing Phase K without a new input is now
  explicitly blocked.

Module 292:
  performed the seventh plan challenge and selected OptionD_SidePkg_291.
  AdaptiveGainFirst_292 is FALSE / BLOCKED as the next move, and
  SidePkgTriage_293(P_minor^0) is the next target.

Module 293:
  split the side package into convention rows, proof-hygiene rows,
  threshold/low-level rows, degeneracy rows, and adaptive-core rows. It
  returned ShellSelectionP0_283 and DegFreePhaseGate_282 to the adaptive core
  rather than treating them as harmless side bookkeeping, and selected
  LowLevelBudgetTriage_294(P_minor^0) as the next narrow target.

Module 294:
  classified below-lambda_min leakage. The module records that low-level
  smallness is not proved by the shell-grid definition, gives deterministic
  counting barriers for possible reconstructions, and leaves
  LowLevelBudgetP0_284, LowLevelCutoffP0_283, and LowLevelCountingBarrier_294
  open.

Module 295:
  performed the twelfth plan update. It keeps the side-package branch narrow,
  questions whether low-level triage is useful without an exact
  reconstruction formula, and selects LowLevelCountingBarrierAudit_296 as the
  next concrete test.

Module 296:
  audited the low-level counting barrier. Pure counting is blocked under the
  current P_minor^0 data, while the exact fourth-moment tail reduces to the
  open second-energy target lambda_min^2 E2_minor^0=o_W(1).

Module 297:
  proved the local second-energy tail inside P_minor^0 by combining the
  trivial logarithmic pointwise envelope with normalized Parseval. This closes
  only the local fourth-moment low-level tail.

Module 298:
  separated vacuous actual bad-shift/frequency removal from useful threshold
  closure. Empty bad sets can be forced by maximal thresholds inside the local
  model, but the row/column shell and removal budgets remain open.

Module 299:
  extracted the exact continuous threshold-window criteria. Useful windows
  require the optimized row/column barriers from Module 284 to be small, plus
  integer/range, declared-schedule, and W-uniformity rows. The trivial caps
  and vacuous schedule do not close the window.

Module 300:
  audited the row barrier against the current same-family energy inputs.
  Pointwise bounds, Parseval, and the local low-level tail give only a
  polylogarithmic row-barrier ceiling, not `o_W(1)`. The row barrier remains
  open, and the current route is blocked.

Module 301:
  wrote Reflective_4, reviewing Modules 261-300 and preserving the open
  endpoint statuses. The reflection selects the row-energy distribution audit
  as the next mathematical target.

Module 302:
  audited row-moment distribution inside P_minor^0. The layer-cake criterion
  is exact but structural, the current Markov tail reproduces the Module 300
  polylogarithmic ceiling, and the fourth-moment large-spectrum route is
  circular unless supplied by an independent non-endpoint theorem. Row-tail
  and q=2 row-square targets remain open.

Module 303:
  expanded the q=2 row-square moment into an exact same-shift restricted
  kernel over the data-dependent large-spectrum fibers S_{d,j}. The identity
  is structural only: full-frequency orthogonality, fixed-fiber transfer, and
  endpoint fourth moments are blocked as automatic proof routes, while
  SameShiftSquareKernelGain_303 remains open.

Module 304:
  performed the thirteenth plan update. It questions a direct attack on the
  full data-dependent row-square kernel and selects the smaller fixed-fiber
  benchmark first, to decide whether the obstruction is already present
  before selection transfer.

Module 305:
  benchmarked prescribed fibers U_d independent of beta_0. The exact
  fixed-fiber kernel identity is structural, Parseval/Bessel tools return
  the same ceiling scale as Modules 300/302, and full-frequency diagnostics
  do not prove the restricted row-square target. FixedFiberRowSquareGain_305
  remains open.

Module 306:
  recorded the fixed-fiber blocked verdict. Since no fixed-fiber gain exists
  in the current toolkit, selection transfer is blocked as the next move; the
  remaining size-sensitive criterion is structural only. The row-square branch
  is sent to the scheduled plan challenge.

Module 307:
  performed the eighth plan challenge. It pauses direct row-square
  continuation under the current toolkit, declines to assume the
  size-sensitive fixed-fiber criterion, keeps selection transfer blocked as
  the next move, and selects the column-multiplicity barrier audit as the next
  local test.

Module 308:
  audited the column barriers. Raw counting and the sharper first-moment
  incidence/energy bound both give only ceilings, with an uncontrolled
  `(m_minor^0)^theta_r` factor after the Module 284 weights are restored.
  Low-level tail control and vacuous removal do not prove column-barrier
  smallness. ColumnMultiplicityGainTarget_308 remains open.

Module 309:
  rewrote the column multiplicity moment through exact layer-cake tails.
  First-moment Markov tails collapse back to the Module 308 first-incidence
  ceiling, so layer-cake alone is not a gain. The next concrete target is the
  `r=2` same-frequency shift-pair expansion.

Module 310:
  expanded the concrete `r=2` column multiplicity moment into exact
  same-frequency shift-pair incidences. The diagonal row is first-energy
  controlled, the off-diagonal row remains open, and first incidence again
  collapses to the Module 308 ceiling. The next test is a weighted
  coefficient-pair energy audit.

Module 311:
  audited the weighted coefficient-pair route. Energy-square and fourth-power
  Cauchy estimates both return ceiling-scale bounds under current local
  inputs. The weighted route remains open, but needs an exact autocorrelation
  expansion before another analytic claim is made.

Module 312:
  expanded the weighted same-frequency pair energy into an exact
  anti-diagonal two-shift autocorrelation kernel with the minor cutoff
  K_minor^0. Full-frequency and minor-kernel decompositions are diagnostic
  only; current tools still do not prove a weighted pair gain.

Module 313:
  performed the fourteenth plan update. It blocks a direct attack on the
  bundled anti-diagonal target as the next move and selects a smaller
  full/zero/major minor-kernel row split for Module 314.

Module 314:
  split the Module 312 minor-kernel identity into full-frequency
  anti-diagonal, zero-mode product, and major-kernel correction rows. The
  split is exact and structural; independent row smallness is blocked under
  current tools, and the zero-mode product row is the next audit target.

Module 315:
  audited the zero-mode product row. The minor convention does not make
  beta_0(d,0) vanish, and no current estimate controls the zero row. However,
  because minor arcs exclude zero frequency, an exact centered rewrite removes
  the explicit zero row and moves the next audit to the centered full
  anti-diagonal row.

Module 316:
  audited that centered full row. Centering removes only the zero Fourier
  coefficient; the row is still the full nonzero-frequency column second
  moment. Current Cauchy, Parseval, energy-square, and fourth-power routes do
  not close it, so the next audit is the major-kernel correction row.

Module 317:
  audited the major-kernel correction row. It is a positive major-frequency
  pair-energy row, not a harmless error. Current positivity, cardinality,
  pair-BDH, first-moment HL, and conditional projected-major shortcuts do not
  close it; a genuine route would need the exact residual eight-slot major
  model in the same `P_minor^0` conventions.

Module 318:
  gave the signed minor-kernel combination verdict. The centered
  full-minus-major row is exactly `WOff_311`; without a new signed
  minor-kernel theorem, the split is diagnostic rather than a smaller proof
  route.

Module 319:
  inventoried candidate new inputs for the exact centered minor-kernel row.
  Endpoint assumptions and current-tool ceilings are rejected; the selected
  next smaller target is a size-sensitive minor-kernel criterion.

Module 320:
  formulated the size-sensitive cross-shell `Phi` criterion. A proved
  admissible `Phi` could feed the r=2 column-pair route, but deterministic
  energy-product, column-cap, and incidence bounds still recover current
  ceilings.

Module 321:
  audited the data-dependent fibers. Current row caps, column caps, shell
  restrictions, energy tails, and selection rules do not force overlap gain or
  independence; complete same-frequency concentration is still compatible with
  the deterministic constraints.

Module 322:
  performed the fifteenth plan update and ninth plan challenge. It pauses the
  direct cap-only/fiber-only continuation, blocks a direct attack on
  FiberOverlapGainTarget_321 as the next move under current inputs, and selects
  an extraction-only residual eight-slot minor expansion for Module 323.

Module 323:
  expanded the centered minor-kernel row into the exact eight-slot residual
  top face. Centered lower faces vanish only by the nonzero minor-kernel
  identity, and threshold-localized rows keep a data-dependent kernel through
  the large-spectrum masks. The expansion is structural and does not prove
  residual cancellation.

Module 324:
  classified internal autocorrelation diagonals, sixteen cross-block slot
  collision equations, finite-prime collision load, and the full-frequency
  anti-diagonal diagnostic. It blocks the shortcut from collision catalog to
  collision smallness and selects a generic-versus-collision local-model
  split for Module 325.

Module 325:
  formulated the generic-versus-collision local-model split for the eight-slot
  minor row. It extracts the generic size-only factor, the collision-defect
  partition, structural diagonal rows, finite-prime collision-load rows,
  overflow rows, data-dependent kernel-selection rows, generic noncollision
  row, and local-model insertion row. All analytic smallness rows remain open.

Module 326:
  audited the exact signed inclusion-exclusion in the eight-slot minor local
  model. It records the top-Mobius identity, proper-support cancellation, and
  the unrestricted generic zero-mode identity, while leaving full-cover
  collision clusters, stratified generic remainders, and signed local-model
  insertion open.

Module 327:
  classified the full-cover clusters that survive the signed support audit.
  It separates one-prime full-cover events, products of proper-support events
  whose union covers all eight labels, structural full-cover clusters, and a
  diagnostic cover-load envelope. All cover-load smallness rows remain open.

Module 328:
  turned that diagnostic envelope into a sharper criterion using prime-local
  Mobius coefficients. It blocks reading the crude edge cover load as the
  exact signed coefficient, and it blocks first-load, energy-only, and
  rank-only routes as current closures.

Module 329:
  audited the prime-local Mobius weights themselves. It derives
  delta_{p,S}=e_p(S)/(p-|S|), the singleton-appendage penalty, the
  pointwise Mobius-degree bound, and a one-prime full-cover power table.
  Partition counting and kernel-weighted Mobius-cover rows remain open.

Module 330:
  turned the pointwise Mobius-degree table into a finite-cutoff
  kernel-weighted cover-moment criterion. The criterion is conditional:
  partition-class counting, structural-rank uniformity, multi-prime
  CRT/uniformity, finite-prime tails, and signed local-model insertion remain
  open.
```

The next step should not claim threshold closure. The local low-level tail is
handled, vacuous removal is only bookkeeping, and Modules 300-330 show that
the existing first-energy, row-distribution, row-square, fixed-fiber, column,
weighted-pair, autocorrelation, centered full-row, and major-correction inputs
do not prove the threshold window, the signed minor-kernel row, or the
generic/collision/full-cover/sharp-cover/Mobius-cover/partition-counting rows.

The next planned module is:

```text
Module 316:
  performed CenteredFullAntiDiagonalAudit_316(P_minor^0), auditing the
  full-frequency anti-diagonal row after replacing B_d^0 by B_d^{0,circ}.

Module 317:
  performed MajorKernelCorrectionAudit_317(P_minor^0), auditing the major row
  in the centered full-minus-major formulation.

Module 318:
  performed SignedMinorKernelCombinationVerdict_318(P_minor^0), deciding
  whether the split has produced a genuinely smaller route or only restated
  the original minor-kernel target.

Module 319:
  performed AntiDiagonalNewInputInventory_319(P_minor^0), listing only genuinely
  new non-endpoint inputs that could attack the same-family minor-kernel
  anti-diagonal row.

Module 320:
  performed SizeSensitiveMinorKernelCriterion_320(P_minor^0), defining the
  exact size/energy/kernel criterion and checking which losses would survive
  the Module 310 threshold conversion and Module 284 column-barrier weights.

Module 321:
  performed DataDependentFiberGainAudit_321(P_minor^0), deciding whether the
  current row caps, column caps, shell restrictions, energy tails, or selection
  rules imply any genuine overlap gain for the `Phi` criterion.

Module 322:
  performed PlanUpdate_15_Challenge_9_322, the scheduled combined plan update
  and plan challenge after the fiber-gain blockage.

Module 323:
  performed ResidualEightSlotMinorExpansion_323(P_minor^0), expanding the
  centered minor-kernel row into the exact eight residual slots without
  claiming cancellation.

Module 324:
  performed CollisionDiagonalStrataAudit_324(P_minor^0), classifying the
  collision and diagonal strata of the eight-slot minor row.

Module 325:
  performed GenericCollisionLocalModelSplit_325(P_minor^0), formulating the
  exact generic-versus-collision split needed for the eight-slot minor row.

Module 326:
  performed SignedInclusionExclusionMinorAudit_326(P_minor^0), deciding which
  generic and collision-defect terms are only formally cancelled and which
  survive as same-family analytic rows.

Module 327:
  performed FullCoverClusterAudit_327(P_minor^0), classifying the full-cover
  Mobius coefficients that survive signed inclusion-exclusion.

Module 328:
  performed FullCoverLoadCriterion_328(P_minor^0), turning the cover-load
  envelope into a sharper prime-local Mobius criterion and testing what current
  load moments can actually supply.

Module 329:
  performed PrimePartitionMobiusAudit_329(P_minor^0), computing or bounding the
  prime-local Mobius weights that enter the sharp cover functional.

Module 330:
  performed PrimePartitionCoverMomentCriterion_330(P_minor^0), combining the
  pointwise Mobius-degree table with partition-counting, kernel weights, and
  finite-prime tails.

Module 331:
  perform PartitionClassCountingAudit_331(P_minor^0), testing whether one fixed
  prime partition class can be counted with the actual kernel, threshold masks,
  dyadic ranges, W-residue conventions, structural rank, wraparound, and the
  h+k kernel variable.
```

## What Is Proved?

Compact status table:

| Claim | Status |
|---|---|
| Existence of irrational `alpha` with `A_alpha(x) -> L0 > 1` | **OPEN** |
| All-alpha no-positive-limit theorem | **OPEN** |
| Metric theorem `A_alpha(x) -> 1` for Lebesgue-a.e. irrational `alpha` | **PROVEN according to project ledger** |
| Finite-type no-positive-limit theorem | **CONDITIONAL** |
| `s=2` rational-major endpoint | **OPEN** |
| Residual derivative cube endpoint `ResCube_3^sharp` | **OPEN** |
| Current local shell target `PhaseKernelBound_273^0` | **OPEN** |
| Local low-level fourth-moment tail inside `P_minor^0` | **PROVEN inside `P_minor^0` only** |
| Vacuous actual bad-set removal inside `P_minor^0` | **PROVEN inside `P_minor^0` only; not threshold closure** |
| Row barrier `RowBarrierP0_284(q)=o_W(1)` | **OPEN** |
| Column barriers `ColumnBarrierP0_284(r)`, `SigmaColumnBarrierP0_284(r)` | **OPEN** |
| Fixed-fiber row-square gain `FixedFiberRowSquareGain_305` | **OPEN** |
| Direct row-square continuation as next move `RowSquareContinue_307` | **FALSE / BLOCKED** |
| Column-barrier moment audit `ColumnBarrierMomentAudit_308` | **STRUCTURAL / EXTRACTION** |
| Current column-barrier route `CurrentColumnBarrierRoute_308(r)` | **FALSE / BLOCKED** |
| Column multiplicity gain `ColumnMultiplicityGainTarget_308(r)` | **OPEN** |
| Column-multiplicity distribution audit `ColumnMultiplicityDistributionAudit_309` | **STRUCTURAL / EXTRACTION** |
| First-moment layer-cake route `FirstMomentLayerCakeCollapse_309(r)` | **FALSE / BLOCKED** |
| Column tail gain `ColumnTailGainTarget_309(r)` | **OPEN** |
| Column-pair expansion `ColumnPairMultiplicityExpansion_310` | **STRUCTURAL / EXTRACTION** |
| Off-diagonal same-frequency pair row `OffDiagonalSameFrequencyPair_310` | **OPEN** |
| Weighted column-pair energy target `WeightedColumnPairEnergyTarget_310` | **OPEN** |
| Weighted column-pair energy audit `WeightedColumnPairEnergyAudit_311` | **STRUCTURAL / EXTRACTION** |
| Current weighted route `WeightedCurrentToolsClose_311` | **FALSE / BLOCKED** |
| Weighted column second moment `WeightedColumnSecondMomentTarget_311` | **OPEN** |
| Weighted pair autocorrelation expansion `WeightedPairAutocorrelationExpansion_312` | **STRUCTURAL / EXTRACTION** |
| Current autocorrelation route `CurrentAutocorrelationToolsClose_312` | **FALSE / BLOCKED** |
| Anti-diagonal two-shift gain `AntiDiagonalTwoShiftKernelGain_312` | **OPEN** |
| Fourteenth plan update `PlanUpdate_14_313` | **STRUCTURAL / EXTRACTION** |
| Direct anti-diagonal attack as next move `DirectAntiDiagonalAttack_313` | **FALSE / BLOCKED** |
| Minor-kernel row split `MinorKernelRowSplit_314` | **STRUCTURAL / EXTRACTION** |
| Independent row smallness route `IndependentRowSmallnessRoute_314` | **FALSE / BLOCKED** |
| Full/zero/major row controls from Module 314 | **OPEN** |
| Zero-mode product audit `ZeroModeProductAudit_315` | **STRUCTURAL / EXTRACTION** |
| Zero mode killed by minor convention `ZeroModeKilledByMinorConvention_315` | **FALSE / BLOCKED** |
| Current zero-mode product control `CurrentZeroModeProductControl_315` | **FALSE / BLOCKED** |
| Centered rewrite removes explicit zero row `CenteredRewriteRemovesExplicitZeroRow_315` | **STRUCTURAL / EXTRACTION** |
| Centered full anti-diagonal audit `CenteredFullAntiDiagonalAudit_316` | **STRUCTURAL / EXTRACTION** |
| Current centered full route `CurrentCenteredFullToolsClose_316` | **FALSE / BLOCKED** |
| Centered full column second moment `CenteredFullColumnSecondMomentTarget_316` | **OPEN** |
| Major-kernel correction audit `MajorKernelCorrectionAudit_317` | **STRUCTURAL / EXTRACTION** |
| Current major-correction route `CurrentMajorCorrectionToolsClose_317` | **FALSE / BLOCKED** |
| Major local-model transfer `MajorLocalModelTransfer_317` | **OPEN** |
| Signed minor-kernel verdict `SignedMinorKernelCombinationVerdict_318` | **STRUCTURAL / EXTRACTION** |
| Signed full-major identity `SignedFullMajorIdentity_318` | **STRUCTURAL / EXTRACTION** |
| Signed combination as smaller route `SignedCombinationAsSmallerRoute_318` | **FALSE / BLOCKED** |
| Signed minor-kernel gain `SignedMinorKernelGain_318` | **OPEN** |
| Anti-diagonal new-input inventory `AntiDiagonalNewInputInventory_319` | **STRUCTURAL / EXTRACTION** |
| Current inventory closes anti-diagonal `CurrentInventoryClosesAntiDiagonal_319` | **FALSE / BLOCKED** |
| Direct/data-dependent/eight-slot candidate inputs from Module 319 | **OPEN** |
| Size-sensitive minor-kernel criterion `SizeSensitiveMinorKernelCriterion_320` | **STRUCTURAL / EXTRACTION** |
| Conditional Phi criterion `PhiCriterion_320(Phi)` | **CONDITIONAL** |
| Current size-sensitive closure `CurrentSizeSensitiveClosure_320` | **FALSE / BLOCKED** |
| Admissible Phi gain `AdmissiblePhiGain_320` | **OPEN** |
| Data-dependent fiber gain audit `DataDependentFiberGainAudit_321` | **STRUCTURAL / EXTRACTION** |
| Current fiber caps force Phi gain `CurrentFiberCapsForcePhiGain_321` | **FALSE / BLOCKED** |
| Fiber overlap gain target `FiberOverlapGainTarget_321` | **OPEN** |
| Combined plan update/challenge `PlanUpdate_15_Challenge_9_322` | **STRUCTURAL / EXTRACTION** |
| Direct cap-only/fiber-only Phase K continuation `PhaseKColumnBranchContinue_322` | **FALSE / BLOCKED** |
| Direct fiber-overlap attack as next move `FiberOverlapDirectAttack_322` | **FALSE / BLOCKED** |
| Residual eight-slot minor pivot `ResidualEightSlotMinorPivot_322` | **STRUCTURAL / EXTRACTION** |
| Residual eight-slot minor expansion `ResidualEightSlotMinorExpansion_323` | **STRUCTURAL / EXTRACTION** |
| Eight-slot top-face identity `RawEightSlotTopFaceIdentity_323` | **STRUCTURAL / EXTRACTION** |
| Zero-mean lower-face identity `ZeroMeanLowerFaceIdentity_323` | **STRUCTURAL / EXTRACTION** |
| Fixed-kernel reading of localized rows `FixedKernelInterpretation_323(U,V)` | **FALSE / BLOCKED** |
| Eight-slot expansion closes minor gain `EightSlotExpansionClosesMinorGain_323` | **FALSE / BLOCKED** |
| Collision and diagonal strata audit `CollisionDiagonalStrataAudit_324` | **STRUCTURAL / EXTRACTION** |
| Slot-difference and structural diagonal catalogs from Module 324 | **STRUCTURAL / EXTRACTION** |
| Finite-prime collision load `FinitePrimeCollisionLoad_324` | **STRUCTURAL / EXTRACTION** |
| Current collision-strata closure `CurrentCollisionStrataClosure_324` | **FALSE / BLOCKED** |
| Generic-versus-collision local-model split `GenericCollisionLocalModelSplit_325` | **STRUCTURAL / EXTRACTION** |
| Generic local factor and collision-defect decomposition from Module 325 | **STRUCTURAL / EXTRACTION** |
| Structural diagonal, finite-prime load, overflow, data-dependent kernel-selection, generic noncollision, and local-model insertion rows from Module 325 | **OPEN** |
| Current generic/collision closure `CurrentGenericCollisionClosure_325` | **FALSE / BLOCKED** |
| Signed inclusion-exclusion minor audit `SignedInclusionExclusionMinorAudit_326` | **STRUCTURAL / EXTRACTION** |
| Top-Mobius, proper-support, and full generic zero identities from Module 326 | **STRUCTURAL / EXTRACTION** |
| Full-cover collision, stratified generic remainder, and signed local-model insertion rows from Module 326 | **OPEN** |
| Shortcut that signed inclusion-exclusion kills all collision defects | **FALSE / BLOCKED** |
| Current signed inclusion-exclusion closure `CurrentSignedIEClosure_326` | **FALSE / BLOCKED** |
| Full-cover cluster audit `FullCoverClusterAudit_327` | **STRUCTURAL / EXTRACTION** |
| Full-cover support, one-prime, multi-prime, structural cluster catalogs, and cover-load envelope from Module 327 | **STRUCTURAL / EXTRACTION** |
| Full-cover load smallness, rank uniformity, and kernel-weighted cover rows from Module 327 | **OPEN** |
| Current full-cover closure `CurrentFullCoverClosure_327` | **FALSE / BLOCKED** |
| Full-cover load criterion `FullCoverLoadCriterion_328` | **STRUCTURAL / EXTRACTION** |
| Finite-prime Mobius expansion and sharp cover functional from Module 328 | **STRUCTURAL / EXTRACTION** |
| Kernel-weighted sharp cover criterion from Module 328 | **CONDITIONAL** |
| Sharp cover smallness `SharpCoverSmallness_328` | **OPEN** |
| Crude cover load as exact coefficient, first-load, energy-only, and rank-only cover routes | **FALSE / BLOCKED** |
| Prime-partition Mobius audit `PrimePartitionMobiusAudit_329` | **STRUCTURAL / EXTRACTION** |
| Prime-partition defect formula, Mobius-degree bound, pair-block weights, singleton penalty, and one-prime power table from Module 329 | **STRUCTURAL / EXTRACTION** |
| Prime Mobius smallness, partition-class counting, and kernel-weighted Mobius-cover rows from Module 329 | **OPEN** |
| Current prime-Mobius closure `CurrentPrimeMobiusClosure_329` | **FALSE / BLOCKED** |
| Prime-partition cover-moment criterion `PrimePartitionCoverMomentCriterion_330` | **STRUCTURAL / EXTRACTION** |
| Mobius cover-moment functional `MobiusCoverMomentFunctional_330` | **STRUCTURAL / EXTRACTION** |
| Kernel-weighted Mobius moment criterion `KernelWeightedMobiusMomentCriterion_330` | **CONDITIONAL** |
| Partition counting, structural-rank, multi-prime, and finite-prime-tail rows from Module 330 | **OPEN** |
| Current rank-heuristic and cover-moment closures from Module 330 | **FALSE / BLOCKED** |
| Partition-class counting audit `PartitionClassCountingAudit_331` | **OPEN next target** |

For the live object-by-object ledger, read:

```text
docs/status/global_status.md
docs/status/theorem_status_index.md
docs/modules/dependency_graph.md
```

## Why So Many Modules?

This project has many tempting shortcuts. Some look plausible but are not
valid at the exact endpoint. Examples:

```text
ordinary pair-BDH does not automatically prove CPC_3^sharp;
first-moment Hardy-Littlewood does not prove RBDH;
fixed frequency-set estimates do not automatically control adaptive shells;
model or smoothed selector estimates do not automatically transfer to the
actual sharp moving selector;
Sigma_w(d,h) is not pointwise kappa_w(d)^2.
```

The modules exist to prevent those jumps. A module may define an object,
extract an identity, audit a route, or mark a shortcut blocked. That is
progress, but it is not the same thing as proving the endpoint.

## How To Read The Repository

Start here:

```text
README.md
docs/status/global_status.md
docs/status/theorem_status_index.md
docs/status/long_term_plan.md
docs/modules/modules_156_178_summary.md
```

Then read the newest module named in `docs/status/long_term_plan.md`.

For operating rules and forbidden upgrades:

```text
AGENTS.md
docs/status/forbidden_upgrades.md
docs/codex/continuation_protocol.md
```

## Repository Layout

```text
AGENTS.md                         Codex operating rules and status discipline
README.md                         This orientation page
CITATION.cff                      Citation metadata placeholder
LICENSE_PENDING.md                License decision placeholder

source_texts/                     Original large text artifacts
docs/
  status/                         Global status, theorem index, forbidden upgrades
  modules/                        Module chain, dependency graph, generated indexes
  reviews/                        Project-wide reviews and audits
  codex/                          Continuation protocol and prompts
papers/                           Paper outlines and theorem inventories
experiments/                      HEURISTIC experiment stubs
scripts/                          Lightweight audit and index scripts
```

## Continuation Rule

When continuing the project, do not try to prove the original theorem by
assertion. Continue from the latest module, preserve status labels, and run:

```text
python scripts/status_audit.py
python scripts/build_index.py
```

If modules changed, also run:

```text
python scripts/extract_modules.py docs/paper/Prime_Resonance_Gap_500_Page_Paper.txt docs/modules/generated_index.md
```

Most importantly:

```text
Do not call the original problem solved.
Do not assign endpoint status PROVEN unless a module supplies the proof.
Do not turn structural reductions into analytic estimates.
```

## Status Snapshot

This table is a reader-friendly snapshot of the main project statuses. If it
ever conflicts with `docs/status/global_status.md`, the global status file
wins.

| Object / Claim | Status | Short Meaning |
|---|---:|---|
| Original selected-average problem: exists irrational `alpha` with `A_alpha(x)->L0>1` | OPEN | Main problem; no construction or proof yet |
| All-alpha no-positive-limit theorem | OPEN | No theorem rules out positive limits for every irrational `alpha` |
| Metric theorem `A_alpha(x)->1` a.e. | PROVEN according to project ledger | Applies to Lebesgue-a.e. alpha, not all alpha |
| Finite-type no-positive-limit theorem | CONDITIONAL | Needs finite-type hypotheses and side packages |
| `s=2` rational-major endpoint | OPEN | Major analytic engine still missing |
| Residual derivative cube `ResCube_3^sharp` | OPEN | Central Fourier fourth-moment endpoint |
| `RBDH_pair_short(Hcal)` | OPEN | Endpoint-equivalent object, not available |
| `CPC_3^sharp(Hcal)` | OPEN | Endpoint-equivalent object, not available |
| `SPAC_2^sharp` | OPEN | Endpoint-equivalent object, not available |
| `SU2Pair_2^sharp` | OPEN | Endpoint-equivalent object, not available |
| `DyadicDerivativeU^2` | OPEN | Structural target; analytic estimate missing |
| `AU^3` | OPEN | Endpoint-equivalent object, not available |
| `WProjectedLocalMatch_3^major` | CONDITIONAL | Major-arc local-model schema only |
| `ProjectedMajorTarget_3^B` | OPEN | Needs local matching and model neutrality |
| `ProjectedModelNeutralityGate_260(P_adm)` | CONDITIONAL | Gate with open generic-tail, kernel, collision, and uniformity rows |
| `ProjectedModelNeutrality_3^major` | OPEN | Not proved by the gate |
| `CollNeutral_260(P_adm)` | OPEN | Absolute collision neutrality missing |
| `AbsCollStrataGate_264` | OPEN | Absolute collision-strata route missing |
| `SignedCoverGate_264` | OPEN | Signed full-cover route missing; not an absolute row |
| `KernelAbsBudget_265` | OPEN | Absolute kernel budget missing |
| `KernelSignedBudget_265` | OPEN | Signed kernel budget missing |
| `UniformityLedger_266(P_adm)` | OPEN | Same-family W-limit and parameter uniformity not proved |
| `NarrowMinorArc_3^B` | CONDITIONAL | Minor-arc criterion; needs all input rows |
| `MinorArcTransfer_3^B` | OPEN | Transfer from model/cyclic rows to target missing |
| `TransIncCore_269` | STRUCTURAL / EXTRACTION | Exact transverse graph identified |
| `TransIncBound_269` | OPEN | Non-tautological transverse bound missing |
| `ThresholdRemovalAudit_270` | STRUCTURAL / EXTRACTION | Threshold tension identified |
| `ThresholdOnlyClosure_270` | OPEN | Moment-and-threshold closure missing |
| `TransPhaseExpansion_271` | STRUCTURAL / EXTRACTION | Exact phase kernels expanded |
| `PhaseIncidenceGate_271` | OPEN | Same-family restricted phase-kernel estimate missing |
| `PhaseToolCompatAudit_272` | STRUCTURAL / EXTRACTION | Standard tools audited |
| `AvailableToolClosure_272` | OPEN | No listed off-the-shelf tool closes the phase gate |
| `TransverseIncidenceGate_273` | STRUCTURAL / EXTRACTION | Candidate gate, not a usable proof input |
| `PhaseKernelBound_273` | OPEN | Shell graph-restriction bound missing |
| `TransGateCompatAudit_274` | STRUCTURAL / EXTRACTION | Side-row requirements named |
| `TransGateSideRows_274` | OPEN | W-limit, cutoff, boundary, selector, and dyadic rows missing |
| `TransDegeneracyAudit_275` | STRUCTURAL / EXTRACTION | Degeneracies routed |
| `DegFreePhaseGate_275` | OPEN | Genuine nondegenerate transverse remainder missing |
| `TransverseGateVerdict_276` | STRUCTURAL / EXTRACTION | Phase I classified as mixed/conditional |
| `TransverseGateProofPkg_276` | OPEN | Full transverse proof package missing |
| `PlanUpdate_10_277 / PlanChallenge_6_277` | STRUCTURAL / EXTRACTION | Governance update; Phase J selected |
| `MinimalTransverseFamily_278(P_minor^0)` | STRUCTURAL / EXTRACTION | Minimal W-cyclic model family fixed |
| `XiDualPhaseExpansion_279(P_minor^0)` | STRUCTURAL / EXTRACTION | `Xi_273^0` expanded exactly |
| `FixedSetShellAudit_280(P_minor^0)` | STRUCTURAL / EXTRACTION | Automatic fixed-set to shell transfer blocked |
| `FixedSetShellTransfer_280` | OPEN | Needs uniform fiber, selection, or direct shell theorem |
| `UniformFiberBound_280` | OPEN | Adaptive-fiber uniform estimate missing |
| `SelectionTransfer_280` | OPEN | Fixed-set-to-shell selection theorem missing |
| `DirectShellBound_280` | OPEN | Direct estimate for `X_J(omega)` missing |
| `LSBesselBenchmark_281(P_minor^0)` | STRUCTURAL / EXTRACTION | Bessel/large-sieve benchmark performed |
| `LargeSieveBesselClosure_281` | OPEN | Benchmark does not close the shell target |
| `AdaptiveBesselGain_281` | OPEN | No adaptive Bessel gain beyond row/column ceilings |
| `DegRowsP0Audit_282(P_minor^0)` | STRUCTURAL / EXTRACTION | Degeneracy rows classified inside the minimal family |
| `BoundaryCutoff_282 / WPP_282 / Selector_282` | STRUCTURAL / EXTRACTION | Zero only by internal `P_minor^0` convention, not target transfer |
| `DegRowsP0Small_282` | OPEN | Lambda-summed smallness of routed local degeneracies missing |
| `MajorDiffBound_282` | OPEN | Major-like relations among minor frequencies not controlled |
| `PhysDiagLocal_282` | OPEN | Same-family physical-diagonal shifted-correlation row missing |
| `DegFreePhaseGate_282` | OPEN | Deg-free shell phase estimate missing |
| `SideRowsP0Audit_283(P_minor^0)` | STRUCTURAL / EXTRACTION | Minimum side rows classified inside the fixed local family |
| `BoundaryConventionP0_283 / ResidueConventionP0_283 / SelectorConventionP0_283` | STRUCTURAL / EXTRACTION | Zero only as internal `P_minor^0` conventions, not export rows |
| `SideRowsP0Ready_283` | OPEN | W-uniformity, threshold/removal, dyadic, and adaptive-shell rows still missing |
| `WUniformP0_283` | OPEN | Same two-stage W-limit uniformity not proved for the shell estimate |
| `ThresholdBudgetP0_283` | OPEN | Threshold schedules not shown compatible with final lambda-summed target |
| `LowLevelCutoffP0_283` | OPEN outside the local fourth-moment tail | Module 297 closes only the P_minor^0 fourth-moment low-level piece |
| `DyadicUniformityP0_283` | OPEN | Uniformity over D, lambda, sigma, R, eta, W, and both signs of d missing |
| `ShellSelectionP0_283` | OPEN | Adaptive data-dependent shell control not supplied by fixed-set estimates |
| `ThresholdBudgetP0Audit_284(P_minor^0)` | STRUCTURAL / EXTRACTION | Exact threshold budget barriers named inside the local family |
| `ThresholdBudgetP0Closure_284(q,r)` | OPEN | Still requires removal, row/column, shell-counting, and compatibility budgets to be `o_W(1)` |
| `RowBarrierP0_284 / ColumnBarrierP0_284 / SigmaColumnBarrierP0_284` | OPEN | Optimized barriers are diagnostics, not estimates |
| `AdaptiveShellVerdict_285(P_minor^0)` | STRUCTURAL / EXTRACTION | Current Phase J adaptive-shell package classified |
| `CurrentToolsCloseP0_285` | FALSE / BLOCKED | Current fixed-set, Bessel, threshold, side-row, and degeneracy tools do not prove `PhaseKernelBound_273^0` |
| `AdaptiveShellGainP0_285` | OPEN | Would require a new uniform-fiber, selection-transfer, or direct-shell theorem with compatible losses |
| `PlanUpdate_11_286` | STRUCTURAL / EXTRACTION | Phase J paused as current-tool blocked; Phase K selected |
| `PhaseK_AdaptiveShellTriage` | STRUCTURAL / EXTRACTION | New-input triage, not an analytic estimate |
| `DirectShellTTStarAudit_287(P_minor^0)` | STRUCTURAL / EXTRACTION | Direct-shell `TT*` cross terms routed and shortcuts blocked |
| `DirectShellCrossTermGain_287` | OPEN | Uniform cross-term gain for adversarial `omega` and data-dependent `J` missing |
| `DirectShellTTStarClosure_287` | OPEN | Would require cross-term gain plus side, degeneracy, and threshold rows |
| `SelectionComplexityAudit_288(P_minor^0)` | STRUCTURAL / EXTRACTION | Adaptive shell selection complexity audited |
| `SelectionComplexityGain_288` | OPEN | No entropy, stopping-time, sparse, or VC theorem supplied for `S_d(J)` |
| Raw union selection for `S_d(J)` | FALSE / BLOCKED | Selection class too large for harmless logarithmic loss |
| `UniformFiberStress_289(P_minor^0)` | STRUCTURAL / EXTRACTION | Uniform-fiber route stress-tested over row/column shells |
| `RowColumnOnlyUniformFiberGain_289` | FALSE / BLOCKED | Row/column data alone reproduce deterministic ceilings |
| `WeightedRCSubgraphGain_289(P_minor^0)` | OPEN | Would need structured residual Fourier control of weighted row/column subgraphs |
| `PhaseKAdaptiveShellVerdict_290(P_minor^0)` | STRUCTURAL / EXTRACTION | Phase K current closure verdict recorded |
| `PhaseKCurrentClosure_290` | FALSE / BLOCKED | Direct-shell, selection, and uniform-fiber Phase K tests do not prove `AdaptiveShellGainP0_285` |
| `PhaseKStatusCleanup_291(P_minor^0)` | STRUCTURAL / EXTRACTION | Phase K status map cleaned and Module 292 challenge packet prepared |
| `ContinuePhaseKWithoutNewInput_291` | FALSE / BLOCKED | Repeating the same Phase K tests cannot prove `AdaptiveShellGainP0_285` |
| `ChallengePacket_291` | STRUCTURAL / EXTRACTION | Decision packet for the seventh plan challenge |
| `PlanChallenge_7_292` | STRUCTURAL / EXTRACTION | Seventh plan challenge completed using `ChallengePacket_291` |
| `ChallengeDecision_292` | STRUCTURAL / EXTRACTION | Selects OptionD: side-package triage |
| `AdaptiveGainFirst_292` | FALSE / BLOCKED | Next move should not be another adaptive-shell gain attempt without a new input |
| `SidePkgTriage_293(P_minor^0)` | STRUCTURAL / EXTRACTION | Side package split into convention, uniformity, threshold, degeneracy, and adaptive-core rows |
| `SidePkgReady_293` | OPEN | Side package still not proved after triage |
| `ShellSelectionAsSideRow_293` | FALSE / BLOCKED | Shell selection is adaptive-core, not harmless side bookkeeping |
| `DegFreeAsSideRow_293` | FALSE / BLOCKED | Deg-free phase gate is core phase work, not side bookkeeping |
| `LowLevelBudgetTriage_294(P_minor^0)` | STRUCTURAL / EXTRACTION | Below-`lambda_min` leakage classified; no smallness proved |
| `LowLevelBudgetP0_284 / LowLevelCutoffP0_283` | OPEN outside the local fourth-moment tail | The P_minor^0 fourth-moment low-level piece is closed, but export or alternate reconstructions are not |
| `LowLevelCountingBarrier_294` | OPEN | Deterministic counting criterion not proved `o_W(1)` |
| `LowLevelByDefinition_294` | FALSE / BLOCKED | Excluding low levels from the shell grid is not an estimate |
| `PlanUpdate_12_295` | STRUCTURAL / EXTRACTION | Twelfth plan update; selects the next low-level counting audit |
| `LowLevelCountingBarrierAudit_296(P_minor^0)` | STRUCTURAL / EXTRACTION | Pure counting audited; energy-tail target extracted |
| `PureCountingLowLevelClosure_296` | FALSE / BLOCKED | Counting barrier not small from current P_minor^0 data |
| `LowLevelEnergyTailCriterion_296` | STRUCTURAL / EXTRACTION | `M_low,0 <= lambda_min^2 E2_minor^0` |
| `LowLevelEnergyTailTarget_296(P_minor^0)` | PROVEN inside P_minor^0 | Trivial log envelope plus Parseval gives `(A_N^0)^2 N^{-2 kappa_lambda}E2_minor^0=o_W(1)` |
| `E2MinorEnergyTailAudit_297(P_minor^0)` | STRUCTURAL / EXTRACTION | Local second-energy tail audit completed |
| `LowLevelFourthMomentTailP0_297` | PROVEN inside P_minor^0 | `M_low,0=o_W(1)` for the local fourth-moment low-level piece |
| `ShiftFreqRemovalAudit_298(P_minor^0)` | STRUCTURAL / EXTRACTION | Separates vacuous local removal from useful threshold closure |
| `VacuousActualRemovalP0_298` | PROVEN inside P_minor^0 | Empty bad-shift/frequency sets for maximal local thresholds only |
| `VacuousRemovalAsThresholdClosure_298` | FALSE / BLOCKED | Maximal thresholds do not make row/column shell budgets small |
| `ShiftRemovalBudget_284(q) / FreqRemovalBudget_284(r)` | OPEN | Useful moment-budget rows still missing |
| `ThresholdCompatibleRemovalSchedule_298` | OPEN | Need one non-vacuous schedule compatible with removals and shell budgets |
| `ThresholdWindowCompatibilityAudit_299(P_minor^0)` | STRUCTURAL / EXTRACTION | Continuous row/column window criteria extracted |
| `ContinuousRowWindowCriterion_299(q) / ContinuousColumnWindowCriterion_299(r)` | STRUCTURAL / EXTRACTION | Optimization identities only, not analytic estimates |
| `CurrentTrivialWindowRoute_299` | FALSE / BLOCKED | Trivial caps reproduce row/column ceiling scale and do not prove barrier smallness |
| `ThresholdWindowClosure_299(q,r)` | OPEN | Needs barrier smallness plus integer/range and uniform schedule rows |
| `BarrierSmallnessPackage_299(q,r)` | OPEN | Requires row barrier and at least one column barrier to be `o_W(1)` |
| `RowBarrierMomentAudit_300(P_minor^0)` | STRUCTURAL / EXTRACTION | Current energy-only inputs tested against the row barrier |
| `EnergyOnlyRowBarrierBound_300(q)` | STRUCTURAL / EXTRACTION | Gives only a polylogarithmic ceiling, not smallness |
| `CurrentRowBarrierRoute_300(q)` | FALSE / BLOCKED | Pointwise envelope plus Parseval plus low-level tail do not force `RowBarrierP0_284(q)=o_W(1)` |
| `LowLevelTailToRowBarrier_300` | FALSE / BLOCKED | Module 297 controls below-threshold tail only, not high-level row distribution |
| `RowMomentGainTarget_300(q)` | OPEN | Needs same-family row-energy distribution or high-moment gain |
| `Reflective_4` | STRUCTURAL / EXTRACTION | Memory log for Modules 261-300; no theorem upgrade |
| `RowMomentDistributionAudit_302(P_minor^0)` | STRUCTURAL / EXTRACTION | Row-distribution route audited; no row-barrier smallness proved |
| `LayerCakeRowCriterion_302(q)` | STRUCTURAL / EXTRACTION | Exact criterion only, not an estimate |
| `CurrentMarkovRowDistribution_302(q)` | FALSE / BLOCKED | Markov reproduces the Module 300 ceiling |
| `EndpointFourthMomentRowRoute_302` | FALSE / BLOCKED | Circular unless an independent non-endpoint fourth-moment theorem is supplied |
| `RowTailGainTarget_302(q)` | OPEN | Needs a same-family tail gain beating first-energy Markov |
| `RowSquareMomentTarget_302` | OPEN | Concrete q=2 high-moment row target |
| `RowSquareMomentExpansion_303(P_minor^0)` | STRUCTURAL / EXTRACTION | q=2 row-square object expanded exactly; no gain proved |
| `RowSquareKernelIdentity_303(lambda_j)` | STRUCTURAL / EXTRACTION | Exact same-shift restricted-kernel identity |
| `DiagonalFourthPowerRow_303(lambda_j)` | STRUCTURAL / EXTRACTION | Diagonal row identified; current proof routes blocked |
| `OffDiagonalSameShiftRow_303(lambda_j)` | OPEN | Needs same-shift restricted-kernel control |
| `FullFrequencyShortcut_303` | FALSE / BLOCKED | Restricted data-dependent fibers are not full frequency sets |
| `FixedFiberShortcut_303` | FALSE / BLOCKED | Fixed-set estimates need uniformity or selection transfer |
| `EndpointFourthMomentShortcut_303` | FALSE / BLOCKED | Circular and does not control the off-diagonal row alone |
| `SameShiftSquareKernelGain_303(P_minor^0)` | OPEN | New q=2 row-square kernel target |
| `PlanUpdate_13_304` | STRUCTURAL / EXTRACTION | Thirteenth plan update; selects fixed-fiber benchmark first |
| `FixedFiberRowSquareBenchmark_305(P_minor^0)` | STRUCTURAL / EXTRACTION | Prescribed-fiber benchmark completed; no gain proved |
| `FixedFiberKernelIdentity_305(U)` | STRUCTURAL / EXTRACTION | Exact fixed-fiber same-shift kernel identity |
| `FixedFiberParsevalCeiling_305(U)` | STRUCTURAL / EXTRACTION | Valid ceiling, not row-barrier smallness |
| `FixedFiberSizeCriterion_305(U)` | STRUCTURAL / EXTRACTION | Conditional size/loss criterion only |
| `CurrentToolsFixedFiberGain_305` | FALSE / BLOCKED | Current Parseval/Bessel tools recover ceilings only |
| `FullFrequencyFixedFiberDiagnostic_305` | FALSE / BLOCKED | Full-frequency diagnostic is not the restricted target |
| `FixedFiberRowSquareGain_305(P_minor^0)` | OPEN | New fixed-fiber same-shift estimate would be needed |
| `FixedFiberBlockedVerdict_306(P_minor^0)` | STRUCTURAL / EXTRACTION | Current fixed-fiber route classified before challenge |
| `SelectionTransferNext_306` | FALSE / BLOCKED | No fixed-fiber gain exists to transfer |
| `CurrentFixedFiberRoute_306` | FALSE / BLOCKED | Current toolkit gives only ceilings |
| `SizeSensitiveSubcriterion_306(M_U,E2_U)` | STRUCTURAL / EXTRACTION | Criterion only, not verified |
| `SizeSensitiveClosure_306` | OPEN | Needs actual prescribed-fiber size/energy package |
| `PauseRowSquareBranch_306` | CONDITIONAL / STEERING | Pause unless challenge selects a new input |
| `PlanChallenge_8_307` | STRUCTURAL / EXTRACTION | Eighth plan challenge completed; selects the column audit |
| `ChallengeDecision_307` | STRUCTURAL / EXTRACTION | Column-barrier moment audit selected as next local test |
| `RowSquareContinue_307` | FALSE / BLOCKED | Direct row-square continuation blocked as the next move under current tools |
| `ColumnBarrierMomentAudit_308(P_minor^0)` | STRUCTURAL / EXTRACTION | Column barriers audited; first-incidence inputs give ceilings only |
| `ColumnIncidenceFirstMoment_308(lambda_j)` | STRUCTURAL / EXTRACTION | Incidence bound for `MultMomentP0_284(r;lambda_j)` |
| `EnergyIncidenceColumnCeiling_308 / SigmaEnergyIncidenceCeiling_308` | STRUCTURAL / EXTRACTION | Valid ceilings retain an uncontrolled `(m_minor^0)^theta_r` factor |
| `CurrentColumnBarrierRoute_308(r)` | FALSE / BLOCKED | Current local tools do not prove either column barrier small |
| `LowLevelTailToColumnBarrier_308 / VacuousRemovalToColumnBarrier_308` | FALSE / BLOCKED | Low-level tail and maximal removal do not control high-level multiplicities |
| `ColumnMultiplicityGainTarget_308(r)` | OPEN | Needs a same-family high-multiplicity distribution gain |
| `ColumnMultiplicityDistributionAudit_309(P_minor^0)` | STRUCTURAL / EXTRACTION | Layer-cake distribution audit completed |
| `ColumnLayerCakeIdentity_309(lambda_j)` | STRUCTURAL / EXTRACTION | Exact identity for column multiplicity moments |
| `FirstMomentColumnTailBound_309(lambda_j,T)` | STRUCTURAL / EXTRACTION | Markov tail from first incidence only |
| `FirstMomentLayerCakeCollapse_309(r)` | FALSE / BLOCKED | First-moment layer-cake reproduces the Module 308 ceiling |
| `ColumnTailGainCriterion_309(r;U)` | STRUCTURAL / EXTRACTION | Criterion only, not a proved tail theorem |
| `ColumnTailGainTarget_309(r)` | OPEN | Needs high-multiplicity tail decay beyond first incidence |
| `ColumnPairMultiplicityExpansion_310(P_minor^0)` | STRUCTURAL / EXTRACTION | Concrete r=2 column moment expanded into same-frequency shift pairs |
| `ColumnPairIdentity_310(lambda_j)` | STRUCTURAL / EXTRACTION | Exact pair identity for `MultMomentP0_284(2;lambda_j)` |
| `ColumnDiagonalPair_310(lambda_j)` | STRUCTURAL / EXTRACTION | Diagonal shift-pair row isolated and first-energy controlled |
| `OffDiagonalSameFrequencyPair_310(lambda_j)` | OPEN | Same-frequency large-spectrum shift-pair incidence missing |
| `FirstIncidencePairCollapse_310(lambda_j)` | FALSE / BLOCKED | Pair route collapses to Module 308 ceiling under first incidence |
| `WeightedPairEnergyCriterion_310(lambda_j)` | STRUCTURAL / EXTRACTION | Threshold-to-weighted-coefficient-pair criterion only |
| `WeightedColumnPairEnergyTarget_310(P_minor^0)` | OPEN | Needs same-family weighted off-diagonal pair energy gain |
| `WeightedColumnPairEnergyAudit_311(P_minor^0)` | STRUCTURAL / EXTRACTION | Weighted route audited; current tools give ceilings |
| `EnergySquareWPairCeiling_311 / FourthPowerWPairCeiling_311` | STRUCTURAL / EXTRACTION | Valid energy-square and fourth-power ceilings only |
| `WeightedCurrentToolsClose_311` | FALSE / BLOCKED | Current Parseval/Cauchy inputs do not close weighted pair energy |
| `WeightedColumnSecondMomentTarget_311(P_minor^0)` | OPEN | Needs distribution control of weighted columns `sum_d |beta_0(d,xi)|^2` |
| `WeightedPairAutocorrelationExpansion_312(P_minor^0)` | STRUCTURAL / EXTRACTION | Exact anti-diagonal two-shift autocorrelation expansion |
| `SameFrequencyAutocorrelationIdentity_312 / MinorKernelDecomposition_312` | STRUCTURAL / EXTRACTION | Exact identities only; not cancellation |
| `CurrentAutocorrelationToolsClose_312` | FALSE / BLOCKED | Full-frequency, absolute-kernel, and Cauchy/Parseval routes do not close weighted pair energy |
| `AntiDiagonalTwoShiftKernelGain_312(P_minor^0)` | OPEN | Needs same-family two-shift kernel gain after threshold weights |
| `PlanUpdate_14_313` | STRUCTURAL / EXTRACTION | Fourteenth plan update completed; selects row split before direct attack |
| `DirectAntiDiagonalAttack_313` | FALSE / BLOCKED | Bundled target is too broad as the next move under current tools |
| `MinorKernelRowSplit_314(P_minor^0)` | STRUCTURAL / EXTRACTION | Exact split into full-frequency, zero-mode, and major-correction rows |
| `FullAntiDiagonalRowIdentity_314 / ZeroModeProductIdentity_314 / MajorKernelCorrectionIdentity_314` | STRUCTURAL / EXTRACTION | Exact row identities only |
| `IndependentRowSmallnessRoute_314` | FALSE / BLOCKED | Current tools do not make the rows independently harmless |
| `FullAntiDiagonalControl_314 / ZeroModeProductControl_314 / MajorKernelCorrectionControl_314` | OPEN | Row control remains missing |
| `SignedMinorKernelCombinationTarget_314(P_minor^0)` | OPEN | Needs same-family control of the signed row combination |
| `ZeroModeProductAudit_315(P_minor^0)` | STRUCTURAL / EXTRACTION | Audits zero-mode row; exact centered rewrite removes explicit zero row |
| `ZeroModeKilledByMinorConvention_315` | FALSE / BLOCKED | Minor arcs exclude zero frequency but do not force `beta_0(d,0)=0` |
| `ZeroModeProductIdentity_315 / CenteredRewriteRemovesExplicitZeroRow_315` | STRUCTURAL / EXTRACTION | Exact identities only; no zero-mode estimate follows |
| `CurrentZeroModeProductControl_315` | FALSE / BLOCKED | No available same-family estimate controls the standalone zero row |
| `CenteredFullAntiDiagonalAudit_316(P_minor^0)` | STRUCTURAL / EXTRACTION | Centered full row audited; full nonzero-frequency column second moment remains open |
| `CurrentCenteredFullToolsClose_316` | FALSE / BLOCKED | Cauchy, Parseval, energy-square, and fourth-power routes need unavailable same-family full-column estimates |
| `CenteredFullAntiDiagonalControl_316 / CenteredFullColumnSecondMomentTarget_316` | OPEN | Same-family full nonzero-frequency column control missing |
| `MajorKernelCorrectionAudit_317(P_minor^0)` | STRUCTURAL / EXTRACTION | Major correction audited as a positive major-frequency pair-energy row |
| `CurrentMajorCorrectionToolsClose_317` | FALSE / BLOCKED | Positivity, cardinality, pair-BDH, first-moment, and projected-major shortcuts do not close the row |
| `MajorLocalModelTransfer_317(P_minor^0)` | OPEN | Exact residual eight-slot major model in the same local family missing |
| `SignedMinorKernelCombinationVerdict_318(P_minor^0)` | STRUCTURAL / EXTRACTION | Centered full-minus-major is exactly `WOff_311`; split is diagnostic without a new signed theorem |
| `SignedCombinationAsSmallerRoute_318` | FALSE / BLOCKED | The split alone is not a smaller proof route |
| `SignedMinorKernelGain_318(P_minor^0)` | OPEN | Same-family signed minor-kernel theorem missing |
| `AntiDiagonalNewInputInventory_319(P_minor^0)` | STRUCTURAL / EXTRACTION | Candidate inputs filtered; endpoint assumptions and current ceilings rejected |
| `CurrentInventoryClosesAntiDiagonal_319` | FALSE / BLOCKED | No proved candidate input closes `WOff_311` |
| `ResidualEightSlotMinorCancellation_319(P_minor^0)` | OPEN | Genuine but unproved candidate input |
| `SizeSensitiveMinorKernelCriterion_320(P_minor^0)` | STRUCTURAL / EXTRACTION | Cross-shell Phi criterion formulated; deterministic closure blocked |
| `PhiCriterion_320(Phi)` | CONDITIONAL | Usable only if an admissible same-family Phi is independently proved |
| `AdmissiblePhiGain_320(P_minor^0)` | OPEN | Needed fiber-overlap or entropy gain missing |
| `DataDependentFiberGainAudit_321(P_minor^0)` | STRUCTURAL / EXTRACTION | Current caps and selection rules audited for fiber-overlap gain |
| `CurrentFiberCapsForcePhiGain_321 / SelectionRuleGivesIndependence_321` | FALSE / BLOCKED | Current data do not force overlap gain or independence |
| `FiberOverlapGainTarget_321(P_minor^0)` | OPEN | Needs same-family overlap/entropy theorem beating complete-concentration ceilings |
| `PlanUpdate_15_Challenge_9_322` | STRUCTURAL / EXTRACTION | Combined plan update/challenge completed after fiber-gain blockage |
| `PhaseKColumnBranchContinue_322 / FiberOverlapDirectAttack_322` | FALSE / BLOCKED | Direct cap-only/fiber-only continuation is blocked as the next move under current inputs |
| `ResidualEightSlotMinorPivot_322(P_minor^0)` | STRUCTURAL / EXTRACTION | Selects residual eight-slot minor expansion as the next extraction-only audit |
| `ResidualEightSlotMinorExpansion_323(P_minor^0)` | STRUCTURAL / EXTRACTION | Exact eight-slot residual top face extracted; no cancellation proved |
| `ThresholdLocalizedKernelIdentity_323(U,V)` | STRUCTURAL / EXTRACTION | Cross-shell masks are kept inside a localized nonzero-frequency kernel |
| `FixedKernelInterpretation_323(U,V)` | FALSE / BLOCKED | Data-dependent shell masks cannot be treated as a fixed external kernel |
| `CollisionDiagonalStrataAudit_324(P_minor^0)` | STRUCTURAL / EXTRACTION | Internal/cross-block diagonals, collision load, and kernel anti-diagonal cataloged |
| `CurrentCollisionStrataClosure_324` | FALSE / BLOCKED | Cataloging strata does not prove weighted collision smallness |
| `GenericCollisionLocalModelSplit_325(P_minor^0)` | STRUCTURAL / EXTRACTION | Generic/collision local-model split formulated; no smallness proved |
| `GenericMinorLocalFactor_325 / CollisionDefectDecomposition_325` | STRUCTURAL / EXTRACTION | Exact local factors and defect partition only |
| `StructuralDiagonalRows_325 / FinitePrimeCollisionLoadRows_325 / OverflowRows_325` | OPEN | Analytic collision and high-load estimates missing |
| `DataDependentKernelSelectionRows_325 / GenericNoncollisionRow_325 / LocalModelInsertion_325` | OPEN | Data-dependent masks, generic contribution, and model insertion not proved |
| `CurrentGenericCollisionClosure_325` | FALSE / BLOCKED | The split does not close the minor row |
| `SignedInclusionExclusionMinorAudit_326(P_minor^0)` | STRUCTURAL / EXTRACTION | Exact top-Mobius/proper-support audit; no analytic closure |
| `SubsetMobiusIdentity_326 / ProperSupportCancellation_326` | STRUCTURAL / EXTRACTION | Signed subset sum extracts the full eight-label coefficient and kills proper-support terms |
| `FullGenericMinorZeroIdentity_326` | STRUCTURAL / EXTRACTION | Unrestricted cyclic nonzero-frequency minor kernel kills the full size-only generic row |
| `FullCoverCollisionRows_326 / StratifiedGenericRemainderRows_326 / SignedLocalModelInsertion_326` | OPEN | Surviving full-cover, restricted generic, and model-insertion rows remain unproved |
| `SignedIECancelsAllCollisionDefects_326 / CurrentSignedIEClosure_326` | FALSE / BLOCKED | Inclusion-exclusion alone does not close collision defects or the minor row |
| `FullCoverClusterAudit_327(P_minor^0)` | STRUCTURAL / EXTRACTION | Classifies full-cover cluster families that survive signed inclusion-exclusion |
| `FullCoverSupportCriterion_327 / OnePrimeFullCoverCatalog_327 / MultiPrimeCoverProductCatalog_327` | STRUCTURAL / EXTRACTION | Support criterion and one-prime/multi-event cover catalogs only |
| `StructuralFullCoverClusterCatalog_327 / FullCoverLoadEnvelope_327` | STRUCTURAL / EXTRACTION | Structural cover clusters and a diagnostic cover-load envelope only |
| `FullCoverLoadSmallness_327 / FullCoverRankUniformity_327 / KernelWeightedCoverRows_327` | OPEN | Kernel-weighted cover estimates and rank/uniformity remain missing |
| `CurrentFullCoverClosure_327` | FALSE / BLOCKED | Full-cover catalogs do not prove cover smallness |
| `FullCoverLoadCriterion_328(P_minor^0)` | STRUCTURAL / EXTRACTION | Replaces the crude cover-load reading with a prime-local Mobius sharp-cover criterion |
| `FinitePrimeMobiusExpansion_328 / SharpCoverFunctional_328` | STRUCTURAL / EXTRACTION | Finite-cutoff Mobius expansion and sharp cover envelope only |
| `KernelWeightedSharpCoverCriterion_328` | CONDITIONAL | Usable only if the same-family kernel-weighted sharp cover estimate is proved |
| `SharpCoverSmallness_328` | OPEN | Needed kernel-weighted sharp-cover smallness remains missing |
| `CrudeCoverLoadAsExactCoefficient_328 / FirstLoadCoverRoute_328 / EnergyOnlyCoverRoute_328 / RankOnlyCoverRoute_328` | FALSE / BLOCKED | Current crude-load, first-load, energy-only, and rank-only routes do not close the cover row |
| `PrimePartitionMobiusAudit_329(P_minor^0)` | STRUCTURAL / EXTRACTION | Computes prime-local Mobius weights by partition shape; no averaging follows |
| `PrimePartitionDefectFormula_329 / MobiusDegreeBound_329` | STRUCTURAL / EXTRACTION | Gives `delta_{p,S}=e_p(S)/(p-|S|)` and `mu_p(T)<=C_8 p^{-(1+|T|-b_max)}` |
| `PairBlockWeight_329 / SingletonAppendagePenalty_329 / OnePrimeFullCoverPowerTable_329` | STRUCTURAL / EXTRACTION | Pointwise examples and one-prime full-cover power table only |
| `PrimeMobiusSmallness_329 / PartitionClassCounting_329 / KernelWeightedMobiusCoverRows_329` | OPEN | Counting, kernel-weighted estimates, and tails remain missing |
| `CurrentPrimeMobiusClosure_329` | FALSE / BLOCKED | Prime-local Mobius algebra does not close the cover row |
| `PrimePartitionCoverMomentCriterion_330(P_minor^0)` | STRUCTURAL / EXTRACTION | Defines the finite-cutoff kernel-weighted Mobius cover-moment criterion |
| `MobiusCoverMomentFunctional_330` | STRUCTURAL / EXTRACTION | Envelope from pointwise Mobius-degree bounds; not an estimate |
| `KernelWeightedMobiusMomentCriterion_330` | CONDITIONAL | Usable only if proved in the same `P_minor^0` family with tails and masks |
| `PartitionClassCountingRows_330 / StructuralRankUniformityRows_330 / MultiPrimeCoverMomentRows_330 / FinitePrimeTailRows_330` | OPEN | Counting, rank, CRT/uniformity, and tail rows remain missing |
| `CurrentRankHeuristicClosure_330 / CurrentCoverMomentClosure_330` | FALSE / BLOCKED | Rank heuristics and the finite functional do not prove cover smallness |
| `PartitionClassCountingAudit_331(P_minor^0)` | OPEN | Next target |
| Automatic fixed-set theorem `=> PhaseKernelBound_273^0` | FALSE / BLOCKED | Data-dependent shell selection is not automatic |
| Large sieve for one fixed frequency set `=> Xi_273^0` | FALSE / BLOCKED | Fixed-set-only diagnostic, not the adaptive shell estimate |
| First-moment HL `=> RBDH` | FALSE / BLOCKED | Mean local density is not endpoint variance control |
| Ordinary pair-BDH `=> CPC_3^sharp` | FALSE / BLOCKED | Missing residual, rectangle, and endpoint-strength rows |
| Pointwise replacement of `Sigma_w(d,h)` by `kappa_w(d)^2` | FALSE / BLOCKED | Exact rectangle local factor is different |
| Model/smoothed/frozen selector estimate `=>` actual sharp moving selector | FALSE / BLOCKED | Requires named selector-transfer theorem |
