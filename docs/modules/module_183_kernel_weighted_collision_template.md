# Module 183: Kernel-weighted collision-defect estimate template

## 1. Precise theorem / claim being advanced

This module gives a conditional estimate template for the collision-defect term
from Module 182. The point is to replace the phrase "control collisions" by a
specific divisor-average target over the pair-difference forms of the projected
cube.

Let:

```text
Delta_w^{coll}(d,h,k;t)
  = Omega_w^{proj}(d,h,k;t) - Omega_w^{gen}.
```

Assume the projected local factors satisfy a collision-envelope bound of the
form:

```text
|Delta_w^{coll}(d,h,k;t)|
  <= C sum_{i<j} beta_w(L_{ij}(d,h,k;t)) + Err_w(d,h,k;t),
```

where `L_{ij}` ranges over nonzero pair-difference forms among the eight
projected vertices and:

```text
beta_w(m) = sum_{p>w, p|m} 1/p
```

for `m != 0`. Structural collisions `m=0` are separated into their own error
term.

Then the projected model collision defect is controlled if the kernel-weighted
averages of `beta_w(L_{ij})` and `Err_w` are `o(1)`.

## 2. Status label

`CONDITIONAL`

The reduction from collision defects to divisor averages is conditional on the
collision-envelope bound and the kernel-weighted divisor estimates. It does
not prove the endpoint.

## 3. Definitions and variables

The projected vertices from Module 182 are:

```text
v_{00,0} = n - t0
v_{00,1} = n - t0 + d
v_{10,0} = n + h - t1
v_{10,1} = n + h - t1 + d
v_{01,0} = n + k - t2
v_{01,1} = n + k - t2 + d
v_{11,0} = n + h + k - t3
v_{11,1} = n + h + k - t3 + d.
```

For two vertices `v_i,v_j`, write:

```text
L_{ij}(d,h,k;t) = v_i - v_j.
```

The basic pair-difference generators are:

```text
d,
h + t0 - t1,
k + t0 - t2,
h + k + t0 - t3,
h - k + t2 - t1,
k + t1 - t3,
h + t2 - t3,
```

plus the corresponding forms with `+d` or `-d` when the two vertices use
different `d` endpoints.

Let the major-arc projection kernel weights be:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3).
```

The kernel-weighted collision average is:

```text
Coll_w(D)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k}
      E_t |W_M(t)|
        sum_{i<j} beta_w(L_{ij}(d,h,k;t)).
```

## 4. Assumptions

This module assumes:

- the projected model and collision defect from Module 182;
- the local-factor collision envelope:

```text
|Delta_w^{coll}|
  <= C sum_{i<j} beta_w(L_{ij}) + Err_w;
```

- a kernel `K_M` with enough absolute summability for the displayed averages;
- structural zero sets `L_{ij}=0` are removed or shown negligible;
- for each active nonstructural `L_{ij}`, the variables being averaged give
  uniform divisibility control:

```text
E_{h,k,t} |W_M(t)| 1_{p | L_{ij}(d,h,k;t)}
  <= C_K / p + boundary_error(p,N)
```

on average over `d`;

- the boundary errors are summable after the weight `1/p`.

## 5. Proof / disproof / reduction

Under the collision-envelope assumption:

```text
(1/D) sum_d E_{h,k,t} |W_M(t)| |Delta_w^{coll}|
  <= C Coll_w(D)
     + (1/D) sum_d E_{h,k,t} |W_M(t)| Err_w.
```

It remains to estimate `Coll_w(D)`. For each nonstructural pair-difference
form:

```text
E beta_w(L_{ij})
  = sum_{p>w} (1/p) P(p | L_{ij}).
```

Using the uniform divisibility control:

```text
E beta_w(L_{ij})
  <= C_K sum_{p>w} 1/p^2
     + sum_{p>w} boundary_error(p,N)/p.
```

Since:

```text
sum_{p>w} 1/p^2 = o_w(1),
```

the divisor average is small provided the boundary-error sum is also small in
the project limit order. Summing over the finite set of pair-difference forms
gives:

```text
Coll_w(D) = o_w(1) + boundary_error_total(N,w).
```

Therefore, under the stated assumptions:

```text
(1/D) sum_{D<|d|<=2D}
  E_{h,k,t} |W_M(t)| |Delta_w^{coll}(d,h,k;t)|
  = o(1)
```

after the usual limit order, if the structural collision strata and `Err_w`
terms are negligible.

## 6. Edge cases

- If `L_{ij}=0` identically on a region, `beta_w(L_{ij})` is not the right
  object; that region is a structural collision stratum.
- If the kernel has long tails, `E_t |W_M(t)|` may not be bounded uniformly.
- If the projection kernel depends on `N`, the constants in the divisibility
  estimate must be tracked.
- For short ranges of `h` or `k`, the estimate `P(p|L) <= C/p` may fail for
  large `p`; boundary errors must be explicit.
- Pair differences involving `d` require averaging over the dyadic `d` block,
  not only over `h,k`.
- This estimate controls collision defects only after the projected local
  model has already been identified correctly.

## 7. Where it fits in the project map

Module 182 reduced projected model neutrality to collision-defect control.
Module 183 gives a conditional route:

```text
collision defect
  -> beta_w(pair differences)
  -> kernel-weighted divisor averages
  -> o_w(1), subject to boundary and structural-collision control.
```

This is one piece of the major-arc program. It does not address the actual
major-arc model-matching theorem, and it does not touch the minor-arc
large-spectrum branch.

## 8. What remains open

The following are still open:

- prove the local-factor collision-envelope bound in the exact projected
  singular model;
- prove the required kernel absolute-summability and boundary estimates for
  the chosen major-arc projection;
- remove or bound all structural collision strata;
- prove projected local-model matching for the actual major-arc cube;
- prove minor-arc large-spectrum decay;
- close `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.

## Red flags / forbidden upgrades

- Do not treat this conditional template as an endpoint proof.
- Do not ignore structural zero sets of pair-difference forms.
- Do not use unweighted divisor averages when the projection kernel is active.
- Do not replace projected residual models by unprojected models.
- Do not use ordinary pair-BDH as a replacement for the residual cube endpoint.
- Do not transfer this model calculation to the actual sharp moving selector
  without the full transfer package.
