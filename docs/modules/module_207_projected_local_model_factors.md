# Module 207: Exact projected major-arc local model and `Omega_w^proj` factors

## 1. Precise theorem / claim being advanced

This module defines the exact local singular model used by the projected
major-arc target from Module 206.

For the eight projected vertices:

```text
v_{00,0}=n-t0,             v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,           v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,           v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,         v_{11,1}=n+h+k-t3+d,
```

and for every labeled subset `S` of these vertices, define:

```text
Theta_{w,S}^proj(d,h,k;t)
```

by an Euler product over primes `p>w`. The residual projected local model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The claim is structural:

```text
Omega_w^proj is the only local model compatible with
the projected residual product B_d=f(.+d)conj(f(.)).
```

It specializes to the known pair model `kappa_w`, rectangle model `Sigma_w`,
and full two-rectangle model `Theta_w` on the corresponding lower-dimensional
or unprojected faces. It also records explicitly why the rectangle model must
not be pointwise replaced by the square of the pair model.

This module defines the model. It does not prove projected local-model
matching, projected model neutrality, or the endpoint.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The Euler factors and inclusion-exclusion formula are the structural local
model required by the project. No analytic estimate is proved.

## 3. Definitions and variables

Use the notation of Module 206:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
t=(t0,t1,t2,t3).
```

Let the eight labeled projected vertices be:

```text
V(d,h,k;t)={v_{ab,e}: a,b,e in {0,1}},
```

with:

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

For a subset `S subset V(d,h,k;t)`, let:

```text
s=|S|.
```

For a prime `p>w`, define:

```text
r_p(S;d,h,k;t)
  = # { distinct residue classes mod p occupied by vertices in S }.
```

Equivalently, write each vertex as `n+a_j`; then `r_p` is the cardinality of
the set of offsets `a_j mod p` for labels in `S`.

The empty subset convention is:

```text
r_p(emptyset)=0,
Theta_{w,emptyset}^proj=1.
```

## 4. Exact local prime factors

For `p>w`, define the projected local prime factor:

```text
theta_{p,S}^proj(d,h,k;t)
  = (1-1/p)^(-s) (1 - r_p(S;d,h,k;t)/p).
```

Then:

```text
Theta_{w,S}^proj(d,h,k;t)
  = prod_{p>w} theta_{p,S}^proj(d,h,k;t).
```

This is the W-tail local singular model after primes `p<=w` have been absorbed
by the W-trick. Any residue incompatibility at primes `p<=w` belongs to a
separate W-residue error, not to this product.

The full projected eight-form local model is:

```text
Theta_w^proj(d,h,k;t)
  = Theta_{w,V(d,h,k;t)}^proj(d,h,k;t).
```

The residual projected local model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The generic collision-free factor for subsets of size `s` is:

```text
theta_{p,s}^gen
  = (1-1/p)^(-s) (1-s/p),

Theta_{w,s}^gen
  = prod_{p>w} theta_{p,s}^gen.
```

The generic residual model is:

```text
Omega_w^gen
  = sum_{s=0}^8 binom(8,s)(-1)^(8-s) Theta_{w,s}^gen.
```

The projected collision defect is:

```text
Delta_w^coll(d,h,k;t)
  = Omega_w^proj(d,h,k;t) - Omega_w^gen.
```

Module 208 will stratify the collision hyperplanes that make
`Delta_w^coll` non-generic.

## 5. Assumptions and conventions

This module assumes:

- the W-tricked model has fixed the residue classes at primes `p<=w`;
- for primes `p>w`, local obstruction is measured by distinct forbidden
  residue classes among the active affine forms;
- the subset `S` is a subset of labeled vertices, even if two labels occupy
  the same residue class for some parameters;
- structural zero coincidences are not silently discarded;
- Euler products are interpreted with the project limit order and with the
  structural-collision caveat below.

If two labeled forms are structurally identical, then `r_p(S)<s` for all large
`p`. The corresponding product may carry a divergent collision load. That is
not a contradiction; it means the point lies on a structural collision stratum
and must be routed to the collision analysis rather than treated as generic.

## 6. Proof / reduction

For fixed `p>w`, suppose the labels in `S` occupy `r_p` distinct residue
classes modulo `p`. The probability that none of those classes is the
forbidden prime residue is:

```text
1 - r_p/p.
```

Each of the `s` prime-weight factors is normalized by the one-point density
`1-1/p`. Therefore the local normalized prime factor is:

```text
(1-1/p)^(-s) (1-r_p/p),
```

which is exactly `theta_{p,S}^proj`.

Multiplying over `p>w` gives `Theta_{w,S}^proj`. Expanding:

```text
f=nu-1
```

over the eight projected vertices gives inclusion-exclusion over all labeled
subsets:

```text
Omega_w^proj
  = sum_S (-1)^(8-|S|) Theta_{w,S}^proj.
```

If there are no collisions modulo `p`, then `r_p=s`, and:

```text
theta_{p,S}^proj=theta_{p,s}^gen.
```

This gives the generic factor and the decomposition:

```text
Omega_w^proj = Omega_w^gen + Delta_w^coll.
```

No averaging estimate follows from this algebra alone.

## 7. Relation to `kappa_w`, `Sigma_w`, and `Theta_w`

### Pair model

For one `B_d` slot, the two vertices are:

```text
n-t_i,
n-t_i+d.
```

The offsets are congruent to:

```text
0, d
```

after translating by `t_i`. Hence:

```text
r_p = #{0,-d mod p},
```

and the two-point local factor is:

```text
kappa_w(d)
  = prod_{p>w} (1-1/p)^(-2)
      (1 - #{0,-d mod p}/p).
```

Thus `kappa_w(d)` is the two-vertex marginal of the projected local model.
The kernel shift of a single slot does not change this marginal.

### Rectangle model

For two `B_d` slots separated by a projected displacement:

```text
H = h + t0 - t1,
```

the four offsets are:

```text
0, d, H, H+d.
```

Equivalently, after negating all offsets, the exact rectangle factor is:

```text
Sigma_w(d,H)
  = prod_{p>w} (1-1/p)^(-4)
      (1 - #{0,-d,-H,-H-d mod p}/p).
```

Therefore the projected rectangle marginal between the first two slots is:

```text
Sigma_w(d,h+t0-t1).
```

The other projected rectangle faces use the corresponding projected
displacements, for example:

```text
k+t0-t2,
h+k+t0-t3,
h-k+t2-t1,
k+t1-t3,
h+t2-t3.
```

depending on which two slots are selected.

### Why `Sigma_w(d,h)` is not `kappa_w(d)^2`

At a prime `p>w`, the rectangle local factor is:

```text
theta_p^Sigma(d,h)
  = (1-1/p)^(-4)
      (1 - #{0,-d,-h,-h-d mod p}/p).
```

The square of the pair local factor has prime factor:

```text
theta_p^kappa(d)^2
  = (1-1/p)^(-4)
      (1 - #{0,-d mod p}/p)^2.
```

These are different local events. `Sigma_w(d,h)` asks that the union of four
classes avoid zero modulo `p`. `kappa_w(d)^2` treats two pair events as if
they were independent at the same prime.

For example, if:

```text
p does not divide d, h, or h+d,
```

then:

```text
theta_p^Sigma(d,h)
  = (1-1/p)^(-4)(1-4/p),
```

while:

```text
theta_p^kappa(d)^2
  = (1-1/p)^(-4)(1-2/p)^2.
```

The difference is already visible at order `1/p^2`. On collision strata the
difference can be larger. Thus the forbidden replacement of the rectangle
factor by the pointwise square of the pair factor is not a valid identity.

### Full two-rectangle model

For the unprojected cube `t0=t1=t2=t3=0`, the eight offsets are:

```text
0, d, h, h+d, k, k+d, h+k, h+k+d.
```

The full eight-form local model is:

```text
Theta_w(d,h,k)
  = prod_{p>w} (1-1/p)^(-8)
      (1 - r_p(V(d,h,k;0))/p).
```

The projected full model is the same construction with the shifted offsets
from `t0,t1,t2,t3`:

```text
Theta_w^proj(d,h,k;t)
  = prod_{p>w} (1-1/p)^(-8)
      (1 - r_p(V(d,h,k;t))/p).
```

The residual model is not this full factor alone. It is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

When `t=0`, this reduces to the unprojected residual model:

```text
Omega_w(d,h,k).
```

## 8. Edge cases

- The empty subset contributes `1`; omitting it breaks the
  inclusion-exclusion algebra for `f=nu-1`.
- The subsets are labeled. If two labels collide, they are still two factors
  in the residual product, even though they may occupy one residue class.
- Structural collisions can make the naive generic Euler product inappropriate
  without a separate stratum analysis.
- Projection shifts change rectangle and cube offsets; using the unprojected
  `Omega_w(d,h,k)` loses this information.
- The full eight-form factor `Theta_w^proj` is not the residual model.
- Primes `p<=w` are not part of the W-tail product; residue failures at those
  primes must be in a W-residue error term.
- Prime powers are not controlled by merely writing the local factor.
- The formula is a local model. It is not a variance-strength matching theorem
  for the actual prime weight.
- Selector transfer to the actual sharp moving selector is outside this local
  Euler-factor definition.

## 9. Where it fits in the project map

The Phase C chain is now:

```text
Module 206
  -> exact projected major-arc target
Module 207
  -> exact projected local singular factors
Module 208
  -> collision hyperplane stratification
Module 209
  -> W-admissible projected local-model theorem.
```

This module supplies the local-model dictionary needed by:

```text
ProjectedLocalMatch_3^major
```

and by the model-neutrality chain from Modules 182-193.

## 10. What remains open

This module does not prove:

- `ProjectedMajorTarget_3^B`;
- `ProjectedLocalMatch_3^major`;
- any Hardy-Littlewood estimate for `Theta_{w,S}^proj`;
- variance-strength matching for the signed residual combination;
- averaged collision-defect control for `Delta_w^coll`;
- W-admissible projected local-model matching;
- cyclic-to-interval boundary transfer;
- kernel absolute-mass or tail control for the chosen major-arc projection;
- prime-power removal in projected fourth-moment norm;
- selector transfer to the actual sharp moving selector;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not replace `Omega_w^proj` by the full eight-form factor
  `Theta_w^proj`.
- Do not replace `Omega_w^proj(d,h,k;t)` by unprojected
  `Omega_w(d,h,k)` when kernel shifts are active.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not treat the local Euler product as projected local-model matching.
- Do not use first-moment Hardy-Littlewood asymptotics as variance-strength
  residual matching.
- Do not ignore structural collision strata where `r_p<s` for all large
  primes.
- Do not transfer cyclic, smoothed, W-tricked, or model local factors to the
  actual sharp moving selector without the full transfer package.
- Do not claim the residual cube endpoint, the original problem, the all-alpha
  theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
