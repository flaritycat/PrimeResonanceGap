# Module 239: Easiest model subrow proof and blocked extension

## 1. Precise theorem / claim being advanced

This module performs the proof-or-blocked test requested by Phase F1 for the
easiest boundary subrow.

The fixed row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

Define the easiest subrow:

```text
EasyModelSubrow_239(lambda)
```

to be the `S=emptyset` boundary/model/tail/convention subrow attached to one
boundary label:

```text
lambda in Lambda_8.
```

Conditional claim:

```text
EasyModelPkg_239(lambda)
  => EasyModelSubrow_239(lambda).
```

More explicitly, under the package below:

```text
BoundaryTupleHL_225(emptyset,lambda)
  holds with zero error,

BoundaryModelMass_225(emptyset,lambda)
  holds,

TailTuple_235(emptyset)
  holds,

WResTuple_236(emptyset)
  is zero or o_W(1),

PPTupleBoundary_236(emptyset,tau)
  is zero or o_W(1) in the prime-only/model convention,

NormRow_224^P and active ZeroBd_226
  are zero or o_W(1) by the declared normalization/zero-mode convention.
```

The blocked verdict is:

```text
EasyModelSubrow_239 does not extend to nonempty actual weighted tuple rows.
```

The extension is blocked unless the project supplies:

```text
FixedSupportTupleHL_238,
```

or the corresponding nonempty rows:

```text
BoundaryIntervalHL_234(S,lambda),
TailTuple_235(S),
WResTuple_236(S),
PPTupleBoundary_236(S,tau)
```

for `S nonempty`.

## 2. Status label

`CONDITIONAL`

The `S=emptyset` identities are exact, but the smallness of the boundary and
tail masses depends on explicit kernel, volume, and convention hypotheses.
The nonempty actual weighted tuple extension remains open.

## 3. Definitions and variables

Use:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The eight labels are:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

For a boundary label `lambda`, let:

```text
Bd_lambda(d,n,h,k;t)
  = 1_{v_lambda notin I_N^core(L_N)},

BdVol_lambda(d,h,k;t)
  = E_n Bd_lambda(d,n,h,k;t).
```

The `S=emptyset` tuple and model rows are:

```text
BTuple_225(emptyset,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)| BdVol_lambda(d,h,k;t),
```

and:

```text
BdModel_225(emptyset,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        BdVol_lambda(d,h,k;t)
        |Theta_{w,emptyset}^proj(d,h,k;t)|.
```

The empty local factor is:

```text
Theta_{w,emptyset}^proj=1.
```

The boundary-volume parameter from Module 233 is:

```text
delta_vol_233(lambda;N,rho0)
  = sup BdVol_lambda(d,h,k;t)
```

over the fixed truncated row.

The empty tail tuple is:

```text
TailTuple_235(emptyset)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| TailT_224(t).
```

Since the empty product is `1`, this is just the four-kernel tail mass:

```text
TailTuple_235(emptyset)=Tail_W(T0)
```

in the fixed row normalization.

## 4. Assumptions

`EasyModelPkg_239(lambda)` consists of the following requirements.

### A. Fixed-row discipline

All objects use the same:

```text
P_M,
K_M,
R0 and eta0,
selector class s0,
W-residue convention,
prime-only or model convention,
centering convention,
interval cutoff convention,
dyadic shell D0<|d|<=2D0,
fixed w, then N -> infinity, then w -> infinity limit order.
```

No selector, projection, denominator, W-residue, or prime-power convention is
changed inside this subrow.

### B. Boundary volume and kernel mass

The empty boundary model mass has:

```text
A_W(M) delta_vol_233(lambda;N,rho0)=o_W(1),
```

where:

```text
A_W(M)=E_t |W_M(t)|.
```

This is the `S=emptyset` instance of the Module 233 volume criterion.

### C. Kernel tail

The empty tail row satisfies:

```text
Tail_W(T0)=o_W(1).
```

Equivalently, by Module 235 it is enough to assume:

```text
A_1(M)^3 tau_M(T0)=o_W(1).
```

### D. Pure convention rows

The W-residue and prime-power convention is pure for this subrow:

```text
WFail_236=0
```

on the fixed row, or at least:

```text
WResTuple_236(emptyset)=o_W(1),
```

and:

```text
pp_s0=0
```

or:

```text
PPTupleBoundary_236(emptyset,tau)=o_W(1)
```

for every `tau in Lambda_8`.

The normalization/zero-mode convention satisfies either:

```text
NormExact_237
and
z_M(T0)=0,
```

or the small drift and leakage alternatives from Module 237:

```text
NormDrift_237,
ZeroBd_226=o_W(1).
```

## 5. Proof / disproof / reduction

### A. Empty tuple row

For `S=emptyset`:

```text
prod_{sigma in S} mu_s0(v_sigma)=1,
Theta_{w,emptyset}^proj=1.
```

Therefore:

```text
BTuple_225(emptyset,lambda)
  = (1/D0) sum_d E_{h,k,t}|W_M(t)| BdVol_lambda(d,h,k;t)
```

and:

```text
BdModel_225(emptyset,lambda)
  = (1/D0) sum_d E_{h,k,t}|W_M(t)| BdVol_lambda(d,h,k;t).
```

Thus:

```text
|BTuple_225(emptyset,lambda)
  - BdModel_225(emptyset,lambda)|=0.
```

This is the exact `BoundaryTupleHL_225(emptyset,lambda)` row from Module
234.

### B. Empty model mass

By the definition of `delta_vol_233`:

```text
BdVol_lambda(d,h,k;t)
  <= delta_vol_233(lambda;N,rho0).
```

Hence:

```text
BdModel_225(emptyset,lambda)
  <= A_W(M) delta_vol_233(lambda;N,rho0).
```

Assumption B gives:

```text
BdModel_225(emptyset,lambda)=o_W(1).
```

This proves the empty model-mass row conditionally on a checkable
boundary-volume and kernel-mass budget.

### C. Empty tail row

For the empty product:

```text
TailTuple_235(emptyset)
  = E_t |W_M(t)| 1_{max_i |t_i|>T0}
  = Tail_W(T0).
```

Assumption C gives:

```text
TailTuple_235(emptyset)=o_W(1).
```

This is a genuine kernel-tail subrow. It does not prove any nonempty
`TailTuple_235(S)`.

### D. Pure W/prime-power and normalization rows

If:

```text
WFail_236=0,
pp_s0=0,
NormExact_237,
z_M(T0)=0,
```

then the W-residue, prime-power, normalization, and zero-mode rows are zero
by convention in this easiest subrow.

If the zero alternatives are not available, the small rows explicitly listed
in Assumption D are enough by Modules 236 and 237.

Therefore:

```text
EasyModelPkg_239(lambda)
  => EasyModelSubrow_239(lambda).
```

### E. Blocked extension to the actual weighted row

For `S nonempty`, the row becomes:

```text
E_n 1_{J_{lambda,r}}(n)
  prod_{sigma in S} mu_s0(n+a_sigma)
```

or one of its tail/W-residue/prime-power variants. The proof above used only:

```text
prod_{sigma in emptyset} mu_s0(v_sigma)=1.
```

That identity disappears for `S nonempty`. Boundary volume no longer controls
the product unless a weighted tuple theorem prevents concentration of the
weights on the fixed support.

Thus the route:

```text
EasyModelSubrow_239
  => BoundaryIntervalHL_234(S,lambda) for S nonempty
```

is blocked.

The missing input is exactly:

```text
FixedSupportTupleHL_238.
```

This is a blocked extension, not a contradiction. It says the easiest subrow
is genuinely smaller, but it is not representative of the analytic heart of
the fixed boundary row.

## 6. Edge cases

- The `S=emptyset` tuple row is exact, but it contains no prime-type weight.
  It cannot be used as evidence for nonempty `S`.
- If `A_W(M)` grows, the boundary volume must beat that growth even in the
  empty model row.
- If `Tail_W(T0)=o_W(1)` fails, even the empty tail subrow is not closed.
- If W-residue compatibility fails on the boundary or tail support,
  `WResTuple_236(emptyset)` must be estimated rather than declared zero.
- If `pp_s0` is nonzero, prime-power boundary rows are not eliminated by this
  module.
- If `NormExact_237` fails, the small normalization-drift row is still needed.
- If `z_M(T0) != 0`, exact cyclic zero-mode removal is not enough.
- If one changes selector class, projection, W-residue family, or dyadic
  shell, this is no longer the fixed subrow.
- If nonempty tuple rows are proved by assuming the unlocalized projected
  residual endpoint, the proof has left the local boundary route.

## 7. Where it fits in the project map

The Phase F1 chain now has:

```text
Module 238
  -> composition and bottleneck:
     FixedSupportTupleHL_238.

Module 239
  -> easiest subrow:
     S=emptyset / model-convention row closes conditionally,
     nonempty actual tuple extension is blocked without FixedSupportTupleHL.
```

This satisfies the Phase F1 success criterion in a limited but honest sense:
one subrow has been reduced to concrete, checkable kernel-volume and
convention conditions. The first genuine analytic bottleneck remains
nonempty fixed-support weighted tuple control.

## 8. What remains open

This module does not prove:

- any nonempty `BoundaryIntervalHL_234(S,lambda)`;
- any nonempty `TailTuple_235(S)`;
- any nonempty `WResTuple_236(S)`;
- any nonempty `PPTupleBoundary_236(S,tau)`;
- `FixedSupportTupleHL_238`;
- the full `FixedRowPkg_238`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)` unconditionally;
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

- Do not treat the `S=emptyset` subrow as evidence for nonempty weighted tuple
  rows.
- Do not cite the empty model proof as a proof of `BdPrefRow_224^P`.
- Do not replace nonempty boundary interval HL by boundary volume.
- Do not use first-moment HL, ordinary pair-BDH, or model mass as actual
  weighted tuple matching.
- Do not use `Tail_W(T0)=o_W(1)` as a substitute for nonempty
  `TailTuple_235(S)`.
- Do not hide W-residue, prime-power, normalization, or zero-mode terms inside
  the empty-row notation.
- Do not prove nonempty fixed-support tuple rows by assuming the projected
  residual endpoint.
- Do not change selector class, projection, W-residue convention, or dyadic
  shell inside this easiest subrow.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
