# Module 184: Structural collision strata for projected cubes

## 1. Precise theorem / claim being advanced

This module classifies the structural collision strata for the projected
eight-vertex cube from Modules 181-183. The purpose is to separate pair
differences that are genuinely available for divisor averaging from pair
differences that can vanish on affine subspaces and must be removed or bounded
as structural collision strata.

The structural claim is that every pair collision among the projected vertices
is governed by an affine form:

```text
L_{\sigma,e;\sigma',e'}(d,h,k;t)
  = (a-a')h + (b-b')k + (e-e')d - (t_sigma - t_sigma'),
```

where:

```text
sigma=(a,b), sigma'=(a',b') in {0,1}^2,
e,e' in {0,1}.
```

Thus structural collision strata are exactly the zero sets of these affine
forms for distinct vertices.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a classification and bookkeeping module. It does not prove the
collision-defect average from Module 183.

## 3. Definitions and variables

Write:

```text
t_{00}=t0
t_{10}=t1
t_{01}=t2
t_{11}=t3.
```

For `sigma=(a,b) in {0,1}^2` and `e in {0,1}`, define the projected vertex:

```text
v_{sigma,e}
  = n + a h + b k + e d - t_sigma.
```

This gives:

```text
v_{00,0}=n-t0,             v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,           v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,           v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,         v_{11,1}=n+h+k-t3+d.
```

For two distinct vertices define:

```text
Delta a = a-a'
Delta b = b-b'
Delta e = e-e'
Delta t = t_sigma - t_sigma'
```

and:

```text
L_{\sigma,e;\sigma',e'} = Delta a h + Delta b k + Delta e d - Delta t.
```

The structural collision stratum is:

```text
Z_{\sigma,e;\sigma',e'}
  = { (d,h,k,t) : L_{\sigma,e;\sigma',e'}(d,h,k;t)=0 }.
```

## 4. Assumptions

This module assumes:

- the projected cube model of Module 181;
- `D < |d| <= 2D`, so the pure `d` difference is not zero;
- the kernel shifts `t0,t1,t2,t3` are retained as active variables;
- structural collision strata are separated before applying
  `beta_w(L)=sum_{p>w,p|L} 1/p`.

Any size estimate for these strata requires additional assumptions on the
ranges and weights of `h,k,t`.

## 5. Proof / disproof / reduction

For vertices:

```text
v_{\sigma,e}=n+a h+b k+e d-t_sigma
v_{\sigma',e'}=n+a' h+b' k+e' d-t_sigma',
```

their difference is:

```text
v_{\sigma,e}-v_{\sigma',e'}
  = (a-a')h + (b-b')k + (e-e')d - (t_sigma-t_sigma').
```

This proves that every pair collision is described by one affine form in
`d,h,k,t`.

The possible square displacements are:

```text
(Delta a, Delta b) in
  (0,0),
  (+/-1,0),
  (0,+/-1),
  (+/-1,+/-1).
```

They correspond to:

```text
same square slot:       Delta e d
horizontal edge:        +/- h + Delta e d - Delta t
vertical edge:          +/- k + Delta e d - Delta t
positive diagonal:      +/- (h+k) + Delta e d - Delta t
negative diagonal:      +/- (h-k) + Delta e d - Delta t.
```

The same-slot case has `Delta t=0`. For distinct endpoints it gives:

```text
L = +/- d,
```

which has no structural zero in the dyadic range `D < |d| <= 2D`.

All other cases are codimension-one affine strata in the variables being
averaged. Explicitly, up to sign, the active families are:

```text
h + Delta e d - (t_{10}-t_{00})
h + Delta e d - (t_{11}-t_{01})

k + Delta e d - (t_{01}-t_{00})
k + Delta e d - (t_{11}-t_{10})

h+k + Delta e d - (t_{11}-t_{00})
h-k + Delta e d - (t_{10}-t_{01})
```

with `Delta e in {-1,0,1}`. Sign changes give the same zero strata with the
pair order reversed.

Thus the structural part of Module 183 is:

```text
StructColl(D)
  = (1/D) sum_{D<|d|<=2D} E_{h,k,t} |W_M(t)|
      sum_active 1_{L_{\sigma,e;\sigma',e'}(d,h,k;t)=0}.
```

The collision-defect template from Module 183 applies only after proving:

```text
StructColl(D)=o(1)
```

or after removing these strata and accounting for their contribution.

## 6. Edge cases

- Pure `d` differences are safe only because `d` is restricted away from zero.
- If the `h` or `k` averaging window is very short, a codimension-one stratum
  may not be negligible.
- Kernel shifts can force equations like `h=t1-t0`, even when the unprojected
  cube would have only `h=0`.
- Diagonal strata `h+k=Delta t-Delta e d` and
  `h-k=Delta t-Delta e d` must both be kept.
- If the kernel has large support, `Delta t` can be comparable to or larger
  than the `h,k,d` ranges.
- Boundary transfer is needed before any counting statement about these
  strata can be used in the original interval model.
- Removing structural strata from the model-matching side must be mirrored on
  the model-neutrality side.

## 7. Where it fits in the project map

Modules 182 and 183 reduced the projected model-neutrality branch to
collision-defect control and then to divisor averages over nonzero
pair-difference forms. Module 184 supplies the missing bookkeeping step:

```text
projected pair differences
  -> structural zero strata
  -> nonstructural divisor-average forms.
```

The next step is to estimate `StructColl(D)` under explicit kernel and range
hypotheses.

## 8. What remains open

This module does not prove:

- `StructColl(D)=o(1)`;
- the kernel-weighted divisor average from Module 183;
- projected local-model matching;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- any actual sharp moving-selector transfer.

## Red flags / forbidden upgrades

- Do not apply `beta_w(L)` to a form on its zero stratum.
- Do not ignore diagonal structural strata.
- Do not count projected collisions using only the unprojected conditions
  `h=0`, `k=0`, `h=k`, or `d=0`.
- Do not assume codimension-one strata are negligible without range and kernel
  hypotheses.
- Do not use ordinary pair-BDH as a replacement for the residual cube endpoint.
- Do not transfer this classification to the actual sharp moving selector
  without the full transfer package.
