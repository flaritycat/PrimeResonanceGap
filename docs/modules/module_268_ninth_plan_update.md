# Module 268: Ninth plan update after the Phase H verdict

## 1. Precise theorem / claim being advanced

This module performs the ninth 9-iteration plan update required by the
long-term schedule.

Define:

```text
PlanUpdate_9_268.
```

The update records the result of the Phase H projected model-neutrality
window and chooses the next branch.

The decision is:

```text
Pause Phase H as a conditional dependency map.
Begin Phase I: minor-arc transverse-incidence feasibility window.
```

The immediate next action is:

```text
Module 269:
  extract the exact transverse-incidence object inside NarrowMinorArc_3^B.
```

The reason for the decision is that Module 267 left model neutrality with two
conditional routes but no analytic closure:

```text
absolute route:
  AbsPMNGate_267
    => ProjectedModelNeutralityGate_260
    => ProjectedModelNeutrality_3^major,

signed exact-model route:
  SignedExactNeutralGate_267
    => ExactModelNeutral_260
    => ProjectedModelNeutrality_3^major,
  but not CollNeutral_260.
```

Continuing immediately to full projected-major matching would stack the open
model-neutrality rows on top of open local-model matching. Returning to the
minor-arc transverse-incidence obstruction tests a different bottleneck
already isolated in Modules 203, 204, and 257.

This plan update does not prove any analytic estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a schedule and branch-decision module. It changes the working plan
but does not upgrade any theorem status.

## 3. Definitions and variables

The cadence counters before this module are:

```text
Latest completed module: 267
Post-Reflective_1 solving count: 86
Long-term-plan count: 80
```

This module advances them to:

```text
Latest completed module: 268
Post-Reflective_1 solving count: 87
Long-term-plan count: 81
```

The cadence arithmetic is:

```text
81 is divisible by 9,
81 is not divisible by 15,
87 is not the next reflection threshold.
```

Therefore:

```text
ninth plan update is due,
sixth plan challenge is not due until count 90,
next reflective log remains expected around Module 301.
```

The Phase H endpoint of the previous window is:

```text
ProjectedModelNeutralityVerdict_267(P_adm).
```

The minor-arc package to reenter is:

```text
NarrowMinorArc_3^B(D;R,eta)
  => M_minor(D;R,eta)=o(1),
```

where:

```text
M_minor(D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)}
        |widehat{B_d}(xi)|^4.
```

For:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
```

Module 203 decomposed the large-spectrum incidences:

```text
I_lambda
  = I_shift(lambda)
    disjoint union I_freq(lambda)
    disjoint union I_trans(lambda).
```

The next window targets the unresolved transverse term:

```text
sum_{lambda in Lambda}
  lambda^2 Eng(I_trans(lambda))=o(1),
```

without using `M_minor=o(1)` as the estimate.

## 4. Assumptions

This update assumes only the recorded outputs of Modules 203, 204, 257, and
260-267:

```text
NarrowMinorArc_3^B is conditional/open.
MinorArcTransfer_3^B is conditional/open.
ProjectedModelNeutralityGate_260 is conditional/open.
AbsPMNGate_267 is conditional/open.
SignedExactNeutralGate_267 is conditional/open.
```

The update does not assume:

```text
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
or the original/all-alpha/unconditional finite-type conclusions.
```

The next phase must preserve:

```text
zero-frequency exclusion,
major/minor partition discipline,
dyadic D-range discipline,
fixed-w then N -> infinity then w -> infinity order,
declared selector class,
threshold-buffer discipline,
W-residue and prime-power side rows.
```

## 5. Proof / disproof / reduction

### A. What Phase H clarified

Phase H successfully clarified the projected model-neutrality branch:

```text
Module 260:
  named the model-neutrality gate.

Module 263:
  expanded the exact signed residual model into subset layers.

Module 264:
  split collision control into absolute and signed routes.

Module 265:
  separated absolute kernel costs from signed kernel cancellation.

Module 266:
  required same-family W-limit, denominator, projection, cutoff, selector,
  and dyadic uniformity.

Module 267:
  separated the literal absolute Module 260 gate from the signed exact-model
  direct route.
```

This is real progress in the proof map. It is not analytic closure.

The remaining Phase H rows are substantial:

```text
absolute fork:
  KernelAbsBudget_265,
  AbsCollStrataGate_264,
  UniformityLedger_266,
  all inside AbsPMNGate_267;

signed fork:
  KernelSignedBudget_265,
  SignedCoverGate_264,
  UniformityLedger_266,
  all inside SignedExactNeutralGate_267.
```

Neither fork currently gives a smaller established theorem. The absolute fork may
be too expensive because it pays `|W_M|`, structural singular strata,
exponential collision overflow, kernel tails, and finite-prime-set CRT
errors. The signed fork may be smaller, but it is not the literal absolute
gate and can become endpoint-strength if the full-cover clusters are
estimated by assuming projected major cancellation.

### B. Why not continue directly to projected-major matching

The projected major target has the schematic form:

```text
WProjectedLocalMatch_3^major(P_adm)
  + ProjectedModelNeutrality_3^major(P_adm)
    => ProjectedMajorTarget_3^B(P_adm).
```

After Module 267, the second input is still open. The first input was already
recorded as conditional and dependent on residual subset-HL matching,
boundary transfer, W-residue and prime-power transfer, denominator
admissibility, collision synchronization, and selector transfer.

Thus a direct move to full projected-major matching would combine two open
large packages:

```text
open model neutrality + open local-model matching.
```

That is a poor next proof test. It risks turning the ledger into a stack of
conditional package names rather than a search for a smaller analytic row.

### C. Why not isolate another boundary/projection slice immediately

Modules 257 and 258 showed that fixed boundary rows can contribute to
transfer packages only as localized slices:

```text
MinorArcTransfer_3^B,
CycIntTransfer_3^major.
```

They do not prove:

```text
NarrowMinorArc_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
or ProjectedMajorTarget_3^B.
```

The boundary branch is therefore useful as transfer bookkeeping, but it is
not currently the smallest unresolved analytic obstruction. Returning there
immediately would likely extend Phase G rather than solve a new bottleneck.

### D. Why return to minor-arc transverse incidence

Module 203 isolated a specific analytic risk:

```text
Eng(I_trans(lambda)).
```

This transverse region is defined after removing:

```text
bad shifts,
persistent minor frequencies.
```

It is not a boundary row, not a projected-major local model, and not a model
neutrality statement. It is a distinct large-spectrum obstruction.

The next useful test is to ask whether `I_trans(lambda)` can be rewritten as
a genuine incidence, restriction, inverse, or correlation problem that is
smaller than:

```text
M_minor(D;R,eta)=o(1).
```

If it can, the project gains a new non-tautological analytic target. If it
cannot, the project should mark the transverse route endpoint-strength or
blocked as a shortcut at the next challenge.

### E. Phase I schedule

Define:

```text
Phase I: minor-arc transverse-incidence feasibility window.
```

Target window:

```text
Modules 269-277.
```

Expected work:

```text
Module 269:
  extract the exact transverse-incidence object in NarrowMinorArc_3^B,
  including I_trans(lambda), Eng(I_trans), thresholds, selector class,
  dyadic shell, and model domain.

Module 270:
  audit the bad-shift and persistent-frequency removals, deciding what is
  really left after E_d(lambda)<=mu(lambda) and N_xi(lambda)<=K(lambda).

Module 271:
  expand a transverse large Fourier coefficient of B_d into the underlying
  shifted f-correlations and record the exact phase equations generated by
  two or more transverse incidences.

Module 272:
  compare available tools against the transverse object: large sieve,
  additive energy, ordinary pair-BDH, rectangle-BDH, first-moment HL, and
  generic finite-complexity HL.

Module 273:
  formulate a non-tautological transverse incidence gate, with a candidate
  bound Gamma_trans(lambda;D,R,eta,w) and explicit non-endpoint criteria.

Module 274:
  audit W-limit, threshold-buffer, prime-power, major/minor arc-boundary,
  and selector-transfer compatibility for the transverse gate.

Module 275:
  test whether low-dimensional degeneracies in the transverse equations
  reduce to bad-shift, persistent-frequency, major-arc leakage, or boundary
  rows already named.

Module 276:
  give a proof-or-blocked verdict for the transverse incidence gate:
  local/model-side, mixed, endpoint-strength, or false / blocked as a
  shortcut.

Module 277:
  perform the tenth plan update and the sixth plan challenge, since the
  long-term-plan count will reach 90.
```

The success criterion for Phase I is:

```text
produce a named transverse-incidence row that is demonstrably smaller than
M_minor=o(1), or classify the transverse route as mixed, endpoint-strength,
or blocked with a precise reason.
```

The failure criterion is:

```text
only renaming Gamma_trans without unpacking the incidences, phase equations,
thresholds, transfer rows, and forbidden shortcuts.
```

### F. Updated continuation rule

The next module should not prove or assume the minor-arc estimate. It should
extract the exact object:

```text
I_trans(lambda)
```

and define what a legitimate:

```text
TransIncCore_269(lambda;D,R,eta)
```

would need to control.

The phase should stop early if the transverse row can be estimated only by:

```text
M_minor=o(1),
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
or a selector-transfer theorem not supplied in fourth-moment residual form.
```

## 6. Edge cases

- This update does not abandon Phase H; it pauses Phase H after its verdict
  and preserves `AbsPMNGate_267` and `SignedExactNeutralGate_267` as open
  conditional routes.
- `SignedExactNeutralGate_267` must not be renamed as `CollNeutral_260`.
- The minor-arc branch must exclude `xi=0`; zero-frequency leakage belongs to
  centering or major-arc bookkeeping.
- A transverse incidence theorem in a cyclic or smoothed model does not reach
  the target selector without `MinorArcTransfer_3^B`.
- Threshold sets `Spec_d^minor(lambda)` need buffer discipline; near-threshold
  perturbations cannot be ignored.
- Bad-shift and persistent-frequency rows must not be counted twice after
  defining `I_trans(lambda)`.
- A large-sieve or additive-energy estimate for the wrong object does not
  supply `Gamma_trans`.
- Ordinary pair-BDH, rectangle-BDH, first-moment HL, and generic
  finite-complexity HL remain blocked as shortcuts unless upgraded to the
  exact residual, projected, W-uniform, variance-strength object.
- Boundary transfer rows may help `MinorArcTransfer_3^B`; they do not by
  themselves supply analytic minor-arc cancellation.

## 7. Where it fits in the project map

The project map now has:

```text
Phase G:
  fixed-row boundary feasibility diagnostics, completed as conditional.

Phase H:
  projected model-neutrality feasibility diagnostics, completed as
  conditional after the Module 267 verdict.

Phase I:
  minor-arc transverse-incidence feasibility, beginning with Module 269.
```

The active next chain is:

```text
Module 203:
  NarrowMinorArc_3^B names I_trans(lambda).

Module 204:
  MinorArcTransfer_3^B records transfer burdens.

Module 257:
  boundary/minor reentry blocks boundary shortcuts.

Module 268:
  PlanUpdate_9_268 selects Phase I.

Module 269:
  TransIncCore extraction.
```

This keeps the endpoint map balanced:

```text
major model neutrality:
  clarified but open;

boundary transfer:
  clarified but open;

minor transverse incidence:
  now the active bottleneck to test.
```

## 8. What remains open

This module does not prove:

- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `TransIncCore_269`;
- any bound for `Eng(I_trans(lambda))`;
- `ShiftMoment_q(lambda)`;
- `MultMoment_r(lambda)`;
- low-level minor leakage control;
- major/minor arc-boundary stability;
- W-limit or selector transfer for minor arcs;
- `AbsPMNGate_267(P_adm)`;
- `SignedExactNeutralGate_267(P_adm)`;
- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `CycIntTransfer_3^major`;
- `MajorSelectorTransfer_3^P`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat this plan update as evidence for minor-arc cancellation.
- Do not use `Gamma_trans` as a new name for `M_minor`.
- Do not establish `TransIncCore` by assuming `ResCube_3^sharp`,
  `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not use ordinary pair-BDH, rectangle-BDH, first-moment HL, or generic HL
  as the transverse incidence theorem.
- Do not transfer cyclic, model, smoothed, or frozen minor-arc statements to
  the actual sharp moving selector without the fourth-moment transfer rows.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
