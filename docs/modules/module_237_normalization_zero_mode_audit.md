# Module 237: Normalization and zero-mode audit

## 1. Precise theorem / claim being advanced

This module audits the remaining fixed-row normalization package:

```text
NormRow_224^P(s0,D0;N,w,rho0)=o_W(1),
ZeroBd_226=o_W(1) when needed.
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
NormZeroAudit_237(s0,D0,rho0).
```

Conditional claim:

```text
NormZeroAudit_237(s0,D0,rho0)
  => NormRow_224^P=o_W(1)
     and ZeroBd_226=o_W(1) when ZeroBd_226 is active.
```

The verdict is:

```text
NormRow_224^P may be declared zero only when cyclic and interval averages
use the same normalization on the same core by definition.

ZeroBd_226 may be declared zero only when the exact zero-mode convention
survives interval and kernel truncation.
```

Otherwise both are genuine side rows. They are lower-dimensional than the
projected residual endpoint, but they can become mixed if they require
projection smoothing, centering transfer, W-normalization changes, or
selector transfer.

## 2. Status label

`CONDITIONAL`

The module gives deterministic domination criteria and a classification. It
does not prove the normalization row or any zero-mode leakage estimate.

## 3. Definitions and variables

Use the fixed notation of Modules 224-236:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The projected kernel satisfies:

```text
P_M F(x)=E_t K_M(t)F(x-t),
m_M(0)=0
```

in the exact cyclic model. For:

```text
t=(t0,t1,t2,t3),
```

write:

```text
W_M(t)=K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The residual derivative object is:

```text
B_d(n)=f_s0(n+d)conj(f_s0(n)).
```

If centering is used, write:

```text
c_d^cyc=E_n^cyc B_d(n),
c_d^int=E_n^int B_d(n),
B_{d,cyc}^circ=B_d-c_d^cyc,
B_{d,int}^circ=B_d-c_d^int.
```

The normalization row from Module 224 is:

```text
NormRow_224^P(s0,D0;N,w,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      |Vol_cyc(rho0)-Vol_int(d,rho0)| Lambda_{d,s0},
```

where:

```text
|ActualProjCube_{d,cyc,s0}^P|
  + |ActualProjCube_{d,int,s0}^P|
  <= Lambda_{d,s0}.
```

Define:

```text
DeltaVol_237(d;rho0)
  = |Vol_cyc(rho0)-Vol_int(d,rho0)|.
```

The normalized average envelope is:

```text
LambdaAvg_237
  = (1/D0) sum_{D0<|d|<=2D0} Lambda_{d,s0}.
```

For the truncated interval kernel, define the one-slot zero-mode leakage:

```text
z_M(T0)
  = E_t K_M(t) 1_{|t|<=T0}
```

in the same interval normalization as the row. In the exact cyclic projection:

```text
E_t^cyc K_M(t)=m_M(0)=0.
```

Thus `z_M(T0)` measures the failure of the truncated interval kernel to
annihilate constants.

## 4. Assumptions

`NormZeroAudit_237(s0,D0,rho0)` consists of the following rows.

### A. Fixed-row discipline

No convention changes are allowed:

```text
same P_M,
same K_M,
same T0,
same selector class s0,
same centering convention,
same W-normalization,
same dyadic shell D0<|d|<=2D0,
same cyclic and interval cutoff conventions declared in rho0,
fixed w, then N -> infinity, then w -> infinity.
```

Changing any of these creates a mixed transfer row, not a normalization
identity.

### B. Normalization branch

One of the following must be declared.

Exact normalization branch:

```text
NormExact_237:
  Vol_cyc(rho0)=Vol_int(d,rho0)
  for every D0<|d|<=2D0
  in the actual normalization used by both cubes.
```

In this branch:

```text
NormRow_224^P=0.
```

Small normalization-drift branch:

```text
NormDrift_237:
  DeltaVol_237^*(rho0) LambdaAvg_237=o_W(1),
```

where:

```text
DeltaVol_237^*(rho0)
  = sup_{D0<|d|<=2D0} DeltaVol_237(d;rho0).
```

The envelope `LambdaAvg_237` must be proved in the same fixed-row
normalization. It cannot be replaced by the projected endpoint.

### C. Centering consistency

If the row uses uncentered `B_d` and the projection is the exact nonzero
cyclic projection on both sides, no centering row is active.

If centered objects are used, require:

```text
CenterDiff_237
  = (1/D0) sum_{D0<|d|<=2D0}
      |c_d^cyc-c_d^int| Gamma_{d,s0}
  = o_W(1),
```

where `Gamma_{d,s0}` is a declared envelope for inserting one constant slot
and the remaining projected residual slots in the fixed-row cube.

This is a low-dimensional centering row. It is not part of
`BoundaryTupleHL_225`, `BoundaryModelMass_225`, or `WPPBoundary_225`.

### D. Truncated zero-mode leakage

If the interval or kernel truncation no longer annihilates constants exactly,
define:

```text
ZeroBd_226
  = (1/D0) sum_{D0<|d|<=2D0}
      ZLeak_d^237.
```

A sufficient bound is:

```text
ZLeak_d^237
  <= E_d^zero(rho0)
     sum_{j=1}^4 |z_M(T0)|^j A_1(M)^{4-j} |c_d|^j,
```

where:

```text
A_1(M)=E_t |K_M(t)|
```

and `E_d^zero(rho0)` is a declared envelope for the remaining nonconstant
slots after `j` constant insertions. The required row is:

```text
ZeroBd_226=o_W(1).
```

The cleanest sufficient condition is:

```text
z_M(T0)=0
```

in the interval normalization. A weaker condition is:

```text
(1/D0) sum_{D0<|d|<=2D0}
  E_d^zero(rho0)
  sum_{j=1}^4 |z_M(T0)|^j A_1(M)^{4-j} |c_d|^j
  = o_W(1).
```

## 5. Proof / disproof / reduction

### A. Normalization row

By the definition from Module 224:

```text
NormRow_224^P
  = (1/D0) sum_{D0<|d|<=2D0}
      DeltaVol_237(d;rho0) Lambda_{d,s0}.
```

If `NormExact_237` holds, then:

```text
DeltaVol_237(d;rho0)=0
```

for every shift in the fixed shell, and hence:

```text
NormRow_224^P=0.
```

If the drift branch holds, then:

```text
NormRow_224^P
  <= DeltaVol_237^*(rho0) LambdaAvg_237
  = o_W(1).
```

Thus the normalization row is controlled without using an endpoint estimate.

### B. Centering consistency

Write:

```text
B_{d,cyc}^circ
  = B_{d,int}^circ + (c_d^int-c_d^cyc).
```

Expanding a four-slot projected cube, every term containing at least one
copy of:

```text
c_d^int-c_d^cyc
```

is bounded by `CenterDiff_237` after inserting the declared envelope
`Gamma_{d,s0}`. Therefore:

```text
CenterDiff_237=o_W(1)
```

is enough to synchronize the cyclic and interval centering conventions in the
fixed row.

This is not a proof that `c_d` is small. It is only a transfer statement
between two centering conventions.

### C. Zero-mode leakage

In the exact cyclic model:

```text
E_t^cyc K_M(t)=m_M(0)=0,
```

so a constant slot contributes zero after applying `P_M`.

After truncation to:

```text
|t|<=T0,
```

the corresponding interval kernel mass is `z_M(T0)`, which need not vanish.
Expanding:

```text
B_d=B_d^\circ+c_d
```

inside the four projected slots, the terms with at least one constant slot
are bounded by:

```text
sum_{j=1}^4 |z_M(T0)|^j A_1(M)^{4-j} |c_d|^j
```

times the declared envelopes for the remaining nonconstant slots. This is
exactly the sufficient bound in Assumption D. Hence:

```text
ZeroBd_226=o_W(1)
```

under the stated zero-mode leakage budget.

### D. Classification

The normalization row is zero by convention only in the exact normalization
branch. It is local if the volume drift is supported by interval-endpoint or
core-size losses and the envelope `LambdaAvg_237` is local to the fixed row.

The zero-mode row is zero by convention only if constants are annihilated in
the actual interval/truncated projection used by the row, not merely in the
formal cyclic projection.

The row is mixed if it requires:

```text
projection smoothing,
changing the truncation T0,
changing centering conventions,
W-normalization transfer,
selector transfer,
or denominator/grid changes.
```

It is endpoint-strength if `LambdaAvg_237`, `Gamma_{d,s0}`, or
`E_d^zero(rho0)` is supplied by assuming:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1).
```

## 6. Edge cases

- If the cyclic and interval averages are normalized on different cores,
  `NormRow_224^P` is not automatically zero.
- If `Vol_int(d,rho0)` depends on `d` through endpoint loss, the supremum
  `DeltaVol_237^*` must include both positive and negative shifts.
- If the envelope `Lambda_{d,s0}` is taken from the projected residual
  endpoint, the normalization row has become endpoint-strength.
- If `m_M(0)=0` cyclically but `z_M(T0) != 0` after truncation, constants can
  leak into the interval cube.
- If `T0` is changed to force `z_M(T0)=0`, that is a kernel/projection
  transfer change and must be recorded.
- If centered and uncentered conventions are mixed, every term containing
  `c_d^cyc-c_d^int` must be counted.
- If prime-power or W-residue mass contributes to `c_d`, it belongs to the
  appropriate W/prime-power row plus this centering row; it cannot disappear.
- If `A_1(M)` grows, the zero-mode leakage budget must include that growth.
- If the model side and actual side use different normalizations, both need
  their own normalization row or a declared synchronization identity.

## 7. Where it fits in the project map

The Phase F1 fixed-row chain now has:

```text
Module 233
  -> boundary model mass criterion.

Module 234
  -> boundary tuple-HL audit.

Module 235
  -> kernel absolute-tail budget.

Module 236
  -> W-residue and prime-power boundary audit.

Module 237
  -> normalization and zero-mode audit.
```

This completes the first pass over the individual subrows listed in
`LocalBdPkg_226`. The next module can compose the fixed-row subpackages and
identify the first genuine bottleneck.

## 8. What remains open

This module does not prove:

- `NormExact_237`;
- `NormDrift_237`;
- a local bound for `LambdaAvg_237`;
- `CenterDiff_237=o_W(1)`;
- `z_M(T0)=0` or a small zero-mode leakage bound;
- `ZeroBd_226=o_W(1)` unconditionally;
- `NormRow_224^P=o_W(1)` unconditionally;
- `WPPBoundary_225=o_W(1)`;
- `KernelAbsTail_225(P_M,T0)`;
- `BoundaryIntervalHL_234(S,lambda)` for nonempty `S`;
- `BoundaryTupleHL_225(S,lambda)` for nonempty `S`;
- `BoundaryModelMass_225(S,lambda)` beyond Module 233's criterion;
- `LocalBdPkg_226`;
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

- Do not declare `NormRow_224^P=0` unless cyclic and interval normalizations
  are literally the same on the same core.
- Do not treat `m_M(0)=0` in the cyclic model as automatic zero-mode removal
  after interval or kernel truncation.
- Do not hide zero-mode leakage inside boundary, W/prime-power, kernel-tail,
  tuple-HL, or model-mass notation.
- Do not mix centered and uncentered products without a centering row.
- Do not use an endpoint residual fourth-moment estimate as the envelope for
  normalization drift.
- Do not change selector class, projection, truncation, W-normalization, or
  dyadic shell inside this fixed-row audit.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
