# Module 200: Dyadic derivative U^2 route to minor arcs

## 1. Precise theorem / claim being advanced

This module tests whether the dyadic derivative `U^2` formulation gives a new
route to the minor-arc branch.

The verdict is:

```text
Dyadic derivative U^2 is an exact reformulation of the residual Fourier
fourth moment. It gives the minor-arc estimate only after a frequency-localized
derivative input is added.
```

In particular, if:

```text
Delta_d f(n)=f(n+d)conj(f(n))=B_d(n),
```

and `Pi_minor` denotes Fourier projection onto `Minor(R,eta)`, then:

```text
(1/D) sum_{D<|d|<=2D} ||Pi_minor Delta_d f||_{U^2}^4
  =
(1/D) sum_{D<|d|<=2D}
  sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

Thus the dyadic derivative route is not blocked, but it is not an independent
estimate. It must supply a new theorem controlling the minor-arc projection of
the derivative.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The identities and route separation are deterministic. No analytic
minor-arc decay is proved here.

## 3. Definitions and variables

Work in the finite cyclic Fourier model or an already transferred interval
model. Let:

```text
f = nu - 1
Delta_d f(n)=f(n+d)conj(f(n))
B_d(n)=Delta_d f(n)
c_d=E_n B_d(n)
B_d^circ(n)=B_d(n)-c_d
```

Use normalized Fourier transform:

```text
widehat{B_d}(xi)=E_n B_d(n)e(-xi n).
```

Let:

```text
Major(R,eta)
  = { xi : xi is within eta of a/q for (a,q)=1, 1 <= q <= R },

Minor(R,eta)
  = { xi != 0 } \ Major(R,eta).
```

Define Fourier projections:

```text
Pi_major B_d = sum_{xi in Major(R,eta), xi != 0}
                 widehat{B_d}(xi)e(xi n),

Pi_minor B_d = sum_{xi in Minor(R,eta)}
                 widehat{B_d}(xi)e(xi n).
```

The dyadic derivative `U^2` quantities are:

```text
DDU2(D)
  = (1/D) sum_{D<|d|<=2D} ||B_d^circ||_{U^2}^4,

DDU2_major(D;R,eta)
  = (1/D) sum_{D<|d|<=2D} ||Pi_major B_d||_{U^2}^4,

DDU2_minor(D;R,eta)
  = (1/D) sum_{D<|d|<=2D} ||Pi_minor B_d||_{U^2}^4.
```

The corresponding Fourier targets are:

```text
M_major(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Major(R,eta), xi != 0} |widehat{B_d}(xi)|^4,

M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

The exact residual local model on the physical cube remains:

```text
Omega_w(d,h,k)
  = sum_{S subset {0,1}^3} (-1)^(8-|S|) Theta_{w,S}(d,h,k).
```

## 4. Assumptions

The extraction assumes:

- normalized Fourier inversion and Parseval;
- the dyadic short-shift range `D < |d| <= 2D`;
- zero frequency removed before the endpoint is formed;
- major/minor arcs as in Module 179;
- all interval-to-cyclic, boundary, W-trick, and selector transfers are kept
  explicit;
- no analytic estimate is imported from endpoint equivalence alone.

Any analytic dyadic derivative route must additionally supply a named
frequency-localized input, such as:

```text
DerivativeMinorU2_B(D;R,eta):
  DDU2_minor(D;R,eta)=o(1),
```

or the Module 197 density/energy criterion for the same projected derivative.

## 5. Proof / disproof / reduction

### A. The exact dyadic derivative identity

By the `U^2` Fourier identity:

```text
||B_d^circ||_{U^2}^4
  = sum_{xi != 0} |widehat{B_d}(xi)|^4.
```

Since the major and minor arcs partition the nonzero frequencies:

```text
DDU2(D)
  = DDU2_major(D;R,eta) + DDU2_minor(D;R,eta)
  = M_major(D) + M_minor(D).
```

Also, applying the Fourier projection before taking the `U^2` norm gives:

```text
||Pi_minor B_d||_{U^2}^4
  = sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

Therefore:

```text
DDU2_minor(D;R,eta)=M_minor(D).
```

This is exact and useful, but it is not a new estimate.

### B. What the derivative formulation does and does not add

The dyadic derivative formulation highlights that the endpoint is an averaged
`U^2` problem for:

```text
Delta_d f(n)=f(n+d)conj(f(n)).
```

This may be useful if one has tools for derivatives, inverse theorems, or
frequency-localized correlation estimates.

However, without a new theorem, the statement:

```text
DDU2_minor(D;R,eta)=o(1)
```

is merely:

```text
M_minor(D)=o(1)
```

written in derivative language. It does not bypass the large-spectrum,
adaptive-energy, linear-margin, local-model, or selector-transfer issues from
Modules 197-199.

### C. The physical box form hides the major/minor split

Expanding the unprojected derivative `U^2` norm gives:

```text
E_{n,h,k}
  B_d(n) conj(B_d(n+h)) conj(B_d(n+k)) B_d(n+h+k),
```

which is the eight-vertex residual cube from Module 178. This physical-space
form is excellent for local-model analysis, but it does not display the
major/minor Fourier split.

To isolate minor arcs, the Fourier projection must appear:

```text
Pi_minor Delta_d f.
```

That projection is nonlocal in physical space. It cannot be replaced by an
unprojected box estimate unless a separate major/minor decomposition theorem
justifies the replacement.

### D. Conditional route supplied by derivative language

A non-tautological dyadic derivative route should prove one of the following:

```text
DerivativeMinorU2_B:
  (1/D) sum_d ||Pi_minor Delta_d f||_{U^2}^4=o(1);

DerivativeLargeSpectrum_B:
  large Fourier coefficients of Delta_d f occur only on major arcs,
  except for a density/energy tail satisfying Module 197;

DerivativeRestriction_B:
  R_{2,B}^minor(rho;D) <= Psi_*(rho;D)
  with the Module 197 density/energy integral;

DerivativeInverseNoMinor:
  if ||Pi_minor Delta_d f||_{U^2} is large on average,
  then Delta_d f correlates with a forbidden minor-arc phase,
  and those correlations are ruled out.
```

Any of these would be genuine analytic progress. Merely citing
`DyadicDerivativeU^2` as endpoint-equivalent would not.

### E. Relation to AU^3

The anisotropic `AU^3` / box formulation is another way to arrange the same
eight vertices:

```text
n, n+d, n+h, n+h+d, n+k, n+k+d, n+h+k, n+h+k+d.
```

This equivalence is structural modulo the side packages in the project ledger.
It does not prove minor-arc decay. A projected `AU^3` or projected derivative
statement would still need to control:

```text
Pi_minor Delta_d f.
```

## 6. Edge cases

- Centering matters. `B_d^circ` removes exactly `xi=0`; the minor projection
  is defined only after zero frequency is excluded.
- `Pi_minor Delta_d f` is not the same as differentiating a minor-arc
  projection of `f`. The derivative and projection do not commute in any
  useful free way.
- An all-frequency dyadic derivative `U^2` theorem would close the endpoint,
  but that theorem is precisely an open endpoint-grade input.
- A physical-space cube estimate without projection does not isolate minor
  arcs.
- Major-arc local models still require `Omega_w`, not only `Theta_w`,
  `Sigma_w`, or `kappa_w`.
- The dyadic range `D <= Hcal(N)` remains part of the target.
- Boundary, W-limit order, prime powers, and selector transfer remain outside
  the structural identity.
- Exceptional shifts must be controlled by averaged `U^2` mass, not only by
  counting bad `d`.

## 7. Where it fits in the project map

Module 200 follows the Phase B insufficiency audit:

```text
Module 197
  -> adaptive density/energy criterion
Module 198
  -> ordinary pair-BDH shortcut blocked
Module 199
  -> ordinary rectangle/HL shortcuts blocked
Module 200
  -> dyadic derivative U^2 is useful only with projected derivative input.
```

The next scheduled step is:

```text
Module 201
  -> minor-arc spectral large-spectrum obstruction map.
```

That module should ask what a large value of:

```text
DDU2_minor(D;R,eta)
```

would force spectrally.

## 8. What remains open

This module does not prove:

- `DerivativeMinorU2_B`;
- the Module 197 density/energy criterion;
- `R_{2,B}^minor(rho;D) <= Psi_*(rho;D)`;
- any large-spectrum exclusion on minor arcs;
- any major-arc estimate using `Omega_w`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay;
- transfer to actual sharp moving selectors;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem, all-alpha theorem, or
  unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat endpoint equivalence as an analytic estimate.
- Do not cite dyadic derivative `U^2` as a proof of minor-arc cancellation.
- Do not omit the projection `Pi_minor` when discussing minor arcs.
- Do not move projection from `Delta_d f` to `f` without a lemma.
- Do not replace the residual derivative cube model `Omega_w` by only the full
  eight-form model.
- Do not use first-moment HL, ordinary pair-BDH, or ordinary rectangle-BDH as a
  substitute for projected derivative control.
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
