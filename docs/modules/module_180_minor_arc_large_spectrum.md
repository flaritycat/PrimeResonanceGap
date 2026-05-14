# Module 180: Minor-arc large-spectrum criterion for the residual derivative cube

## 1. Precise theorem / claim being advanced

This module isolates the minor-arc part of Module 179 as a large-spectrum
counting problem. It does not prove the minor-arc estimate. It gives an exact
layer-cake identity and a dyadic sufficient criterion that any successful
minor-arc proof may target.

Let:

```text
M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

For `lambda > 0`, define the minor-arc large spectrum:

```text
Spec_d^minor(lambda)
  = { xi in Minor(R,eta) : |widehat{B_d}(xi)| >= lambda }.
```

Then:

```text
M_minor(D)
  = integral_0^infty
      4 lambda^3
      (1/D) sum_{D<|d|<=2D} #Spec_d^minor(lambda)
    dlambda.
```

Consequently, the minor-arc endpoint follows if the averaged minor-arc large
spectrum has enough decay in `lambda`, together with the necessary low-level
`L^2` envelope.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The layer-cake identity and dyadic reduction are deterministic. The required
large-spectrum decay is an open analytic input.

## 3. Definitions and variables

As in Modules 178 and 179:

```text
f = nu - 1
B_d(n) = f(n+d) conj(f(n))
c_d = E_n B_d(n)
B_d^circ(n) = B_d(n) - c_d
Q_d = E_{n,h,k} B_d(n) conj(B_d(n+h)) conj(B_d(n+k)) B_d(n+h+k)
```

Use normalized Fourier transform:

```text
widehat{B_d}(xi) = E_n B_d(n) e(-xi n).
```

The residual local model remains:

```text
Omega_w(d,h,k)
  = sum_{S subset {0,1}^3} (-1)^(8-|S|) Theta_{w,S}(d,h,k).
```

Major and minor arcs are as in Module 179:

```text
Major(R,eta)
  = { xi : xi is within eta of a/q for some (a,q)=1, 1 <= q <= R }

Minor(R,eta)
  = { xi != 0 } \ Major(R,eta).
```

For a dyadic block `D < |d| <= 2D`, define:

```text
L_minor(lambda;D)
  = (1/D) sum_{D<|d|<=2D} #Spec_d^minor(lambda).
```

Also define the averaged minor-arc `L^2` envelope:

```text
E2_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^2.
```

## 4. Assumptions

The deterministic extraction assumes only:

- the finite Fourier model or an already transferred interval Fourier model;
- the major/minor decomposition from Module 179;
- finite frequency support for each `N`;
- the short-shift range `D <= Hcal(N)`.

To turn the extraction into the estimate `M_minor(D)=o(1)`, one still needs:

- a low-level threshold `lambda_0=lambda_0(N)` with
  `lambda_0^2 E2_minor(D)=o(1)`;
- averaged large-spectrum decay above `lambda_0`;
- uniformity in `D`, `R`, `eta`, `w`, and the cutoff transfer.

## 5. Proof / disproof / reduction

For any finite family of nonnegative numbers `a_xi`,

```text
sum_xi a_xi^4
  = integral_0^infty 4 lambda^3 # { xi : a_xi >= lambda } dlambda.
```

Apply this with:

```text
a_xi = |widehat{B_d}(xi)| 1_{xi in Minor(R,eta)}
```

and average over `D < |d| <= 2D`. This gives:

```text
M_minor(D)
  = integral_0^infty 4 lambda^3 L_minor(lambda;D) dlambda.
```

For a dyadic sufficient criterion, choose a low threshold `lambda_0` and a
dyadic grid `lambda_j` covering the range `lambda_0 <= lambda <= A(N)`, where
`A(N)` is any deterministic upper envelope for `|widehat{B_d}(xi)|` on the
model under discussion. Then:

```text
M_minor(D)
  <= lambda_0^2 E2_minor(D)
     + 16 sum_{lambda_j >= lambda_0}
          lambda_j^4 L_minor(lambda_j;D).
```

The first term is the low-level contribution, using:

```text
|widehat{B_d}(xi)|^4
  <= lambda_0^2 |widehat{B_d}(xi)|^2
  when |widehat{B_d}(xi)| < lambda_0.
```

The second term groups the remaining coefficients dyadically. Therefore a
minor-arc proof may proceed by proving:

```text
lambda_0^2 E2_minor(D) = o(1)
```

and:

```text
sum_{lambda_j >= lambda_0}
  lambda_j^4 L_minor(lambda_j;D) = o(1).
```

A stronger but simpler sufficient route is:

```text
sup_{xi in Minor(R,eta)} |widehat{B_d}(xi)| = o(1)
```

on average in `d`, together with a uniform averaged `L^2` envelope. This route
is usually too strong to expect without careful W-tricked input, but it shows
why isolated pointwise Fourier smallness is not by itself the endpoint.

## 6. Edge cases

- Low-level leakage: the contribution below `lambda_0` is harmless only with a
  usable `L^2` envelope.
- Threshold range: `A(N)` must match the selected Fourier model and any
  unboundedness in `nu`.
- Major-arc leakage: frequencies near small rationals must not be counted as
  minor arcs by a poorly separated choice of `R` and `eta`.
- Zero frequency: `xi=0` is excluded before the large-spectrum decomposition.
- Boundary transfer: interval/cyclic Fourier comparisons can change the shape
  of large spectra unless the cutoff package is explicit.
- W-trick order: any large-spectrum bound must survive `N -> infinity` first,
  then `w -> infinity`.
- Collision hyperplanes: large spectra caused by degenerate eight-form
  collisions must be separated from genuine minor-arc cancellation.
- Prime powers: Fourier envelopes for `nu` may include prime-power artifacts
  unless transferred or removed.

## 7. Where it fits in the project map

Module 178 identifies the centered derivative cube. Module 179 splits the
Fourier fourth moment into major and minor arcs. Module 180 refines the
minor-arc branch into a large-spectrum counting target:

```text
ResCube_3^sharp
  -> nonzero Fourier fourth moment
  -> major/minor split
  -> minor large-spectrum decay plus L^2 envelope.
```

The major-arc branch still routes through the exact residual model
`Omega_w(d,h,k)`.

## 8. What remains open

This module does not prove:

- the averaged large-spectrum decay
  `sum lambda_j^4 L_minor(lambda_j;D)=o(1)`;
- the low-level `L^2` envelope in the full W-tricked range;
- any major-arc estimate with `Omega_w`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- any transfer to actual sharp moving selectors;
- any tail, high-count, Liouville, harmonic-carrier, or all-alpha closure.

## Red flags / forbidden upgrades

- Do not call this a proof of the minor-arc endpoint.
- Do not replace large-spectrum decay by first-moment Hardy-Littlewood counts.
- Do not claim ordinary pair-BDH controls the fourth-moment residual cube.
- Do not forget the low-level `L^2` envelope.
- Do not let major-arc frequencies leak into the minor-arc spectrum.
- Do not replace `Omega_w(d,h,k)` by only the full eight-form model
  `Theta_w(d,h,k)` on the major side.
- Do not transfer model/cyclic/smoothed estimates to the actual sharp moving
  selector without the full transfer package.
