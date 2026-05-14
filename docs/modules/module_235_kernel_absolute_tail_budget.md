# Module 235: Kernel absolute-tail budget for the fixed row

## 1. Precise theorem / claim being advanced

This module isolates the fixed-row kernel package from Module 225:

```text
KernelAbsTail_225(P_M,T0):
  A_W(M)=E_t |W_M(t)|=O_W(1),
  TailCube_225(T0)=o_W(1).
```

The fixed row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

Define:

```text
KernelTailBudget_235(P_M,T0;s0,D0,rho0).
```

Conditional claim:

```text
KernelTailBudget_235(P_M,T0;s0,D0,rho0)
  => KernelAbsTail_225(P_M,T0).
```

The important verdict is:

```text
A_W(M)=O_W(1) is a projection-kernel condition.
TailCube_225(T0)=o_W(1) is not a kernel condition alone.
```

The tail cube also requires an absolute residual-product envelope on the
region:

```text
max_i |t_i|>T0.
```

If this envelope is supplied by boundary/tail weighted tuple estimates, the
row is mixed but still local to the fixed row. If it is supplied by the
unlocalized projected residual endpoint, the row is endpoint-strength.

## 2. Status label

`CONDITIONAL`

The module gives a deterministic budget and classification. It does not prove
the absolute kernel mass of the chosen major projection and does not prove the
tail cube estimate.

## 3. Definitions and variables

Use the fixed data:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The nonzero major projection has kernel:

```text
P_M F(x)=E_t K_M(t)F(x-t),
K_M(t)=sum_xi m_M(xi)e(xi t),
m_M(0)=0.
```

For the four projected cube slots:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The one-kernel and four-kernel absolute masses are:

```text
A_1(M)=E_t |K_M(t)|,
A_W(M)=E_{t0,t1,t2,t3}|W_M(t0,t1,t2,t3)|.
```

When the four `t_i` are averaged independently with the same normalization:

```text
A_W(M)=A_1(M)^4.
```

For a truncation parameter `T0`, define:

```text
tau_M(T0)=E_{|t|>T0}|K_M(t)|,
Tail_W(T0)=E_t |W_M(t)| 1_{max_i |t_i|>T0}.
```

Then:

```text
Tail_W(T0) <= 4 A_1(M)^3 tau_M(T0)
```

up to the harmless normalization convention of the four `t_i` averages.

The kernel-tail event from Module 225 is:

```text
TailT_224(t)=1_{max_i |t_i|>T0}.
```

The residual product is:

```text
ProductB_d(n,h,k;t)
  = B_d(n-t0)
    conj(B_d(n+h-t1))
    conj(B_d(n+k-t2))
    B_d(n+h+k-t3).
```

The tail cube is:

```text
TailCube_225(T0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)| TailT_224(t).
```

## 4. Assumptions

`KernelTailBudget_235(P_M,T0;s0,D0,rho0)` consists of the following
requirements.

### A. Fixed-row discipline

No projection or selector switch is allowed inside the budget:

```text
same P_M,
same K_M,
same R0 and eta0,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same W-residue convention,
same interval cutoff convention,
fixed w, then N -> infinity, then w -> infinity.
```

If one replaces a sharp projection by a smoothed projection to improve
`A_W(M)` or `tau_M(T0)`, the proof has moved to a different projection and
must include a projection-transfer row. That is mixed, not this pure fixed
budget.

### B. Absolute kernel mass

The fixed kernel satisfies either:

```text
A_W(M)=O_W(1),
```

or every later fixed-row saving is stated with the explicit multiplier
`A_W(M)`. The convenient bounded version is:

```text
limsup_{N->infinity} A_W(M) <= C_W(w,rho0),
```

with:

```text
limsup_{w->infinity} C_W(w,rho0) < infinity
```

whenever the row needs an actual `O_W(1)` bound.

### C. Kernel tail mass

The projection has a truncation scale `T0=T0(N,w,rho0)` satisfying:

```text
Tail_W(T0)=o_W(1)
```

or, in one-kernel form:

```text
A_1(M)^3 tau_M(T0)=o_W(1).
```

This condition controls only the absolute mass of the kernel tail. It does
not by itself control `TailCube_225(T0)` when the residual product is
unbounded.

### D. Tail residual-product envelope

Define a tail absolute cube envelope:

```text
U_tail_235(T0)
```

by the least admissible weighted-essential supremum satisfying:

```text
E_{n,h,k}|ProductB_d(n,h,k;t)|
  <= U_tail_235(T0)
```

for every admissible `(d,t)` in the tail region:

```text
D0<|d|<=2D0,
max_i |t_i|>T0
```

outside a separately named exceptional set whose contribution is already
included in the expanded tuple formulation below.

Equivalently, one may supply the stronger expanded tuple package:

```text
TailTuple_235(S):
  (1/D0) sum_{D0<|d|<=2D0}
    E_{n,h,k,t} |W_M(t)| TailT_224(t)
      prod_{sigma in S} mu_s0(v_sigma)
  = o_W(1)
```

for every:

```text
S subset Lambda_8,
```

after applying `AbsMajorant_225(s0)`.

The budget condition is:

```text
Tail_W(T0) U_tail_235(T0)=o_W(1)
```

in the uniform-envelope formulation, or:

```text
TailTuple_235(S)=o_W(1) for every S subset Lambda_8
```

in the expanded tuple formulation.

## 5. Proof / disproof / reduction

### A. Absolute mass reduction

By definition:

```text
A_W(M)=E_t |W_M(t)|.
```

If the four kernels are independently averaged:

```text
A_W(M)=A_1(M)^4.
```

The four-fold tail satisfies:

```text
Tail_W(T0)
  = E_t |W_M(t)| 1_{max_i |t_i|>T0}
  <= sum_{j=0}^3
      E_t |W_M(t)| 1_{|t_j|>T0}
  <= 4 A_1(M)^3 tau_M(T0).
```

Thus Assumptions B and C give the kernel half of
`KernelAbsTail_225(P_M,T0)`.

### B. Tail cube reduction by a uniform product envelope

If the tail residual product has the uniform averaged envelope
`U_tail_235(T0)`, then:

```text
TailCube_225(T0)
  <= Tail_W(T0) U_tail_235(T0).
```

The budget condition:

```text
Tail_W(T0) U_tail_235(T0)=o_W(1)
```

therefore gives:

```text
TailCube_225(T0)=o_W(1).
```

### C. Tail cube reduction by tuple expansion

Using `AbsMajorant_225(s0)`:

```text
|ProductB_d(n,h,k;t)|
  <= C_s0^8 prod_{sigma in Lambda_8}(1+mu_s0(v_sigma)).
```

Expanding the positive product gives:

```text
|ProductB_d|
  <= C_s0^8
     sum_{S subset Lambda_8}
       prod_{sigma in S} mu_s0(v_sigma).
```

Therefore:

```text
TailCube_225(T0)
  <= C_s0^8
     sum_{S subset Lambda_8} TailTuple_235(S).
```

If all tail tuple rows are `o_W(1)`, then:

```text
TailCube_225(T0)=o_W(1).
```

Together with the absolute kernel mass bound, this proves the conditional
implication:

```text
KernelTailBudget_235(P_M,T0;s0,D0,rho0)
  => KernelAbsTail_225(P_M,T0).
```

### D. Classification

The budget is projection-local if:

```text
A_W(M), tau_M(T0), and TailTuple_235(S)
```

are proved for the same fixed projection `P_M` and selector class `s0`.

It is mixed if it needs:

```text
projection smoothing transfer,
major-arc multiplier replacement,
W-residue boundary transfer,
prime-power tail transfer,
or range/denominator changes caused by a large T0.
```

It is endpoint-strength if `TailCube_225(T0)` is proved by assuming:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1)
```

or any equivalent unlocalized projected residual fourth-moment estimate.

## 6. Edge cases

- If `K_M` is a sharp major-arc cutoff, `A_1(M)` may grow; bounded absolute
  mass is not automatic.
- If smoothing is introduced to force `A_1(M)=O(1)`, the model and projection
  must be updated and compared back to the original target.
- If `T0` is too small, `tau_M(T0)` may be large and the kernel tail dominates.
- If `T0` is too large, the shifted vertices may leave the fixed finite-range
  regime and create range or CRT errors.
- If the residual product is unbounded, `Tail_W(T0)=o_W(1)` alone is
  insufficient.
- If a tail tuple row uses cancellation in `W_M`, it does not apply after the
  absolute value in `TailCube_225`.
- If prime powers occur only in the tail region, they still require the
  projected fourth-moment prime-power row, not just first-moment sparsity.
- Negative shifts `d` do not change the kernel budget but do affect the
  finite-range envelope of the shifted vertices.
- If `m_M(0) != 0`, the row is no longer the nonzero projected major row from
  Module 224.

## 7. Where it fits in the project map

The Phase F1 fixed-row analysis now has:

```text
Module 233
  -> BoundaryModelMass_225 reduced to boundary volume plus local-factor
     budgets.

Module 234
  -> BoundaryTupleHL_225 reduced to boundary interval weighted HL,
     with nonempty rows still open.

Module 235
  -> KernelAbsTail_225 reduced to absolute kernel mass, kernel tail mass,
     and tail residual-product envelopes.
```

This module narrows `LocalBdPkg_226` by showing exactly where the projection
kernel enters. It does not prove the boundary/prefix row and does not replace
the tuple or model-mass rows.

## 8. What remains open

This module does not prove:

- bounded absolute mass for the chosen `P_M`;
- a tail scale `T0` with `Tail_W(T0)=o_W(1)`;
- any `TailTuple_235(S)` estimate;
- a uniform residual-product envelope `U_tail_235(T0)`;
- `KernelAbsTail_225(P_M,T0)` unconditionally;
- `BoundaryIntervalHL_234(S,lambda)` for nonempty `S`;
- `BoundaryTupleHL_225(S,lambda)` for nonempty `S`;
- `BoundaryModelMass_225(S,lambda)` beyond Module 233's conditional
  criterion;
- `WPPBoundary_225`;
- `NormRow_224^P`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
- `ProjectedMajorTarget_3^B`;
- `CycIntTransfer_3^major(P_adm)`;
- selector transfer to the actual sharp moving selector;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not assume `A_W(M)=O_W(1)` for a sharp projection without proof.
- Do not treat `Tail_W(T0)=o_W(1)` as `TailCube_225(T0)=o_W(1)`.
- Do not use cancellation from `W_M` after taking `|W_M|`.
- Do not hide kernel tails inside `BoundaryModelMass_225` or
  `BoundaryTupleHL_225`.
- Do not switch to a smoothed projection without a projection-transfer row.
- Do not use first-moment prime-power sparsity as projected fourth-moment tail
  control.
- Do not prove `TailCube_225` by assuming the projected residual endpoint.
- Do not change selector class, projection, denominator grid, or dyadic shell
  inside this fixed-row budget.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
