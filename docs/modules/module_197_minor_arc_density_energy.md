# Module 197: Minor-arc density/energy criterion for B_d

## 1. Precise theorem / claim being advanced

This module refines the minor-arc large-spectrum criterion from Module 180 into
a density/energy criterion.

The minor-arc fourth-moment target is:

```text
M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4
  = o(1).
```

Module 180 expressed this through the cardinality of the large spectrum. The
present module records the sharper energy-tail identity:

```text
M_minor(D)
  = integral_0^infty
      2 lambda E_minor(>=lambda;D) dlambda,
```

where:

```text
E_minor(>=lambda;D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Spec_d^minor(lambda)}
        |widehat{B_d}(xi)|^2.
```

It then gives a conditional criterion: the minor-arc estimate follows if
large-spectrum density bounds are paired with a uniform minor-arc restriction
envelope controlling how much Fourier `L^2` energy can concentrate on sets of
that density.

## 2. Status label

`CONDITIONAL`

The energy-tail identity is deterministic. The conclusion `M_minor(D)=o(1)`
is conditional on the density and restriction-energy hypotheses stated below.
Those hypotheses are not proved in this module.

## 3. Definitions and variables

As in Modules 179-180:

```text
f = nu - 1
B_d(n) = f(n+d) conj(f(n))
c_d = E_n B_d(n)
B_d^circ(n) = B_d(n) - c_d
widehat{B_d}(xi) = E_n B_d(n) e(-xi n)
```

The minor arcs are:

```text
Minor(R,eta) = { xi != 0 } \ Major(R,eta).
```

For `lambda > 0`, define:

```text
Spec_d^minor(lambda)
  = { xi in Minor(R,eta) : |widehat{B_d}(xi)| >= lambda }.
```

The averaged density-count profile is:

```text
L_minor(lambda;D)
  = (1/D) sum_{D<|d|<=2D} #Spec_d^minor(lambda).
```

The averaged energy-tail profile is:

```text
E_minor(>=lambda;D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Spec_d^minor(lambda)}
        |widehat{B_d}(xi)|^2.
```

For an arbitrary family of minor-arc frequency sets:

```text
T = { T_d subset Minor(R,eta) }_{D<|d|<=2D},
```

write:

```text
size_D(T) = (1/D) sum_{D<|d|<=2D} #T_d,

energy_D(T)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in T_d} |widehat{B_d}(xi)|^2.
```

The minor-arc restriction envelope at averaged count `rho` is:

```text
R_2^minor(rho;D)
  = sup_{T_d subset Minor(R,eta), size_D(T)<=rho} energy_D(T).
```

This is an actual envelope for the active `B_d`; a usable proof must bound it
by an external estimate, not by circular knowledge of the desired fourth
moment.

## 4. Assumptions

The deterministic part assumes:

- the finite Fourier model or a transferred interval model;
- normalized Fourier transform;
- the dyadic shift range `D < |d| <= 2D`;
- the major/minor decomposition from Module 179;
- zero frequency has already been excluded.

The conditional minor-arc criterion assumes that there are functions:

```text
lambda_0 = lambda_0(N,w,D,R,eta),
A_N      = A_N(w,D,R,eta),
Lambda_* = Lambda_*(lambda;D),
Psi_*    = Psi_*(rho;D),
```

such that:

```text
|widehat{B_d}(xi)| <= A_N
```

on the chosen finite model, and uniformly over the required dyadic `D` range:

```text
lambda_0^2 E2_minor(D) = o(1),
```

where:

```text
E2_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^2.
```

The density profile satisfies:

```text
L_minor(lambda;D) <= Lambda_*(lambda;D)
  for lambda_0 <= lambda <= A_N.
```

The restriction-energy envelope satisfies:

```text
R_2^minor(rho;D) <= Psi_*(rho;D)
```

for all values of `rho` in the range of `Lambda_*`.

Finally, the density/restriction integral is small:

```text
integral_{lambda_0}^{A_N}
  2 lambda Psi_*(Lambda_*(lambda;D);D) dlambda
  = o(1).
```

## 5. Proof / disproof / reduction

For a nonnegative number `a`,

```text
a^4 = integral_0^infty 2 lambda a^2 1_{a>=lambda} dlambda.
```

Apply this with:

```text
a = |widehat{B_d}(xi)| 1_{xi in Minor(R,eta)}.
```

Summing over minor-arc frequencies and averaging over `d` gives:

```text
M_minor(D)
  = integral_0^infty
      2 lambda E_minor(>=lambda;D) dlambda.
```

Split the integral at `lambda_0`. The low-level part obeys:

```text
integral_0^{lambda_0}
  2 lambda E_minor(>=lambda;D) dlambda
  <= lambda_0^2 E2_minor(D)
  = o(1).
```

For `lambda >= lambda_0`, take:

```text
T_d = Spec_d^minor(lambda).
```

Then:

```text
size_D(T) = L_minor(lambda;D) <= Lambda_*(lambda;D),
```

and therefore, by the restriction envelope:

```text
E_minor(>=lambda;D)
  = energy_D(T)
  <= R_2^minor(L_minor(lambda;D);D)
  <= Psi_*(Lambda_*(lambda;D);D),
```

assuming `Psi_*` is taken monotone in `rho`, or replaced by its monotone
majorant. Hence:

```text
integral_{lambda_0}^{A_N}
  2 lambda E_minor(>=lambda;D) dlambda
  <= integral_{lambda_0}^{A_N}
       2 lambda Psi_*(Lambda_*(lambda;D);D) dlambda
  = o(1).
```

The contribution above `A_N` is empty by definition of the upper Fourier
envelope. Therefore:

```text
M_minor(D)=o(1).
```

Equivalently, in dyadic form, it is enough to prove:

```text
lambda_0^2 E2_minor(D)
  + C sum_{lambda_j in [lambda_0,A_N]}
        lambda_j^2 Psi_*(Lambda_*(lambda_j;D);D)
  = o(1).
```

This criterion improves the bookkeeping from Module 180. A large-spectrum
count alone controls only how many large coefficients exist. The endpoint
needs to know how much Fourier energy those sets can capture.

### Why ordinary inputs are still insufficient

Ordinary pair-BDH is not the same as the restriction envelope
`R_2^minor(rho;D)`. Pair-BDH may control an averaged pair variance or a
second-order Fourier quantity, but here the sets `T_d` may be chosen
adaptively from the large spectrum of the pair product:

```text
B_d(n)=f(n+d)conj(f(n)).
```

The criterion requires uniform control over arbitrary minor-arc frequency
families of prescribed density, averaged in the short shift `d`. That is a
higher-order spectral concentration statement.

First-moment Hardy-Littlewood asymptotics are also insufficient. They can
predict average tuple densities, but they do not bound:

```text
sum_{xi in T_d} |widehat{B_d}(xi)|^2
```

for adaptive minor-arc sets `T_d`, nor do they provide the zero-frequency
subtraction, short-shift averaging, or variance-strength residual control
needed for the fourth moment.

## 6. Edge cases

- Zero frequency: `xi=0` must be excluded before defining the minor spectrum.
- Major-arc leakage: `Minor(R,eta)` must be separated from small-denominator
  frequencies or defined by a partition of unity.
- Circularity: the restriction envelope must hold for arbitrary `T_d` of the
  stated density, not only for a fixed set chosen independently of `B_d`.
- Monotonicity: if `Psi_*` is not monotone in `rho`, replace it by its monotone
  majorant before inserting `Lambda_*`.
- Low-level leakage: `lambda_0^2 E2_minor(D)=o(1)` is a real requirement, not
  automatic from density decay.
- Unbounded weights: `A_N` must account for the size of the W-tricked prime
  weight and any cutoff normalization.
- Rare bad shifts: estimates must be averaged over `D < |d| <= 2D`; a small
  exceptional set of shifts is harmless only if its energy contribution is
  included in `Psi_*` or the low-level envelope.
- Boundary transfer: interval-to-cyclic transfers may change the available
  frequency sets and must be recorded separately.
- W-limit order: any `o(1)` must respect the project order `N -> infinity`
  first, then `w -> infinity`, unless a later module states a different
  diagonal with proof.

## 7. Where it fits in the project map

Module 197 begins Phase B of the long-term plan:

```text
Module 179
  -> Fourier major/minor decomposition
Module 180
  -> minor-arc large-spectrum count criterion
Module 197
  -> minor-arc density/energy restriction criterion.
```

The next comparison should test whether existing objects such as ordinary
pair-BDH can supply this density/energy restriction. The expected answer is
negative unless the pair-BDH input is upgraded to a residual, adaptive,
minor-arc restriction estimate for the products `B_d`.

## 8. What remains open

This module does not prove:

- the density bound `L_minor(lambda;D) <= Lambda_*(lambda;D)`;
- the restriction-energy bound
  `R_2^minor(rho;D) <= Psi_*(rho;D)`;
- the low-level envelope `lambda_0^2 E2_minor(D)=o(1)`;
- any major-arc estimate using `Omega_w`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay unconditionally;
- transfer to actual sharp moving selectors;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem, all-alpha theorem, or
  unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite this module as a proof of minor-arc cancellation.
- Do not treat `R_2^minor(rho;D)` as bounded unless an external restriction
  estimate is supplied.
- Do not replace adaptive minor-arc energy control by ordinary pair-BDH.
- Do not replace variance-strength spectral control by first-moment
  Hardy-Littlewood asymptotics.
- Do not ignore the low-level `L^2` term.
- Do not include major-arc frequencies or the zero frequency in the minor
  spectrum.
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
