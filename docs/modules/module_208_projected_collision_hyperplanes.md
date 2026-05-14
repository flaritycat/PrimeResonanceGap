# Module 208: Collision hyperplane stratification for the projected residual cube

## 1. Precise theorem / claim being advanced

This module stratifies the collision geometry behind the projected local model
from Module 207.

For the eight projected vertices:

```text
v_{00,0}=n-t0,             v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,           v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,           v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,         v_{11,1}=n+h+k-t3+d,
```

every pair collision is governed by an affine pair-difference form:

```text
L_{sigma,e;sigma',e'}(d,h,k;t)
  = v_{sigma,e}-v_{sigma',e'}.
```

The structural claim is:

```text
the 28 labeled pair differences are generated, up to sign and multiplicity,
by d and by six projected slot-displacements with endpoint shifts
0, +d, and -d.
```

This gives a clean split:

```text
structural zero strata:      L=0,
large-prime congruence strata: p|L with L != 0 and p>w,
boundary/kernel-tail strata: interval or projection artifacts,
W-residue strata:            primes p<=w.
```

The exact local model `Omega_w^proj` includes the congruence collisions through
the residue-class counts `r_p`. Estimates are required only when one compares
that exact model with its generic collision-free model or transfers it to the
actual interval/selector setting.

This module is a stratification, not a proof of collision negligibility.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The affine classification is deterministic. The size of each stratum is an
analytic question handled only conditionally in earlier and later modules.

## 3. Definitions and variables

Let:

```text
Sigma_square={00,10,01,11}.
```

Write:

```text
t_{00}=t0,
t_{10}=t1,
t_{01}=t2,
t_{11}=t3.
```

For `sigma=(a,b) in {0,1}^2`, define:

```text
A_sigma(h,k;t)=a h + b k - t_sigma.
```

The projected vertices are:

```text
v_{sigma,e}=n + A_sigma(h,k;t) + e d,
e in {0,1}.
```

For two distinct labeled vertices, define:

```text
L_{sigma,e;sigma',e'}
  = A_sigma-A_sigma' + (e-e')d.
```

A collision modulo `p` occurs exactly when:

```text
p | L_{sigma,e;sigma',e'}.
```

The structural zero stratum for that pair is:

```text
Z_{sigma,e;sigma',e'}
  = { (d,h,k,t) : L_{sigma,e;sigma',e'}=0 }.
```

On the complement of structural zero strata, define:

```text
beta_w(L)=sum_{p>w, p|L} 1/p,
```

and the labeled collision load:

```text
B_w^lab(d,h,k;t)
  = sum_{(sigma,e)<(sigma',e')} beta_w(L_{sigma,e;sigma',e'}).
```

The order on labeled pairs is arbitrary and only prevents double counting.

## 4. Basic pair-difference forms

Define the six projected slot-displacements from the first slot of each pair:

```text
H_0  = h + t0 - t1,          00 -> 10,
K_0  = k + t0 - t2,          00 -> 01,
S_0  = h+k + t0 - t3,        00 -> 11,
R_0  = h-k + t2 - t1,        01 -> 10, up to sign,
K_1  = k + t1 - t3,          10 -> 11,
H_1  = h + t2 - t3,          01 -> 11.
```

Let:

```text
BaseProj={H_0,K_0,S_0,R_0,K_1,H_1}.
```

Then all labeled pair-difference forms are, up to sign:

```text
d,
A,
A+d,
A-d,
```

where `A in BaseProj`.

Thus the 28 labeled differences reduce to the 19 basic forms:

```text
d,
H_0, H_0+d, H_0-d,
K_0, K_0+d, K_0-d,
S_0, S_0+d, S_0-d,
R_0, R_0+d, R_0-d,
K_1, K_1+d, K_1-d,
H_1, H_1+d, H_1-d.
```

The reduction is only for bookkeeping. The local factor still uses labeled
vertices: multiple labeled collisions at the same prime can affect `r_p` with
bounded multiplicity.

For divisor estimates it is often convenient to use the reduced load:

```text
B_w^red(d,h,k;t)
  = beta_w(d)
    + sum_{A in BaseProj}
        ( beta_w(A) + beta_w(A+d) + beta_w(A-d) ),
```

after excluding structural zeros. Since every labeled pair difference appears
in this reduced list up to sign and bounded multiplicity:

```text
B_w^lab <= C B_w^red
```

for an absolute constant `C`.

## 5. Strata

### A. Structural zero strata

The structural set is:

```text
Z_struct
  = union_{labeled pairs} { L_{sigma,e;sigma',e'}=0 }.
```

Equivalently, up to sign:

```text
d=0,
A=0,
A+d=0,
A-d=0
```

for `A in BaseProj`.

Because the dyadic range has:

```text
D<|d|<=2D,
```

the pure stratum `d=0` is absent. The remaining structural strata are
codimension-one affine hyperplanes in `(d,h,k,t)`.

They belong to the exact projected local model: on such strata the residue
class count `r_p` changes for every large prime. They cannot be handled by
`beta_w(L)` because `beta_w(0)` is not defined.

Their contribution must be handled by one of:

```text
1. a structural-stratum estimate with the same kernel weights;
2. a synchronized removal from both actual and model sides;
3. a separate lower-dimensional local model on the stratum.
```

### B. Large-prime congruence collision strata

For `p>w`, the nonstructural congruence stratum is:

```text
C_p(L)
  = { (d,h,k,t) : L != 0 and p|L }.
```

These strata are already encoded in:

```text
r_p(S;d,h,k;t)
```

inside `Theta_{w,S}^proj`. They become analytic error terms only after
comparing:

```text
Omega_w^proj
```

with the generic collision-free model:

```text
Omega_w^gen.
```

The Module 187 envelope routes them through:

```text
B_w = sum beta_w(L),
```

with the small-load or overflow qualification.

### C. Boundary and kernel-tail strata

The local Euler product is not responsible for points where the projected
physical cube has left the valid interval. These are boundary strata such as:

```text
n+A_sigma+e d outside the interval,
h or k outside its averaging window,
max_i |t_i|>T for a kernel truncation T.
```

They require separate terms:

```text
CycIntBd_major,
TailBd_major,
BoundaryMatch.
```

They must not be hidden inside `Omega_w^proj` or `Delta_w^coll`.

### D. W-residue and small-prime strata

Primes `p<=w` are removed by the W-trick. Any failure of the projected vertices
to lie in the prescribed W-residue classes belongs to:

```text
WResBd_major(D;w),
```

not to the Euler product over `p>w`.

### E. Prime-power strata

Prime powers are not described by the first-order local residue count
`r_p`. Their removal or transfer belongs to:

```text
PPErr_major(D;w).
```

## 6. Proof / reduction

For two vertices:

```text
v_{sigma,e}=n+A_sigma+e d,
v_{sigma',e'}=n+A_sigma'+e' d,
```

their difference is:

```text
L_{sigma,e;sigma',e'}
  = A_sigma-A_sigma' + (e-e')d.
```

If `sigma=sigma'` and `e != e'`, then:

```text
L=+d or -d.
```

This gives the same-slot form `d`.

If `sigma != sigma'`, the square-slot difference
`A_sigma-A_sigma'` is, up to sign, one of:

```text
H_0, K_0, S_0, R_0, K_1, H_1.
```

Since:

```text
e-e' in {-1,0,1},
```

the resulting pair difference is, up to sign:

```text
A,
A+d,
A-d.
```

This proves the 19-form reduced list.

The distinction between structural and congruence strata is also immediate:

```text
L=0
```

is an affine hyperplane over the integers, while:

```text
L != 0 and p|L
```

is a large-prime congruence condition. The first must be separated before
`beta_w(L)` is formed; the second is precisely what `beta_w(L)` measures.

No smallness estimate is obtained from this classification.

## 7. Edge cases

- The reduced 19-form list must not erase labeled multiplicities when local
  residue counts `r_p` are computed.
- The pure form `d` has no structural zero in the dyadic range, but
  congruences `p|d` for `p>w` still contribute to the collision load.
- Structural equations with `A+d=0` or `A-d=0` are just as real as equations
  with `A=0`.
- If the kernel support is broad, the shifts `t_i` can move many points onto
  structural hyperplanes even when the unprojected cube is generic.
- Boundary or tail regions are not local Euler-factor collisions.
- W-residue failures at small primes are not W-tail collisions.
- Removing a structural region only from the actual projected cube changes the
  comparison with `Omega_w^proj`.
- Counting codimension-one strata requires range and absolute-kernel-mass
  hypotheses; it is not automatic from this module.

## 8. Where it fits in the project map

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

This module refines the collision part of:

```text
Omega_w^proj = Omega_w^gen + Delta_w^coll.
```

It also updates the older collision modules by making clear which forms are
basic after projection and which strata are outside the `beta_w` load.

## 9. What remains open

This module does not prove:

- negligibility of `Z_struct`;
- the Module 185 structural counting hypotheses for the actual projection;
- the Module 192 averaged collision-defect hypotheses;
- the kernel/range estimates for `B_w^red`;
- W-admissible projected local-model matching;
- cyclic-to-interval boundary transfer;
- prime-power removal in projected fourth-moment norm;
- selector transfer to the actual sharp moving selector;
- `ProjectedMajorTarget_3^B`;
- `ProjectedLocalMatch_3^major`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not apply `beta_w(L)` on `L=0`.
- Do not discard structural collision strata unless the same operation is
  mirrored on the actual and model sides.
- Do not count projected collisions using only the unprojected equations
  `h=0`, `k=0`, or `h=k`.
- Do not treat the reduced 19-form list as a replacement for the labeled
  residue-count definition of `r_p`.
- Do not hide boundary, kernel-tail, W-residue, or prime-power errors in
  `Delta_w^coll`.
- Do not replace the projected residual model by the full eight-form model or
  by the unprojected residual model.
- Do not replace the rectangle local model by a pointwise square of the pair
  local model.
- Do not claim projected local-model matching, the residual cube endpoint, the
  original problem, the all-alpha theorem, the unconditional finite-type
  theorem, `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
