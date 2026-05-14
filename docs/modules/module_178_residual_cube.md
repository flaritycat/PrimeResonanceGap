# Module 178: Centered derivative U^2 as an eight-form residual cube

## 1. Precise theorem / claim being advanced

Let `f=nu-1`. For a short shift `d`, define:

```text
B_d(n)=f(n+d)conj(f(n))
c_d=E_n B_d(n)
B_d^circ(n)=B_d(n)-c_d
```

Then:

```text
||B_d^circ||_{U^2}^4 = Q_d - |c_d|^4
```

where:

```text
Q_d = E_{n,h,k} B_d(n) conj(B_d(n+h)) conj(B_d(n+k)) B_d(n+h+k).
```

Equivalently, `Q_d` is an alternating eight-vertex cube over:

```text
n, n+d, n+h, n+h+d, n+k, n+k+d, n+h+k, n+h+k+d.
```

## 2. Status label

`STRUCTURAL / EXACT IDENTITY` for the identity.

`OPEN` for the analytic estimate:

```text
(1/D) sum_{D<|d|<=2D} (Q_d - |c_d|^4) = o(1).
```

## 3. Definitions and variables

```text
f=nu-1
B_d(n)=f(n+d)conj(f(n))
c_d=E_n B_d(n)
B_d^circ=B_d-c_d
```

The spectral target is:

```text
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1).
```

## 4. Exact residual local model

Let:

```text
L_epsilon(n,d,h,k)=n+epsilon_1 d+epsilon_2 h+epsilon_3 k
```

For `S subset {0,1}^3`, define:

```text
Theta_{w,S}(d,h,k)
```

as the local singular model for the forms `L_epsilon` with `epsilon in S`.

The residual cube local model is the inclusion-exclusion model:

```text
Omega_w(d,h,k)=sum_{S subset {0,1}^3} (-1)^{8-|S|} Theta_{w,S}(d,h,k).
```

Do not use only the full eight-form model `Theta_w`; the residual model includes all lower-dimensional subtraction terms.

## 5. Proof / reduction

Use Fourier:

```text
||B_d||_{U^2}^4 = sum_xi |Bhat_d(xi)|^4
c_d = Bhat_d(0)
```

Therefore:

```text
||B_d^circ||_{U^2}^4 = sum_{xi != 0} |Bhat_d(xi)|^4 = ||B_d||_{U^2}^4 - |c_d|^4.
```

Then expand `B_d` in physical space to obtain the eight-vertex cube.

## 6. Edge cases

- Forgetting zero-frequency subtraction is a centering error.
- Using only `Theta_w` is a model error; use `Omega_w`.
- Pair-BDH does not control the eight-form cube.
- First-moment HL does not imply the fourth-moment residual endpoint.
- Boundary and collision packages remain required.
- The range `D <= Hcal(N)` is part of the theorem.

## 7. Project-map location

Module 178 follows Module 177's derivative decomposition and precedes Module 179's Fourier major/minor decomposition.

## 8. What remains open

The open endpoint is:

```text
ResCube_3^sharp(Hcal):
(1/D) sum_d sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1).
```

This is equivalent, modulo side packages, to the direct route into `CPC_3^sharp`, hence to `RBDH_pair_short`.

## Red flags / forbidden upgrades

Do not claim `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH`, or `AU^3` is proved. This module identifies the formula, not the analytic bound.
