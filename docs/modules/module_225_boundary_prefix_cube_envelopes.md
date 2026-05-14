# Module 225: Boundary/prefix row cube expansion and envelopes

## 1. Precise theorem / claim being advanced

This module expands the fixed test row from Module 224:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0)
```

into its eight-vertex residual fourth-moment cube and records the exact
envelopes that would make it `o_W(1)`.

The claim is a conditional reduction:

```text
AbsMajorant_225(s0)
  + KernelAbsTail_225(P_M,T0)
  + BoundaryTupleHL_225(S,lambda)
  + BoundaryModelMass_225(S,lambda)
  + WPPBoundary_225
  + NormRow_224^P=o_W(1)

    => BdPrefRow_224^P(s0,D0;N,w,rho0)=o_W(1).
```

Here:

```text
lambda in Lambda_8={00,10,01,11} x {0,1}
```

labels which one of the eight residual vertices lies in the boundary or
prefix support. The reduction is local in the sense that every summand is
supported on at least one declared boundary/prefix vertex after forming
`B_d`.

This module does not prove any of the displayed envelopes.

## 2. Status label

`CONDITIONAL`

The expansion and domination are deterministic once the majorant and support
conventions are fixed. The analytic estimates needed to make the row small
remain open.

## 3. Definitions and variables

Keep the fixed choices from Module 224:

```text
Pi=P_M,
edge=cyc_s0 -> int_s0,
s0 in {model, W, sm, fr},
D0<|d|<=2D0,
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
w fixed, N -> infinity, then w -> infinity.
```

The selector class is held fixed. There is no:

```text
fr -> mv,
sm -> fr,
bern -> sm,
fs -> bern,
major/minor partition change.
```

For the fixed class:

```text
nu=nu_s0,
f=f_s0=nu_s0-1,
B_d(n)=f(n+d)conj(f(n)).
```

The four projected `B_d` slots are:

```text
x00=n-t0,
x10=n+h-t1,
x01=n+k-t2,
x11=n+h+k-t3.
```

The eight residual vertices are:

```text
v_{00,0}=x00,
v_{00,1}=x00+d,
v_{10,0}=x10,
v_{10,1}=x10+d,
v_{01,0}=x01,
v_{01,1}=x01+d,
v_{11,0}=x11,
v_{11,1}=x11+d.
```

Let:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

Write `v_lambda` for the vertex with label `lambda`.

The residual product is:

```text
ProductB_d(n,h,k;t)
  = B_d(x00) conj(B_d(x10)) conj(B_d(x01)) B_d(x11).
```

For the real-valued prime or W-tricked weights in this branch, the signed
residual cube is:

```text
ProductB_d(n,h,k;t)
  = sum_{S subset Lambda_8}
      (-1)^(8-|S|)
      prod_{lambda in S} nu(v_lambda),
```

with the conjugations already absorbed in the four `B_d` slots. If a later
complex-valued model class is introduced, the same line must be rewritten with
conjugated labeled weights before it is used. In the prime or W-tricked
settings used here, the relevant majorants are nonnegative, so the absolute
boundary row is handled through a positive tuple majorant rather than through
cancellation in the signed residual sum.

The core and boundary/prefix support from Module 224 are:

```text
Core_224(d,n,h,k;t)
  = prod_{lambda in Lambda_8} 1_{v_lambda in I_N^core(L_N)}
    prod_{i=0}^3 1_{|t_i|<=T0},

BdPref_224(d,n,h,k;t)=1-Core_224(d,n,h,k;t).
```

For each vertex label define the vertex boundary event:

```text
Bd_lambda(d,n,h,k;t)
  = 1_{v_lambda notin I_N^core(L_N)}.
```

The kernel-tail event is:

```text
TailT_224(t)=1_{max_i |t_i|>T0}.
```

Then:

```text
BdPref_224
  <= TailT_224 + sum_{lambda in Lambda_8} Bd_lambda.
```

This is the exact union decomposition used in the reduction.

## 4. Assumptions

The first required assumption is a nonnegative tuple majorant for the fixed
selector class:

```text
AbsMajorant_225(s0).
```

It means there is a nonnegative weight `mu_s0` such that:

```text
|f_s0(n)| <= C_s0 (1+mu_s0(n))
```

on the interval and W-tricked residue class used by `rho0`, and every tuple
estimate below is stated for products of `mu_s0`. In the prime-only or
W-tricked von-Mangoldt setting one may take `mu_s0` to be the corresponding
nonnegative prime or W-weight. If no such majorant is declared, this
absolute-value route is unavailable.

The second assumption is the fixed kernel package:

```text
KernelAbsTail_225(P_M,T0):
  A_W(M)=E_t |W_M(t)|=O_W(1),
  TailCube_225(T0)=o_W(1),
```

where:

```text
TailCube_225(T0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)| TailT_224(t).
```

The third assumption is a boundary-marked tuple envelope for every:

```text
S subset Lambda_8,
lambda in Lambda_8.
```

Define the boundary tuple average:

```text
BTuple_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        E_n Bd_lambda(d,n,h,k;t)
          prod_{sigma in S} mu_s0(v_sigma).
```

Let:

```text
BdVol_lambda(d,h,k;t)
  = E_n Bd_lambda(d,n,h,k;t)
```

in the same interval convention. The boundary local model for the tuple is:

```text
BdModel_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        BdVol_lambda(d,h,k;t)
        |Theta_{w,S}^proj(d,h,k;t)|.
```

The required pair of assumptions is:

```text
BoundaryTupleHL_225(S,lambda):
  |BTuple_225(S,lambda)-BdModel_225(S,lambda)|=o_W(1),

BoundaryModelMass_225(S,lambda):
  BdModel_225(S,lambda)=o_W(1).
```

The fourth assumption handles small-prime, W-residue, and prime-power
interactions on the same boundary support:

```text
WPPBoundary_225=o_W(1).
```

It is the sum of the W-residue failures and prime-power artifacts whose
support also intersects `Bd_lambda` or `TailT_224`. If the W-residue
convention is exact and `s0` is prime-only, this term may be zero. Otherwise
it must be estimated in the same projected fourth-moment normalization.

The normalization row is the one already fixed in Module 224:

```text
NormRow_224^P(s0,D0;N,w,rho0)=o_W(1).
```

## 5. Proof / disproof / reduction

Begin with the absolute row:

```text
BdPrefRow_224^P
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)|
        BdPref_224(d,n,h,k;t).
```

Use:

```text
BdPref_224 <= TailT_224 + sum_lambda Bd_lambda.
```

This gives:

```text
BdPrefRow_224^P
  <= TailCube_225(T0)
     + sum_{lambda in Lambda_8} VertexBdRow_225(lambda),
```

where:

```text
VertexBdRow_225(lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)|
        Bd_lambda(d,n,h,k;t).
```

By `AbsMajorant_225(s0)`:

```text
|ProductB_d(n,h,k;t)|
  <= C_s0^8 prod_{lambda in Lambda_8} (1+mu_s0(v_lambda)).
```

Expanding the positive product gives:

```text
prod_{lambda in Lambda_8} (1+mu_s0(v_lambda))
  = sum_{S subset Lambda_8} prod_{sigma in S} mu_s0(v_sigma).
```

Therefore:

```text
VertexBdRow_225(lambda)
  <= C_s0^8 sum_{S subset Lambda_8} BTuple_225(S,lambda).
```

For every pair `(S,lambda)`, insert and subtract the boundary local model:

```text
BTuple_225(S,lambda)
  <= |BTuple_225(S,lambda)-BdModel_225(S,lambda)|
     + BdModel_225(S,lambda).
```

If:

```text
TailCube_225=o_W(1),
BoundaryTupleHL_225(S,lambda)=o_W(1),
BoundaryModelMass_225(S,lambda)=o_W(1),
WPPBoundary_225=o_W(1),
```

for all `S` and `lambda`, then:

```text
BdPrefRow_224^P=o_W(1).
```

Together with:

```text
NormRow_224^P=o_W(1),
```

Module 224 then gives the fixed cyclic-to-interval projected actual-cube
transfer on the shell `D0<|d|<=2D0`.

This is a reduction, not an estimate. The hard analytic content is precisely
the boundary-marked tuple family `BoundaryTupleHL_225(S,lambda)` and the
absolute model mass bound `BoundaryModelMass_225(S,lambda)`.

## 6. Why first-moment boundary counting is insufficient

A first-moment boundary estimate has the schematic form:

```text
E_n Bd_lambda(d,n,h,k;t) = O(L_N/N + endpoint losses).
```

That is not the same as:

```text
E_n Bd_lambda(d,n,h,k;t)
  prod_{sigma in S} mu_s0(v_sigma)
```

uniformly over:

```text
D0<|d|<=2D0,
h,k,
t,
S subset Lambda_8,
lambda in Lambda_8.
```

The reason is that the residual fourth-moment row contains up to eight
unbounded or structured prime-type weights, and the proof has passed to
`|W_M(t)|`, so cancellation from the projected kernel is no longer available.
Boundary volume alone would be enough only after a weighted tuple envelope
shows that prime-type mass does not concentrate on the boundary/prefix
support in this normalization.

Thus ordinary first-moment Hardy-Littlewood, ordinary pair-BDH, or a bare
boundary-volume estimate cannot replace `BoundaryTupleHL_225` and
`BoundaryModelMass_225`.

## 7. Locality diagnosis

After expansion, the row is still plausibly local only under the following
interpretation:

```text
at least one of the eight residual vertices is forced into a boundary,
prefix, or kernel-tail set of relative size o(1).
```

It is not automatically local merely because Module 224 named it as a
boundary row. The locality survives only if the tuple envelopes above hold
with constants uniform in the fixed shell and W-limit order.

The dangerous cases are:

```text
large |W_M| absolute mass,
boundary concentration of prime-type weights,
structural collision strata contained in the boundary,
W-residue failures near endpoints,
prime-power support intersecting boundary sets,
normalization drift between cyclic and interval averages.
```

If any of these forces an unlocalized residual fourth-moment estimate, Module
226 should mark the row mixed or endpoint-strength rather than local.

## 8. Edge cases

- If `L_N` is too small, the boundary model mass may not go to zero after
  weighted tuple amplification.
- If `L_N` is too large, the boundary row may remove too much of the interval
  and alter the target.
- If `T0` is too small, `TailCube_225` may dominate. If `T0` is too large,
  the kernel range may destroy finite-range CRT control.
- If `A_W(M)` grows with `R0` or `eta0`, the boundary volume saving must beat
  that growth.
- If two or more vertices collide structurally on the boundary, the local
  factor must use the correct labeled subset model, not a generic
  collision-free factor.
- If the W-residue convention fails near an endpoint, the error belongs to
  `WPPBoundary_225`, not to `Theta_{w,S}^proj`.
- If prime powers are present in `s0`, first-moment prime-power sparsity is
  not enough; the boundary cube contribution must be controlled.
- If the target uses a centered product, zero-mode leakage from boundary
  truncation must be added to the normalization or centering row.
- Negative `d` is included in the same vertex boundary events and cannot be
  dropped without a separate symmetry argument.

## 9. Where it fits in the project map

The Phase E local-row test is now:

```text
Module 224
  -> fix BdPrefRow_224^P and its support
Module 225
  -> expand it into boundary-marked eight-vertex tuple envelopes
Module 226
  -> decide whether those envelopes are genuinely local, conditional, or
     endpoint-strength.
```

This module uses the local-model dictionary from Module 207, the kernel
absolute-mass warning from Module 190, the cyclic-to-interval framework from
Module 210, and the prime-power / W-residue separation from Module 211.

It does not enter the endpoint-equivalence audit yet. That starts in Module
227 after the row verdict of Module 226.

## 10. What remains open

This module does not prove:

- `AbsMajorant_225(s0)` for every possible selector class;
- `KernelAbsTail_225(P_M,T0)`;
- `TailCube_225(T0)=o_W(1)`;
- any `BoundaryTupleHL_225(S,lambda)`;
- any `BoundaryModelMass_225(S,lambda)`;
- `WPPBoundary_225=o_W(1)`;
- `NormRow_224^P=o_W(1)`;
- `BdPrefRow_224^P=o_W(1)`;
- `CycIntTransfer_3^major(P_adm)` in full;
- selector transfer to the actual sharp moving selector;
- smoothed-to-sharp, frozen-to-moving, Bernoulli, or finite-stage extraction;
- `MajorMinorSelCompat_3(P_adm)`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not replace `BoundaryTupleHL_225` by first-moment boundary volume.
- Do not use cancellation in `W_M` after taking `|W_M|`.
- Do not replace the boundary-marked `Theta_{w,S}^proj` family by the full
  eight-form model alone.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2` on rectangle
  faces.
- Do not hide W-residue, prime-power, zero-mode, or normalization errors in
  the boundary notation.
- Do not transfer this fixed `s0` row to `mv` without the selector-transfer
  packages.
- Do not claim the boundary row is proved merely because it is supported on a
  small set.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
