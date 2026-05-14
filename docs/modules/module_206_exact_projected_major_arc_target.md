# Module 206: Exact projected major-arc target for the residual derivative product

## 1. Precise theorem / claim being advanced

This module begins Phase C by stating the exact projected major-arc target for
the residual derivative product.

Let:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)).
```

For a nonzero major-arc projection `P_M`, define:

```text
M_major^P(D;R,eta)
  = (1/D) sum_{D<|d|<=2D} ||P_M B_d||_{U^2}^4.
```

The projected major-arc target is:

```text
ProjectedMajorTarget_3^B(D;R,eta;P_M):
  M_major^P(D;R,eta)=o(1),
```

uniformly in the required dyadic shift range and with the project W-limit
order.

The structural claim of this module is:

```text
ProjectedMajorTarget_3^B
```

is exactly the average of a kernel-projected residual cube. Therefore the
major-arc proof must proceed through:

```text
actual projected cube
  -> projected residual local model Omega_w^proj
  -> projected model neutrality,
```

with all boundary, zero-mode, W-trick, and selector-transfer terms named.

This module does not prove the projected target, the local model matching, the
model neutrality, or any endpoint theorem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The Fourier identity and physical projected-cube expansion are deterministic.
All estimates are left as named open or conditional inputs.

## 3. Definitions and variables

Work first in a finite cyclic model `G_N` with normalized averaging. Any
interval version must be obtained by an explicit transfer term.

Let:

```text
widehat{F}(xi)=E_{n in G_N} F(n)e(-xi n),
F(n)=sum_{xi in dual(G_N)} widehat{F}(xi)e(xi n).
```

The residual derivative product is:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
c_d=E_n B_d(n),
B_d^circ(n)=B_d(n)-c_d.
```

The dyadic shift range is:

```text
D<|d|<=2D,
D in D_range(N,Hcal).
```

The signs `d>0` and `d<0` are both included unless a later module explicitly
restricts the range and proves the restriction harmless.

Choose major-arc parameters:

```text
R=R(N,w),
eta=eta(N,w).
```

Let:

```text
Major(R,eta)
  = { xi : xi is within eta of a/q for (a,q)=1, 1<=q<=R }.
```

The zero frequency is removed from the projected major arcs:

```text
M = Major(R,eta) \ {0}.
```

Let `P_M` be the chosen major-arc projection. For a sharp projection:

```text
m_M(xi)=1_M(xi).
```

For a smoothed projection:

```text
|m_M(xi)| <= C_M,
supp(m_M) subset Major(R,eta_+)\{0},
m_M(0)=0.
```

The projection is:

```text
widehat{P_M F}(xi)=m_M(xi)widehat{F}(xi).
```

Let `K_M` be the inverse kernel:

```text
P_M F(x)=E_t K_M(t)F(x-t),
K_M(t)=sum_xi m_M(xi)e(xi t).
```

The four-slot projected kernel weight is:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

Use the shorthand:

```text
t=(t0,t1,t2,t3).
```

## 4. The exact projected major-arc objects

The Fourier major-arc quantity is:

```text
M_major^P(D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      sum_xi |m_M(xi)|^4 |widehat{B_d}(xi)|^4.
```

For the sharp projection this is:

```text
M_major^P(D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Major(R,eta), xi != 0}
        |widehat{B_d}(xi)|^4.
```

The physical projected cube for a fixed `d` is:

```text
ActualProjCube_d^P
  = E_{n,h,k}
      P_M B_d(n)
      conj(P_M B_d(n+h))
      conj(P_M B_d(n+k))
      P_M B_d(n+h+k).
```

Equivalently:

```text
ActualProjCube_d^P
  = E_{n,h,k} E_t W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3).
```

The projected major-arc target is:

```text
ProjectedMajorTarget_3^B(D;R,eta;P_M):
  (1/D) sum_{D<|d|<=2D} ActualProjCube_d^P=o(1).
```

In the cyclic model this is the same as `M_major^P(D;R,eta)=o(1)`.

Expanding:

```text
B_d(x)=f(x+d)conj(f(x))
```

gives the eight projected vertices:

```text
v_{00,0}=n-t0,
v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,
v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,
v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,
v_{11,1}=n+h+k-t3+d.
```

Let:

```text
V(d,h,k;t)={v_{ab,e}: a,b,e in {0,1}}.
```

The target projected local model object is named:

```text
Omega_w^proj(d,h,k;t).
```

It is the residual inclusion-exclusion local model attached to the eight
projected vertices `V(d,h,k;t)`. More explicitly, with:

```text
Theta_{w,S}^proj(d,h,k;t)
```

denoting the exact local singular model for the subset `S subset V(d,h,k;t)`,
define:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

Module 207 must state the exact Euler factors in `Theta_{w,S}^proj`. This
module fixes the object, its vertices, and its averaging domains.

The model projected cube for fixed `d` is:

```text
ModelProjCube_d^P
  = E_{h,k} E_t W_M(t) Omega_w^proj(d,h,k;t).
```

The local-model matching error is:

```text
MatchErr_major^P(D)
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_d^P - ModelProjCube_d^P|.
```

The projected model-neutrality target is:

```text
NeutralErr_major^P(D)
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|.
```

The major-arc strategy is therefore:

```text
MatchErr_major^P(D)=o(1),
NeutralErr_major^P(D)=o(1)
  => ProjectedMajorTarget_3^B(D;R,eta;P_M).
```

## 5. Assumptions and boundary terms

The structural identities assume:

- normalized Fourier inversion on the finite cyclic model;
- `m_M(0)=0`;
- the same projection `P_M` is used on all four `B_d` slots;
- the same kernel `K_M` is used in the actual cube and in the model cube;
- the W-tricked residue class is fixed before the `N -> infinity` limit;
- all averages are normalized in the same model.

Every transfer to the actual interval or sharp moving-selector environment
requires explicit error terms.

### A. Zero-mode convention

Because:

```text
m_M(0)=0,
```

one has:

```text
P_M B_d=P_M B_d^circ.
```

The major-arc projected target is a nonzero-frequency target. The mean
coefficient:

```text
c_d=widehat{B_d}(0)
```

is not part of `M_major^P`.

### B. Projection-boundary error

If a smoothed projection is used, it may not equal the sharp major-arc
indicator. Define:

```text
ProjBd_major(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_xi | |m_M(xi)|^4 - 1_M(xi) |
        |widehat{B_d}(xi)|^4,
```

or the analogous buffered partition error. It must be controlled before a
smoothed estimate is advertised as a sharp major-arc estimate.

### C. Cyclic-to-interval boundary error

For an interval model, define:

```text
CycIntBd_major(D)
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_{d,cyc}^P - ActualProjCube_{d,int}^P|.
```

This term includes wraparound, cutoffs, endpoint losses, and vertices moved
outside the valid range by `d,h,k,t`.

### D. Kernel-tail error

For a truncation `T`, define:

```text
TailBd_major(D;T)
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_d^P
        - ActualProjCube_{d,|t_i|<=T}^P|.
```

The same truncation must be reflected in the model side if it is used.

### E. W-residue and prime-power errors

The projected major-arc target must keep separate:

```text
WResBd_major(D;w),
PPErr_major(D;w).
```

These represent W-residue failures and prime-power removal in the projected
fourth-moment norm or in the equivalent projected cube average.

### F. Selector-transfer error

If the target selector is the actual sharp moving selector:

```text
chi_alpha(p)=1_{||alpha p||<1/log p},
```

then the required projected major-arc transfer error is:

```text
SelErr_major^P(D)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M(B_{d,sharp}-B_{d,model})||_{U^2}^4.
```

This is not automatic from a model, frozen, or smoothed selector estimate.

## 6. Proof / reduction

By the `U^2` Fourier identity:

```text
||P_M B_d||_{U^2}^4
  = sum_xi |widehat{P_M B_d}(xi)|^4
  = sum_xi |m_M(xi)|^4 |widehat{B_d}(xi)|^4.
```

This proves the Fourier form of `M_major^P`.

By the physical `U^2` identity:

```text
||P_M B_d||_{U^2}^4
  = E_{n,h,k}
      P_M B_d(n)
      conj(P_M B_d(n+h))
      conj(P_M B_d(n+k))
      P_M B_d(n+h+k).
```

Substituting:

```text
P_M B_d(x)=E_t K_M(t)B_d(x-t)
```

in each of the four slots gives:

```text
ActualProjCube_d^P
  = E_{n,h,k,t} W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3).
```

Expanding each `B_d` gives the eight projected vertices in Section 4. Expanding
each:

```text
f=nu-1
```

requires inclusion-exclusion over all subsets of those eight vertices. That is
why the local model object must be `Omega_w^proj`, not an unprojected
`Omega_w` and not only the full eight-form model.

Finally:

```text
|(1/D)sum_d ActualProjCube_d^P|
  <= MatchErr_major^P(D) + NeutralErr_major^P(D).
```

Thus:

```text
MatchErr_major^P(D)=o(1)
and
NeutralErr_major^P(D)=o(1)
```

would imply:

```text
ProjectedMajorTarget_3^B(D;R,eta;P_M).
```

This is only a reduction. The two estimates are not proved here.

## 7. Edge cases

- If `m_M(0) != 0`, the major-arc target reintroduces `|c_d|^4` and no longer
  matches the centered residual endpoint.
- If a smoothed multiplier is used, the Fourier weight is `|m_M(xi)|^4`, not
  `m_M(xi)` and not a sharp indicator.
- If the local model uses `Omega_w(d,h,k)` without the kernel shifts
  `t0,t1,t2,t3`, it is the wrong model for the projected target.
- If only the full eight-form local factor is used, the residual
  inclusion-exclusion from `f=nu-1` is lost.
- If `P_M` has overlapping major-arc neighborhoods, the multiplier must encode
  the overlap or a partition of unity must be specified.
- If the kernel has long tails, interval boundary terms may dominate unless
  `TailBd_major` and `CycIntBd_major` are controlled.
- Negative `d` and positive `d` must be treated with the same vertex and
  boundary conventions.
- Collision hyperplanes among the projected vertices are part of the local
  model; they cannot be removed on one side only.
- Prime powers may be negligible in a first moment but still need projected
  fourth-moment or projected-cube control.
- Selector transfer must be applied after forming `B_d`, not only at the level
  of `f`.

## 8. Where it fits in the project map

Phase B left the minor-arc side as:

```text
NarrowMinorArc_3^B
MinorArcTransfer_3^B.
```

Phase C now returns to major arcs:

```text
Module 206
  -> exact projected major-arc target
Module 207
  -> exact projected local model and Omega_w factors
Module 208
  -> collision hyperplane stratification
Module 209
  -> W-admissible projected local-model theorem.
```

This module is the entry point for:

```text
ProjectedLocalMatch_3^major.
```

It sets the target that later modules must match. It does not perform the
matching.

## 9. What remains open

This module does not prove:

- `ProjectedMajorTarget_3^B`;
- `ProjectedLocalMatch_3^major`;
- `MatchErr_major^P(D)=o(1)`;
- `NeutralErr_major^P(D)=o(1)`;
- the exact Euler-factor formula for `Theta_{w,S}^proj`;
- W-admissible major-arc local matching;
- kernel absolute-mass or kernel-tail bounds for the chosen projection;
- cyclic-to-interval boundary transfer;
- prime-power removal in projected fourth-moment norm;
- selector transfer to the actual sharp moving selector;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite `ProjectedMajorTarget_3^B` as proved.
- Do not claim `ProjectedLocalMatch_3^major` from this module.
- Do not use `Omega_w(d,h,k)` when the projected kernel shifts are active;
  use `Omega_w^proj(d,h,k;t)`.
- Do not use only the full eight-form model in place of residual
  inclusion-exclusion over all subsets.
- Do not let a smoothed projection stand in for a sharp projection without
  `ProjBd_major`.
- Do not let cyclic identities become interval estimates without
  `CycIntBd_major`.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not use ordinary pair-BDH or first-moment Hardy-Littlewood as substitutes
  for projected residual fourth-moment matching.
- Do not upgrade smoothed, frozen, cyclic, or W-tricked model estimates to the
  actual sharp moving selector without the full transfer package.
- Do not claim the residual cube endpoint, the original problem, the all-alpha
  theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
