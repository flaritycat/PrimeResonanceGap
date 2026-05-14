# Module 199: Rectangle/BDH and first-moment HL insufficiency audit

## 1. Precise theorem / claim being advanced

This module audits two tempting shortcuts after Modules 197-198:

```text
ordinary rectangle-BDH
  => adaptive residual minor-arc energy control for B_d,

first-moment Hardy-Littlewood
  => variance-strength residual fourth-moment control.
```

The verdict is:

```text
Both shortcuts are blocked unless upgraded by named residual, margin,
adaptive, and variance-strength packages.
```

This does not reject endpoint-grade `RBDH_pair_short(Hcal)`. The endpoint
class still treats a sufficiently exact rectangle-BDH engine, with all side
packages, as a possible route. What is blocked is using a weaker rectangle
variance, mean rectangle-HL, or first-moment tuple asymptotic as if it were the
Module 197 minor-arc restriction estimate for:

```text
B_d(n)=f(n+d)conj(f(n)).
```

## 2. Status label

`FALSE / BLOCKED`

The false statements are the shortcut implications above. Strengthened
rectangle or Hardy-Littlewood packages remain possible conditional routes if
they supply the exact residual, adaptive, W-uniform, variance-strength
requirements.

## 3. Definitions and variables

As in Modules 179, 197, and 198:

```text
f = nu - 1
B_d(n)=f(n+d)conj(f(n))
P_d(n)=nu(n+d)conj(nu(n))
R_d(n)=P_d(n)-kappa_w(d)
L_d(n)=f(n+d)+conj(f(n))
```

For nonzero frequencies:

```text
widehat{B_d}(xi)
  = widehat{R_d}(xi) - widehat{L_d}(xi).
```

The Module 197 target is the adaptive minor-arc restriction envelope:

```text
R_{2,B}^minor(rho;D)
  = sup_{T_d subset Minor(R,eta), size_D(T)<=rho}
      (1/D) sum_{D<|d|<=2D}
        sum_{xi in T_d} |widehat{B_d}(xi)|^2.
```

A rectangle autocorrelation for the uncentered pair product is:

```text
A_d(h)
  = E_n P_d(n+h)conj(P_d(n)).
```

The exact rectangle local model is:

```text
Sigma_w(d,h).
```

The ordinary rectangle residual is:

```text
C_d^{rect}(h)=A_d(h)-Sigma_w(d,h).
```

An ordinary rectangle-BDH-type estimate has the schematic form:

```text
RectBDH_P(D):
  (1/D) sum_{D<|d|<=2D} E_h |C_d^{rect}(h)|^2 = o(1).
```

A first-moment rectangle Hardy-Littlewood estimate has the weaker schematic
form:

```text
MeanRectHL_P(D):
  (1/D) sum_{D<|d|<=2D} E_h C_d^{rect}(h) = o(1),
```

or an equivalent averaged tuple-count asymptotic without absolute square.

For the residual cube, the exact local model is not `Sigma_w`. It is the
inclusion-exclusion eight-vertex residual model:

```text
Omega_w(d,h,k)
  = sum_{S subset {0,1}^3} (-1)^(8-|S|) Theta_{w,S}(d,h,k).
```

## 4. Assumptions

The audit assumes:

- the finite cyclic Fourier model or a transferred interval model;
- normalized Fourier transform;
- the short dyadic range `D < |d| <= 2D`;
- zero frequency removed before the residual minor-arc target is formed;
- major/minor arcs as in Module 179;
- the exact local models `kappa_w`, `Sigma_w`, `Theta_{w,S}`, and `Omega_w`;
- no free passage between `P_d`, `R_d`, and `B_d`;
- no free passage from first moments to variances;
- no free selector, boundary, W-limit, or prime-power transfer.

## 5. Proof / disproof / reduction

### A. Mean rectangle-HL does not give rectangle-BDH

The implication:

```text
MeanRectHL_P(D) => RectBDH_P(D)
```

is blocked by the standard mean-versus-variance obstruction. A toy residual:

```text
C_d^{rect}(h)=e(eta h),   eta != 0,
```

has zero mean in `h` but:

```text
E_h |C_d^{rect}(h)|^2 = 1.
```

Thus first-moment rectangle information can identify the average local
density but does not control the variance in `h`. Rectangle-BDH is an `L^2_h`
statement. First-moment HL is not.

This is the current residual-cube version of the older project warning:

```text
mean rectangle-HL does not imply rectangle-BDH.
```

### B. Ordinary rectangle-BDH controls the wrong residual object

Even if an ordinary rectangle-BDH statement controls:

```text
C_d^{rect}(h)
  = E_n P_d(n+h)conj(P_d(n)) - Sigma_w(d,h),
```

it is still a statement about the uncentered pair product `P_d` and the
rectangle model `Sigma_w`. The minor-arc target of Modules 179 and 197 is for:

```text
B_d(n)=f(n+d)conj(f(n)).
```

The passage:

```text
P_d -> R_d -> B_d
```

requires at least:

```text
pair-centering by kappa_w(d),
linear-margin absorption for L_d,
zero-frequency removal,
major/minor separation,
boundary and selector transfer.
```

Without these packages, a rectangle estimate for `P_d` cannot be cited as a
minor-arc estimate for `B_d`.

### C. Aggregate fourth moment is not adaptive restriction energy

Suppose one had a rectangle route strong enough to imply an aggregate
minor-arc fourth moment:

```text
M_B^minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4
  = o(1).
```

Then Module 197 is unnecessary for that route; the minor-arc target is already
closed. But ordinary rectangle-BDH is usually not supplied in this residual
minor-arc form.

If the route instead tries to use Module 197, it must control arbitrary
minor-arc frequency families:

```text
T_d subset Minor(R,eta).
```

The needed envelope is:

```text
R_{2,B}^minor(rho;D) <= Psi_*(rho;D).
```

An `L^2_h` rectangle variance does not automatically give this adaptive
Fourier restriction envelope. To get it from a fourth-moment bound, one uses
Cauchy:

```text
energy_B(T)
  <= size_D(T)^(1/2) M_B^minor(D)^(1/2).
```

But that requires a bound for the residual object `B_d` itself. A rectangle
bound for `P_d`, or a mean HL count for rectangles, is not enough.

### D. First-moment HL does not supply the residual local model

A generic first-moment Hardy-Littlewood statement for finite-complexity
tuples may produce average asymptotics for selected linear forms. The residual
cube needs more:

```text
Omega_w(d,h,k)
  = sum_S (-1)^(8-|S|) Theta_{w,S}(d,h,k),
```

and then a variance-strength or absolute-error statement after this
inclusion-exclusion. Matching the full eight-form local model alone is not the
same as matching the residual cube, and matching averages is not the same as
controlling:

```text
sum_{xi in T_d} |widehat{B_d}(xi)|^2
```

or:

```text
sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

This is why first-moment HL does not replace either:

```text
ProjectedLocalMatch_3^major
```

on the major side or:

```text
R_{2,B}^minor(rho;D) <= Psi_*(rho;D)
```

on the minor side.

### E. Minimal strengthened objects

A legitimate rectangle/HL route must name at least one of the following:

```text
ExactResidualRectBDH_B:
  an actual residual rectangle/fourth-moment estimate for B_d
  after kappa, Sigma, and linear-margin transfer;

AdaptiveResidualMinor_B:
  R_{2,B}^minor(rho;D) <= Psi_*(rho;D)
  with the Module 197 density/energy integral;

VarianceStrengthHL_8^res:
  subset-by-subset residual HL for Omega_w
  with averaged absolute or L^2 error strong enough for the cube;

FullEndpointRBDH_pair_short:
  the project endpoint package, including local models, margin absorption,
  selector transfer, W-limit order, boundary, prime-power, and range coverage.
```

Anything weaker is a heuristic or a partial input, not a closure of the
minor-arc residual fourth moment.

## 6. Edge cases

- A true endpoint-grade `RBDH_pair_short(Hcal)` is not being rejected here.
  The blocked object is an ordinary or underspecified rectangle-BDH shortcut.
- If rectangle-BDH is defined to include exact residual transfer to `B_d`,
  linear-margin absorption, adaptive minor-arc restriction, and selector
  transfer, it has become a renamed endpoint package.
- Mean rectangle-HL can still be useful for identifying local models; it just
  cannot replace variance estimates.
- A bound for the full frequency fourth moment of `B_d` would imply the
  minor-arc target, but this module does not supply such a bound.
- Major-arc local models require `Omega_w`, not only `Sigma_w` or the full
  eight-form model `Theta_w`.
- Weighted, smoothed, or cyclic rectangle estimates cannot be moved to the
  actual sharp moving selector without the named transfer hypotheses.
- Exceptional shifts `d` must be controlled in averaged energy, not only in
  density.
- This module blocks proof routes, not numerical experimentation or heuristic
  diagnostics.

## 7. Where it fits in the project map

Module 199 continues the Phase B insufficiency audit:

```text
Module 197
  -> adaptive density/energy criterion for B_d
Module 198
  -> ordinary pair-BDH shortcut blocked
Module 199
  -> ordinary rectangle/HL shortcuts blocked.
```

It prepares the next scheduled step:

```text
Module 200
  -> test whether dyadic derivative U^2 gives a better route to minor arcs.
```

The project should now stop treating familiar BDH/HL labels as sufficient
unless the exact residual and adaptive content is stated.

## 8. What remains open

This module does not prove:

- `RectBDH_P(D)` for the actual W-tricked primes;
- any exact residual rectangle-BDH estimate for `B_d`;
- the linear-margin absorption package for `L_d`;
- `R_{2,B}^minor(rho;D) <= Psi_*(rho;D)`;
- the Module 197 density bound or low-level `L^2` envelope;
- `VarianceStrengthHL_8^res`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay;
- transfer to actual sharp moving selectors;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem, all-alpha theorem, or
  unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite mean rectangle-HL as rectangle-BDH.
- Do not cite first-moment Hardy-Littlewood as variance-strength residual
  control.
- Do not cite an ordinary rectangle estimate for `P_d` as a residual minor-arc
  estimate for `B_d`.
- Do not replace `Omega_w` by `Sigma_w` or by the full eight-form model alone.
- Do not hide the linear margin `L_d`.
- Do not treat aggregate fourth-moment control for one object as adaptive
  restriction control for another object.
- Do not rename the full endpoint package as "ordinary rectangle-BDH".
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
