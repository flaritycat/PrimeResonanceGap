# Module 181: Major-arc projected residual local model

## 1. Precise theorem / claim being advanced

This module refines the major-arc branch from Module 179. The main point is
that Fourier major-arc projection changes the physical-space local model. The
major-arc proof target is therefore not the unprojected residual model
`Omega_w(d,h,k)` alone, but the exact projected residual model obtained by
applying the same major-arc kernel to the four `B_d` slots in the `U^2` cube.

Let `P_M` be the sharp or smoothed Fourier projection onto the nonzero major
arcs. The major-arc contribution may be written:

```text
M_major(D)
  = (1/D) sum_{D<|d|<=2D} ||P_M B_d||_{U^2}^4.
```

The structural claim is that this contribution expands to a kernel-weighted
eight-form residual cube. The required major-arc analytic work is:

```text
actual projected residual cube
  = projected residual local model + o(1),
```

followed by:

```text
averaged projected residual local model = o(1).
```

Neither estimate is proved in this module.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The projection expansion and the identification of the correct local model are
structural. The model-matching and model-neutrality estimates are open analytic
inputs.

## 3. Definitions and variables

As before:

```text
f = nu - 1
B_d(n) = f(n+d) conj(f(n))
c_d = E_n B_d(n)
B_d^circ(n) = B_d(n) - c_d
Q_d = E_{n,h,k} B_d(n) conj(B_d(n+h)) conj(B_d(n+k)) B_d(n+h+k)
```

Let `M=Major(R,eta) \ {0}` be the nonzero major-arc set from Module 179. For a
sharp projection:

```text
widehat{P_M B_d}(xi) = 1_M(xi) widehat{B_d}(xi).
```

For a smoothed projection, replace `1_M` by a multiplier `m_M(xi)` with
controlled overlap and `m_M(0)=0`. Let `K_M` be the inverse Fourier kernel:

```text
P_M B_d(x) = E_t K_M(t) B_d(x-t).
```

The unprojected residual local model is:

```text
Omega_w(d,h,k)
  = sum_{S subset {0,1}^3} (-1)^(8-|S|) Theta_{w,S}(d,h,k).
```

The projected residual model must use the shifted vertices:

```text
n - t0,           n - t0 + d,
n + h - t1,       n + h - t1 + d,
n + k - t2,       n + k - t2 + d,
n + h + k - t3,   n + h + k - t3 + d.
```

For `S` a subset of the eight shifted vertices, equivalently
`S subset {0,1}^2 x {0,1}`, let:

```text
Theta_{w,S}^{proj}(d,h,k;t0,t1,t2,t3)
```

denote the exact local singular model for the forms in `S` among these eight
shifted vertices. Define:

```text
Omega_w^{proj}(d,h,k;t0,t1,t2,t3)
  = sum_S (-1)^(8-|S|) Theta_{w,S}^{proj}(d,h,k;t0,t1,t2,t3).
```

When `t0=t1=t2=t3=0`, this reduces to the unprojected residual model
`Omega_w(d,h,k)`.

## 4. Assumptions

The structural expansion assumes:

- a finite Fourier model or a transferred interval Fourier model;
- a major-arc projection `P_M` with kernel `K_M`;
- the short-shift range `D <= Hcal(N)`;
- W-trick residue compatibility for all shifted forms;
- explicit treatment of collision hyperplanes among the shifted vertices;
- the inclusion-exclusion residual model for `f=nu-1`.

The analytic major-arc closure would additionally require:

- a projected local-model matching theorem for every active kernel shift;
- a projected model-neutrality theorem showing that the averaged
  `Omega_w^{proj}` contribution is `o(1)`;
- uniformity in `D`, `R`, `eta`, `w`, and the projection kernel.

## 5. Proof / disproof / reduction

For a sharp projection, Parseval gives:

```text
||P_M B_d||_{U^2}^4
  = sum_{xi in M} |widehat{B_d}(xi)|^4.
```

For a smoothed multiplier `m_M`, the corresponding expression is:

```text
||P_M B_d||_{U^2}^4
  = sum_xi |m_M(xi)|^4 |widehat{B_d}(xi)|^4.
```

In physical space:

```text
P_M B_d(x) = E_t K_M(t) B_d(x-t).
```

Therefore:

```text
||P_M B_d||_{U^2}^4
  = E_{n,h,k} E_{t0,t1,t2,t3}
      K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3).
```

Expanding `B_d(x)=f(x+d)conj(f(x))` produces the eight shifted vertices listed
above. Expanding each `f=nu-1` produces the inclusion-exclusion residual model
`Omega_w^{proj}`.

Thus the major-arc branch has two separate analytic obligations:

```text
Model matching:
(1/D) sum_d | actual projected cube_d - projected model_d | = o(1).
```

and:

```text
Model neutrality:
(1/D) sum_d projected model_d = o(1).
```

The first is a variance-strength Hardy-Littlewood-type statement with the
correct projected residual local model. The second is a local singular-model
calculation after zero-frequency removal, collision removal, and W-limit
ordering. Neither follows from ordinary pair-BDH or first-moment
Hardy-Littlewood asymptotics.

## 6. Edge cases

- Projection kernel: replacing the projected model by unprojected
  `Omega_w(d,h,k)` loses the `t0,t1,t2,t3` shifts.
- Smoothed projection: if a smooth multiplier is used, the fourth power
  `|m_M(xi)|^4` appears in the Fourier fourth moment.
- Zero frequency: major arcs must not reintroduce the removed `xi=0`
  contribution.
- Major-arc overlap: overlapping rational neighborhoods require a partition of
  unity or a multiplier with explicit overlap bounds.
- Collision hyperplanes: shifted vertices can collide because of `d,h,k` or
  because of kernel shifts `t0,t1,t2,t3`.
- W-trick compatibility: all shifted vertices must be residue-compatible after
  projection.
- Kernel tails: broad kernels can move points outside the transferred interval
  unless boundary terms are controlled.
- Model neutrality: matching the correct local model is not enough if the
  projected residual model itself has a surviving main term.

## 7. Where it fits in the project map

Modules 179 and 180 split the Fourier endpoint and refine the minor-arc branch.
Module 181 refines the major-arc branch:

```text
ResCube_3^sharp
  -> nonzero Fourier fourth moment
  -> major/minor split
  -> major projected residual model matching
  -> major projected model neutrality.
```

Together with the minor large-spectrum criterion, this gives a more explicit
two-front analytic program for the residual cube endpoint.

## 8. What remains open

This module does not prove:

- projected local-model matching for the major arcs;
- projected model-neutrality for `Omega_w^{proj}`;
- the minor-arc large-spectrum estimates from Module 180;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the finite-type theorem without all required endpoint and transfer packages;
- the original positive existence problem or the all-alpha no-positive-limit
  theorem.

## Red flags / forbidden upgrades

- Do not use the unprojected `Omega_w(d,h,k)` when the projected kernel shifts
  are active.
- Do not use only the full eight-form model `Theta_w`; the residual model is
  the inclusion-exclusion combination over all subsets.
- Do not claim model matching implies model neutrality.
- Do not claim first-moment Hardy-Littlewood asymptotics imply this major-arc
  variance-strength estimate.
- Do not use ordinary pair-BDH as a substitute for `CPC_3^sharp`.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not transfer cyclic, smoothed, or model-selector estimates to the actual
  sharp moving selector without the full transfer package.
