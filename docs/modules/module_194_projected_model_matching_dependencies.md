# Module 194: Projected local-model matching dependency list

## 1. Precise theorem / claim being advanced

This module states the exact major-arc model-matching theorem still required
after Module 193. The model-neutrality package now has a conditional route,
but the actual major-arc cube has not yet been matched to the projected local
model.

The missing theorem is:

```text
ProjectedLocalMatch_3^major:
(1/D) sum_{D<|d|<=2D}
  | ActualProjCube_d - ModelProjCube_d | = o_W(1),
```

where:

```text
ActualProjCube_d
  = E_{n,h,k} E_t W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3),
```

and:

```text
ModelProjCube_d
  = E_{h,k} E_t W_M(t)
      Omega_w^{proj}(d,h,k;t).
```

This module does not prove `ProjectedLocalMatch_3^major`. It extracts its
dependency list and failure modes.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a dependency-list module. It identifies the theorem that remains
between the actual major-arc projected cube and the conditional projected
model-neutrality result from Module 193.

## 3. Definitions and variables

Let:

```text
f = nu - 1,
B_d(x)=f(x+d)conj(f(x)).
```

Let the projected kernel shifts be:

```text
t=(t0,t1,t2,t3),
W_M(t)=K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The actual projected cube is:

```text
ActualProjCube_d
  = E_{n,h,k,t} W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3).
```

Expanding `B_d=f(.+d)conj(f(.))` gives the projected eight vertices:

```text
n-t0,             n-t0+d,
n+h-t1,           n+h-t1+d,
n+k-t2,           n+k-t2+d,
n+h+k-t3,         n+h+k-t3+d.
```

For `S` a subset of these vertices:

```text
Theta_{w,S}^{proj}(d,h,k;t)
```

is the exact projected local singular model. The residual projected model is:

```text
Omega_w^{proj}(d,h,k;t)
  = sum_S (-1)^(8-|S|) Theta_{w,S}^{proj}(d,h,k;t).
```

The model cube is:

```text
ModelProjCube_d
  = E_{h,k,t} W_M(t) Omega_w^{proj}(d,h,k;t).
```

The matching error is:

```text
MatchErr(D)
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_d - ModelProjCube_d|.
```

## 4. Assumptions required for the missing theorem

`ProjectedLocalMatch_3^major` requires all of the following packages.

Projected HL package:

For every subset `S` of the eight projected vertices,

```text
E_n prod_{v in S} nu(v)
  = Theta_{w,S}^{proj}(d,h,k;t) + Error_S(d,h,k;t)
```

with enough uniformity after averaging in:

```text
d,h,k,t
```

against the signed kernel `W_M(t)`.

Residual inclusion-exclusion package:

The above estimates must be compatible with expanding:

```text
f = nu - 1.
```

The full eight-form estimate alone is insufficient; every subset `S` in the
inclusion-exclusion sum is required.

Variance-strength package:

The average of the absolute matching error must be small:

```text
(1/D) sum_d |sum_S (-1)^(8-|S|) AveragedError_S(d)| = o_W(1).
```

First-moment asymptotics for each individual tuple are not enough unless their
errors are uniform and summable in this signed residual combination.

Kernel package:

The same projection kernel used in the Fourier major arcs must be used in the
model:

```text
W_M(t)=K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The theorem must specify whether `P_M` is sharp or smoothed, because a
different multiplier changes both `K_M` and the physical-space model.

Boundary package:

Kernel shifts and interval cutoffs must not move vertices outside the valid
range without an explicit boundary error:

```text
BoundaryMatch(D,M,T)=o_W(1).
```

W-trick and residue package:

All shifted vertices must be compatible with the W-tricked residue class, and
the order:

```text
N -> infinity first, then w -> infinity
```

must be preserved.

Collision package:

Structural collisions and congruence collisions are already part of the exact
local model. The matching theorem must not remove them on the actual side
unless the same removal is mirrored on the model side.

Prime-power package:

If `nu` is von-Mangoldt-like, prime-power contributions must be excluded or
transferred with an explicit error:

```text
PrimePowerErr(D)=o_W(1).
```

Range package:

The result must hold uniformly for the required short-shift and major-arc
ranges:

```text
D <= Hcal(N),
q <= R,
major-arc width eta,
kernel/truncation parameters M,T.
```

## 5. Proof / disproof / reduction

The formal reduction is straightforward but important.

Expand the actual projected cube:

```text
B_d(x)=f(x+d)conj(f(x)),  f=nu-1.
```

This produces:

```text
ActualProjCube_d
  = E_{h,k,t} W_M(t)
      sum_S (-1)^(8-|S|)
        E_n prod_{v in S} nu(v).
```

If the projected HL package supplies:

```text
E_n prod_{v in S} nu(v)
  = Theta_{w,S}^{proj}(d,h,k;t) + Error_S(d,h,k;t),
```

then:

```text
ActualProjCube_d - ModelProjCube_d
  = E_{h,k,t} W_M(t)
      sum_S (-1)^(8-|S|) Error_S(d,h,k;t)
    + boundary/prime-power/transfer errors.
```

Thus `ProjectedLocalMatch_3^major` is exactly the assertion that the averaged
absolute value of this residual error is `o_W(1)`.

Module 193 then gives:

```text
ModelProjCube_d averaged over d = o_W(1)
```

under its hypotheses. Combining both conditional statements would control the
major-arc projected model contribution:

```text
(1/D) sum_d ActualProjCube_d = o_W(1).
```

This combination is still conditional, still only treats the major-arc model
branch, and still leaves the minor-arc branch and endpoint transfers open.

## 6. Edge cases

- Matching only the full eight-form singular series is insufficient because
  the residual model uses all subsets `S`.
- Matching an unprojected model misses the kernel shifts `t0,t1,t2,t3`.
- Proving average tuple asymptotics without variance-strength error control
  does not imply the absolute averaged matching error.
- Kernel cancellation cannot hide large absolute boundary errors unless a
  signed-kernel theorem is stated.
- Removing collision strata on only one side breaks the actual/model
  comparison.
- If the projection is smoothed, the major-arc Fourier expression contains
  `|m_M(xi)|^4`, and the physical kernel must match that multiplier.
- The theorem must preserve zero-frequency removal; the major arcs here are
  nonzero major arcs.
- Prime powers, W-residue failures, and denominator overlap must be handled
  before any sharp selector transfer.

## 7. Where it fits in the project map

The major-arc branch now separates into:

```text
actual projected cube
  -> ProjectedLocalMatch_3^major
  -> projected residual local model
  -> Module 193 model neutrality.
```

Modules 181-193 organize the projected model and its conditional neutrality.
Module 194 names the remaining matching theorem needed to connect actual
prime-weight cubes to that model.

## 8. What remains open

This module does not prove:

- `ProjectedLocalMatch_3^major`;
- the projected HL package for all subsets `S`;
- variance-strength residual error control;
- kernel absolute-mass and boundary transfer for the actual chosen projection;
- prime-power transfer;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not treat Module 193 model neutrality as model matching.
- Do not replace the projected model by the unprojected model.
- Do not use full eight-form Hardy-Littlewood alone in place of residual
  inclusion-exclusion over all subsets.
- Do not use first-moment Hardy-Littlewood asymptotics as variance-strength
  matching.
- Do not transfer cyclic, smoothed, frozen, or model-selector estimates to the
  actual sharp moving selector without the full transfer package.
