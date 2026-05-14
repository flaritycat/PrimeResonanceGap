# Module 216: Global selector-transfer matrix for the actual sharp moving selector

## 1. Precise theorem / claim being advanced

This module turns the selector inventory of Module 215 into a transfer matrix
for reaching the actual sharp moving selector:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

Define:

```text
SharpSelectorTransferMatrix_3.
```

Claim:

```text
SharpSelectorTransferMatrix_3
```

is the structural matrix of transfer rows that must be checked before any
model, cyclic, W-tricked, smoothed, frozen, Bernoulli, finite-stage, or
reference-measure statement can be used as an actual sharp moving-selector
statement in the residual derivative cube branch.

This module classifies each row as:

```text
plausibly local / boundary-level,
mixed,
or potentially endpoint-strength.
```

It does not prove any row of the matrix.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The matrix is a bookkeeping and dependency object. No analytic transfer
estimate is established.

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
model   abstract local or projected model
```

The actual target is:

```text
mv: chi_alpha(p)=1_{||alpha p||<1/log p}.
```

For a selector or model class `s`, write:

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

Let `a->b` be an adjacent transfer edge. The three residual fourth-moment
transfer norms are:

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

When two classes live on different probability spaces, insert the declared
transport map:

```text
T_{a->b}.
```

The transfer matrix is not limited to these core norms. It also records the
side rows that can change the object before the norm is measured.

## 4. Assumptions

This matrix assumes:

- the selector class on each side of an edge is declared;
- the object being transferred is one of the residual `B_d` fourth-moment
  targets, not a one-point selector average;
- major and minor projections are declared before comparison;
- all W-trick estimates use fixed `w`, then `N -> infinity`, then
  `w -> infinity`;
- boundary, prefix, transition, denominator, tail, projection, W-residue,
  prime-power, and centering terms are not hidden inside a single generic
  selector error;
- if a row is classified as "potentially endpoint-strength", it cannot be used
  as a harmless side condition in a proof.

## 5. Transfer-matrix construction / reduction

The matrix is constructed by applying the following rule to every selector edge
from Module 215.

First, identify the edge:

```text
a -> b,
```

for example:

```text
sm -> fr,
fr -> mv,
bern -> sm,
W -> mv.
```

Second, identify which residual target is being transferred:

```text
unprojected,
minor,
major projected.
```

Third, decompose the difference between the two sides into rows:

```text
B_{d,b}-T_{a->b}B_{d,a}
  = boundary
    + prefix
    + transition
    + moving-window
    + denominator
    + tail
    + projection
    + W-residue
    + prime-power
    + centering / zero-mode
    + core residual selector difference.
```

This is a dependency decomposition, not an equality with canonical summands.
Each proof route must define its summands. The matrix says which summands must
exist and how strong the estimate must be.

Finally, classify each row by whether it appears local, mixed, or
endpoint-strength. This classification is conservative: if a row contains a
full residual fourth-moment norm without structural localization, it is marked
potentially endpoint-strength.

## 6. Global transfer matrix

| Row | Typical edge | Required object / norm | Existing package | Relation to endpoint | Verdict |
|---|---|---|---|---|---|
| Boundary | `cyc->int`, `fr->mv`, sharp interval changes | projected or minor `U^2` fourth moment restricted to interval endpoints, dyadic shell edges, or vertices leaving range | `CycIntTransfer_3^major`, `MinorArcTransfer_3^B` | plausibly local if support is genuinely boundary and envelopes are available | keep separate; do not hide in selector notation |
| Prefix | `fr->mv`, `fs->mv` | fourth-moment contribution from initial ranges where dyadic freezing, construction, or W-normalization is not stable | not yet isolated globally | plausibly local, but can interact with large gaps or exceptional alpha | needs Module 216 row, later row-specific estimate |
| Smooth-to-sharp transition | `sm->fr` | fourth-moment contribution of `||alpha p||` near `1/log X` after forming `B_d` | Module 204 / 213 side row | mixed; local in selector boundary, but can resonate with `B_d` | not a first-moment smoothing error |
| Moving-window | `fr->mv` | fourth-moment contribution of replacing `1/log X` by `1/log p` on a dyadic shell | Module 213 side row | mixed to potentially endpoint-strength for exceptional alpha | central Phase D obstruction |
| Denominator | `bern->sm`, `sm->fr`, projection changes | stability of rational denominators, major/minor partitions, finite-band support, and CRT moduli | `DenAdm`, Module 209, Module 213 side row | plausibly local if partition overlap is bounded; mixed if large-spectrum sets move | must be checked for major and minor arcs separately |
| Tail | `fs->bern`, `sm->fr`, W/model changes | Fourier tails, construction tails, dyadic tails, unbounded-weight tails after forming `B_d` | Modules 191, 204, 213 | mixed; harmless only with residual fourth-moment envelopes | not controlled by ordinary mean tail bounds |
| Projection | major/minor model changes | difference between `P_M`, `Pi_minor`, buffered arcs, sharp arcs, and smoothed multipliers | Modules 206, 209, 213 | mixed; can be local near arc boundaries or endpoint-strength if spectrum moves | requires separate major/minor rows |
| W-residue | `W->int`, W-tricked models to actual forms | residue compatibility at every projected vertex after shifts, kernel moves, and selector changes | Modules 209, 210, 211, 213 | plausibly local for fixed residues and bounded shifts; mixed near boundaries | never part of `Omega_w^proj` |
| Prime-power | W-tricked von-Mangoldt to prime-only or reverse | projected/minor/unprojected fourth-moment contribution with at least one prime-power vertex | `PPSPTransfer_3^major`, Module 204 | mixed to potentially endpoint-strength | first-moment sparsity is insufficient |
| Centering / zero-mode | centered residual products | control of `c_{d,b}-c_{d,a}` and zero-mode leakage after projection or interval truncation | Modules 206, 210, 213 | mixed; low-dimensional but can leak through truncation | must be stated if `B_d^circ` is used |
| Bernoulli extraction | `bern->sm`, `bern->fr`, `bern->mv` | high-probability or expectation statement converted to deterministic fixed-alpha statement in the needed fourth-moment norm | not yet isolated globally | mixed to endpoint-strength | expectation is not deterministic transfer |
| Finite-stage extraction | `fs->bern`, `fs->mv` | survivor/reference/core-floor model transferred to a real selector object | not yet isolated globally | mixed to endpoint-strength | construction model is not actual selector |
| Core residual selector difference | any non-actual edge to `mv` | `SelErr_4`, `SelErr_4^minor`, or `SelErr_major^P` with no localization | Modules 204 and 213 name it | potentially endpoint-strength | cannot be treated as a side error |

## 7. Row formulas

This section records schematic formulas for the rows. A proof route may use a
stronger or more specialized version, but it must not use a weaker norm.

### A. Boundary row

For a boundary set `Bd_{a,b}(d,n,h,k,t)`, require a bound of the form:

```text
BdSel_4^major(a->b)
  = (1/D) sum_{D<|d|<=2D}
      E_{n,h,k,t} |W_M(t)| |ProductB_{d,a,b}(n,h,k;t)|
        Bd_{a,b}(d,n,h,k;t)
  = o_W(1),
```

or the minor/unprojected analogue. The product must be the actual residual
product in the chosen transfer edge.

### B. Prefix row

For a prefix set `Pref_N`, require:

```text
PrefSel_4(a->b)
  = (1/D) sum_{D<|d|<=2D}
      ||1_{Pref_N}(B_{d,b}-T_{a->b}B_{d,a})||_{U^2}^4
  = o(1),
```

with projected variants when the target is major or minor.

### C. Transition row

For a transition band:

```text
Trans_X(delta)
  = {p : | ||alpha p|| - 1/log X | <= delta },
```

or the moving analogue around `1/log p`, require the fourth-moment
contribution of every residual product containing a transition vertex to be
small. A first-moment count of `Trans_X(delta)` is only sufficient if lifted
through a residual envelope.

### D. Moving-window row

For `p in [X,2X]`, the frozen-to-moving discrepancy is:

```text
1/log p - 1/log X.
```

The required row is:

```text
MoveSel_4(fr->mv;D)
  = (1/D) sum_{D<|d|<=2D}
      ||B_{d,mv}-B_{d,fr}||_{U^2}^4
  = o(1),
```

or the projected/minor version, with the difference localized to the moving
threshold layer if that is the proof route.

### E. Denominator and projection rows

If a transfer changes denominator support or arc partitions, require:

```text
DenProjSel_4(a->b)
  = (1/D) sum_{D<|d|<=2D}
      ||(Pi_b-Pi_a)B_{d,a}||_{U^2}^4
  = o(1),
```

where `Pi` denotes the relevant major or minor projection. The row must record
the denominator range, overlap constants, and buffered-arc convention.

### F. Tail row

For any truncated component `Tail_{a,b}`, require:

```text
TailSel_4(a->b)
  = (1/D) sum_{D<|d|<=2D}
      ||Tail_{a,b} B_d||_{U^2}^4
  = o(1).
```

Ordinary one-point tail estimates are not enough unless a fourth-moment lift is
provided.

### G. W-residue row

For W-residue failures `WFail_{a,b}`, require the projected or unprojected
fourth-moment contribution of every residual product touching `WFail_{a,b}` to
be:

```text
o_W(1).
```

This row is separate from the Euler product over primes `p>w`.

### H. Prime-power row

Prime-power transfer must be measured by:

```text
PPSel_4(a->b)
```

in the same normalization as the target. In the projected major branch this is
the Module 211 object:

```text
PPCubeErr_major
```

or a stronger projected norm implying it.

### I. Centering and zero-mode row

If centering is used, require:

```text
CenterSel_4(a->b)
  = (1/D) sum_{D<|d|<=2D}
      |c_{d,b}-c_{d,a}|^4
  = o(1),
```

plus a zero-mode leakage bound after projection, interval cutoffs, and kernel
truncation.

### J. Core residual selector row

The core row is:

```text
CoreSel_4(a->b)
  = SelErr_4(a->b),
CoreSel_4^minor(a->b)
  = SelErr_4^minor(a->b),
CoreSel_major^P(a->b)
  = SelErr_major^P(a->b).
```

This row is not a harmless side package. Without localization or additional
structure it is as hard as transferring the endpoint itself.

## 8. Conditional composition statement

For any selector chain:

```text
s_0 -> s_1 -> ... -> s_J=mv,
```

define:

```text
SharpSelectorTransfer_3(s_0->mv)
```

to mean that every relevant matrix row is small in the correct residual
fourth-moment normalization for every adjacent edge.

Then the formal implication is:

```text
EndpointEstimate(s_0)
  + SharpSelectorTransfer_3(s_0->mv)
    => EndpointEstimate(mv).
```

The proof is the repeated triangle inequality in the corresponding `U^2`
fourth-moment norm. This is only a conditional composition statement; the
matrix rows are not estimated here.

## 9. Edge cases

- A small transition set in first moment can be large in residual fourth
  moment if it correlates with `B_d`.
- A denominator partition change can move frequencies between major and minor
  arcs even when the underlying selector changes little.
- A prefix range can dominate for exceptional alpha or for early construction
  stages unless explicitly bounded.
- A W-residue failure near an interval endpoint belongs to both residue and
  boundary accounting unless the proof chooses a disjoint convention.
- A smoothed-to-sharp transition can reintroduce zero-mode leakage after
  centering.
- A Bernoulli expectation bound does not produce a fixed-alpha theorem without
  extraction.
- A finite-stage survivor measure can have the right density but wrong
  residual correlations.
- A row marked "plausibly local" is not proved merely by being local in name.
- A row marked "potentially endpoint-strength" should be challenged before it
  is accepted as a side package.

## 10. Where it fits in the project map

The Phase D chain now has:

```text
Module 214
  -> third 9-iteration plan update
Module 215
  -> selector inventory for Modules 156-213
Module 216
  -> global selector-transfer matrix.
```

This module prepares Module 217, the second 15-iteration plan challenge. The
challenge should decide whether Phase D is identifying genuinely smaller
transfer problems or merely restating the endpoint under selector-transfer
names.

## 11. What remains open

This module does not prove:

- any row of `SharpSelectorTransferMatrix_3`;
- `SharpSelectorTransfer_3(s_0->mv)`;
- `MinorArcTransfer_3^B`;
- `MajorSelectorTransfer_3^P`;
- boundary transfer;
- prefix safety;
- transition control;
- frozen-to-moving transfer;
- denominator transfer;
- tail transfer;
- projection transfer;
- W-residue transfer;
- prime-power transfer;
- centering or zero-mode transfer;
- Bernoulli or finite-stage deterministic extraction;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat the matrix as proof of selector transfer.
- Do not treat a local-looking row as proved without the stated fourth-moment
  estimate.
- Do not use first-moment boundary, transition, or tail estimates as
  substitutes for residual fourth-moment transfer.
- Do not hide the core residual selector row inside a generic side error.
- Do not convert Bernoulli or finite-stage estimates into fixed-alpha
  statements without deterministic extraction.
- Do not move between major and minor projections without denominator and
  projection-boundary rows.
- Do not transfer model, cyclic, W-tricked, smoothed, frozen, finite-stage, or
  Bernoulli estimates to the actual sharp moving selector without the relevant
  matrix rows.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
