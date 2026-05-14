# Module 222: Consolidated selector-transfer dependency graph

## 1. Precise theorem / claim being advanced

This module consolidates the selector-transfer rows from Modules 216, 218,
219, and 220 into one dependency graph.

Define:

```text
SelectorTransferGraph_3^consol.
```

This is not a new analytic package. It is a structural graph that records
which already named rows feed:

```text
major projected transfer,
minor transfer,
full nonzero transfer,
deterministic extraction to the actual selector.
```

The claim is:

```text
SelectorTransferGraph_3^consol
```

is the current minimal selector-transfer ledger for the residual derivative
cube branch. It consolidates duplicate row names, labels each row as local,
mixed, endpoint-strength, or blocked-as-shortcut, and identifies the smallest
honest next analytic target.

The graph does not prove:

```text
SharpSelectorTransfer_3,
MajorSelectorTransfer_3^P,
MinorArcTransfer_3^B,
MajorMinorSelCompat_3(P_adm),
FrozenMovingObstruction_3^Pi,
DetExtract_3^Pi(s -> mv).
```

It only prevents those objects from being combined ambiguously.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is a consolidation and classification ledger. It adds no new
estimate and does not upgrade any theorem status.

## 3. Definitions and variables

Selector classes:

```text
fs      finite-stage / reference / survivor / core-floor model selector
bern    hidden Bernoulli lift
sm      smoothed finite-band frozen selector
fr      sharp frozen dyadic selector
mv      actual sharp moving selector
W       W-tricked prime or von-Mangoldt model
cyc     cyclic model
int     interval model
model   abstract projected or local model
```

The actual selector is:

```text
mv: chi_alpha(p)=1_{||alpha p||<1/log p}.
```

For every selector class `s`, write:

```text
nu_s,
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)).
```

For centered products:

```text
c_{d,s}=E_n B_{d,s}(n),
B_{d,s}^circ=B_{d,s}-c_{d,s}.
```

Let `a -> b` be an adjacent selector or model edge. The three transfer norms
are:

```text
SelErr_4(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      ||B_{d,b}-T_{a->b}B_{d,a}||_{U^2}^4,

SelErr_4^minor(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      ||Pi_minor(B_{d,b}-T_{a->b}B_{d,a})||_{U^2}^4,

SelErr_major^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M(B_{d,b}-T_{a->b}B_{d,a})||_{U^2}^4.
```

When projections differ, the graph uses:

```text
Pi_b B_{d,b} - T_{a->b}(Pi_a B_{d,a})
```

instead of applying one common projection.

## 4. Classification labels

Rows are classified conservatively.

```text
local
```

means the row is genuinely supported on a geometric boundary, prefix,
fixed-residue, or fixed-prime-power set after the residual product is formed.
It is still not proved.

```text
mixed
```

means the row has a local-looking source but can interact with Fourier
spectrum, selector thresholds, W-residue classes, major/minor partitions, or
shift averages.

```text
endpoint-strength
```

means the row contains an unlocalized residual fourth-moment norm, or a
localized norm whose smallness appears as hard as the endpoint unless extra
structure is supplied.

```text
blocked-as-shortcut
```

means the proposed implication is invalid unless another row in this graph is
proved.

## 5. Consolidated graph

| Consolidated row | Existing names folded into the row | Feeds | Classification | Verdict |
|---|---|---|---|---|
| Boundary and prefix support | `BdSel_4`, `SelBd_major^P`, `BdInt_4`, `Prefix_major^P`, `PrefSel_4`, `DyadPrefixMove_3^Pi` | major, minor, full | local if the support is genuinely boundary; mixed otherwise | smallest plausible analytic target, but still needs residual fourth-moment lifting |
| Smooth-to-sharp threshold layer | `TransWin_major^P`, threshold stability in `MinorArcTransfer_3^B`, smoothed-to-sharp rows | major, minor, full | mixed | first-moment transition counts are insufficient |
| Frozen-to-moving layer | `MoveWin_major^P`, `MoveSel_4^Pi(fr->mv)`, `MoveLayerCube_3^Pi`, `AmpNormMove_3^Pi` | major, minor, full | mixed to endpoint-strength | cannot be treated as `1/log p = 1/log X + O(1/log^2 X)` |
| Major/minor projection partition | `PartBdSel_4`, `ArcBdSel_4`, `P_M` versus `Pi_minor`, projection-boundary rows | full nonzero transfer | mixed to endpoint-strength | most dangerous composition gap from Module 218 |
| Denominator, projection, and grid compatibility | `DenProjSel_4`, `DenMMErr`, `DenProjMove_3^Pi`, `GridCompat_3^Pi`, denominator ranges in major/minor packages | major, minor, full, extraction | mixed | merge denominator and projection bookkeeping before estimating |
| W-residue and small-prime compatibility | `WResSel_major^P`, W-admissible minor transfer, W-residue parts of `PPWMMErr`, W-parts of `ExtractCompat_3^Pi` | major, minor, full, extraction | local to mixed | separate from Euler-factor local models |
| Prime-power removal | `PPSel_4`, `PPErr_4`, `PPCubeErr_major`, prime-power part of `PPWMMErr` | major, minor, full | mixed to endpoint-strength | first-moment sparsity is not enough |
| Centering and zero-mode | `CenterSel_4`, `ZeroMMErr`, `CenterMove_3`, `Delta c_d` rows | major, minor, full, extraction | mixed, lower-dimensional | must be synchronized with zero-frequency convention |
| Bernoulli extraction | `BernSum_3^Pi`, `BernCouple_3^Pi`, Bernoulli row of Module 216 | extraction to `mv` | mixed to endpoint-strength | expectation alone is blocked |
| Finite-stage extraction | `StageConv_3^Pi`, `DiagStable_3^Pi`, finite-stage row of Module 216 | extraction to `mv` | mixed to endpoint-strength | density convergence alone is blocked |
| Alpha-exception accounting | `AlphaExc_3^Pi`, metric exceptional-set rows | extraction / quantifier control | blocked-as-shortcut for all-alpha use | at most metric unless strengthened |
| Core residual selector difference | `CoreSel_4`, `CoreSel_4^minor`, `CoreSel_major^P`, unlocalized `SelErr_4` rows | major, minor, full | endpoint-strength | cannot be used as a harmless side package |

## 6. Duplicate-name consolidation

The graph recommends the following mergers.

First, the boundary and prefix names should be treated as one support family:

```text
Boundary / prefix support rows.
```

The proof may still split endpoint boundary, cyclic interval boundary, dyadic
prefix, and cutoff mismatch. The ledger should not pretend those are
independent analytic breakthroughs unless they are estimated separately.

Second, the denominator names should be merged before use:

```text
DenProjSel_4,
DenMMErr,
DenProjMove_3^Pi,
GridCompat_3^Pi.
```

These all enforce that the same frequency and parameter grid is being used.

Third, the zero-mode names should be merged:

```text
CenterSel_4,
ZeroMMErr,
CenterMove_3,
Delta c_d rows.
```

The same centering convention must hold across major, minor, and extraction
steps.

Fourth, frozen-to-moving names should not be cited as separate evidence:

```text
MoveWin_major^P,
MoveSel_4^Pi(fr->mv),
MoveLayerCube_3^Pi.
```

They are cause, target, and residual cube expansion of the same obstruction.

Fifth, Bernoulli and finite-stage extraction names should remain separate in
probability space, but they share one graph position:

```text
probabilistic or finite-stage model -> actual mv.
```

Both require residual fourth-moment coupling after forming `B_d`.

## 7. Composition map

The consolidated path to an actual full nonzero selector estimate has four
levels.

### Level 1: projected estimates in non-actual classes

Major and minor estimates may first be proved in:

```text
model, W, cyc, int, sm, fr, bern, fs.
```

Those estimates are not actual selector estimates.

### Level 2: selector-edge transfer inside each projection

For each adjacent edge:

```text
a -> b,
```

the proof must control the active rows from the graph in the correct norm:

```text
SelErr_major^P,
SelErr_4^minor,
or SelErr_4.
```

Unlocalized core rows are endpoint-strength unless localized.

### Level 3: major/minor composition

Major and minor selector transfers can be combined only after:

```text
PartBdSel_4,
ArcBdSel_4,
DenMMErr,
ZeroMMErr,
ChainMMErr,
BdMMErr,
PPWMMErr
```

are controlled in one convention.

### Level 4: actual selector extraction

If the estimate came from `bern` or `fs`, then even a good model estimate must
pass through:

```text
BernSum_3^Pi,
BernCouple_3^Pi,
StageConv_3^Pi,
DiagStable_3^Pi,
ExtractCompat_3^Pi,
AlphaExc_3^Pi
```

as relevant. Otherwise the theorem is about the model, not the actual moving
selector.

## 8. Smallest honest next analytic target

The smallest honest next analytic target is not:

```text
SharpSelectorTransfer_3,
CoreSel_4,
MoveLayerCube_3^Pi,
DetExtract_3^Pi.
```

Those are too global or too close to endpoint-strength.

The smallest plausible target is one fixed genuinely supported boundary or
prefix row in one projection and one selector edge:

```text
Boundary / prefix support row
  for fixed Pi,
  fixed a -> b,
  fixed dyadic D range,
  fixed W-limit order.
```

A concrete first test should have no moving threshold, no Bernoulli
extraction, and no major/minor partition change. For example, a projected
major cyclic-to-interval or cutoff-boundary row with the selector class held
fixed is the cleanest target. If even this local row cannot be estimated in
the residual fourth-moment norm, then the selector-transfer branch is not
ready for the mixed rows.

This target is intentionally modest. The project needs one real residual
fourth-moment transfer estimate before it tries to close the mixed or
endpoint-strength rows.

## 9. Edge cases

- A row that is local before forming `B_d` may be mixed after the `U^2` cube
  introduces eight vertices.
- Major and minor projections may use the same words but different denominator
  grids; then the graph must use the denominator/projection row.
- A boundary estimate for a model space does not transfer to `mv` without the
  extraction and selector rows.
- A frozen-to-moving threshold layer may look thin but still carry large
  residual fourth-moment mass.
- A Bernoulli estimate that is summable over `X` but not over `D`, `R`, `eta`,
  `w`, and `rho` is not sufficient for the endpoint grid.
- A metric alpha exceptional-set estimate does not imply an all-alpha theorem.
- Prime-power and W-residue rows overlap near boundaries unless the proof
  chooses a disjoint accounting convention.
- Centering before projection and centering after projection are not
  automatically equivalent.

## 10. Where it fits in the project map

The Phase D chain now has:

```text
Module 214
  -> third 9-iteration plan update
Module 215
  -> selector inventory
Module 216
  -> global selector-transfer matrix
Module 217
  -> narrowed plan challenge
Module 218
  -> major/minor selector-transfer compatibility
Module 219
  -> frozen-to-moving threshold transfer obstruction
Module 220
  -> deterministic extraction requirement
Module 221
  -> Reflective_2
Module 222
  -> consolidated selector-transfer dependency graph.
```

The next scheduled iteration is Module 223, the fourth 9-iteration plan
update. It should decide whether the next target window attacks the local
boundary/prefix row identified above or redirects to endpoint-equivalence
auditing.

## 11. What remains open

This module does not prove:

- any boundary or prefix row;
- any smooth-to-sharp threshold row;
- `MoveLayerCube_3^Pi`;
- `MajorMinorSelCompat_3(P_adm)`;
- `PartBdSel_4=o(1)` or `ArcBdSel_4=o(1)`;
- denominator, projection, W-residue, prime-power, or centering transfer;
- `DetExtract_3^Pi(s -> mv)`;
- `MinorArcTransfer_3^B`;
- `MajorSelectorTransfer_3^P`;
- `SharpSelectorTransfer_3`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite `SelectorTransferGraph_3^consol` as a transfer theorem.
- Do not introduce another selector-transfer package unless it merges or
  removes ambiguity from existing rows.
- Do not use `CoreSel_4` as a side error.
- Do not combine major and minor transfer without the Module 218 rows.
- Do not treat frozen-to-moving transfer as a first-order threshold drift.
- Do not turn Bernoulli or finite-stage estimates into actual fixed-alpha
  selector estimates without Module 220 extraction rows.
- Do not use metric exceptional-set extraction as an all-alpha theorem.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
