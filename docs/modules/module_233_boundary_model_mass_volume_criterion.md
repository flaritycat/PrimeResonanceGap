# Module 233: Boundary model-mass volume criterion

## 1. Precise theorem / claim being advanced

This module formulates the first Phase F1 test promised by Module 232.

The fixed row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
s0 in {model, W, sm, fr},
D0<|d|<=2D0.
```

For each:

```text
S subset Lambda_8,
lambda in Lambda_8,
```

the model-side target from Module 225 is:

```text
BoundaryModelMass_225(S,lambda):
  BdModel_225(S,lambda)=o_W(1).
```

Define the conditional criterion:

```text
BoundaryModelVolume_233(S,lambda).
```

Claim:

```text
BoundaryModelVolume_233(S,lambda)
  => BoundaryModelMass_225(S,lambda).
```

The criterion is deliberately model-side. It tests whether the boundary model
mass follows from:

```text
deterministic boundary-volume saving,
absolute kernel-mass control,
exact projected local-factor control,
and a localized collision/bad-factor remainder.
```

It does not prove the actual boundary tuple estimate
`BoundaryTupleHL_225(S,lambda)` and does not prove the fixed boundary row
`BdPrefRow_224^P=o_W(1)`.

## 2. Status label

`CONDITIONAL`

The implication is a deterministic domination once the volume, kernel, and
local-factor hypotheses are supplied. Those hypotheses are not proved here.

## 3. Definitions and variables

Use the fixed notation of Modules 224-226:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
w fixed, N -> infinity, then w -> infinity.
```

The eight labeled vertices are written as:

```text
v_lambda=n+a_lambda(d,h,k;t).
```

Explicitly:

```text
a_{00,0}=-t0,
a_{00,1}=d-t0,
a_{10,0}=h-t1,
a_{10,1}=h+d-t1,
a_{01,0}=k-t2,
a_{01,1}=k+d-t2,
a_{11,0}=h+k-t3,
a_{11,1}=h+k+d-t3.
```

Let:

```text
I_N^core(L_N)={m in {1,...,N}: L_N<m<=N-L_N},
Bd_lambda(d,n,h,k;t)=1_{v_lambda notin I_N^core(L_N)}.
```

The boundary volume attached to the vertex `lambda` is:

```text
BdVol_lambda(d,h,k;t)
  = E_n Bd_lambda(d,n,h,k;t).
```

The model mass is:

```text
BdModel_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        BdVol_lambda(d,h,k;t)
        |Theta_{w,S}^proj(d,h,k;t)|.
```

Here `Theta_{w,S}^proj` is the exact labeled projected local factor from
Module 207. This module does not replace it by `Theta_w^proj`,
`Omega_w^proj`, `kappa_w(d)^2`, or any collision-free generic factor.

Define the deterministic range envelope:

```text
R_bd(rho0)=D0+H0+K0+T0+1.
```

When the fixed row is restricted to:

```text
|h|<=H0,
|k|<=K0,
|t_i|<=T0,
D0<|d|<=2D0,
```

the offsets satisfy:

```text
|a_lambda(d,h,k;t)| <= C_lambda R_bd(rho0).
```

The boundary-volume saving parameter is:

```text
delta_vol_233(lambda;N,rho0)
  = sup BdVol_lambda(d,h,k;t)
```

over the same fixed truncated row.

## 4. Assumptions

`BoundaryModelVolume_233(S,lambda)` is the following package.

### A. Fixed-row discipline

No parameter, projection, selector, or shell is changed:

```text
same P_M,
same R0 and eta0,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same W-residue convention,
same interval cutoff convention,
fixed w, then N -> infinity, then w -> infinity.
```

There is no:

```text
fr -> mv,
sm -> fr,
bern -> sm,
fs -> bern,
major/minor partition transfer.
```

### B. Boundary-volume saving

The fixed row satisfies:

```text
L_N+R_bd(rho0)=o(N)
```

in the fixed-`w`, `N -> infinity` limit, and hence:

```text
delta_vol_233(lambda;N,rho0)
  <= C_lambda (L_N+R_bd(rho0))/N.
```

More generally, it is enough to assume directly that
`delta_vol_233(lambda;N,rho0) -> 0` in the project limit order.

### C. Absolute kernel budget

Let:

```text
A_W(M)=E_t |W_M(t)|.
```

The kernel side satisfies either:

```text
A_W(M)=O_W(1),
```

or the final product:

```text
A_W(M) G_{w,S}(rho0) delta_vol_233(lambda;N,rho0)
```

still tends to zero in the W-admissible limit order below. Any tail outside
`|t_i|<=T0` belongs to `KernelAbsTail_225(P_M,T0)` and is not hidden inside
this model-volume criterion.

### D. Exact local-factor budget

There is a localized bad-factor set:

```text
Bad_{w,S}(d,h,k;t)
```

and a fixed-row envelope:

```text
G_{w,S}(rho0)
```

such that on the good set:

```text
|Theta_{w,S}^proj(d,h,k;t)| <= G_{w,S}(rho0).
```

The bad part is already boundary-localized:

```text
BadBdModel_233(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        BdVol_lambda(d,h,k;t)
        |Theta_{w,S}^proj(d,h,k;t)|
        1_{Bad_{w,S}(d,h,k;t)}
  = o_W(1).
```

The good-part budget is:

```text
lim_{w->infinity} limsup_{N->infinity}
  A_W(M) G_{w,S}(rho0) delta_vol_233(lambda;N,rho0)
  = 0.
```

## 5. Proof / disproof / reduction

Split the model mass into good and bad local-factor regions:

```text
BdModel_225(S,lambda)
  = GoodBdModel_233(S,lambda)
    + BadBdModel_233(S,lambda).
```

The bad part is `o_W(1)` by Assumption D.

On the good part:

```text
|Theta_{w,S}^proj(d,h,k;t)| <= G_{w,S}(rho0)
```

and:

```text
BdVol_lambda(d,h,k;t)
  <= delta_vol_233(lambda;N,rho0).
```

Therefore:

```text
GoodBdModel_233(S,lambda)
  <= G_{w,S}(rho0) delta_vol_233(lambda;N,rho0)
     (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)|.
```

The remaining average is bounded by the absolute kernel budget:

```text
GoodBdModel_233(S,lambda)
  <= A_W(M) G_{w,S}(rho0)
     delta_vol_233(lambda;N,rho0).
```

Assumption D makes this term `o_W(1)`. Thus:

```text
BdModel_225(S,lambda)=o_W(1),
```

which is exactly:

```text
BoundaryModelMass_225(S,lambda).
```

It remains only to justify the displayed volume bound. For fixed
`d,h,k,t`, the event:

```text
n+a_lambda(d,h,k;t) notin I_N^core(L_N)
```

is contained in the union of two intervals of total length at most:

```text
C (L_N+|a_lambda(d,h,k;t)|+1).
```

Dividing by the `n`-normalization gives:

```text
BdVol_lambda(d,h,k;t)
  <= C_lambda (L_N+R_bd(rho0))/N
```

on the fixed truncated row.

### What the test says

For the model side alone, the row is genuinely smaller than the projected
residual endpoint if the exact local factors are bounded, or if their bad
collision mass is already localized and summable, because only a small
boundary volume is being paid.

The test fails if proving `BadBdModel_233=o_W(1)` requires an unlocalized
projected residual fourth-moment estimate. In that case the model-mass row
has become endpoint-strength rather than a local boundary-volume problem.

## 6. Edge cases

- For `S=emptyset`, `Theta_{w,S}^proj=1`, so the criterion reduces to the
  pure boundary-volume and kernel-mass budget.
- If `h`, `k`, or `t` are not restricted by `H0`, `K0`, and `T0`, the
  displayed deterministic volume bound may be false.
- If `D0+H0+K0+T0` is comparable to `N`, the boundary support is not small.
- If `A_W(M)` grows, the boundary volume must beat that growth.
- If `G_{w,S}(rho0)` grows too quickly as `w` varies, the W-limit order may
  fail even when `delta_vol_233 -> 0` for fixed `w`.
- If structural collision strata make `Theta_{w,S}^proj` large on the
  boundary, they must be included in `BadBdModel_233`; they cannot be erased
  by replacing the model with a generic factor.
- If the boundary set interacts with W-residue or prime-power errors, those
  errors belong to `WPPBoundary_225`, not to this pure model-mass criterion.
- Negative shifts `d` are covered by the offset bound and cannot be discarded
  without a separate symmetry argument.
- This model-side criterion does not control the actual weighted tuple row
  `BoundaryTupleHL_225(S,lambda)`.

## 7. Where it fits in the project map

The Phase F1 chain now begins:

```text
Module 224
  -> fixed projected-major boundary/prefix row
Module 225
  -> expansion into tuple and model envelopes
Module 226
  -> conditional local verdict under LocalBdPkg_226
Module 232
  -> branch decision to attack model mass first
Module 233
  -> BoundaryModelVolume_233(S,lambda)
     => BoundaryModelMass_225(S,lambda).
```

This advances only the model-mass subrow of `LocalBdPkg_226`. It does not
settle the tuple-matching, kernel-tail, W/prime-power, normalization, or
selector-transfer rows.

## 8. What remains open

This module does not prove:

- the local-factor envelope `G_{w,S}(rho0)` for every `S`;
- the bad local-factor bound `BadBdModel_233(S,lambda)=o_W(1)`;
- bounded absolute kernel mass for the chosen `P_M`;
- `KernelAbsTail_225(P_M,T0)`;
- `BoundaryTupleHL_225(S,lambda)`;
- `WPPBoundary_225`;
- `NormRow_224^P`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
- `ProjectedMajorTarget_3^B`;
- `CycIntTransfer_3^major(P_adm)`;
- selector transfer to the actual sharp moving selector;
- smoothed-to-sharp or frozen-to-moving transfer;
- Bernoulli or finite-stage deterministic extraction;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat `BoundaryModelVolume_233` as proving the actual boundary row.
- Do not use this model-side volume criterion as a substitute for
  `BoundaryTupleHL_225(S,lambda)`.
- Do not hide kernel tails inside `BoundaryModelMass_225`.
- Do not use cancellation from `W_M` after taking `|W_M|`.
- Do not replace `Theta_{w,S}^proj` by the full eight-form factor, by
  `Omega_w^proj`, or by a generic collision-free model.
- Do not replace rectangle faces by `kappa_w(d)^2`; `Sigma_w` remains the
  exact rectangle model.
- Do not change selector class, projection, denominator grid, or dyadic shell
  inside this fixed-row criterion.
- Do not prove the model-mass bad part by assuming the projected residual
  endpoint.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
