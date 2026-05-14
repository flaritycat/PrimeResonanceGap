# Module 236: W-residue and prime-power boundary audit

## 1. Precise theorem / claim being advanced

This module audits the fixed-row side package:

```text
WPPBoundary_225=o_W(1).
```

The fixed row is:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

Define:

```text
WPPBoundaryAudit_236(s0,D0,rho0).
```

Conditional claim:

```text
WPPBoundaryAudit_236(s0,D0,rho0)
  => WPPBoundary_225=o_W(1).
```

The audit separates:

```text
W-residue boundary failures,
prime-power boundary artifacts,
their overlap/accounting convention.
```

The verdict is:

```text
WPPBoundary_225 may be declared zero only under exact fixed-row W-residue and
prime-only conventions. Otherwise it is a genuine side package. It is local
only when all W-residue and prime-power contributions remain supported on the
fixed boundary/tail set after the eight residual vertices are formed.
```

This module does not prove the side package.

## 2. Status label

`CONDITIONAL`

The implication is a deterministic accounting reduction once the named
W-residue, prime-power, and overlap rows are supplied. Those rows remain open.

## 3. Definitions and variables

Use the fixed data from Modules 224-235:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The eight residual vertices are:

```text
v_{00,0}=n-t0,
v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,
v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,
v_{01,1}=n+k+d-t2,
v_{11,0}=n+h+k-t3,
v_{11,1}=n+h+k+d-t3.
```

Let:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

The fixed boundary and tail indicators are:

```text
Bd_lambda(d,n,h,k;t)
  = 1_{v_lambda notin I_N^core(L_N)},

TailT_224(t)=1_{max_i |t_i|>T0}.
```

Set:

```text
BdTail_236(d,n,h,k;t)
  = 1_{ TailT_224(t)=1
         or Bd_lambda(d,n,h,k;t)=1 for some lambda in Lambda_8 }.
```

Thus:

```text
BdTail_236
```

is exactly the boundary/tail support relevant to `WPPBoundary_225`.

For W-residue compatibility, let:

```text
WFail_lambda(d,n,h,k;t)
```

be the indicator that the represented integer attached to `v_lambda` fails
the fixed admissible W-residue convention of the row. In a single-residue
notation this means that the represented integer is not of the form:

```text
W v_lambda + b
```

with the declared admissible residue `(b,W)=1`, after all shifts, cutoffs, and
kernel moves used by `rho0`. In a finite residue-family convention it means
failure of the declared admissible residue tuple at some prime `p<=w`.

Define:

```text
WFail_236
  = 1_{ WFail_lambda=1 for some lambda in Lambda_8 }.
```

For prime powers, write:

```text
nu_s0=nu_s0^pr + pp_s0
```

when the class contains a von-Mangoldt-type prime-power remainder, and set:

```text
pp_s0=0
```

by convention in a prime-only or purely model class. Let:

```text
PPFail_lambda(d,n,h,k;t)
```

be the indicator that the represented integer at `v_lambda` belongs to the
support of `pp_s0`, and:

```text
PPFail_236
  = 1_{ PPFail_lambda=1 for some lambda in Lambda_8 }.
```

## 4. Assumptions

`WPPBoundaryAudit_236(s0,D0,rho0)` consists of the following rows.

### A. Fixed-row discipline

No convention changes are allowed inside the audit:

```text
same P_M,
same K_M,
same selector class s0,
same W-residue convention,
same prime-only or prime-power convention,
same interval cutoff convention,
same dyadic shell D0<|d|<=2D0,
fixed w, then N -> infinity, then w -> infinity.
```

Changing from actual W-tricked von-Mangoldt weights to prime-only weights is a
prime-power transfer row, not a harmless relabeling. Changing the W-residue
family is a W-residue transfer row.

### B. W-residue boundary row

Define the W-residue boundary contribution:

```text
WResBoundary_236
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)|
        BdTail_236(d,n,h,k;t)
        WFail_236(d,n,h,k;t).
```

The required row is:

```text
WResBoundary_236=o_W(1).
```

This row is declared identically zero only if the fixed W-trick convention
guarantees:

```text
WFail_236=0
```

on the whole fixed row, including boundary, cutoff, and kernel-shifted
vertices.

### C. Prime-power boundary row

Let:

```text
ProductB_d^{>=1 pp}(n,h,k;t)
```

denote the full expansion of the projected residual product in which at
least one of the eight underlying `f_s0` vertices is replaced by `pp_s0`.

Define:

```text
PPBoundary_236
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)|
        |ProductB_d^{>=1 pp}(n,h,k;t)|
        BdTail_236(d,n,h,k;t).
```

The required row is:

```text
PPBoundary_236=o_W(1).
```

This row is identically zero only if:

```text
pp_s0=0
```

in the fixed selector/model class.

### D. Overlap and accounting convention

W-residue failures and prime-power artifacts can occur on the same summand.
The audit requires either:

```text
DisjointAccount_236:
  each summand is assigned to exactly one of WResBoundary_236
  or PPBoundary_236,
```

or an explicit overlap row:

```text
WPPOverlap_236
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)|
        BdTail_236 WFail_236 PPFail_236
  = o_W(1).
```

The overlap row is optional only when the disjoint accounting convention is
declared before the estimate is used.

### E. Positive tuple routes

Using `AbsMajorant_225(s0)`, the rows above may be proved by positive tuple
envelopes. For W-residue failures, a sufficient family is:

```text
WResTuple_236(S)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| BdTail_236 WFail_236
        prod_{sigma in S} mu_s0(v_sigma)
  = o_W(1)
```

for every:

```text
S subset Lambda_8.
```

For prime powers, a sufficient family is:

```text
PPTupleBoundary_236(S,tau)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| BdTail_236 PPFail_tau
        prod_{sigma in S} mu_s0(v_sigma)
  = o_W(1)
```

for every:

```text
S subset Lambda_8,
tau in Lambda_8.
```

Here `PPFail_tau` marks which vertex supplies the prime-power factor. These
tuple rows are stronger than first-moment sparsity; they are in the same
boundary/tail normalization as the fixed row.

## 5. Proof / disproof / reduction

By Module 225, `WPPBoundary_225` is the contribution from small-prime
W-residue failures and prime-power artifacts whose support intersects:

```text
Bd_lambda
```

or:

```text
TailT_224.
```

That support is exactly `BdTail_236`.

Every such summand has at least one of:

```text
WFail_236=1,
PPFail_236=1.
```

Therefore, with disjoint accounting:

```text
WPPBoundary_225
  <= WResBoundary_236 + PPBoundary_236.
```

Without disjoint accounting one may use:

```text
WPPBoundary_225
  <= WResBoundary_236 + PPBoundary_236 + WPPOverlap_236,
```

where the overlap term prevents the proof ledger from silently assigning the
same bad summand to two different packages.

If:

```text
WResBoundary_236=o_W(1),
PPBoundary_236=o_W(1),
```

and either:

```text
DisjointAccount_236
```

or:

```text
WPPOverlap_236=o_W(1),
```

then:

```text
WPPBoundary_225=o_W(1).
```

### Positive tuple domination

For W-residue failures, `AbsMajorant_225(s0)` gives:

```text
|ProductB_d|
  <= C_s0^8
     sum_{S subset Lambda_8}
       prod_{sigma in S} mu_s0(v_sigma).
```

Thus:

```text
WResBoundary_236
  <= C_s0^8
     sum_{S subset Lambda_8} WResTuple_236(S).
```

For prime powers, expand:

```text
f_s0=f_s0^pr+pp_s0.
```

The terms with at least one `pp_s0` vertex are dominated by:

```text
C_s0^8
sum_{tau in Lambda_8}
sum_{S subset Lambda_8}
  1_{PPFail_tau}
  prod_{sigma in S} mu_s0(v_sigma),
```

with harmless changes in constants depending on the chosen nonnegative
majorant for `pp_s0`. Therefore:

```text
PPBoundary_236
  <= C_s0^8
     sum_{tau in Lambda_8}
     sum_{S subset Lambda_8}
       PPTupleBoundary_236(S,tau).
```

Hence the positive tuple route implies the W-residue and prime-power boundary
rows. It does not prove those tuple rows.

### Classification

The row is zero by convention when:

```text
WFail_236=0
and
pp_s0=0
```

on the entire fixed row.

It is local when the only nonzero bad summands are boundary/tail-supported
and are controlled by the positive tuple rows above.

It is mixed when the proof needs:

```text
changing W-residue families,
prime-only to von-Mangoldt transfer,
projection smoothing,
kernel-tail transfer,
or large-range CRT bookkeeping.
```

It is endpoint-strength if `WResBoundary_236` or `PPBoundary_236` is proved
by assuming:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
```

or the corresponding projected fourth-moment estimate for:

```text
Delta B_d=B_d-B_d^pr.
```

## 6. Edge cases

- W-residue failures at primes `p<=w` are not part of
  `Theta_{w,S}^proj`; that product only runs over `p>w`.
- If all shifted vertices remain in the declared W-residue classes,
  `WResBoundary_236` is zero. This must be checked after kernel shifts and
  cutoffs, not only for the unshifted core.
- If `pp_s0=0`, the prime-power row is zero by convention. If not, it must be
  estimated in projected fourth-moment or boundary tuple normalization.
- A first-moment estimate for prime powers does not control products with the
  other seven residual vertices.
- A prime-power vertex can also be a W-residue failure near a boundary; the
  overlap must be assigned or estimated.
- If `T0` is large, kernel shifts can create new residue or range failures.
- If smoothing changes the projection, the error belongs to projection
  transfer as well as W/prime-power accounting.
- If centering is used, prime-power or W-residue mass in `c_d` must be routed
  to `NormRow_224^P` or a zero-mode leakage row.
- Negative shifts are included in the same shell and may move vertices across
  residue-compatible cutoffs.

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
  -> WPPBoundary_225 split into W-residue, prime-power, and overlap rows.
```

This module imports the discipline of Module 211 into the smaller fixed
boundary row from Modules 224-226. It keeps W-residue and prime-power errors
outside `Theta_{w,S}^proj`, outside kernel-tail notation, and outside the
model-mass and tuple-HL rows.

## 8. What remains open

This module does not prove:

- `WResBoundary_236=o_W(1)`;
- `PPBoundary_236=o_W(1)`;
- `WPPOverlap_236=o_W(1)` when no disjoint accounting is declared;
- any `WResTuple_236(S)`;
- any `PPTupleBoundary_236(S,tau)`;
- `WPPBoundary_225=o_W(1)` unconditionally;
- `KernelAbsTail_225(P_M,T0)`;
- `BoundaryIntervalHL_234(S,lambda)` for nonempty `S`;
- `BoundaryTupleHL_225(S,lambda)` for nonempty `S`;
- `BoundaryModelMass_225(S,lambda)` beyond Module 233's criterion;
- `NormRow_224^P`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
- `PPSPTransfer_3^major(P_adm)`;
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

- Do not put primes `p<=w` into `Theta_{w,S}^proj`; W-residue failures are
  separate errors.
- Do not hide prime-power artifacts inside `Omega_w^proj` unless an explicit
  prime-power model and matching theorem are supplied.
- Do not treat first-moment prime-power sparsity as projected fourth-moment
  boundary control.
- Do not hide W-residue or prime-power errors inside kernel tails, tuple HL,
  model mass, or normalization.
- Do not double count overlap between W-residue and prime-power failures
  without a stated accounting convention.
- Do not change selector class, projection, W-residue family, or dyadic shell
  inside this fixed-row audit.
- Do not prove `WPPBoundary_225` by assuming the projected residual endpoint.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
