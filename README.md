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
data-dependent shells.

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

The current active phase is **Phase J: minimal transverse proof-package
feasibility**.

Current frontier:

```text
Latest module frontier: Module 280
Active phase: Phase J, minimal transverse proof-package feasibility
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
```

The next planned module is:

```text
Module 281:
  benchmark large-sieve or Bessel-type estimates against Xi_273^0.
```

The benchmark must decide whether a candidate estimate is one of:

```text
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
fixed-set-only diagnostic,
or endpoint-strength / blocked.
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
