# Module 215: Selector inventory for Modules 156-213

## 1. Precise theorem / claim being advanced

This module inventories the selector class used, implied, or left ambiguous in
Modules 156-213.

Define:

```text
SelectorInventory_156_213.
```

Claim:

```text
SelectorInventory_156_213 is a structural audit ledger.
```

It records, for each route or package in the current endpoint branch:

```text
declared selector class,
whether the declaration is explicit or inferred,
target selector if transfer is needed,
required transfer norm,
whether the transfer package is already named,
whether the transfer appears weaker than the endpoint.
```

This module does not prove selector transfer, does not repair ambiguous
selector declarations, and does not upgrade any model, smoothed, frozen,
cyclic, W-tricked, or lifted estimate to the actual sharp moving selector.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module extracts selector bookkeeping from existing files. It adds no
analytic estimate.

## 3. Definitions and variables

Selector classes:

```text
mv      actual sharp moving selector
fr      sharp frozen dyadic selector
sm      smoothed finite-band frozen selector
bern    hidden Bernoulli lift
fs      finite-stage / reference / survivor / core-floor model selector
W       W-tricked prime or von-Mangoldt model without an actual selector line
cyc     cyclic model
int     interval model
model   abstract local, projected, or probabilistic model
amb     selector ambiguous in the available module record
none    no selector-bearing theorem is being asserted
```

The actual sharp moving selector is:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

The residual product is:

```text
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)).
```

The major-arc projected selector-transfer norm is:

```text
SelErr_major^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M(B_{d,b}-B_{d,a})||_{U^2}^4,
```

with transport maps inserted when the two selector classes live on different
spaces.

The minor-arc selector-transfer norm is:

```text
SelErr_4^minor(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      ||Pi_minor(B_{d,b}-B_{d,a})||_{U^2}^4.
```

For unprojected residual endpoint routes, the minimum transfer strength is:

```text
SelErr_4(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      ||B_{d,b}-B_{d,a}||_{U^2}^4,
```

plus the relevant major/minor projection, boundary, W-residue, prime-power,
threshold, denominator, prefix, and tail terms.

## 4. Assumptions

This inventory assumes:

- `docs/modules/modules_156_178_summary.md` is the only module-level record in
  this repository for Modules 156-177;
- standalone files exist for Modules 178-213;
- a selector class is `explicit` only when the module states it directly;
- a selector class is `inferred` only when the module's object forces it from
  context, such as a W-tricked model or a cyclic model;
- if neither the summary nor the standalone file declares the selector, the
  inventory records `amb`, not a repaired declaration;
- transfer to `mv` always requires a projected or unprojected fourth-moment
  selector-transfer norm after forming `B_d`;
- first-moment selector approximation is insufficient for the residual cube
  endpoint unless a separate lift to the relevant fourth-moment norm is named.

## 5. Audit method / reduction

The audit uses the following rule.

For each module or module range, read the available module-level record and
assign the strongest justified selector classification:

```text
explicit  if the selector class is stated in the module;
inferred  if the module forces a class such as W, cyclic, projected, or model;
amb       if the selector is not declared in the available record;
none      if the module is only a plan, audit, or documentation item.
```

Then determine the target selector needed for the endpoint branch. If the
target is the actual project selector, record:

```text
target = mv.
```

Finally, record the minimum norm in which transfer must occur. For residual
cube statements this is never merely a one-point selector norm; it must pass
through:

```text
B_d(n)=f(n+d)conj(f(n))
```

and then through the relevant major, minor, or unprojected fourth-moment
normalization.

This proves only the structural inventory claim: every selector-bearing route
is assigned to one of the declared classes or marked as a gap. It does not
prove any transfer estimate.

## 6. Inventory table

Legend for the final column:

```text
weaker? yes       the named transfer appears genuinely below the endpoint
weaker? unclear   the package may be useful but could hide endpoint strength
weaker? no        the requirement is endpoint-strength or tautological
weaker? n/a       no selector-bearing transfer is being asserted
```

### A. Summary-derived Modules 156-177

The selector data for this range is summary-derived. These entries should be
restated from source before being used in a formal theorem.

| Modules | Route / package | Selector class | Declaration | Target | Required transfer norm | Named package | Weaker? | Verdict |
|---|---|---:|---:|---:|---|---|---:|---|
| 156 | Conditional closure of `s=2` rational-major branch from `RBDH_pair_short` plus side packages | amb / endpoint-sharp inferred | inferred from endpoint label only | mv | full residual fourth-moment selector transfer after side packages | not isolated in summary | unclear | gap before citation |
| 157 | WHL4/WHL8 two-rectangle route to RBDH | model / amb | inferred | mv if used for endpoint | rectangle-to-residual transfer plus `SelErr_4` | not isolated in summary | unclear | no direct selector upgrade |
| 158 | Spectral-density major/minor route to RBDH | model / projected inferred | inferred | mv | major/minor projected fourth-moment transfer | later `MinorArcTransfer_3^B`, `MajorSelectorTransfer_3^P` | unclear | route needs explicit selector line |
| 159 | Direct `CPC_3^sharp` / `AU^3` route | amb / sharp endpoint label | inferred | mv | endpoint-level selector transfer unless actual selector is explicitly declared | not isolated in summary | no | do not treat `sharp` as selector proof |
| 160-162 | Range coverage, required range, parameter envelope | none / amb | n/a | n/a | range compatibility only | n/a | n/a | not selector-bearing by itself |
| 163-169 | Source envelopes: rational-major, divisor, harmonic, tail, high-count, boundary, W-trick | W / model / amb | inferred | mv when used in final theorem | source-envelope transfer plus `SelErr_4` or projected variant | later side packages only partially name it | unclear | source envelopes do not imply actual selector |
| 170-172 | Consolidated range theorem, engine-matching matrix, conditional finite-type theorem package | amb | summary insufficient | mv if final theorem target is actual alpha | full theorem-level selector and gap-object transfer | not isolated in summary | unclear | restatement required before use |
| 173-176 | Three-paper architecture and theorem inventories | none | n/a | n/a | documentation only | n/a | n/a | no selector theorem asserted |
| 177 | Direct CPC attack via shifted derivative expansion | amb / endpoint-sharp inferred | inferred | mv | residual `B_d` fourth-moment selector transfer | not isolated in summary | no | endpoint route remains open |

### B. Residual cube setup, Modules 178-187

| Module | Route / package | Selector class | Declaration | Target | Required transfer norm | Named package | Weaker? | Verdict |
|---|---|---:|---:|---:|---|---|---:|---|
| 178 | Centered derivative `U^2` as residual cube | W / amb | inferred from `nu` | mv if used for original selector | `SelErr_4` after centering and zero-mode removal | not named yet | unclear | structural identity only |
| 179 | Fourier major/minor decomposition | W / cyclic / sm / model | explicit warnings | mv | major/minor projected fourth-moment transfer | later Modules 204 and 213 | unclear | decomposition only |
| 180 | Minor-arc large-spectrum criterion | model / cyclic / sm | explicit warnings | mv | `SelErr_4^minor` plus threshold stability | later `MinorArcTransfer_3^B` | unclear | criterion not actual-selector theorem |
| 181 | Major-arc projected residual local model | sharp/sm projection, model selector | explicit projection, selector warning | mv | `SelErr_major^P` plus projection-boundary transfer | later Module 213 | unclear | local model only |
| 182 | Projected neutrality and collision defects | model / projected | explicit warning | mv | `SelErr_major^P` after collision transfer | later Module 213 | unclear | model calculation only |
| 183 | Kernel-weighted collision template | model / projected | explicit warning | mv | kernel-compatible `SelErr_major^P` | later Module 213 | unclear | conditional model template |
| 184 | Structural collision strata | projected model | explicit warning | mv | selector transfer after structural-stratum accounting | later Module 213 | unclear | classification only |
| 185 | Structural collision negligibility | projected model | explicit warning | mv | selector transfer plus boundary/range transfer | later Module 213 | unclear | conditional, not selector transfer |
| 186 | Nonstructural divisor averages | projected model | explicit warning | mv | selector transfer after divisor averaging | later Module 213 | unclear | conditional model estimate |
| 187 | Local-factor collision envelope | projected model | explicit warning | mv | selector transfer after local-factor comparison | later Module 213 | unclear | conditional envelope only |

### C. Collision and W-limit dependency window, Modules 188-196

| Module | Route / package | Selector class | Declaration | Target | Required transfer norm | Named package | Weaker? | Verdict |
|---|---|---:|---:|---:|---|---|---:|---|
| 188 | Overflow collision load | model | explicit warning | mv | collision-compatible `SelErr_major^P` | later Module 213 | unclear | no actual selector statement |
| 189 | Exponential beta-load moment | model | explicit warning | mv | selector transfer after beta-load average | later Module 213 | unclear | no actual selector statement |
| 190 | Kernel mass and range audit | sharp/sm projection, not selector | explicit warning | mv | projection and selector transfer | later Module 213 | unclear | audit only |
| 191 | W-limit and tail uniformity | W / model | inferred and warning | mv | W-admissible selector and tail transfer | later Modules 204/213 | unclear | no diagonal upgrade |
| 192 | Averaged collision-defect bound | same selector as input / model | explicit same-selector condition | mv if target is actual | same-selector preservation plus `SelErr_major^P` | later Module 213 | unclear | conditional composition only |
| 193 | Generic projected neutrality after collision removal | model / projected | explicit warning | mv | `SelErr_major^P` plus boundary transfer | later Module 213 | unclear | model neutrality only |
| 194 | Projected local-model matching dependencies | model / sm / frozen possible | explicit selector requirement | mv | `SelErr_major^P` if target actual | later Module 213 | unclear | dependency list only |
| 195 | Hidden upgrade audit | none / audit | explicit no-upgrade conclusion | n/a | n/a | n/a | n/a | confirms no selector upgrade |
| 196 | First plan update | none / plan | n/a | n/a | future selector transfer | later Modules 204/213 | n/a | planning only |

### D. Minor-arc dependency window, Modules 197-205

| Module | Route / package | Selector class | Declaration | Target | Required transfer norm | Named package | Weaker? | Verdict |
|---|---|---:|---:|---:|---|---|---:|---|
| 197 | Minor-arc density / energy criterion | model / projected / cyclic possible | explicit warning | mv | `SelErr_4^minor` plus adaptive restriction transfer | later Module 204 | unclear | conditional criterion only |
| 198 | Pair-BDH comparison | cyclic / sm / projected / model warning | explicit warning | mv | pair-margin absorption plus `SelErr_4^minor` | later Module 204 | unclear | shortcut blocked |
| 199 | Rectangle-HL insufficiency audit | cyclic / sm / weighted warning | explicit warning | mv | residual adaptive transfer plus `SelErr_4^minor` | later Module 204 | unclear | shortcut blocked |
| 200 | Dyadic derivative `U^2` minor arcs | projected derivative model | explicit warning | mv | `SelErr_4^minor` after `Pi_minor Delta_d f` | later Module 204 | unclear | structural equivalence only |
| 201 | Minor-arc large-spectrum obstruction map | model / projected | explicit warning | mv | large-spectrum threshold transfer plus `SelErr_4^minor` | later Module 204 | unclear | obstruction map only |
| 202 | First plan challenge | none / plan | n/a | n/a | future selector transfer | Module 204 scheduled | n/a | planning only |
| 203 | `NarrowMinorArc_3^B` | model-dependent criterion | explicit outside package | mv | `SelErr_4^minor`, threshold buffers, W/range transfer | Module 204 | unclear | useful but not target selector |
| 204 | `MinorArcTransfer_3^B` | `cyc -> int -> W -> smooth/frozen -> sharp` | explicit | mv | `SelErr_4^minor` plus arc-boundary, W, prime-power, threshold, dyadic-range errors | itself | unclear | named transfer, still open |
| 205 | Second plan update | none / plan | n/a | n/a | future major selector transfer | Module 213 scheduled | n/a | planning only |

### E. Projected major-arc dependency window, Modules 206-213

| Module | Route / package | Selector class | Declaration | Target | Required transfer norm | Named package | Weaker? | Verdict |
|---|---|---:|---:|---:|---|---|---:|---|
| 206 | `ProjectedMajorTarget_3^B` | selector not fixed; actual case stated | explicit conditional | mv if target actual | `SelErr_major^P` | later Module 213 | unclear | target exact, transfer open |
| 207 | `Omega_w^proj` factors | W-tail local model / model | explicit outside selector transfer | mv | `SelErr_major^P` after local matching | later Module 213 | unclear | local factors only |
| 208 | Collision hyperplanes | projected model / actual interval not transferred | explicit separation | mv | `SelErr_major^P` after collision and interval packages | later Module 213 | unclear | stratification only |
| 209 | `WProjectedLocalMatch_3^major` | theorem must declare selector | explicit | mv if declared actual | `SelErr_major^P(N,w;rho)` | later Module 213 | unclear | conditional schema |
| 210 | `CycIntTransfer_3^major` | cyclic/interval, selector parameter present | inferred | mv | selector transfer separate from interval transfer | later Module 213 | unclear | boundary transfer only |
| 211 | `PPSPTransfer_3^major` | W-tricked prime-only / actual-W | explicit W model | mv | prime-power selector transfer plus `SelErr_major^P` | later Module 213 | unclear | not actual selector |
| 212 | `LocalModelCompat_3^major` | selector fixed before comparison | explicit assumption | mv if target actual | model compatibility does not supply selector transfer | later Module 213 | n/a | guardrail only |
| 213 | `MajorSelectorTransfer_3^P` | fs, bern, sm, fr, mv | explicit | mv | adjacent `SelErr_major^P` plus side errors | itself | unclear | named transfer, still open |

## 7. Gaps extracted from the inventory

The inventory exposes five selector gaps.

### A. Summary-derived ambiguity

Modules 156-177 are not available here as standalone module files. Their
selector class is therefore summary-derived and often ambiguous. Any formal
use of those routes should restate the selector class before citing them.

### B. Endpoint-sharp is not selector-sharp

Labels such as:

```text
CPC_3^sharp,
AU^3,
RBDH_pair_short
```

do not by themselves prove the actual sharp moving selector line:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

They identify endpoint strength or sharp analytic cutoffs only after the
selector class has been declared.

### C. Model estimates dominate the current branch

Most Modules 178-203 are structural or conditional model statements. They
either explicitly forbid transfer to actual sharp moving selectors or leave
selector transfer outside the package.

### D. The first explicit minor transfer is Module 204

Module 204 is the first module in this window that gives a selector-chain
package for minor arcs. It is still conditional and requires:

```text
SelErr_4^minor=o(1)
```

plus arc-boundary, W-admissibility, prime-power, threshold, and dyadic-range
terms.

### E. The first explicit projected major transfer is Module 213

Module 213 is the first module in this window that gives a selector-chain
package for projected major arcs. It is still conditional and requires:

```text
SelErr_major^P=o_W(1)
```

after forming `B_d` and applying `P_M`.

## 8. Does any transfer appear weaker than the endpoint?

The inventory does not certify any selector transfer as weaker than the
endpoint.

Some pieces may plausibly be weaker:

```text
prefix safety,
dyadic endpoint boundary control,
smooth-to-sharp transition bounds away from resonant thresholds,
finite denominator bookkeeping,
W-residue preservation under fixed shifts.
```

But the core selector-transfer norms:

```text
SelErr_4^minor,
SelErr_major^P,
SelErr_4
```

can be endpoint-strength if they are stated without additional structure. This
is why Module 216 should build a transfer matrix that separates plausibly
local/boundary errors from truly residual fourth-moment selector errors.

## 9. Edge cases

- A module that says "sharp" may refer to a sharp analytic cutoff, not the
  actual moving selector.
- A W-tricked prime model may still be selector-free unless a selector class is
  attached to `nu`.
- A cyclic estimate may use the same algebra as an interval estimate but still
  lacks interval and selector transfer.
- A smoothed projection estimate can fail to transfer to a sharp projection
  near arc boundaries.
- A one-point selector approximation can be too weak after forming
  `B_d=f(n+d)conj(f(n))`.
- A high-probability Bernoulli statement still needs deterministic extraction
  for fixed `alpha`.
- A first-moment transfer statement does not control a projected fourth moment
  unless a separate lift is supplied.
- If a selector declaration is ambiguous, this inventory marks it as a gap.

## 10. Where it fits in the project map

The Phase D chain now begins:

```text
Module 214
  -> third 9-iteration plan update
Module 215
  -> selector inventory for Modules 156-213.
```

This inventory supplies the input for Module 216's transfer matrix. The next
module should classify selector transfer errors by type:

```text
boundary,
prefix,
transition,
denominator,
tail,
projection,
W-residue,
prime-power,
core residual fourth-moment.
```

## 11. What remains open

This module does not prove:

- selector transfer for any module in the inventory;
- `MinorArcTransfer_3^B`;
- `MajorSelectorTransfer_3^P`;
- deterministic extraction from Bernoulli or finite-stage selector models;
- frozen-to-moving transfer;
- smoothed-to-sharp transfer;
- prefix, denominator, transition, boundary, projection, W-residue, or tail
  transfer;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat this inventory as proving any selector transfer.
- Do not repair ambiguous selector declarations by interpretation.
- Do not treat `sharp` in an endpoint name as proof of the actual moving
  selector.
- Do not transfer model, cyclic, W-tricked, smoothed, frozen, finite-stage, or
  Bernoulli estimates to `mv` without the appropriate fourth-moment transfer
  package.
- Do not cite Module 204 or Module 213 as proved transfer; they are
  conditional packages.
- Do not use first-moment selector approximation as a substitute for
  `SelErr_4^minor`, `SelErr_major^P`, or `SelErr_4`.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
