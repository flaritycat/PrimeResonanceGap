# Module 266: W-limit, denominator, projection, and dyadic uniformity over `P_adm`

## 1. Precise theorem / claim being advanced

This module performs the fourth proof-or-blocked test required by
`PlanChallenge_5_262`: audit whether the Phase H model-neutrality rows are
uniform over the same admissible family.

Define:

```text
UniformityLedger_266(P_adm).
```

The conditional claim is:

```text
UniformityLedger_266(P_adm)
  + rowwise estimates for the chosen Phase H fork
  => those rowwise estimates are valid as o_W(1) over P_adm.
```

Here the two possible forks are:

```text
absolute fork:
  KernelAbsBudget_265(P_adm)
  + AbsCollStrataGate_264(P_adm),

signed fork:
  KernelSignedBudget_265(P_adm)
  + SignedCoverGate_264(P_adm).
```

This module does not prove either fork. It only states the uniformity contract
that any proof of the fork must satisfy before it can be inserted into
`ProjectedModelNeutralityGate_260(P_adm)`.

## 2. Status label

`CONDITIONAL`

The module gives conditional bookkeeping implications. It establishes no analytic
estimate and does not close projected model neutrality.

## 3. Definitions and variables

Use:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
D<|d|<=2D,
w fixed, N -> infinity, then w -> infinity.
```

For any error term `Err(N,w;rho)`, write:

```text
Err=o_W(1) over P_adm
```

to mean:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} |Err(N,w;rho)|=0.
```

Equivalently:

```text
for every eps>0,
there exists w0,
for every w>=w0,
there exists N0(w),
for every N>=N0(w) and every rho in P_adm(N,w),
|Err(N,w;rho)| <= eps.
```

The projected major-arc multiplier is:

```text
widehat{P_M F}(xi)=m_M(xi)widehat{F}(xi),
m_M(0)=0.
```

The kernel and four-slot weight are:

```text
K_M(t)=sum_xi m_M(xi)e(xi t),
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The model-neutrality object remains:

```text
NeutralErr_major^P(N,w;rho)
  = |(1/D) sum_{D<|d|<=2D}
       E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t)|.
```

No row in this module may change:

```text
Omega_w^proj,
P_M,
W_M,
D<|d|<=2D,
selector class,
cutoff convention,
W-residue convention,
limit order.
```

without an explicitly named transfer row.

## 4. The uniformity ledger

Define:

```text
UniformityLedger_266(P_adm)
```

as the conjunction of the rows below.

### A. W-order row

Define:

```text
WOrder_266(P_adm).
```

This row requires that every estimate used in Phase H is established with:

```text
w fixed first,
N -> infinity uniformly over rho in P_adm(N,w),
then w -> infinity.
```

It also requires:

```text
W=prod_{p<=w} p
```

to remain inside the project W-trick range for the fixed-w estimates.

A diagonal choice:

```text
w=w(N)
```

is allowed only after the two-stage estimate has been established and only if all
residue, interval, denominator, and CRT restrictions remain valid. It cannot
be used to create the estimate.

### B. Generic-tail constants

Define:

```text
GenTailUniform_266(P_adm).
```

For the generic terms:

```text
G_2(w)=sum_{p>w}1/p^2,
Omega_w^gen=O(G_2(w)),
```

all constants multiplying `G_2(w)` must be independent of:

```text
N,D,R,eta,H,K,T,P_M,cutoff,selector.
```

after the admissible family is fixed. If a constant grows with a kernel norm,
range envelope, denominator count, or cutoff complexity, it must be included
explicitly, for example:

```text
A_W(M)G_2(w)=o_W(1),
K_q(M)G_2(w)=o_W(1),
or C_range(N,w;rho)G_2(w)=o_W(1) over P_adm.
```

No term of size:

```text
sum_{w<p<=B} 1/p
```

may be called a generic W-tail.

### C. Denominator and CRT range row

Define:

```text
DenCRTUniform_266(P_adm).
```

The major-arc denominator data must satisfy a uniform package:

```text
1 <= q <= R(N,w),
xi near a/q within eta(N,w),
(a,q)=1,
xi != 0.
```

If a buffered or smoothed partition is used, the overlap constants and buffer
losses must be uniform over `rho`.

For collision and overflow rows, the CRT products created by finite prime
sets must fit the averaging ranges. With:

```text
Q(P)=prod_{p in P} p,
```

the range error in estimates of the form:

```text
E prod_{p in P} 1_{p|L_{phi(p)}} <= C/Q(P) + RangeErr(P,phi;N,w,rho)
```

must satisfy the exponential summability condition uniformly:

```text
sup_{rho in P_adm(N,w)}
sum_P weight(P)
  sum_phi RangeErr(P,phi;N,w,rho)
  = o_W(1).
```

Single-prime estimates do not imply this row. The exponential overflow row
requires finite-prime-set control.

### D. Projection-boundary row

Define:

```text
ProjBoundaryUniform_266(P_adm).
```

The multiplier used in the proof must be the multiplier in the target row:

```text
m_M,
supp(m_M) subset Major(R,eta_+)\{0},
m_M(0)=0.
```

If the proof uses a smoothed projection while the target is sharp, the
projection discrepancy must be paid by:

```text
ProjBd_major(N,w;rho)=o_W(1) over P_adm.
```

If the proof changes `R`, `eta`, the buffer, the multiplier normalization, or
the zero-mode convention, the result is mixed until a projection-transfer row
returns it to the original target.

### E. Kernel truncation and tail row

Define:

```text
KernelTruncUniform_266(P_adm).
```

Every use of a truncation scale `T` must keep:

```text
same K_M,
same W_M,
same T convention on the actual and model sides.
```

The absolute fork requires:

```text
TailExp_265(lambda,T)=o_W(1)
```

uniformly over `rho`, including any residual product, collision load, and
range envelope appearing on the tail. The signed fork requires the analogous
signed tail row in the exact same signed average.

Controlling:

```text
Tail_W(T)=E|W_M|1_{max_i |t_i|>T}
```

alone is not enough if the residual product or collision load can grow on the
tail.

### F. Cutoff, cyclic/interval, and boundary row

Define:

```text
CutBoundaryUniform_266(P_adm).
```

If a proof is cyclic, but the target is interval, the transfer must include:

```text
ActBd_major,
ModelBd_major,
WrapBd_major,
TailBd_major,
CutoffBd_major,
NormBd_major,
ZeroLeak_major.
```

Each must be `o_W(1)` over `P_adm`.

The same cutoff convention must be used in:

```text
ActualProjCube_d^P,
ModelProjCube_d^P,
NeutralErr_major^P,
CollSigned_263,
AbsCollStrataGate_264,
KernelBudgetAudit_265.
```

Changing the cutoff after proving a row is a transfer step, not a local proof.

### G. W-residue and prime-power row

Define:

```text
WPPUniform_266(P_adm).
```

The W-residue convention must be fixed before `N -> infinity`. Primes
`p<=w` are not part of the Euler product:

```text
Theta_{w,S}^proj = prod_{p>w} ...
```

Any small-prime incompatibility belongs to:

```text
WResBd_major(N,w;rho).
```

Prime-power artifacts must be controlled in the projected fourth-moment or
projected cube norm:

```text
PPCubeErr_major(N,w;rho)=o_W(1)
```

or by a stronger W-admissible projected norm/envelope row. First-moment
negligibility of prime powers is not enough.

### H. Dyadic and sign-uniform row

Define:

```text
DyadicUniform_266(P_adm).
```

All estimates must be uniform over:

```text
D in D_range(N,Hcal),
D<|d|<=2D,
d>0 and d<0 unless a signed restriction is shown harmless,
H and K averaging-window ranges,
dyadic edge and endpoint losses.
```

The form `d=0` is absent in the dyadic shell, but congruence events:

```text
p|d, p>w
```

remain part of the collision load. They cannot be dropped by citing the
structural exclusion of `d=0`.

If `H` or `K` is too short, structural diagonal counting and CRT range
estimates may fail. The family `P_adm` must either exclude those ranges or
name their error rows.

### I. Selector-class row

Define:

```text
SelectorUniform_266(P_adm).
```

Every row must declare one selector class:

```text
model, W-tricked prime-only, smoothed, frozen, sharp-moving,
or another explicitly defined class.
```

A theorem in one selector class stays in that class. To move to the actual
sharp moving selector, the proof must supply:

```text
MajorSelectorTransfer_3^P
```

or the corresponding adjacent selector-transfer rows. A model-neutrality
statement in a model selector does not automatically become a moving-selector
statement.

### J. Supremum closure row

Define:

```text
SupClosure_266(P_adm).
```

If a row is established only for a smaller subfamily:

```text
rho in P_good(N,w) subset P_adm(N,w),
```

then it can be used over `P_adm` only after proving:

```text
BadFamErr_266(N,w)
  = sup_{rho in P_adm(N,w)\P_good(N,w)} RowContribution(N,w;rho)
  = o_W(1).
```

Otherwise the row is a restricted theorem, not the Phase H row.

## 5. Conditional assembly

Assume the chosen fork has rowwise estimates for a fixed admissible family,
and assume `UniformityLedger_266(P_adm)`.

For the absolute fork, the rows:

```text
A_W(M)eps_gen(w)=o_W(1),
StructAbs_264=o_W(1),
E_abs B_w^red 1_G=o_W(1),
E_abs exp(C B_w^red)B_w^red 1_{B_w^red>1}1_G=o_W(1),
TailExp_265=o_W(1),
RangeExp_265=o_W(1)
```

are then valid in the required sense:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} |...|=0.
```

For the signed fork, the rows:

```text
GenSigned_265=o_W(1),
StructSigned_264=o_W(1),
proper-support signed compatibility,
full-cover signed cluster estimate,
signed tail and signed range rows
```

are valid only for the same signed `W_M` average and only in the declared
selector/projection/cutoff family.

Thus `UniformityLedger_266` is a transport ledger for estimates already
established inside a fork. It does not create the analytic estimates.

## 6. Classification of failures

If every row in the chosen fork satisfies `UniformityLedger_266`, the row is:

```text
local/model-side
```

for the declared model and selector class.

If the proof changes projection smoothing, denominator range, cutoff,
interval/cyclic model, W-residue convention, or selector class and then
returns through a named transfer row, the row is:

```text
mixed
```

until the transfer row is supplied.

If uniformity is supplied by assuming:

```text
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
or AU^3,
```

then the row is:

```text
endpoint-strength
```

and cannot be used as a proof of Phase H.

If the proof asserts uniformity from pointwise-in-`rho` estimates with
constants depending on `rho`, or from a diagonal `w=w(N)` estimate without the
two-stage W-limit, the row is:

```text
false / blocked as a shortcut.
```

## 7. Verdict for Phase H

Module 266 leaves Phase H in a narrowed but honest state:

```text
absolute fork:
  still open, because its kernel, collision-load, overflow, range, boundary,
  and dyadic constants must be uniform over P_adm;

signed fork:
  still open, because its cancellations must be in the exact signed family
  and cannot be transferred to absolute rows.
```

The next module should give a proof-or-blocked verdict for:

```text
ProjectedModelNeutralityGate_260(P_adm).
```

That verdict should decide whether the Phase H route is:

```text
conditional local/model-side,
mixed,
endpoint-strength,
or false / blocked as a shortcut.
```

## 8. Edge cases

- Fixed `w` estimates with constants depending on `w` are acceptable only if
  the final `w -> infinity` step is still controlled.
- A diagonal `w=w(N)` estimate is not a replacement for the project W-limit
  order.
- Smoothed projection estimates are not sharp projection estimates without
  `ProjBd_major`.
- Cyclic zero-mode identities may fail after interval cutoff or kernel
  truncation.
- Denominator estimates for single moduli do not imply exponential
  finite-prime-set CRT control.
- Short `H` or `K` ranges can destroy structural and diagonal savings.
- Removing bad `rho` values from `P_adm` changes the theorem unless their
  contribution is paid by `BadFamErr_266`.
- Signed kernel estimates cannot be inserted into `E_abs` or boundary rows.
- W-residue and prime-power errors are outside `Omega_w^proj`.

## 9. Where it fits in the project map

The Phase H chain is now:

```text
Module 260:
  ProjectedModelNeutralityGate_260(P_adm).

Module 263:
  SignedSubsetExpansion_263(P_adm).

Module 264:
  CollStrataAudit_264(P_adm).

Module 265:
  KernelBudgetAudit_265(P_adm).

Module 266:
  UniformityLedger_266(P_adm).
```

The next module should be:

```text
Module 267:
  proof-or-blocked verdict for ProjectedModelNeutralityGate_260(P_adm).
```

## 10. What remains open

This module does not prove:

- `UniformityLedger_266(P_adm)` for any analytic fork;
- `WOrder_266`;
- `GenTailUniform_266`;
- `DenCRTUniform_266`;
- `ProjBoundaryUniform_266`;
- `KernelTruncUniform_266`;
- `CutBoundaryUniform_266`;
- `WPPUniform_266`;
- `DyadicUniform_266`;
- `SelectorUniform_266`;
- `SupClosure_266`;
- `KernelAbsBudget_265(P_adm)`;
- `KernelSignedBudget_265(P_adm)`;
- `AbsCollStrataGate_264(P_adm)`;
- `SignedCoverGate_264(P_adm)`;
- `CollNeutral_260`;
- `CollSigned_263=o_W(1)`;
- `NeutralErr_major^P=o_W(1)`;
- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not replace the two-stage W-limit by a diagonal `w=w(N)` proof.
- Do not hide constants depending on `rho` inside `o_W(1)`.
- Do not treat first-order `sum 1/p` terms as generic W-tails.
- Do not use single-prime CRT estimates as exponential overflow control.
- Do not change projection, denominator range, cutoff, selector, W-residue
  convention, or dyadic shell without a named transfer row.
- Do not use cyclic identities as interval estimates without boundary and
  zero-mode rows.
- Do not move signed estimates into absolute rows.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
