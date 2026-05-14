# Prime Resonance Gap: Codex Operating Instructions

This repository documents and continues the Prime Gap Resonance Project.

## Non-negotiable global status

- Original positive existence problem: **OPEN**.
- All-alpha no-positive-limit theorem: **OPEN**.
- Metric theorem `A_alpha(x) -> 1` for Lebesgue-a.e. irrational alpha: **PROVEN according to the project ledger**.
- Finite-type no-positive-limit theorem: **CONDITIONAL**.
- `s=2` rational-major endpoint: **OPEN** (analytic-engine descriptor).

## Allowed status labels

Use only:

- `PROVEN`
- `CONDITIONAL`
- `STRUCTURAL / EXTRACTION`
- `HEURISTIC`
- `OPEN`
- `FALSE / BLOCKED`

Do not invent near-synonyms. The status label is part of the mathematical content, not a mood.

## Forbidden upgrades

Never claim:

- the original positive existence problem is solved;
- the all-alpha no-positive-limit theorem is proved;
- the finite-type theorem is unconditional;
- `Pair-BDH` alone implies `CPC_3^sharp`;
- mean rectangle-HL implies rectangle-BDH;
- first-moment Hardy-Littlewood implies RBDH;
- raw shifted-pair Fourier smallness without subtracting `kappa_w(d)`;
- `Sigma_w(d,h)` may be replaced pointwise by `kappa_w(d)^2`;
- smoothed/frozen/model selector estimates imply actual sharp moving-selector estimates for free.

## Required continuation format

Every new theorem, module, or section must include:

1. Precise theorem or claim.
2. Status label.
3. Definitions and variables.
4. Assumptions.
5. Proof, disproof, or reduction.
6. Edge cases.
7. Project-map location.
8. What remains open.

If producing a paper section, also include:

- theorem statement;
- proof skeleton;
- dependency list;
- status;
- red flags / forbidden upgrades.

## Selector discipline

Always state which selector is used:

- actual sharp moving selector;
- sharp frozen dyadic selector;
- smoothed finite-band frozen selector;
- hidden Bernoulli lift;
- finite-stage model/reference measure;
- survivor/core-floor/rebalanced/hardened measure.

Never upgrade a smoothed, frozen, finite-stage, or model statement to the actual sharp moving selector unless boundary, transition, moving-window, prefix, denominator, and tail transfer hypotheses are explicitly included.

## Gap and tail discipline

Always state whether the average uses:

- full gap `g(p)`;
- clipped gap `g_H(p)=min(g(p),H)`;
- centered clipped gap;
- tail `tau_H(p)=(g(p)-H)_+`;
- dyadic tail level;
- empty interval indicator;
- tuple-count arrays `binom(Y_p(h),j)`.

Fixed-order tuple neutrality does not control empty intervals unless the high-count Bonferroni remainder is controlled.

## Exact local models

For `s=2` shifted-pair / rectangle work:

```text
kappa_w(d) = prod_{p>w} (1-1/p)^(-2) (1 - #{0,-d mod p}/p)

Sigma_w(d,h) = prod_{p>w} (1-1/p)^(-4)
               (1 - #{0,-d,-h,-h-d mod p}/p)
```

The two-rectangle model is `Theta_w(d,h,k)` for the eight cube forms.

`Sigma_w(d,h)` is not pointwise `kappa_w(d)^2`.

## Current analytic endpoint

Current best endpoint class:

```text
RBDH_pair_short(Hcal)
  <=> CPC_3^sharp(Hcal)
  <=> SPAC_2^sharp
  <=> SU2Pair_2^sharp
  <=> DyadicDerivativeU^2
  <=> AU^3
```

Modulo exact local pair and rectangle models, local covariance calibration, pair-margin absorption, linear `U^2` control, boundary transfer, collision control, W-trick limit order, prime-power transfer, and range coverage.

The endpoint itself is **OPEN**.

## First task after unpacking

Read these files first:

1. `docs/status/global_status.md`
2. `docs/status/forbidden_upgrades.md`
3. `docs/codex/continuation_protocol.md`
4. `docs/modules/module_178_residual_cube.md`
5. `docs/status/long_term_plan.md`
6. `docs/codex/SHORT_CODEX_PROMPT.md`

Then continue from the latest completed module and the current next action in
`docs/status/long_term_plan.md`. As of the long-term plan created after Module
187, the next module is:

```text
Module 188: Overflow estimate for large collision load.
```

Do not prove `ResCube_3^sharp` unless an actual proof is supplied. A
decomposition is structural. A bound is analytic. Mixing those up is how proof
ledgers become folklore.

## Verification expectations

Before committing or opening a PR, run:

```bash
python scripts/status_audit.py
python scripts/build_index.py
```

If you add or edit modules, also run:

```bash
python scripts/extract_modules.py docs/paper/Prime_Resonance_Gap_500_Page_Paper.txt docs/modules/generated_index.md
```

These scripts are lightweight sanity checks, not mathematical proof. Yes, even the scripts know their place.

## Reflection cadence

Create a new `Reflective_N.md` memory log every 40 further solving iterations after `Reflective_1.md`.

A solving iteration means a substantive project advance such as a new module, a committed analytic reduction, a proof attempt with a resolved outcome, or a correction that changes the proof map. Record what changed, what was corrected, what remains open, and which forbidden upgrades remain blocked.

## Long-term planning cadence

Follow `docs/status/long_term_plan.md`.

- Update the plan every 9th solving iteration after the plan was adopted.
- Question the plan every 15th solving iteration after the plan was adopted.
- If the 9-, 15-, or 40-iteration cadences coincide, perform all due reviews in
  that iteration.
- Current counters are maintained in `docs/status/long_term_plan.md`.
