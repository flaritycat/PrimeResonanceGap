# Module 217: Second 15-iteration plan challenge

## 1. Precise theorem / claim being advanced

This module performs the second required 15-iteration plan challenge after
the long-term plan was adopted.

Current counters after this module:

```text
Latest completed module: 217
Post-Reflective_1 solving count: 36
Long-term-plan count: 30
```

Challenge verdict:

```text
Continue Phase D, but narrow it sharply.
```

The selector-transfer work should continue because Modules 215-216 exposed a
real structural risk: many endpoint-branch statements are model, cyclic,
W-tricked, smoothed, frozen, Bernoulli, finite-stage, or selector-ambiguous,
not actual sharp moving-selector statements. However, Phase D should not try
to prove a generic selector-transfer theorem.

The main correction is:

```text
Do not accept an unlocalized CoreSel row as a side package.
```

The next modules should isolate specific transfer obstructions:

```text
major/minor projection and denominator compatibility,
frozen-to-moving dyadic threshold transfer,
Bernoulli and finite-stage deterministic extraction.
```

This is a plan challenge, not an analytic estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

No theorem is proved. The module records a diagnosis, a narrowed continuation
decision, and a warning against endpoint-strength selector transfer in
disguise.

## 3. Definitions and variables

The actual sharp moving selector is:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

The residual object remains:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)).
```

The selector-transfer norms from Modules 215-216 are:

```text
SelErr_4(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      ||B_{d,b}-B_{d,a}||_{U^2}^4,

SelErr_4^minor(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      ||Pi_minor(B_{d,b}-B_{d,a})||_{U^2}^4,

SelErr_major^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M(B_{d,b}-B_{d,a})||_{U^2}^4.
```

The selector-transfer matrix from Module 216 is:

```text
SharpSelectorTransferMatrix_3.
```

Its highest-risk row is:

```text
Core residual selector difference.
```

The current endpoint class remains:

```text
ResCube_3^sharp
  -> CPC_3^sharp
  -> RBDH_pair_short
  -> AU^3.
```

All arrows here remain open or conditional according to the project ledger;
this module does not improve their status.

## 4. Assumptions

This plan challenge assumes:

- the global status ledger remains controlling;
- the original positive existence problem remains `OPEN`;
- the all-alpha no-positive-limit theorem remains `OPEN`;
- the finite-type theorem remains `CONDITIONAL`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, and `AU^3` remain
  `OPEN`;
- Modules 215 and 216 are structural audit modules, not transfer proofs;
- the plan challenge cadence is tied to long-term-plan count 30;
- the post-`Reflective_1` count is 36 after this module, so the next
  reflective log is not due yet.

## 5. Proof / disproof / reduction

### A. What assumption is too convenient?

The too-convenient assumption is that selector transfer can be treated as a
side condition once the relevant norm is named.

Module 216 shows the danger. Rows such as:

```text
boundary,
prefix,
W-residue,
denominator overlap
```

may plausibly be local or lower-dimensional after additional support
information. But the rows:

```text
SelErr_4,
SelErr_4^minor,
SelErr_major^P
```

are full residual fourth-moment norms unless localized further. In that form,
they may be as difficult as transferring the endpoint itself.

Required correction:

```text
Future Phase D modules must not state generic CoreSel transfer as an
assumption unless it is explicitly marked endpoint-strength.
```

### B. Which selector row would be abandoned if one conditional estimate had
to be removed?

The row to abandon as a generic side package is:

```text
Core residual selector difference.
```

That row is too broad:

```text
CoreSel_4(a->b),
CoreSel_4^minor(a->b),
CoreSel_major^P(a->b).
```

Without localization, threshold structure, boundary support, denominator
stability, or deterministic extraction, it says almost exactly:

```text
the residual endpoint survives selector change.
```

That is not a side lemma. It is a major analytic theorem. The plan should keep
the row as a warning label, not as an acceptable unresolved black box.

### C. Is the current work moving toward the original problem?

Partly, but indirectly.

Selector discipline is closer to the original problem than many endpoint
formalities because the original problem uses the actual moving selector:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

The work is useful when it prevents false upgrades from model or frozen
statements to this selector. It becomes less useful if it merely appends
another open transfer package to every theorem.

The project should therefore keep Phase D only if the next modules separate
specific transfer mechanisms from the generic endpoint-strength row.

### D. Did any module since the last challenge weaken an earlier claim?

Yes, in the healthy proof-ledger sense.

Modules 203-216 weakened informal optimism in several places:

```text
minor-arc criterion                remains conditional on transfer;
model minor-arc cancellation       does not reach target selector for free;
projected major local matching     requires exact Omega_w^proj;
cyclic major identities            do not imply interval estimates;
prime-power first moment           does not imply projected fourth moment;
local model face identities        do not justify pair-square shortcuts;
selector transfer                  must occur after B_d and projection.
```

These are not regressions. They are corrections. The danger is that many
corrections introduce new named packages. Phase D must now distinguish useful
local rows from endpoint-equivalent rows.

### E. What would convince this plan to stop or redirect?

Phase D should stop or narrow further if any of the following occurs:

```text
1. Module 218 finds major-arc and minor-arc selector-transfer packages use
   incompatible denominator or projection conventions with no smaller
   reconciliation row.

2. Module 219 finds frozen-to-moving threshold transfer is exactly a
   residual fourth-moment endpoint estimate with no boundary localization.

3. Module 220 finds Bernoulli or finite-stage extraction requires an
   endpoint-strength deterministic theorem for fixed alpha.

4. Module 223 cannot identify any selector-transfer row plausibly weaker than
   the endpoint.
```

If these occur, the project should redirect toward endpoint-equivalence audit
or a weaker honest theorem rather than continue adding transfer layers.

### F. Decision for the next window

Continue Phase D through the already scheduled diagnostic modules, but narrow
their assignments.

```text
Module 218:
  Audit major/minor selector-transfer compatibility, with special attention
  to denominator ranges, projection partitions, buffered arcs, and zero-mode
  conventions.

Module 219:
  Isolate the frozen-to-moving dyadic threshold transfer obstruction in the
  residual fourth-moment normalization. It should decide whether the row is
  boundary-local, mixed, or endpoint-strength.

Module 220:
  State deterministic-extraction requirements for Bernoulli and finite-stage
  selector models. It should separate expectation/high-probability transfer
  from fixed-alpha transfer.

Module 221:
  Create `Reflective_2.md`, because the post-`Reflective_1` count will reach
  40.

Module 222:
  Consolidate the selector-transfer graph after the reflection.

Module 223:
  Perform the fourth 9-iteration plan update and decide whether Phase D has
  earned continuation.
```

This is a narrowed continuation, not a proof claim.

## 6. Edge cases

- This module is a plan challenge, not a plan update. The next plan update is
  still expected at long-term-plan count 36, around Module 223.
- The next reflective log is not due here; it is expected when the
  post-`Reflective_1` count reaches 40, around Module 221.
- Continuing Phase D does not mean the selector-transfer route is believed
  easy.
- Abandoning the generic CoreSel row does not abandon selector transfer; it
  prevents endpoint-strength assumptions from being smuggled in as side
  conditions.
- If Module 218 or 219 discovers a genuine contradiction in the selector
  transfer setup, the plan should correct immediately rather than wait for
  Module 223.
- If a transfer row is only first moment, it remains unusable for the
  residual cube endpoint until lifted to the correct fourth-moment norm.

## 7. Where it fits in the project map

Module 217 is the governance checkpoint after the first Phase D selector
inventory and matrix sequence:

```text
Module 214
  -> third 9-iteration plan update
Module 215
  -> selector inventory
Module 216
  -> selector-transfer matrix
Module 217
  -> second 15-iteration plan challenge.
```

The branch continues only in narrowed form:

```text
Module 218
  -> major/minor selector-transfer compatibility
Module 219
  -> frozen-to-moving threshold obstruction
Module 220
  -> Bernoulli / finite-stage deterministic extraction
Module 221
  -> Reflective_2 memory log
Module 222
  -> post-reflection selector graph consolidation
Module 223
  -> fourth 9-iteration plan update.
```

## 8. What remains open

This module does not prove:

- any row of `SharpSelectorTransferMatrix_3`;
- `SharpSelectorTransfer_3`;
- `MinorArcTransfer_3^B`;
- `MajorSelectorTransfer_3^P`;
- frozen-to-moving transfer;
- major/minor selector-transfer compatibility;
- deterministic extraction from Bernoulli or finite-stage models;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat the decision to continue Phase D as evidence for the endpoint.
- Do not use generic `SelErr_4`, `SelErr_4^minor`, or `SelErr_major^P` as a
  harmless side assumption.
- Do not rename the residual endpoint as selector transfer.
- Do not use first-moment selector, boundary, transition, or tail control as a
  substitute for residual fourth-moment transfer.
- Do not transfer model, cyclic, W-tricked, smoothed, frozen, Bernoulli, or
  finite-stage estimates to the actual sharp moving selector without the
  relevant matrix rows.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
