# Module 240: LocalBdPkg practical verdict after fixed-row tests

## 1. Precise theorem / claim being advanced

This module reviews the fixed-row tests from Modules 233-239 and gives a
practical route verdict for:

```text
LocalBdPkg_226(s0,D0,rho0).
```

The fixed row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

The verdict is:

```text
LocalBdPkg_226 remains a formally plausible local route
only when expanded into its fixed-support subrows.
```

Define:

```text
LocalBdPkgPracticalVerdict_240(s0,D0,rho0)
```

to be the classification and route decision recorded in this module.

For practical future use it must not be cited as a compact solved side
package. Its active unsolved core is:

```text
FixedSupportTupleHL_238,
```

headed by the nonempty boundary interval rows:

```text
BoundaryIntervalHL_234(S,lambda),  S nonempty,
```

and accompanied by the corresponding fixed-support tail, W-residue, and
prime-power tuple rows:

```text
TailTuple_235(S),
WResTuple_236(S),
PPTupleBoundary_236(S,tau).
```

The module records the following practical classification:

```text
emptyset/model/convention rows:
  conditionally local and partially closed by Module 239;

nonempty fixed-support weighted tuple rows:
  plausible local only if proved on the declared boundary/tail/support sets
  with the exact projected local factors;

rows requiring extra selector, projection, W-residue-family, prime-power,
  denominator, or range transfer:
  mixed;

rows proved by assuming the unlocalized projected residual fourth moment:
  endpoint-strength and therefore not evidence for LocalBdPkg_226.
```

This is a route verdict. It does not prove `LocalBdPkg_226`,
`BdPrefRow_224^P`, or any endpoint object.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module extracts a corrected proof-map classification from Modules
233-239. It does not add a new analytic estimate.

## 3. Definitions and variables

Use the fixed data:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The residual derivative objects are:

```text
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

The fixed product is:

```text
ProductB_d(n,h,k;t)
  = B_d(x00) conj(B_d(x10)) conj(B_d(x01)) B_d(x11).
```

The eight residual vertices are indexed by:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

Write:

```text
v_sigma=n+a_sigma(d,h,k;t),  sigma in Lambda_8.
```

For a boundary label `lambda`, the boundary event is:

```text
Bd_lambda(d,n,h,k;t)
  = 1_{v_lambda notin I_N^core(L_N)}.
```

The kernel-tail event is:

```text
TailT_224(t)=1_{max_i |t_i|>T0}.
```

The combined fixed support is:

```text
BdTail_236
  = 1_{TailT_224=1 or Bd_lambda=1 for some lambda in Lambda_8}.
```

The exact projected local factor for a labeled subset is:

```text
Theta_{w,S}^proj(d,h,k;t).
```

It is not replaced here by a collision-free generic factor, by the full
eight-form factor, by `Omega_w^proj`, or by rectangle shortcuts. Rectangle
faces still use the exact rectangle model, and `Sigma_w(d,h)` is not
pointwise `kappa_w(d)^2`.

## 4. Assumptions

This module assumes the statements and classifications already recorded in
Modules 224-239. No new analytic estimate is assumed.

The route under review is the Module 226 implication:

```text
LocalBdPkg_226(s0,D0,rho0)
  => BdPrefRow_224^P(s0,D0;N,w,rho0)=o_W(1).
```

The subrow decomposition from Modules 233-238 is:

```text
BoundaryModelVolume_233(S,lambda)
  -> BoundaryModelMass_225(S,lambda),

BoundaryIntervalHL_234(S,lambda)
  -> BoundaryTupleHL_225(S,lambda) for S nonempty,

S=emptyset
  -> BoundaryTupleHL_225(emptyset,lambda) exactly,

KernelTailBudget_235(P_M,T0;s0,D0,rho0)
  -> KernelAbsTail_225(P_M,T0),

WPPBoundaryAudit_236(s0,D0,rho0)
  -> WPPBoundary_225,

NormZeroAudit_237(s0,D0,rho0)
  -> NormRow_224^P and active ZeroBd_226.
```

The easiest subrow from Module 239 is:

```text
EasyModelPkg_239(lambda)
  => EasyModelSubrow_239(lambda).
```

The missing nonempty core remains:

```text
FixedSupportTupleHL_238.
```

## 5. Proof / disproof / reduction

### A. What survived the fixed-row tests

Modules 233-239 show that the fixed boundary row has one genuinely smaller
piece:

```text
S=emptyset,
Theta_{w,emptyset}^proj=1,
prod_{sigma in emptyset} mu_s0(v_sigma)=1.
```

In that case:

```text
BTuple_225(emptyset,lambda)
  = BdModel_225(emptyset,lambda)
```

with zero tuple error, and Module 239 reduces the remaining empty subrow to
explicit kernel-volume and convention hypotheses:

```text
A_W(M) delta_vol_233(lambda;N,rho0)=o_W(1),
Tail_W(T0)=o_W(1),
pure or small W-residue / prime-power / normalization / zero-mode rows.
```

Thus the empty/model/convention part of `LocalBdPkg_226` remains a genuine
local subroute. It is useful as a sanity check and as a proof-map anchor.

### B. What did not survive as routine locality

For `S nonempty`, the actual tuple row is:

```text
E_n Bd_lambda(d,n,h,k;t)
  prod_{sigma in S} mu_s0(v_sigma).
```

The empty-product identity no longer applies. Boundary volume controls only:

```text
BdVol_lambda(d,h,k;t).
```

It does not control concentration of prime-type weights on the boundary
intervals. Therefore the nonempty tuple rows require:

```text
BoundaryIntervalHL_234(S,lambda),
```

with W-admissible error after multiplication by `|W_M(t)|`, exact labeled
local factors, fixed selector class, and the same dyadic shell.

The same diagnosis applies to:

```text
TailTuple_235(S),
WResTuple_236(S),
PPTupleBoundary_236(S,tau),
```

whenever `S nonempty`. These are not consequences of the empty row, model
mass, first-moment boundary volume, ordinary pair-BDH, or full-interval
first-moment Hardy-Littlewood.

### C. Corrected practical reading of Module 226

Module 226 was not false, but after the fixed-row tests its phrase:

```text
conditional local boundary row under LocalBdPkg_226
```

must be read in the expanded sense:

```text
LocalBdPkg_226
  = EmptyModelConvention_240
    + FixedSupportTupleHL_238
    + TailSupportTuple_240
    + WPPFixedSupport_240
    + NormZeroFixed_240
    + exact fixed-row discipline.
```

Here:

```text
EmptyModelConvention_240
  is the Module 239 closed/easiest subrow;

TailSupportTuple_240
  is the nonempty tail tuple family from Module 235;

WPPFixedSupport_240
  is the W-residue / prime-power tuple family from Module 236;

NormZeroFixed_240
  is the Module 237 normalization and zero-mode package.
```

This correction is mostly about future citation discipline. A future module
may cite `LocalBdPkg_226` only if it also states which of these rows is being
used. Otherwise the notation is too coarse and risks hiding the main
analytic obstruction.

### D. Practical route verdict

The route remains worth keeping only in the following narrow form:

```text
Prove one fixed-support weighted tuple theorem
for one nonempty S and one boundary label lambda,
with exact Theta_{w,S}^proj and the fixed row rho0.
```

The smallest honest next analytic target after the plan update is therefore
not the full endpoint, and not the whole `LocalBdPkg_226`. It is a prototype
nonempty fixed-support row such as:

```text
BoundaryIntervalHL_234({sigma},lambda)
```

or a similarly small nonempty tail/W-residue/prime-power tuple row, provided
all support, W-residue, range, and local-factor errors are included in the
same row.

If even the one-point nonempty boundary interval row requires the projected
major residual fourth moment:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
```

then the local boundary route should be marked endpoint-strength for
practical purposes and the project should stop treating it as a smaller side
package.

### E. Why familiar shortcuts remain blocked

The following shortcuts do not supply the missing nonempty fixed-support
tuple control:

```text
BoundaryModelVolume_233(S,lambda),
first-moment boundary volume,
first-moment full-interval Hardy-Littlewood,
ordinary pair-BDH,
Tail_W(T0)=o_W(1),
cyclic m_M(0)=0,
prime-power first-moment sparsity.
```

Each controls either the wrong support, the wrong moment, the wrong model, or
the wrong normalization. None is the boundary/tail-supported, W-admissible,
exact-local-model weighted tuple theorem required by Modules 234-238.

### F. Decision

The practical decision is:

```text
Continue carrying LocalBdPkg_226 as CONDITIONAL only when expanded.
Do not spend more iterations renaming its subrows.
After the sixth plan update, either attempt a one-row nonempty
FixedSupportTupleHL prototype or mark that prototype blocked.
```

This is a narrowing decision, not a proof.

## 6. Edge cases

- The `S=emptyset` proof from Module 239 is real but too small to represent
  nonempty actual weighted tuple rows.
- If `A_W(M)` grows, even boundary-volume model rows require stronger
  volume or local-factor saving.
- If `Theta_{w,S}^proj` is large on a collision stratum, the row must include
  a localized bad-factor estimate; generic collision-free factors are not
  acceptable.
- If the boundary intervals are too short for the required W-uniform tuple
  theorem, the route may fail at `RangeBdTuple_234`.
- If `Tail_W(T0)=o_W(1)` holds but the residual product is unbounded,
  `TailCube_225(T0)` is still open.
- If W-residue or prime-power artifacts are not supported on `BdTail_236`,
  the row is mixed with a transfer problem outside the fixed boundary route.
- If `NormRow_224^P` is declared zero without literal equality of the cyclic
  and interval normalizations, Module 237 has been bypassed.
- If `m_M(0)=0` is used after interval truncation without checking
  `z_M(T0)`, zero-mode leakage may survive.
- If selector class, projection, denominator grid, W-residue convention, or
  dyadic shell changes, the result is not the fixed row under review.
- If the nonempty tuple theorem is proved from the projected endpoint, the
  row is endpoint-strength, not a local side package.

## 7. Where it fits in the project map

The Phase F1 chain is now:

```text
Modules 224-226
  -> fixed boundary row and initial LocalBdPkg verdict.

Modules 233-237
  -> subrow audits: model mass, tuple HL, kernel tail, W/prime-power,
     normalization / zero-mode.

Module 238
  -> composition and first bottleneck:
     FixedSupportTupleHL_238.

Module 239
  -> easiest S=emptyset subrow closed conditionally; extension blocked.

Module 240
  -> practical verdict:
     LocalBdPkg_226 remains usable only as an expanded conditional package,
     with nonempty fixed-support weighted tuple control as the active
     bottleneck.
```

The next scheduled item is the sixth plan update. That update should decide
whether the next analytic attempt is a one-point nonempty boundary interval
prototype or whether Phase F1 should stop.

## 8. What remains open

This module does not prove:

- `LocalBdPkg_226`;
- `FixedRowPkg_238`;
- `FixedSupportTupleHL_238`;
- any nonempty `BoundaryIntervalHL_234(S,lambda)`;
- any nonempty `TailTuple_235(S)`;
- any nonempty `WResTuple_236(S)`;
- any nonempty `PPTupleBoundary_236(S,tau)`;
- the bad-factor rows in `BoundaryModelVolume_233(S,lambda)`;
- `KernelAbsTail_225(P_M,T0)` unconditionally;
- `WPPBoundary_225` unconditionally;
- `NormRow_224^P` unconditionally;
- `ZeroBd_226` unconditionally;
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

- Do not cite `LocalBdPkg_226` without expanding the active rows.
- Do not treat the `S=emptyset` subrow as evidence for nonempty weighted
  tuple rows.
- Do not replace `BoundaryIntervalHL_234(S,lambda)` by boundary volume,
  first-moment HL, ordinary pair-BDH, or model mass.
- Do not use `Tail_W(T0)=o_W(1)` as a substitute for nonempty
  `TailTuple_235(S)` or `TailCube_225(T0)`.
- Do not hide W-residue, prime-power, range, normalization, or zero-mode
  terms in `Theta_{w,S}^proj`.
- Do not replace rectangle local factors by `kappa_w(d)^2`; `Sigma_w`
  remains the exact rectangle model.
- Do not change selector class, projection, denominator grid, W-residue
  convention, or dyadic shell inside the fixed-row verdict.
- Do not prove a fixed-support tuple row by assuming
  `ProjectedMajorTarget_3^B`, `ResCube_3^sharp`, or the projected residual
  endpoint.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
