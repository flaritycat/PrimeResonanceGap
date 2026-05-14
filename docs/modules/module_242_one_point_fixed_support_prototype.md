# Module 242: One-point fixed-support prototype row

## 1. Precise theorem / claim being advanced

This module fixes the first nonempty prototype row promised by Module 241.

The fixed boundary row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

Choose the active prototype labels:

```text
lambda0=(00,0),
sigma0=(00,0),
S1={sigma0}.
```

Thus the boundary-marked vertex and the single weighted vertex are the same:

```text
v_lambda0=v_sigma0=n-t0.
```

Define:

```text
OnePointBIHL_242(s0,D0,rho0)
```

to be the one-point boundary interval row:

```text
BoundaryIntervalHL_234({(00,0)},(00,0)).
```

The claim advanced in this module is only a structural fixation:

```text
OnePointBIHL_242 is the active Phase F2 prototype.
```

It is not proved. It is the next object to test. If this same-vertex
one-point row is not smaller than the projected residual endpoint, then the
larger `FixedSupportTupleHL_238` family should not be treated as a routine
local side package.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module chooses and defines the prototype row, its intervals, its exact
model term, and its side-error slots. It proves no estimate.

## 3. Definitions and variables

Use the fixed data:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The fixed selector class is not changed. In particular there is no:

```text
fr -> mv,
sm -> fr,
bern -> sm,
fs -> bern,
major/minor partition transfer.
```

For the fixed class:

```text
nu=nu_s0,
f=f_s0=nu_s0-1,
B_d(n)=f(n+d)conj(f(n)).
```

The four projected slots are:

```text
x00=n-t0,
x10=n+h-t1,
x01=n+k-t2,
x11=n+h+k-t3.
```

The eight residual vertices are:

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

For this module:

```text
lambda0=sigma0=(00,0),
a_sigma0(d,h,k;t)=-t0,
v_sigma0=n-t0.
```

The core interval is:

```text
I_N^core(L_N)={m in {1,...,N}: L_N<m<=N-L_N}.
```

The active boundary event is:

```text
Bd_lambda0(d,n,h,k;t)
  = 1_{n-t0 notin I_N^core(L_N)}.
```

The corresponding left and right boundary pieces are:

```text
J_{lambda0,L}(d,h,k;t)
  = {n: n-t0 <= L_N},

J_{lambda0,R}(d,h,k;t)
  = {n: n-t0 > N-L_N},
```

intersected with the row's interval averaging domain and with the declared
cutoff convention `cutoff0`. Write:

```text
r in {L,R},
J_r=J_{lambda0,r}(d,h,k;t),
ell_r(d,h,k;t)=E_n 1_{J_r}(n).
```

The one-point actual boundary interval mean is:

```text
M_r^act(d,h,k;t)
  = E_n 1_{J_r}(n) mu_s0(n-t0).
```

The exact one-point model term is:

```text
M_r^mod(d,h,k;t)
  = ell_r(d,h,k;t)
    |Theta_{w,{(00,0)}}^proj(d,h,k;t)|.
```

The pointwise error is:

```text
Err_r^242(d,h,k;t)
  = M_r^act(d,h,k;t)-M_r^mod(d,h,k;t).
```

The active averaged error is:

```text
BIHLErr_242
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_{r in {L,R}} |Err_r^242(d,h,k;t)|.
```

The prototype target is:

```text
BIHLErr_242=o_W(1),
```

plus the side-error slots listed below.

## 4. Assumptions

This module assumes only the definitions and guardrails from Modules 224,
234, 240, and 241. It does not assume the prototype estimate.

The fixed-row discipline is:

```text
same P_M,
same K_M,
same R0 and eta0,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same W-residue convention,
same prime-only or prime-power convention,
same interval cutoff convention,
same normalization and centering convention,
fixed w, then N -> infinity, then w -> infinity.
```

The prototype package, to be tested in later modules, is:

```text
OnePointBIHL_242(s0,D0,rho0):

  BIHLErr_242=o_W(1),
  CutOne_242=o_W(1),
  RangeOne_242=o_W(1),
  WResOne_242=o_W(1),
  PPOne_242=o_W(1),
  NormZeroOne_242=o_W(1) when active.
```

The side-error slots mean:

```text
CutOne_242:
  loss from replacing Bd_lambda0 by J_L union J_R under cutoff0;

RangeOne_242:
  range or CRT-denominator failures caused by the short boundary intervals;

WResOne_242:
  W-residue incompatibility for the single weighted form n-t0;

PPOne_242:
  prime-power contribution to the single weighted form when pp_s0 is active;

NormZeroOne_242:
  normalization, centering, or zero-mode leakage touching this one-point row.
```

No side-error slot may be replaced by the projected residual endpoint.

## 5. Proof / disproof / reduction

### A. Why this is the smallest nonempty row

The empty row had:

```text
S=emptyset,
prod_{sigma in S} mu_s0(v_sigma)=1.
```

The active prototype has:

```text
S1={(00,0)},
prod_{sigma in S1} mu_s0(v_sigma)=mu_s0(n-t0).
```

Thus it is the first row where boundary volume is no longer enough. It asks
for prime-type mass on the boundary interval of one residual vertex.

### B. Boundary interval decomposition

By definition:

```text
Bd_lambda0(d,n,h,k;t)=1_{n-t0 notin I_N^core(L_N)}.
```

Inside the fixed interval averaging convention, this support is the union of
the two endpoint pieces:

```text
J_L={n: n-t0 <= L_N},
J_R={n: n-t0 > N-L_N},
```

plus any cutoff and out-of-range pieces belonging to `CutOne_242` and
`RangeOne_242`.

Therefore:

```text
E_n Bd_lambda0(n) mu_s0(n-t0)
```

is reduced structurally to:

```text
sum_{r in {L,R}} E_n 1_{J_r}(n) mu_s0(n-t0)
```

plus the named side errors.

### C. Exact model attachment

For the one-point row the model term is not boundary volume alone. It is:

```text
ell_r(d,h,k;t)
  |Theta_{w,{(00,0)}}^proj(d,h,k;t)|.
```

This module deliberately keeps the exact projected local factor. It does not
replace it by:

```text
1,
kappa_w(d),
Sigma_w(d,h),
Theta_w(d,h,k),
Omega_w^proj,
```

or by any collision-free generic factor. If a later module proves that the
one-point factor is equal to a simpler expression in a particular normalized
model class, that proof must be recorded there.

### D. Relation to `BoundaryIntervalHL_234`

With:

```text
S={(00,0)},
lambda=(00,0),
```

the Module 234 row becomes exactly:

```text
E_n 1_{J_r}(n) mu_s0(n-t0)
  =
ell_r(d,h,k;t)
  |Theta_{w,{(00,0)}}^proj(d,h,k;t)|
  + Err_r^242(d,h,k;t).
```

The row `OnePointBIHL_242` is the assertion that the `|W_M|`-averaged
absolute sum of these errors, together with the side-error slots, is
`o_W(1)`.

Thus:

```text
OnePointBIHL_242
  => BoundaryIntervalHL_234({(00,0)},(00,0)).
```

This implication is just matching of definitions and named side errors; it
does not estimate `BIHLErr_242`.

### E. Same-vertex versus off-vertex cases

The active row is same-vertex:

```text
sigma0=lambda0=(00,0).
```

It tests whether the weight on the boundary-marked vertex itself has the
right one-point boundary mean.

The off-vertex variants have:

```text
sigma != lambda0,
E_n 1_{J_{lambda0,r}}(n) mu_s0(n+a_sigma(d,h,k;t)).
```

Those variants are not active in this module. They may be harder because the
weighted variable is shifted relative to the boundary-marked interval and can
create extra range or W-residue synchronization. No off-vertex result is
claimed from the same-vertex prototype.

### F. Stop condition

If proving `BIHLErr_242=o_W(1)` requires any unlocalized estimate such as:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
```

or requires:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CoreSel_major^P,
MoveLayerCube_3^Pi,
actual sharp moving-selector transfer,
```

then the row is endpoint-strength or mixed and cannot serve as a local proof
of `LocalBdPkg_226`.

## 6. Edge cases

- This module chooses `(00,0)` only as the active prototype. It does not prove
  uniformity over all eight boundary labels.
- The same-vertex case is not automatic: `E_n 1_{J_r} mu_s0(n-t0)` is still a
  prime-type boundary mean, not boundary volume.
- If `J_L` or `J_R` has zero length after the row's cutoff convention, the
  corresponding interval has zero main term and zero actual term, while any
  mismatch belongs to `CutOne_242`.
- If `t0` is outside the kernel truncation range, this row is no longer the
  interior one-point boundary interval row; the contribution belongs to the
  kernel-tail rows from Module 235.
- If the W-residue class of `n-t0` is not fixed on `J_r`, the error belongs to
  `WResOne_242`.
- If `pp_s0` is active, first-moment sparsity of prime powers is not
  automatically enough after multiplication by `|W_M|`.
- If the projection is changed to improve the kernel, the proof has left the
  fixed prototype and needs a projection-transfer row.
- If the selector class changes, the result does not transfer to the actual
  sharp moving selector.
- If `Theta_{w,{(00,0)}}^proj` is simplified without proof, the exact
  local-model discipline is broken.
- If the row is proved from the projected residual endpoint, it is not a
  local fixed-support row.

## 7. Where it fits in the project map

The Phase F2 chain begins:

```text
Module 241
  -> choose one-row nonempty fixed-support prototype window.

Module 242
  -> fix the active prototype:
     BoundaryIntervalHL_234({(00,0)},(00,0)).

Module 243
  -> derive the exact one-point local model and boundary interval main term.
```

This is the first concrete nonempty row inside:

```text
FixedSupportTupleHL_238.
```

It is intended as an exit test for the boundary route: if the one-point row is
already endpoint-strength, larger nonempty tuple rows should not be treated
as routine local side packages.

## 8. What remains open

This module does not prove:

- `BIHLErr_242=o_W(1)`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242`;
- `BoundaryIntervalHL_234({(00,0)},(00,0))`;
- any off-vertex `BoundaryIntervalHL_234({sigma},lambda)`;
- `FixedSupportTupleHL_238`;
- `LocalBdPkg_226`;
- `FixedRowPkg_238`;
- `BdPrefRow_224^P=o_W(1)`;
- `CycIntTransfer_3^major(P_adm)`;
- selector transfer to the actual sharp moving selector;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite this module as a proof of the one-point boundary row.
- Do not treat the same-vertex prototype as proving off-vertex prototypes.
- Do not replace `E_n 1_{J_r} mu_s0(n-t0)` by boundary volume.
- Do not replace the boundary interval row by full-interval first-moment
  Hardy-Littlewood.
- Do not cite ordinary pair-BDH as a one-point boundary interval theorem.
- Do not use cancellation from `W_M` after the row has taken `|W_M|`.
- Do not change selector class, projection, W-residue convention, dyadic
  shell, denominator grid, or interval cutoff inside the prototype.
- Do not simplify `Theta_{w,{(00,0)}}^proj` without a named proof.
- Do not replace rectangle factors by `kappa_w(d)^2`; `Sigma_w` remains the
  exact rectangle model where rectangle faces arise.
- Do not prove the prototype by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
