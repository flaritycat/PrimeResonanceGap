# Module 196: First 9-iteration plan update

## 1. Precise theorem / claim being advanced

This module performs the first 9-iteration update of the long-term project
plan adopted after Module 187. It records what Phase A clarified, revises the
next 9-iteration target window, and decides whether the project should remain
on major-arc collision dependencies or move to minor-arc large-spectrum
control.

Plan-update verdict:

```text
Phase A has isolated a conditional major-arc collision/model dependency map,
not a proof of the endpoint.

The next scheduled branch should move to minor arcs.
```

The reason is that Modules 188-195 have already named the major-arc collision
and model-matching gaps sharply enough for the current ledger. Continuing on
that branch before addressing minor arcs would risk polishing a dependency map
while leaving the other half of the residual derivative cube untouched.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a planning and proof-ledger module. It does not prove any new analytic
estimate.

## 3. Definitions and variables

The active counters after this module are:

```text
Latest completed module: 196
Post-Reflective_1 solving count: 15
Long-term-plan count: 9
```

The relevant cadence objects are:

```text
Reflective_N cadence: every 40 solving iterations after Reflective_1
plan-update cadence: every 9 solving iterations after plan adoption
plan-challenge cadence: every 15 solving iterations after plan adoption
```

The Phase A modules since the long-term plan adoption are:

```text
188 Overflow estimate for large collision load
189 Exponential-moment criterion for beta-load sums
190 Kernel absolute-mass and range audit for major projection
191 W-limit order and generic tail uniformity
192 Averaged collision-defect bound under the qualified envelope
193 Generic projected model neutrality after collision removal
194 Projected local-model matching dependency list
195 Hidden-upgrade audit
196 First 9-iteration plan update
```

The principal open major-arc objects remain:

```text
StructDef_w(D)=o_W(1),
Overflow_w(D)=o_W(1),
KernelRange_W,
WAdmissibleTail_w,
ProjectedLocalMatch_3^major.
```

The principal minor-arc target remains the nonzero-frequency fourth-moment
decay from Modules 179-180:

```text
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1),
```

with `xi` restricted to minor arcs after the major/minor split.

## 4. Assumptions

This update assumes:

- the long-term plan was adopted after Module 187;
- each Module 188-196 is one substantive solving iteration;
- Module 195's hidden-upgrade audit is binding;
- the global status ledger remains controlling;
- no module in Phase A proves the endpoint, original problem, all-alpha
  theorem, unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`;
- the next plan challenge is triggered by long-term-plan count 15, not by the
  separate post-reflection count 15.

## 5. Proof / disproof / reduction

### A. What Phase A clarified

Modules 188-195 replaced the informal phrase "major-arc collision control" by
a chain of named conditions:

```text
local-factor envelope correction
  -> overflow/exponential-moment criterion
  -> kernel absolute-mass and range package
  -> W-tail and W-limit order
  -> structural collision defect
  -> conditional averaged collision-defect bound
  -> conditional projected model neutrality
  -> projected local-model matching dependency list
  -> hidden-upgrade audit.
```

This is real progress in the proof map because it separates:

```text
neutrality of the projected model
```

from:

```text
matching the actual projected residual cube to that model.
```

It also corrects the earlier linear collision-envelope temptation. The
acceptable envelope is conditional on small load or overflow control; a
first-moment divisor average is not enough.

### B. What Phase A did not prove

Phase A did not prove:

```text
ProjectedLocalMatch_3^major,
minor-arc fourth-moment decay,
sharp selector transfer,
endpoint equivalence closure.
```

It also did not verify the actual kernel/range package for the projection, the
joint-divisibility estimates needed for exponential beta-load control, or the
structural-defect input.

### C. Plan decision

The project should now follow the scheduled Phase B move into minor arcs.

The reason is strategic rather than cosmetic. The major-arc side now has
enough named open inputs to prevent hidden upgrades. The minor-arc side still
contains the broad unresolved target:

```text
large-spectrum control for B_d.
```

Without a comparable map of the minor-arc obstruction, the project cannot know
whether the residual derivative cube endpoint is blocked mainly by local-model
matching, by high-order Fourier concentration, or by both.

### D. Revised next 9-iteration target window

Target window after this update:

```text
Long-term-plan counts 10-18
Expected modules 197-205, if work continues one module per iteration
```

Proposed schedule:

```text
Module 197: Minor-arc density/energy criterion for B_d.
Module 198: Ordinary pair-BDH versus residual fourth-moment comparison.
Module 199: Rectangle/BDH and first-moment HL insufficiency audit.
Module 200: Dyadic derivative U^2 route to minor arcs.
Module 201: Minor-arc spectral large-spectrum obstruction map.
Module 202: First 15-iteration plan challenge.
Module 203: Refined conditional minor-arc criterion after the challenge.
Module 204: Boundary, W-range, and selector compatibility for minor arcs.
Module 205: Second 9-iteration plan update.
```

The Phase B success criterion is:

```text
replace "minor-arc cancellation" by a named open estimate, conditional
criterion, or blocked route.
```

## 6. Edge cases

- Module 196 is a plan update, not a plan challenge. The first plan challenge
  is due at long-term-plan count 15, expected at Module 202.
- The post-`Reflective_1` solving count also becomes 15 here, but that does
  not trigger the 15-iteration plan challenge. The challenge cadence is tied
  to long-term-plan count.
- Moving to minor arcs does not mark the major-arc branch solved. It marks the
  major-arc branch dependency-mapped.
- If a later module proves or falsifies a major-arc input, the plan can return
  to Phase A before Module 205, but the deviation must be recorded.
- If minor-arc work immediately reduces back to `ProjectedLocalMatch_3^major`,
  the project should record that as a coupling between Phase A and Phase B, not
  as independent progress.
- If a module between 197 and 205 is a governance correction rather than an
  analytic module, the counters advance by iteration, even if module-number
  estimates shift.

## 7. Where it fits in the project map

Module 196 sits between Phase A and Phase B:

```text
Modules 188-195
  -> conditional major-arc collision/model dependency map
  -> Module 196 plan update
  -> Modules 197-205 minor-arc large-spectrum program.
```

It also updates the project-governance line:

```text
Reflective_1
  -> long-term plan after Module 187
  -> first plan update at Module 196
  -> first plan challenge expected at Module 202
  -> second plan update expected at Module 205.
```

## 8. What remains open

This module does not prove:

- `StructDef_w(D)=o_W(1)`;
- overflow or exponential beta-load control;
- the actual kernel absolute-mass and range package;
- W-tail admissibility for the actual projection;
- `ProjectedLocalMatch_3^major`;
- minor-arc large-spectrum or fourth-moment decay;
- boundary, prime-power, denominator, prefix, or selector transfer;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat Phase A's dependency map as a proof.
- Do not treat this plan update as evidence for minor-arc cancellation.
- Do not replace `ProjectedLocalMatch_3^major` by projected model neutrality.
- Do not replace overflow control by first-moment divisor estimates.
- Do not treat ordinary pair-BDH or first-moment Hardy-Littlewood input as
  sufficient for the residual fourth-moment target.
- Do not transfer projected, cyclic, frozen, smoothed, or model estimates to
  the actual sharp moving selector without the full transfer package.
- Do not skip the Module 202 plan challenge or Module 205 plan update if the
  cadence remains one module per iteration.
