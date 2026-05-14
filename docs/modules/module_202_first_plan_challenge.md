# Module 202: First 15-iteration plan challenge

## 1. Precise theorem / claim being advanced

This module performs the first 15-iteration plan challenge after adoption of
the long-term plan. It asks whether the current Phase B minor-arc branch should
continue, narrow, pivot back to major-arc matching, or branch toward a weaker
honest theorem.

Challenge verdict:

```text
Continue Phase B through Module 205, but narrow it.
```

The branch has earned a short continuation because Modules 197-201 converted
the vague phrase "minor-arc cancellation" into named requirements and failure
modes. However, the continuation is conditional on making those requirements
more checkable. If the next two modules only rename endpoint-grade estimates,
then the Module 205 plan update should redirect.

This module is governance and proof-ledger discipline. It is not an analytic
estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

No theorem is proved. The module records a plan challenge, a diagnosis of the
current branch, and a bounded decision for the next iterations.

## 3. Definitions and variables

The active counters after this module are:

```text
Latest completed module: 202
Post-Reflective_1 solving count: 21
Long-term-plan count: 15
```

The relevant cadence facts are:

```text
First plan update:       Module 196, completed
First plan challenge:    Module 202, this module
Second plan update:      Module 205, still scheduled
Next reflective log:     Module 221, not due
```

The Phase B modules so far are:

```text
197 Minor-arc density/energy criterion for B_d
198 Ordinary pair-BDH shortcut blocked
199 Ordinary rectangle/HL shortcuts blocked
200 Dyadic derivative U^2 is exact but not new
201 Minor-arc large-spectrum obstruction tree
202 First plan challenge
```

The current residual object remains:

```text
f=nu-1
B_d(n)=f(n+d)conj(f(n))
```

The current minor-arc target remains:

```text
M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4
  = o(1).
```

The named obstruction branches from Module 201 are:

```text
LowLevelLeak(lambda_0),
CountObs(lambda),
EnergyObs(lambda),
BadShiftEnergy(lambda,mu),
PersistentMinorFrequency(lambda),
TransverseIncidence(lambda).
```

The central conditional package from Module 197 is:

```text
R_{2,B}^minor(rho;D) <= Psi_*(rho;D),
```

with the density/energy integral:

```text
integral_{lambda_0}^{A_N}
  2 lambda Psi_*(Lambda_*(lambda;D);D) dlambda
  = o(1).
```

## 4. Assumptions

This plan challenge assumes:

- the global status ledger remains controlling;
- the original positive existence problem remains `OPEN`;
- the all-alpha no-positive-limit theorem remains `OPEN`;
- the finite-type theorem remains `CONDITIONAL`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, and `AU^3` remain
  `OPEN`;
- Modules 197-201 are read as structural, conditional, or blocked-shortcut
  modules according to their labels;
- the plan challenge cadence is tied to long-term-plan count 15;
- the post-reflection cadence does not trigger a new reflective log here.

## 5. Proof / disproof / reduction

### A. What assumption is too convenient?

The convenient assumption is that the adaptive restriction envelope:

```text
R_{2,B}^minor(rho;D) <= Psi_*(rho;D)
```

will be easier than the endpoint itself. Module 201 suggests this may be too
optimistic. In the transverse incidence branch, the envelope can become a
high-order correlation theorem for:

```text
widehat{B_d}(xi)
  = E_n f(n+d)conj(f(n))e(-xi n).
```

If no exploitable structure separates this from `M_minor(D)=o(1)`, then the
criterion is only a renamed endpoint estimate.

Required correction:

```text
Module 203 must separate checkable subconditions from endpoint-equivalent
conditions.
```

### B. Which route would be abandoned if one conditional estimate vanished?

If the adaptive restriction envelope is unavailable, then the Module 197 route
should not be treated as a proof strategy. It remains useful as an obstruction
map, but the analytic route must pivot.

The branch most dependent on this missing estimate is:

```text
TransverseIncidence(lambda)
  -> R_{2,B}^minor(rho;D) <= Psi_*(rho;D).
```

If that branch cannot be made smaller than the endpoint, then Phase B should
stop after the Module 205 plan update and return either to major-arc matching
or to selector/boundary transfer.

### C. Is the current work moving toward the original problem?

Partly. The current work is endpoint-level, not original-problem-level. It
moves toward the compressed rational-major endpoint class:

```text
ResCube_3^sharp
  -> CPC_3^sharp
  -> RBDH_pair_short
  -> AU^3.
```

That endpoint class is part of the project map, but it is not the original
positive existence problem. The risk is real: continued endpoint formalism can
become self-contained bookkeeping.

The mitigating fact is that Modules 197-201 did not merely polish notation;
they blocked false shortcuts and named actual obstruction branches. That is
still useful. It becomes unhelpful if the next modules fail to narrow the
analytic burden.

### D. Did any module since the last challenge weaken an earlier claim?

There was no earlier 15-iteration challenge, but Modules 197-201 did weaken
informal optimism:

```text
ordinary pair-BDH alone              blocked,
ordinary rectangle/HL shortcuts      blocked,
dyadic derivative U^2 alone          only a reformulation,
minor-arc cancellation               decomposes into six obstruction branches.
```

These are not failures of the project. They are corrections to the proof map.
They make the remaining endpoint harder but more honest.

### E. What would convince this plan to stop?

Phase B should stop or pivot if any of the following occurs:

```text
1. Module 203 shows the refined minor-arc criterion is equivalent to the full
   endpoint with no smaller subconditions.

2. Module 204 shows the needed minor-arc estimates cannot survive the actual
   selector, boundary, W-range, or prime-power transfer packages.

3. The transverse incidence branch requires an input indistinguishable from
   AU^3 or ResCube_3^sharp itself.

4. The next plan update cannot name a concrete estimate smaller than
   "minor-arc cancellation".
```

If these occur, the project should not continue Phase B by inertia.

### F. Decision for the next window

Continue Phase B for the remaining scheduled modules before the Module 205
plan update:

```text
Module 203:
  Refined conditional minor-arc criterion after the challenge.
  It should state a named package, with quantitative low-level, count,
  energy, bad-shift, persistent-frequency, and transverse-incidence inputs.

Module 204:
  Boundary, W-range, and selector compatibility for minor arcs.
  It should test whether the Module 203 package can live in the actual
  project setting, not only in a cyclic toy model.

Module 205:
  Second 9-iteration plan update.
  It should decide whether to continue Phase B, pivot back to major-arc
  matching, move to selector transfer, or branch toward a weaker theorem.
```

This is a narrowed continuation, not a proof claim.

## 6. Edge cases

- This module is the first plan challenge, not a second plan update. The next
  plan update remains scheduled for long-term-plan count 18, expected at
  Module 205 if one module equals one iteration.
- The post-`Reflective_1` solving count is 21 after this module; the next
  reflective log is not due.
- Continuing Phase B does not mean the minor-arc route is believed easy.
  It means the route has been narrowed enough to justify two more diagnostic
  modules.
- Pivoting later is not failure if the pivot is recorded with the exact
  obstruction.
- No result from Modules 197-202 transfers to the actual sharp moving selector
  without the named transfer packages.
- If Module 203 discovers an actual contradiction or false premise in Modules
  197-201, the plan should be corrected immediately rather than waiting for
  Module 205.

## 7. Where it fits in the project map

Module 202 is the governance checkpoint after the first Phase B obstruction
sequence:

```text
Module 196
  -> first 9-iteration plan update
Modules 197-201
  -> minor-arc criteria, shortcut audits, derivative reformulation,
     obstruction tree
Module 202
  -> first 15-iteration plan challenge.
```

The branch continues only in narrowed form:

```text
Module 203
  -> refined conditional minor-arc package
Module 204
  -> transfer compatibility audit
Module 205
  -> second 9-iteration plan update and decision point.
```

## 8. What remains open

This module does not prove:

- low-level `L^2` control on minor arcs;
- dyadic large-spectrum density decay;
- adaptive restriction-energy bounds;
- bad-shift, persistent-frequency, or transverse-incidence estimates;
- any major-arc estimate using `Omega_w`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay;
- transfer to actual sharp moving selectors;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat the decision to continue Phase B as evidence for the endpoint.
- Do not treat the obstruction tree as an analytic estimate.
- Do not keep Phase B alive after Module 205 unless it has a checkable
  estimate smaller than the endpoint.
- Do not rename `ResCube_3^sharp`, `AU^3`, or full endpoint-grade RBDH as an
  "adaptive restriction input".
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
