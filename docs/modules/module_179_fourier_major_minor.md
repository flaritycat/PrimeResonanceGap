# Module 179: Fourier major/minor decomposition for the residual derivative cube endpoint

## 1. Precise theorem / claim being advanced

This module reformulates the residual derivative cube endpoint as a Fourier
fourth-moment target and splits that target into major-arc and minor-arc
subtargets.

Let `D <= Hcal(N)` be in the required short-shift range. For each dyadic block
`D < |d| <= 2D`, the endpoint `ResCube_3^sharp(Hcal)` asks for:

```text
(1/D) sum_{D<|d|<=2D} ||B_d^circ||_{U^2}^4 = o(1).
```

With normalized Fourier transform, this is equivalent to the nonzero-frequency
fourth-moment target:

```text
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1).
```

The claim of this module is the equivalence and the major/minor decomposition
of the target. It does not prove either major-arc or minor-arc cancellation.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The Fourier identity and the major/minor split are structural. The estimates
needed to make the displayed `o(1)` true remain open analytic work unless a
separate variance-strength proof is supplied.

## 3. Definitions and variables

Work with the W-tricked prime weight `nu` in the prescribed residue class and
with the limit order `N -> infinity` first, then `w -> infinity`.

```text
f = nu - 1
B_d(n) = f(n+d) conj(f(n))
c_d = E_n B_d(n)
B_d^circ(n) = B_d(n) - c_d
```

Use normalized Fourier transform on the chosen finite cyclic model, or on the
interval model after the standard cutoff transfer:

```text
widehat{B_d}(xi) = E_n B_d(n) e(-xi n).
```

Then:

```text
widehat{B_d}(0) = c_d
widehat{B_d^circ}(0) = 0
widehat{B_d^circ}(xi) = widehat{B_d}(xi)  for xi != 0.
```

The physical-space cube is:

```text
Q_d = E_{n,h,k}
        B_d(n)
        conj(B_d(n+h))
        conj(B_d(n+k))
        B_d(n+h+k).
```

Equivalently, after expanding `B_d`, the eight vertices are:

```text
n, n+d, n+h, n+h+d, n+k, n+k+d, n+h+k, n+h+k+d.
```

For `epsilon in {0,1}^3`, write:

```text
L_epsilon(n,d,h,k) = n + epsilon_1 d + epsilon_2 h + epsilon_3 k.
```

For each subset `S subset {0,1}^3`, let:

```text
Theta_{w,S}(d,h,k)
```

be the exact local singular model for the forms `L_epsilon` with
`epsilon in S`. The residual local model is:

```text
Omega_w(d,h,k)
  = sum_{S subset {0,1}^3} (-1)^(8-|S|) Theta_{w,S}(d,h,k).
```

This inclusion-exclusion model is required because `f=nu-1`. The full
eight-form model alone is not the residual cube model.

## 4. Assumptions

The structural extraction uses:

- normalized Fourier inversion and Parseval on the chosen finite model;
- transfer from interval cutoffs to the finite Fourier model, if the interval
  model is used;
- the short-shift range `D <= Hcal(N)`;
- W-trick residue compatibility;
- exclusion or controlled treatment of collision hyperplanes among the eight
  linear forms;
- exact local models `Theta_{w,S}` and their residual combination `Omega_w`.

The analytic endpoint would additionally require:

- a major-arc residual model theorem with `Omega_w`, not only `Theta_w`;
- a minor-arc fourth-moment cancellation theorem for the pair-product
  spectral density;
- uniformity in `D`, `w`, cutoffs, and all allowed dyadic ranges.

## 5. Proof / disproof / reduction

By the `U^2` Fourier identity,

```text
||B_d||_{U^2}^4 = sum_xi |widehat{B_d}(xi)|^4.
```

Since `c_d=widehat{B_d}(0)`, centering removes exactly the zero frequency:

```text
||B_d^circ||_{U^2}^4
  = sum_xi |widehat{B_d^circ}(xi)|^4
  = sum_{xi != 0} |widehat{B_d}(xi)|^4
  = ||B_d||_{U^2}^4 - |c_d|^4
  = Q_d - |c_d|^4.
```

Averaging over short shifts gives the open endpoint in Fourier form:

```text
ResCube_3^sharp(Hcal):
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1).
```

Choose major-arc parameters `R=R(N)` and `eta=eta(N)` with the required
separation and W-uniformity conditions. Define:

```text
Major(R,eta)
  = { xi : xi is within eta of a/q for some (a,q)=1, 1 <= q <= R }

Minor(R,eta)
  = { xi != 0 } \ Major(R,eta).
```

Then the Fourier endpoint decomposes as:

```text
M_major(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Major(R,eta), xi != 0} |widehat{B_d}(xi)|^4

M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

The endpoint follows from the two analytic estimates:

```text
M_major(D) = o(1)
M_minor(D) = o(1)
```

uniformly for the required dyadic `D` range, after all local-model and transfer
packages have been applied.

On the major arcs, the required local model is the exact residual model
`Omega_w(d,h,k)`. Equivalently, in physical space the major-arc analysis must
match the inclusion-exclusion combination of all local singular models
`Theta_{w,S}` for the eight cube vertices. It is not enough to insert the full
eight-form model `Theta_w(d,h,k)`, and it is not enough to use only pair or
rectangle marginals.

On the minor arcs, the required estimate is fourth-moment spectral-density
cancellation for the derivative products `B_d(n)=f(n+d)conj(f(n))`, averaged
over the short shift `d`. This is stronger than pointwise pair-product
Fourier smallness and stronger than a mean tuple-count asymptotic.

Ordinary pair-BDH is insufficient because it controls a lower-order pair or
rectangle variance object, while `ResCube_3^sharp` is a centered fourth moment
of pair products and expands to an eight-vertex residual cube. It does not
automatically supply the nonzero-frequency fourth moment, the zero-frequency
subtraction, or the inclusion-exclusion local model `Omega_w`.

First-moment Hardy-Littlewood asymptotics are insufficient because the endpoint
needs variance-strength control after centering, uniformly over short `d` and
over major/minor Fourier regions. A first-moment count can identify the average
local density but does not control the residual fourth moment.

## 6. Edge cases

- Zero frequency: `xi=0` must be removed. Keeping it reintroduces `|c_d|^4`.
- Local model: the major arcs require `Omega_w`, not only the full cube model
  `Theta_w` and not only pair or rectangle marginals.
- Collision hyperplanes: coincidences among
  `n, n+d, n+h, n+h+d, n+k, n+k+d, n+h+k, n+h+k+d` must be separated or shown
  negligible.
- Boundary transfer: interval cutoffs, cyclic Fourier models, and dyadic
  cutoffs must be matched explicitly.
- W-trick compatibility: residue classes, W-shifts, and the order of limits
  must be preserved.
- Prime powers: von Mangoldt-style weights require a prime-power transfer or
  exclusion package.
- Major-arc overlap: the choice of `R` and `eta` must prevent double-counting
  or include a partition of unity.
- Range coverage: the estimates must hold uniformly for `D <= Hcal(N)`.
- Complex conjugation: the alternating pattern in `Q_d` must be preserved
  when passing between physical and Fourier forms.

## 7. Where it fits in the project map

Module 179 follows Module 178, which identified the centered derivative
`U^2` cube with the zero-frequency-removed eight-form residual cube.

This module is part of the direct analytic attack on the open `s=2`
rational-major endpoint:

```text
ResCube_3^sharp
  -> CPC_3^sharp
  -> RBDH_pair_short
  -> AU^3
```

The arrows remain conditional on exact local models, boundary transfer,
collision control, W-trick limit order, prime-power transfer, and range
coverage.

## 8. What remains open

The following are not proved in this module:

- major-arc cancellation after subtracting the exact residual model
  `Omega_w(d,h,k)`;
- minor-arc fourth-moment spectral-density cancellation for `B_d`;
- uniformity throughout the full short-shift range `D <= Hcal(N)`;
- transfer from smoothed or cyclic Fourier models to the sharp dyadic endpoint;
- the route from this residual cube target to all other endpoint formulations;
- any tail, high-count, harmonic-carrier, boundary, Liouville, or all-alpha
  closure.

## Red flags / forbidden upgrades

- Do not label this module `PROVEN`.
- Do not claim the original positive existence problem has been resolved.
- Do not claim an all-alpha theorem from this module.
- Do not claim the finite-type theorem is unconditional.
- Do not claim `RBDH_pair_short(Hcal)`, `CPC_3^sharp(Hcal)`, or `AU^3` is
  established here.
- Do not replace `Omega_w(d,h,k)` by only `Theta_w(d,h,k)`.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not use ordinary pair-BDH as a substitute for the fourth-moment residual
  cube estimate.
- Do not use first-moment Hardy-Littlewood asymptotics as a substitute for
  variance-strength residual control.
- Do not transfer smoothed, frozen, cyclic, or model-selector estimates to the
  actual sharp moving selector without the named transfer packages.
