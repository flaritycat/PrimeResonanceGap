# Module 198: Ordinary pair-BDH versus residual fourth-moment comparison

## 1. Precise theorem / claim being advanced

This module tests the scheduled Phase B shortcut:

```text
ordinary pair-BDH alone
  => minor-arc residual fourth-moment control for B_d.
```

The verdict is:

```text
The shortcut is blocked.
```

Ordinary pair-BDH, unless upgraded with residual decomposition, pair-margin
absorption, and adaptive minor-arc restriction control, does not supply the
Module 197 criterion:

```text
R_2^minor(rho;D) <= Psi_*(rho;D)
```

for:

```text
B_d(n)=f(n+d)conj(f(n)),   f=nu-1.
```

The useful output is a clean comparison: pair-BDH may control a centered pair
product `R_d`, but the residual minor-arc target is for `B_d`. Passing from
`R_d` to `B_d` requires a separate linear-margin package.

## 2. Status label

`FALSE / BLOCKED`

The false statement is the standalone implication from ordinary pair-BDH to
the Module 197 residual minor-arc density/energy criterion. A strengthened
pair route remains possible if the missing side packages are supplied.

## 3. Definitions and variables

As before:

```text
f = nu - 1
B_d(n) = f(n+d)conj(f(n))
widehat{B_d}(xi) = E_n B_d(n)e(-xi n)
```

The uncentered pair product is:

```text
P_d(n) = nu(n+d)conj(nu(n)).
```

Let `kappa_w(d)` denote the exact local pair model. The pair-centered object
is:

```text
R_d(n) = P_d(n) - kappa_w(d).
```

Since `nu=1+f`,

```text
P_d(n)
  = 1 + f(n+d) + conj(f(n)) + B_d(n).
```

Thus:

```text
R_d(n)
  = B_d(n) + L_d(n) + (1-kappa_w(d)),
```

where the linear margin is:

```text
L_d(n)=f(n+d)+conj(f(n)).
```

For nonzero frequencies:

```text
widehat{R_d}(xi)
  = widehat{B_d}(xi) + widehat{L_d}(xi),
```

and hence:

```text
widehat{B_d}(xi)
  = widehat{R_d}(xi) - widehat{L_d}(xi).
```

Define the minor-arc fourth moments:

```text
M_B^minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4,

M_R^minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{R_d}(xi)|^4,

M_L^minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{L_d}(xi)|^4.
```

The Module 197 adaptive restriction envelope is:

```text
R_{2,B}^minor(rho;D)
  = sup_{T_d subset Minor(R,eta), size_D(T)<=rho}
      (1/D) sum_{D<|d|<=2D}
        sum_{xi in T_d} |widehat{B_d}(xi)|^2.
```

Here:

```text
size_D(T) = (1/D) sum_{D<|d|<=2D} #T_d.
```

This module distinguishes three inputs that are often conflated:

```text
PairMean(d):      control of E_n P_d(n) against kappa_w(d),
PairBDH_R(d):     fourth-moment/autocorrelation control for R_d,
RABDH_B^minor:    adaptive minor-arc restriction control for B_d.
```

Only the last object directly supplies Module 197.

## 4. Assumptions

The comparison uses:

- the finite cyclic Fourier model or a transferred interval model;
- normalized Fourier transform;
- the dyadic shift range `D < |d| <= 2D`;
- zero frequency removed before minor-arc estimates are formed;
- the exact identity `P_d=1+f(n+d)+conj(f(n))+B_d`;
- no free selector, boundary, W-limit, or prime-power transfer.

No assumption is made that ordinary pair-BDH already includes pair-margin
absorption. If it does include that absorption plus exact residual transfer,
then it is no longer the ordinary shortcut being tested here.

## 5. Proof / disproof / reduction

### A. The zero-mode version is visibly too weak

If pair information means only:

```text
E_n P_d(n) approx kappa_w(d),
```

then it sees only the zero Fourier mode. A nonzero phase can have zero mean
and still have full `U^2` mass. In a finite Fourier model, the toy object:

```text
G(n)=e(xi_0 n),   xi_0 != 0,
```

satisfies:

```text
widehat{G}(0)=0,
sum_{xi != 0} |widehat{G}(xi)|^4 = 1.
```

Thus any route that only controls pair means cannot control the residual
nonzero Fourier fourth moment.

This is the Module 126 obstruction in the current notation.

### B. Pair-centered fourth moment controls R_d, not B_d

Suppose a stronger pair-BDH input gives:

```text
M_R^minor(D)=o(1),
```

or even the corresponding all-frequency version for `R_d`. This still does
not directly give:

```text
M_B^minor(D)=o(1),
```

because:

```text
widehat{B_d}(xi)
  = widehat{R_d}(xi) - widehat{L_d}(xi)
```

for `xi != 0`.

The deterministic inequality is:

```text
M_B^minor(D)
  <= 8 M_R^minor(D) + 8 M_L^minor(D).
```

Therefore pair-BDH for `R_d` would become useful only after supplying:

```text
M_L^minor(D)=o(1).
```

That is a pair-margin absorption or linear `U^2` package. It is a side input,
not a consequence of ordinary pair-BDH.

### C. Adaptive restriction needs an even sharper transfer

Module 197 requires energy control on arbitrary minor-arc frequency families:

```text
T_d subset Minor(R,eta).
```

For such a family:

```text
energy_B(T)
  <= 2 energy_R(T) + 2 energy_L(T),
```

where:

```text
energy_X(T)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in T_d} |widehat{X_d}(xi)|^2.
```

If `M_R^minor(D)` is known, then Cauchy gives a restriction envelope for
`R_d`:

```text
energy_R(T)
  <= size_D(T)^(1/2) M_R^minor(D)^(1/2).
```

But this says nothing about `energy_L(T)`. Hence:

```text
R_{2,B}^minor(rho;D)
```

is not bounded by ordinary pair-BDH unless the linear margin also has an
adaptive minor-arc restriction envelope:

```text
R_{2,L}^minor(rho;D)
  <= Psi_{L,*}(rho;D),
```

with a density/energy integral small enough to match Module 197. This is the
exact failure point for the Module 197 criterion.

### D. Minimal strengthened route

A pair route to the residual minor-arc target must be upgraded to at least:

```text
PairBDH_R^minor:
  M_R^minor(D)=o(1),

LinearMarginMinor:
  M_L^minor(D)=o(1),

or, for Module 197 directly,

AdaptiveResidualMinor:
  R_{2,B}^minor(rho;D) <= Psi_*(rho;D)
```

with the density/energy integral from Module 197.

In other words:

```text
ordinary pair-BDH alone      blocked
pair-BDH + margin absorption conditional route
adaptive residual minor BDH  direct Module 197 route
```

The project should not cite the first line as if it were the second or third.

## 6. Edge cases

- If "pair-BDH" is defined to include exact residual decomposition, pair-margin
  absorption, local-model matching, and selector transfer, then it is no
  longer ordinary pair-BDH. It has become a renamed endpoint package.
- A global fourth moment for `R_d` controls minor arcs for `R_d`, but not for
  `B_d` without the linear margin.
- Cancellation between `widehat{B_d}` and `widehat{L_d}` can make
  `widehat{R_d}` small while `widehat{B_d}` is large. The triangle inequality
  shows the missing term explicitly.
- Zero frequency must be removed. Pair means and residual fourth moments live
  on different Fourier modes after centering.
- The constant term `1-kappa_w(d)` disappears from nonzero Fourier
  frequencies, but it still matters in any physical-space statement before
  centering.
- Major-arc leakage is not addressed here; all sets `T_d` must lie inside the
  chosen minor arcs.
- Boundary, smoothing, and cyclic transfer may change the exact Fourier
  identity and must be checked separately.
- The argument is an obstruction to a proof route, not a counterexample inside
  the actual primes.

## 7. Where it fits in the project map

Module 198 follows Module 197:

```text
Module 197
  -> adaptive density/energy criterion for B_d
Module 198
  -> ordinary pair-BDH cannot supply that criterion by itself.
```

It also updates the older Module 126 obstruction:

```text
Pair-BDH alone is not enough
  -> now expressed at the residual derivative cube minor-arc level.
```

The next scheduled step is to test the nearby shortcuts involving
rectangle-BDH and first-moment Hardy-Littlewood input.

## 8. What remains open

This module does not prove:

- `M_R^minor(D)=o(1)` for the actual pair-centered object;
- `M_L^minor(D)=o(1)` for the linear margin;
- `R_{2,B}^minor(rho;D) <= Psi_*(rho;D)`;
- the Module 197 density bound or low-level `L^2` envelope;
- any major-arc estimate using `Omega_w`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay for `B_d`;
- transfer to actual sharp moving selectors;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem, all-alpha theorem, or
  unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite ordinary pair-BDH as a proof of the residual fourth-moment
  target.
- Do not confuse `R_d=P_d-kappa_w(d)` with `B_d=f(n+d)conj(f(n))`.
- Do not drop the linear margin `L_d`.
- Do not treat a zero-mode pair estimate as nonzero Fourier control.
- Do not treat an all-frequency estimate for `R_d` as an adaptive
  minor-arc restriction estimate for `B_d`.
- Do not call the strengthened route `ordinary pair-BDH`; name every side
  package it uses.
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
