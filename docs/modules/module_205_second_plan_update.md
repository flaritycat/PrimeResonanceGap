# Module 205: Second 9-iteration plan update

## 1. Precise theorem / claim being advanced

This module performs the second required 9-iteration plan update after the
long-term plan was adopted.

Current counters after this module:

```text
Latest completed module: 205
Post-Reflective_1 solving count: 24
Long-term-plan count: 18
```

Claim:

```text
Phase B has met its useful bookkeeping goal but has not produced a proof.
```

More precisely, Modules 197-204 replaced the vague phrase "minor-arc
cancellation" by two named open packages:

```text
NarrowMinorArc_3^B(D;R,eta),
MinorArcTransfer_3^B(D;R,eta;w).
```

The correct next move is to pause further minor-arc refinement and enter
Phase C:

```text
Projected local model matching on major arcs.
```

This is a plan update, not an endpoint theorem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module extracts a decision from the existing ledger. It does not add a new
analytic estimate.

## 3. Definitions and variables

The relevant minor-arc target remains:

```text
M_minor(D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)}
        |widehat{B_d}(xi)|^4,

B_d(n)=f(n+d)conj(f(n)),
f=nu-1.
```

Phase B introduced:

```text
NarrowMinorArc_3^B(D;R,eta)
```

for the analytic large-spectrum inputs:

```text
low-level leakage,
bad-shift energy,
persistent-frequency energy,
transverse incidence energy.
```

It also introduced:

```text
MinorArcTransfer_3^B(D;R,eta;w)
```

for the model-to-target transfer inputs:

```text
fourth-moment transfer,
arc-boundary stability,
W-admissibility,
prime-power control,
threshold stability,
dyadic D-range uniformity,
selector transfer.
```

The major-arc branch to be resumed is:

```text
ProjectedLocalMatch_3^major.
```

Its local-model side must eventually specify the projected major-arc analogue
of the residual derivative product, including the exact local factor
`Omega_w` and all averaging domains.

## 4. Assumptions

No new analytic assumption is accepted as true in this module.

For planning purposes only, retain the existing open packages as named
dependencies:

```text
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ProjectedLocalMatch_3^major,
RBDH_pair_short,
CPC_3^sharp,
AU^3.
```

The global ledger remains unchanged:

```text
original positive existence problem: OPEN,
all-alpha no-positive-limit theorem: OPEN,
finite-type no-positive-limit theorem: CONDITIONAL,
s=2 endpoint class: OPEN.
```

## 5. Plan update / reduction

Phase B produced five useful clarifications.

First, Module 197 showed that the minor-arc fourth moment can be organized by
low-level `L^2`, density, and restriction-energy inputs. This was useful
because it turned a single opaque target into smaller kinds of estimates.

Second, Modules 198 and 199 blocked easy shortcuts. Ordinary pair-BDH,
rectangle-BDH, first-moment Hardy-Littlewood, and mean rectangle estimates do
not directly control the projected residual product:

```text
B_d(n)=f(n+d)conj(f(n)).
```

Third, Module 200 corrected a possible over-compression. The dyadic derivative
`U^2` formulation is not a new estimate by itself; after projecting to minor
arcs, it is the same fourth-moment target in different notation.

Fourth, Modules 201 and 203 produced a useful obstruction tree:

```text
low-level leakage
bad-shift concentration
persistent minor-frequency concentration
transverse incidence concentration.
```

The shift and persistent-frequency pieces have checkable moment forms. The
transverse piece is still the dangerous one: `Gamma_trans` is useful only if
it comes from a real incidence, inverse, restriction, or correlation theorem
that is smaller than the endpoint target.

Fifth, Module 204 showed that even a model proof of `NarrowMinorArc_3^B` would
not automatically reach the actual project selector. One also needs
`MinorArcTransfer_3^B`, including W-limit order, threshold buffers, boundary
transfer, prime-power removal, and sharp moving-selector transfer.

Therefore the Phase B verdict is:

```text
keep the packages as named open dependencies,
do not continue adding minor-arc refinements immediately,
pivot to Phase C.
```

This is not a rejection of the minor-arc route. It is a refusal to keep
renaming the same missing estimate.

## 6. Next 9-iteration target window

The next window is Phase C, counts 19-27 after the long-term plan. If work
continues one module per iteration, this corresponds to Modules 206-214.

Target:

```text
turn ProjectedLocalMatch_3^major into an exact dependency diagram.
```

Expected modules:

```text
Module 206:
  State the exact projected major-arc target for the residual derivative
  product, including the Fourier projection, dyadic domains, and zero-mode
  convention.

Module 207:
  Define the exact major-arc local model, including the required `Omega_w`
  factor and its relation to the existing `kappa_w`, `Sigma_w`, and
  higher-shift local factors.

Module 208:
  Stratify major-arc collision hyperplanes for the projected residual cube and
  separate structural collisions from analytic error terms.

Module 209:
  Formulate the W-admissible projected local-model theorem with all limit
  orders, uniformity ranges, and denominator restrictions.

Module 210:
  Audit cyclic-to-interval boundary transfer for the projected major-arc
  model.

Module 211:
  Audit prime-power and small-prime removal for the projected major-arc model.

Module 212:
  Check compatibility between pair, rectangle, and projected cube local
  models, with no pointwise replacement of `Sigma_w(d,h)` by
  `kappa_w(d)^2`.

Module 213:
  State the selector-class transfer line for projected major arcs, separating
  model, smoothed, frozen, and actual sharp moving selectors.

Module 214:
  Perform the third 9-iteration plan update.
```

The next plan challenge is still expected at long-term-plan count 30, around
Module 217 if work continues one module per iteration. The next reflective log
is still expected when the post-`Reflective_1` count reaches 40, around
Module 221.

## 7. Edge cases

- If Module 206 shows that the projected major-arc target is merely another
  name for the full endpoint target, Phase C should narrow immediately.
- If the exact `Omega_w` factor cannot be stated without assuming selector
  transfer, Phase C should move that burden to Phase D rather than hiding it.
- If W-admissibility fails for a proposed major-arc factor, the module should
  be marked conditional or blocked rather than repaired by a diagonal limit.
- If collision terms require endpoint-strength inputs, they should be routed
  back to the collision packages from Modules 188-194.
- If the major-arc branch becomes purely formal and detached from the residual
  cube endpoint, the Module 214 plan update should redirect.
- The reflection cadence is not due in this iteration.
- The 15-iteration plan challenge is not due in this iteration.

## 8. Where it fits in the project map

The current project map becomes:

```text
Modules 188-196:
  major-arc collision and W-limit dependency mapping

Modules 197-205:
  minor-arc obstruction and transfer dependency mapping

Modules 206-214:
  projected major-arc local-model matching
```

The endpoint branch remains:

```text
major arcs
  -> ProjectedLocalMatch_3^major

minor arcs
  -> NarrowMinorArc_3^B
  -> MinorArcTransfer_3^B

selector transfer
  -> explicit model-to-sharp line only

endpoint class
  -> still OPEN.
```

## 9. What remains open

This module does not prove:

- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- a non-tautological `Gamma_trans`;
- `ProjectedLocalMatch_3^major`;
- the exact major-arc `Omega_w` model;
- W-admissible major-arc local matching;
- selector transfer to the actual sharp moving selector;
- boundary transfer for sharp windows;
- prime-power removal in projected fourth-moment norm;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat this plan update as analytic progress toward the endpoint by
  itself.
- Do not continue Phase B by inventing weaker names for `Gamma_trans`.
- Do not cite `MinorArcTransfer_3^B` unless fourth-moment transfer and selector
  transfer are both explicitly present.
- Do not let `Omega_w` be a vague local factor; it must be exactly stated in
  the next phase.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not upgrade smoothed, frozen, cyclic, or W-tricked model estimates to the
  actual sharp moving selector without the required transfer package.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
