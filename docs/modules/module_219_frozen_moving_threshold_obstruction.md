# Module 219: Frozen-to-moving dyadic threshold transfer obstruction

## 1. Precise theorem / claim being advanced

This module isolates the obstruction in the transfer step:

```text
fr -> mv,
```

from the sharp frozen dyadic selector

```text
chi_{alpha,X}^{fr}(p)=1_{||alpha p||<1/log X}
```

to the actual sharp moving selector

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

Define:

```text
FrozenMovingObstruction_3^Pi,
```

where `Pi` is one of:

```text
Id_nonzero, P_M, Pi_minor.
```

The structural claim is:

```text
Frozen-to-moving selector transfer in the residual derivative cube is exactly
a residual fourth-moment problem supported on moving-threshold discrepancy
factors, plus normalization, dyadic-boundary, projection, and zero-mode rows.
```

In particular:

```text
thin first-moment transition layer
  !=
small residual fourth moment after forming B_d.
```

A sufficient conditional package is:

```text
MoveLayerCube_3^Pi
  + AmpNormMove_3^Pi
  + DyadPrefixMove_3^Pi
  + DenProjMove_3^Pi
  + CenterMove_3
    => MoveSel_4^Pi(fr->mv)=o(1).
```

This is a decomposition and obstruction statement. It does not prove any of
the rows on the left.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The support identity and the residual-product expansion are formal. The
smallness of the moving-threshold layer cubes is open.

## 3. Definitions and variables

Work on a dyadic shell:

```text
I_X=[X,2X),
```

with a slightly enlarged shell `I_X^+` if shifts, interval cutoffs, W-tricks,
or projected kernels can move vertices outside `I_X`.

Let:

```text
tau_fr(X)=1/log X,
tau_mv(t)=1/log t.
```

For `t in I_X`, the pointwise threshold difference is:

```text
Delta_tau_X(t)=tau_fr(X)-tau_mv(t)
  = log(t/X)/(log X log t).
```

Thus:

```text
0 <= Delta_tau_X(t) <= log 2/(log X log(2X))
```

when the frozen threshold is anchored at the lower endpoint `X`. If a proof
freezes at another dyadic representative, replace this by the absolute
difference between the two chosen thresholds.

Define the sign-robust moving-threshold layer:

```text
Lay_X(alpha)
  = { t in I_X^+ :
        min(tau_fr(X),tau_mv(t))
          <= ||alpha t||
          < max(tau_fr(X),tau_mv(t)) }.
```

This is the only place where the two sharp support indicators differ if the
normalizing weights are identical and the dyadic support convention is the
same.

Let `nu_fr` and `nu_mv` be the frozen and moving W-tricked prime or model
weights in the normalization used by the endpoint branch. Define:

```text
f_fr=nu_fr-1,
f_mv=nu_mv-1,
g_X=nu_mv-nu_fr=f_mv-f_fr.
```

For each shift `d`, define:

```text
B_{d,fr}(n)=f_fr(n+d)conj(f_fr(n)),
B_{d,mv}(n)=f_mv(n+d)conj(f_mv(n)),
Delta B_{d,X}(n)=B_{d,mv}(n)-B_{d,fr}(n).
```

The exact product difference is:

```text
Delta B_{d,X}(n)
  = g_X(n+d)conj(f_fr(n))
    + f_fr(n+d)conj(g_X(n))
    + g_X(n+d)conj(g_X(n)).
```

For a projection `Pi`, define the frozen-to-moving fourth-moment transfer
row:

```text
MoveSel_4^Pi(fr->mv;X,D)
  = (1/D) sum_{D<|d|<=2D}
      || Pi Delta B_{d,X} ||_{U^2}^4.
```

In Fourier form:

```text
MoveSel_4^Pi(fr->mv;X,D)
  = (1/D) sum_{D<|d|<=2D}
      sum_xi |m_Pi(xi)|^4 |widehat{Delta B_{d,X}}(xi)|^4,
```

with:

```text
m_Id_nonzero(xi)=1_{xi != 0},
m_Pi=m_M       for projected major arcs,
m_Pi=m_minor   for minor arcs.
```

If centered products are used, also define:

```text
c_{d,s}=E_n B_{d,s}(n),
B_{d,s}^circ=B_{d,s}-c_{d,s},
Delta c_{d,X}=c_{d,mv}-c_{d,fr}.
```

## 4. Assumptions / rows isolated by the module

The frozen-to-moving package has five distinct rows.

### A. Moving layer cube row

Let:

```text
V(n,d,h,k)
  = { n, n+d, n+h, n+h+d,
      n+k, n+k+d, n+h+k, n+h+k+d }.
```

After expanding the `U^2` fourth moment of `Delta B_{d,X}`, every term in the
physical cube contains at least one occurrence of `g_X` at one of the eight
vertices in `V(n,d,h,k)`.

Define:

```text
MoveLayerCube_3^Pi(alpha;X,D)
```

to mean that the projected or unprojected residual cube average of every
expanded term containing at least one `g_X` factor is `o(1)` after averaging
over:

```text
D<|d|<=2D.
```

In schematic unprojected form this is:

```text
(1/D) sum_{D<|d|<=2D}
  E_{n,h,k}
    Product_{v in V(n,d,h,k)} F_v(v)
  = o(1),
```

where each `F_v` is one of:

```text
f_fr, conj(f_fr), g_X, conj(g_X),
```

with at least one `g_X` or `conj(g_X)` factor and with the conjugation pattern
dictated by the `U^2` cube. In the projected major case insert the kernel or
multiplier defining `P_M`; in the minor case insert `Pi_minor`.

This row is the real obstruction. It is not supplied by counting the layer
`Lay_X(alpha)` unless that count is lifted to this residual cube norm.

### B. Amplitude and normalization row

If the endpoint weights are not literally:

```text
same normalizing weight times chi_{alpha,X}^{fr}
same normalizing weight times chi_alpha,
```

then `g_X` has a component supported on the common window, not only on
`Lay_X(alpha)`. This can happen when the moving selector carries a pointwise
normalization depending on `log t`, while the frozen selector carries a dyadic
normalization depending on `log X`.

Define:

```text
AmpNormMove_3^Pi(alpha;X,D)=o(1)
```

for the residual fourth-moment contribution of this amplitude drift. A
relative `O(1/log X)` coefficient is not enough by itself unless a compatible
residual fourth-moment envelope for the remaining factors is also supplied.

### C. Dyadic endpoint and prefix row

The product:

```text
B_d(n)=f(n+d)conj(f(n))
```

uses both `n` and `n+d`; the `U^2` cube uses eight shifted vertices. Even if
`n` lies in `I_X`, some vertices can leave the dyadic shell or enter a range
where the frozen threshold was not declared.

Define:

```text
DyadPrefixMove_3^Pi(alpha;X,D)=o(1)
```

for all frozen-to-moving errors caused by:

```text
vertices outside I_X,
initial prefix ranges,
dyadic shell overlaps,
cutoff mismatch,
short intervals where log t and log X are not comparable.
```

This row is plausibly local only after the support and cutoff conventions are
fixed before forming the cube.

### D. Denominator and projection row

Changing from `fr` to `mv` can alter finite-band approximations, denominator
ranges, buffered major arcs, or minor large-spectrum sets. Define:

```text
DenProjMove_3^Pi(alpha;X,D)=o(1)
```

for failures caused by moving between:

```text
P_M^{fr} and P_M^{mv},
Pi_minor^{fr} and Pi_minor^{mv},
major/minor boundary bands,
W-residue conventions,
finite Fourier denominator ranges.
```

This row must be compatible with `MajorMinorSelCompat_3(P_adm)` from Module
218 whenever the full nonzero endpoint is assembled from major and minor
pieces.

### E. Centering and zero-mode row

If centered products are used, require:

```text
CenterMove_3(alpha;X,D)
  = (1/D) sum_{D<|d|<=2D} |Delta c_{d,X}|^4
  = o(1),
```

plus any zero-mode leakage introduced by cutoffs, projection multipliers, or
transport between cyclic and interval models.

## 5. Proof / extraction

The exact algebra starts with:

```text
f_mv=f_fr+g_X.
```

Therefore:

```text
B_{d,mv}
  = (f_fr(n+d)+g_X(n+d))
    conj(f_fr(n)+g_X(n)),
```

and subtracting `B_{d,fr}` gives:

```text
Delta B_{d,X}
  = g_X(n+d)conj(f_fr(n))
    + f_fr(n+d)conj(g_X(n))
    + g_X(n+d)conj(g_X(n)).
```

Apply the projection `Pi`. By the triangle inequality in the finite `U^2`
seminorm, or by expanding and using a fixed finite number of terms:

```text
||Pi Delta B_{d,X}||_{U^2}^4
  <= C sum_{r in R}
       ||Pi C_{d,r}||_{U^2}^4,
```

where the `C_{d,r}` are the three displayed product components, with any
additional cutoff, amplitude, or transport pieces separated into the rows
above.

For the unprojected norm:

```text
||C_{d,r}||_{U^2}^4
  = E_{n,h,k}
      C_{d,r}(n)
      conj(C_{d,r}(n+h))
      conj(C_{d,r}(n+k))
      C_{d,r}(n+h+k).
```

Each expanded term contains at least one `g_X` factor at one of the eight
vertices in:

```text
V(n,d,h,k).
```

For projected major arcs the same statement holds after inserting the
projecting kernel or multiplier; for minor arcs it holds after applying the
minor projection. Thus a residual cube estimate for every term with at least
one moving-discrepancy factor implies:

```text
MoveSel_4^Pi(fr->mv;X,D)=o(1).
```

The remaining rows account for the fact that `g_X` may contain more than a
pure threshold-layer support difference:

```text
amplitude / normalization drift,
dyadic endpoint and prefix drift,
projection or denominator drift,
centering drift.
```

This proves only the reduction:

```text
MoveLayerCube_3^Pi
  + AmpNormMove_3^Pi
  + DyadPrefixMove_3^Pi
  + DenProjMove_3^Pi
  + CenterMove_3
    => MoveSel_4^Pi(fr->mv)=o(1).
```

No analytic estimate for any row is supplied.

## 6. Classification verdict

The frozen-to-moving row is not automatically boundary-local.

It is boundary-local only if the following stronger statement is available:

```text
every residual cube with at least one moving-threshold layer factor is small
in the same projected or unprojected normalization as the endpoint.
```

Without that statement, the row is:

```text
mixed, and potentially endpoint-strength for exceptional alpha.
```

The reason is that a thin transition layer may correlate with:

```text
f_fr(n),
f_fr(n+d),
major-arc kernels,
minor large-spectrum frequencies,
W-residue classes,
dyadic endpoints,
or the shift average over d.
```

Thus a bound of the schematic form:

```text
sum_{p in I_X} 1_{p in Lay_X(alpha)} = small
```

does not by itself imply:

```text
(1/D) sum_{D<|d|<=2D}
  ||Pi(B_{d,mv}-B_{d,fr})||_{U^2}^4=o(1).
```

The former is a one-point count. The latter is an eight-vertex residual
fourth-moment statement.

## 7. Relation to local models

If this transfer is attacked on projected major arcs by local models, the
ordinary residual model:

```text
Omega_w^proj
```

is not enough. The required model is a moving-layer residual model with at
least one vertex constrained by:

```text
||alpha L_epsilon(n,d,h,k)|| near 1/log L_epsilon(n,d,h,k),
```

or by the corresponding difference between `1/log X` and
`1/log L_epsilon`.

Schematically one needs:

```text
Omega_{w,X,J}^{move,proj}(d,h,k;alpha),
```

where `J` is a nonempty subset of the eight cube vertices carrying
moving-threshold discrepancy factors. This object has both:

```text
p-adic local structure from the prime model,
archimedean alpha-threshold structure from ||alpha t||.
```

It must not be replaced by the collision-free ordinary `Omega_w^proj` unless
a named averaging lemma proves that the moving-layer factors are negligible
in the projected residual cube norm.

## 8. Edge cases

- If the frozen threshold is anchored at `X`, then on `[X,2X)` the frozen
  support is wider than the moving support. If it is anchored at `2X` or at a
  midpoint, the discrepancy can change sign or split into two layers.
- If `p` is close to a dyadic endpoint, then `p`, `p+d`, and the other cube
  vertices may belong to different shells with different frozen thresholds.
- If the selector weight includes moving normalization, the discrepancy is not
  supported only on the threshold layer.
- If `D` is large enough that `n+d` often leaves `I_X`, the row is not a pure
  threshold row; it also contains dyadic boundary transfer.
- If major and minor projections use different buffered arcs for `fr` and
  `mv`, the moving-window transfer can move mass across the major/minor
  boundary.
- If the zero frequency is excluded after transfer but centering is done
  before transfer, `Delta c_{d,X}` must be controlled separately.
- If alpha has unusually many primes near the moving threshold, first-moment
  layer estimates can fail, but even successful first-moment estimates still
  need residual fourth-moment lifting.
- If W-residue restrictions are imposed before the threshold comparison, the
  layer must be counted inside each admissible residue convention used by the
  projected or minor object.
- Prime-power removal remains separate: a prime-power vertex in the layer is
  not removed by ordinary prime layer counting.

## 9. Where it fits in the project map

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
  -> frozen-to-moving threshold transfer obstruction.
```

This module narrows the `fr->mv` moving-window row from Modules 204, 213, and
216. The next scheduled module is the Bernoulli or finite-stage deterministic
extraction requirement for selector statements used in the endpoint branch.

## 10. What remains open

This module does not prove:

- `MoveLayerCube_3^Pi`;
- `AmpNormMove_3^Pi`;
- `DyadPrefixMove_3^Pi`;
- `DenProjMove_3^Pi`;
- `CenterMove_3`;
- `MoveSel_4^Pi(fr->mv)=o(1)`;
- frozen-to-moving transfer for the actual sharp moving selector;
- smoothed-to-sharp frozen transfer;
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

- Do not treat `1/log p = 1/log X + O(1/log^2 X)` as proof of
  frozen-to-moving transfer.
- Do not replace the residual fourth-moment layer cube by a one-point count of
  primes in the threshold layer.
- Do not ignore amplitude or normalization drift inside the common window.
- Do not move from frozen to actual sharp moving selectors without dyadic
  endpoint, prefix, denominator, projection, W-residue, prime-power, and
  zero-mode rows.
- Do not use the ordinary projected local model `Omega_w^proj` for a
  moving-layer cube unless the moving-layer factors have their own model or a
  named negligibility lemma.
- Do not classify the `fr->mv` row as harmless boundary bookkeeping unless
  `MoveLayerCube_3^Pi` is actually proved in the needed norm.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
