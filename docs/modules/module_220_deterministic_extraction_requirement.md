# Module 220: Bernoulli and finite-stage deterministic extraction requirement

## 1. Precise theorem / claim being advanced

This module isolates the extraction requirement for using Bernoulli or
finite-stage selector statements in the actual sharp moving-selector endpoint
branch.

Define:

```text
DetExtract_3^Pi(s -> mv),
```

where:

```text
s in {bern, fs}
```

and:

```text
Pi in {Id_nonzero, P_M, Pi_minor}.
```

Here:

```text
bern = hidden Bernoulli lift,
fs   = finite-stage / reference / survivor / core-floor model selector,
mv   = actual sharp moving selector.
```

The structural claim is:

```text
An expectation or high-probability estimate for bern/fs gives an actual
fixed-alpha endpoint estimate only after an explicit deterministic extraction
package in the same residual fourth-moment norm.
```

The formal conditional implication is:

```text
EndpointEstimate_3^Pi(s)
  + DetExtract_3^Pi(s -> mv)
    => EndpointEstimate_3^Pi(mv).
```

This module does not prove `DetExtract_3^Pi`. It defines the rows that must be
proved before any Bernoulli or finite-stage estimate can be cited as an actual
selector estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module extracts a dependency package and records the exact failure modes.
No probabilistic extraction, deterministic construction, or selector transfer
estimate is established.

## 3. Definitions and variables

The actual selector is:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

For a selector or model class `s`, let:

```text
nu_s,
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)).
```

If centered products are used:

```text
c_{d,s}=E_n B_{d,s}(n),
B_{d,s}^circ=B_{d,s}-c_{d,s}.
```

For a projection `Pi`, define the residual fourth-moment quantity:

```text
Z_s^Pi(X,D;R,eta,w,rho)
  = (1/D) sum_{D<|d|<=2D}
      || Pi B_{d,s} ||_{U^2}^4.
```

The notation suppresses unused parameters. For example:

```text
Pi=Id_nonzero
```

uses the nonzero unprojected norm, while:

```text
Pi=P_M
```

uses the projected major-arc norm, and:

```text
Pi=Pi_minor
```

uses the minor-arc norm.

If `s` and `mv` live on different spaces, let:

```text
T_{s->mv}
```

be the declared transport map. The extraction transfer error is:

```text
ExtractErr_4^Pi(s->mv;X,D;R,eta,w,rho)
  = (1/D) sum_{D<|d|<=2D}
      || Pi( B_{d,mv} - T_{s->mv} B_{d,s} ) ||_{U^2}^4.
```

If projections differ across the two models, replace the displayed expression
by:

```text
|| Pi_mv B_{d,mv} - T_{s->mv}(Pi_s B_{d,s}) ||_{U^2}^4,
```

and include the denominator and projection rows from Modules 218 and 219.

## 4. The extraction package

`DetExtract_3^Pi(s -> mv)` consists of the following rows.

### A. Parameter grid and limit-order row

The proof must specify the parameter grid:

```text
Grid_m^Pi
  = { X,D,R,eta,w,rho,lambda,... }
```

used by the target endpoint branch. The grid must include every dyadic shift
range, major/minor denominator range, smoothing width, W-parameter, threshold
level, and projection parameter that appears in the final argument.

The W-limit order must remain:

```text
lim_{w->infinity} limsup_{N->infinity}
```

with `w` fixed while `N -> infinity`. A diagonal extraction may not choose
`w=w(N)` unless a separate W-uniform theorem is supplied.

Define:

```text
GridCompat_3^Pi=o(1)
```

for failures of the Bernoulli or finite-stage grid to match the actual
endpoint grid.

### B. Bernoulli summability row

For `s=bern`, suppose the random Bernoulli lift is indexed by `omega`.
An expectation estimate:

```text
E_omega Z_bern^Pi(X,D;...) = o(1)
```

does not by itself give one deterministic realization that works across all
endpoint parameters.

The needed high-probability package is a summable exceptional-set estimate:

```text
sum_m
  P_omega(
    sup_{theta in Grid_m^Pi}
      Z_bern^Pi(theta;omega) > eps_m
  )
  < infinity,
```

for some:

```text
eps_m -> 0.
```

Call this row:

```text
BernSum_3^Pi.
```

By Borel-Cantelli, this would produce a deterministic Bernoulli realization
that is good eventually on the declared countable grid. Without summability,
one may have a good realization at each scale without a single realization
that is good for the endpoint limit.

### C. Bernoulli-to-actual coupling row

Even a deterministic good Bernoulli realization is not the actual selector:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

Therefore the package must include:

```text
BernCouple_3^Pi(alpha;omega)
  = ExtractErr_4^Pi(bern->mv;X,D;R,eta,w,rho)
  = o(1)
```

on the same grid and in the same limit order.

This row is the point where a probabilistic reference model becomes a
fixed-alpha actual selector statement. If it is absent, the conclusion is only
about the extracted Bernoulli realization, not about `mv`.

### D. Finite-stage convergence row

For `s=fs`, let:

```text
nu_{fs,K}
```

be the finite-stage, survivor, reference, core-floor, rebalanced, or hardened
model weight at stage `K`. The finite-stage extraction row requires:

```text
StageConv_3^Pi(alpha)
  = lim_{K->infinity}
      sup_{theta in Grid_m^Pi}
        ExtractErr_4^Pi(fs_K->mv;theta)
  = 0
```

for each fixed grid block `m`, with a diagonal rule for sending `m -> infinity`.

Pointwise convergence of selectors, convergence of densities, or convergence
of one-point averages is not enough. The convergence must occur after forming:

```text
B_d(n)=f(n+d)conj(f(n))
```

and measuring the projected or unprojected residual fourth moment.

### E. Diagonal stability row

If the proof selects:

```text
omega_m, K_m, M_m, R_m, w_m
```

depending on the grid block `m`, it must show that the final object is a
single deterministic selector or an admissible limiting selector. Define:

```text
DiagStable_3^Pi=o(1)
```

for the errors caused by changing realization, stage, smoothing band,
denominator range, or W-parameter along the diagonal.

This row blocks the invalid move:

```text
for each scale choose a new good model
  => one fixed-alpha theorem.
```

### F. Major/minor and frozen/moving compatibility row

The extraction must be compatible with:

```text
MajorMinorSelCompat_3(P_adm)
```

from Module 218 and:

```text
FrozenMovingObstruction_3^Pi
```

from Module 219.

Define:

```text
ExtractCompat_3^Pi=o(1)
```

for failures of the extracted model to preserve:

```text
major/minor projection partitions,
arc-boundary conventions,
denominator ranges,
W-residue conventions,
prime-power removal,
frozen-to-moving threshold rows,
centering and zero-mode conventions.
```

### G. Alpha-exception row

For a fixed-alpha theorem, the target alpha must be named or quantified before
extraction. For a metric statement, one may instead prove a summable
exceptional set in alpha:

```text
sum_m meas_alpha(Bad_m) < infinity.
```

Call the row:

```text
AlphaExc_3^Pi.
```

This row may support an almost-everywhere statement if the rest of the package
is present. It does not support an all-alpha statement, and it does not prove
the original positive existence problem.

## 5. Reduction / proof skeleton

Assume:

```text
EndpointEstimate_3^Pi(s)
```

for `s=bern` or `s=fs`, and assume all rows of:

```text
DetExtract_3^Pi(s -> mv).
```

For `s=bern`, `BernSum_3^Pi` gives, at most, a deterministic Bernoulli
realization `omega_*` satisfying:

```text
Z_bern^Pi(theta;omega_*)=o(1)
```

on the declared endpoint grid. This is still not an actual selector theorem.
The coupling row `BernCouple_3^Pi(alpha;omega_*)` then gives:

```text
ExtractErr_4^Pi(bern->mv;theta)=o(1).
```

For `s=fs`, `StageConv_3^Pi` and `DiagStable_3^Pi` give the corresponding
deterministic model-to-actual transfer.

In either case, use:

```text
B_{d,mv}
  = T_{s->mv}B_{d,s}
    + (B_{d,mv}-T_{s->mv}B_{d,s}).
```

After applying `Pi`, the triangle inequality in the finite `U^2`
fourth-moment norm gives:

```text
Z_mv^Pi(theta)
  <= C Z_s^Pi(theta)
     + C ExtractErr_4^Pi(s->mv;theta)
     + side rows.
```

The side rows are exactly:

```text
GridCompat_3^Pi,
DiagStable_3^Pi,
ExtractCompat_3^Pi,
Centering / zero-mode rows.
```

Thus the conditional implication follows:

```text
EndpointEstimate_3^Pi(s)
  + DetExtract_3^Pi(s -> mv)
    => EndpointEstimate_3^Pi(mv).
```

No row of `DetExtract_3^Pi` is estimated here.

## 6. Failure modes extracted

This module separates five common but invalid shortcuts.

First:

```text
E_omega Z_bern^Pi=o(1)
```

only gives average control over the random model. It does not identify the
actual selector and may not provide a single realization across all endpoint
parameters.

Second:

```text
P_omega(Z_bern^Pi > eps)=o(1)
```

at each individual scale is insufficient without a summable union over:

```text
X,D,R,eta,w,rho,lambda.
```

Third, a finite-stage model can have the right density but wrong residual
correlations. Density convergence is not:

```text
ExtractErr_4^Pi=o(1).
```

Fourth, a diagonal that changes the random realization or finite-stage model
at every scale does not define one fixed selector unless the limiting object
and its transfer are specified.

Fifth, extraction cannot bypass the rows already isolated in Modules 218 and
219. Major/minor projection compatibility and frozen-to-moving threshold
transfer remain necessary after extraction.

## 7. Edge cases

- If the Bernoulli variables are alpha-dependent, the probability space and
  the alpha quantifier must be stated before applying Borel-Cantelli.
- If the endpoint requires all dyadic `D <= Hcal(N)`, extracting for one `D`
  at a time is insufficient unless the union over `D` is summable.
- If the major and minor arcs use different denominator grids, a Bernoulli
  realization good for one grid may fail on the other.
- If `w` is allowed to grow during extraction, the W-limit order may be
  inverted.
- If a finite-stage survivor measure changes with `X`, the proof may be
  choosing a new model at every scale rather than a fixed selector.
- If the model estimate is centered and the actual estimate is not, the
  centering row `c_{d,mv}-c_{d,s}` must be included.
- If the Bernoulli model proves only an expectation for `f_s`, it still needs
  lifting through `B_d=f_s(n+d)conj(f_s(n))`.
- If extraction is over alpha in measure, the result is at most metric unless
  a separate all-alpha argument is supplied.
- If extraction produces a deterministic selector different from `mv`, the
  theorem is about that selector until `ExtractErr_4^Pi(s->mv)` is proved.

## 8. Where it fits in the project map

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
  -> Bernoulli / finite-stage deterministic extraction requirement.
```

This module narrows the Bernoulli and finite-stage rows of Module 216. The
next scheduled iteration is Module 221, the required `Reflective_2.md` memory
log after `Reflective_1.md`.

## 9. What remains open

This module does not prove:

- `DetExtract_3^Pi(s -> mv)`;
- `GridCompat_3^Pi`;
- `BernSum_3^Pi`;
- `BernCouple_3^Pi`;
- `StageConv_3^Pi`;
- `DiagStable_3^Pi`;
- `ExtractCompat_3^Pi`;
- `AlphaExc_3^Pi`;
- any deterministic extraction from Bernoulli estimates;
- any deterministic extraction from finite-stage, survivor, reference,
  core-floor, rebalanced, or hardened model selectors;
- `MoveLayerCube_3^Pi`;
- `MajorMinorSelCompat_3(P_adm)`;
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

- Do not turn Bernoulli expectation control into a fixed-alpha theorem without
  `BernSum_3^Pi` and `BernCouple_3^Pi`.
- Do not use a new random realization at every scale as if it were one fixed
  deterministic selector.
- Do not treat finite-stage density convergence as residual fourth-moment
  convergence.
- Do not skip the union over all dyadic `D`, denominator ranges, major/minor
  projections, thresholds, smoothing bands, and W-parameters.
- Do not invert the W-limit order during a diagonal extraction.
- Do not use metric alpha-exception summability as an all-alpha theorem.
- Do not bypass `MajorMinorSelCompat_3` or `FrozenMovingObstruction_3^Pi`
  through probabilistic language.
- Do not transfer model, Bernoulli, finite-stage, smoothed, or frozen
  estimates to the actual sharp moving selector without an explicit residual
  fourth-moment extraction row.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
