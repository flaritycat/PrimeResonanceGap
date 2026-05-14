# Module 243: Exact one-point local model and boundary main term

## 1. Precise theorem / claim being advanced

This module derives the exact local model and boundary interval main term for
the active prototype fixed in Module 242:

```text
OnePointBIHL_242(s0,D0,rho0)
  = BoundaryIntervalHL_234({(00,0)},(00,0)).
```

The fixed row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

The local-model claim is:

```text
Theta_{w,{(00,0)}}^proj(d,h,k;t)=1
```

in the normalized W-tail singleton model, because the active affine form is
one primitive linear form:

```text
L_0(n)=n-t0.
```

Therefore the model main term in Module 242 is:

```text
M_r^mod(d,h,k;t)=ell_r(d,h,k;t)
```

for:

```text
r in {L,R}.
```

Equivalently, the one-point prototype is the boundary prime-mean row:

```text
E_n 1_{J_r}(n) mu_s0(n-t0)
  =
ell_r(d,h,k;t)
  + Err_r^243(d,h,k;t),
```

with the W-admissible target:

```text
BIHLErr_243
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_{r in {L,R}} |Err_r^243(d,h,k;t)|
  = o_W(1),
```

plus the side-error slots:

```text
CutOne_242,
RangeOne_242,
WResOne_242,
PPOne_242,
NormZeroOne_242.
```

This module proves only the local factor simplification and main-term
identification. It does not prove `BIHLErr_243=o_W(1)`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The singleton Euler-factor calculation is structural. The boundary prime-mean
estimate remains open.

## 3. Definitions and variables

Use the fixed data:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active labels are:

```text
lambda0=sigma0=(00,0),
S1={(00,0)}.
```

The active affine form is:

```text
L_0(n;t)=n-t0.
```

The active boundary event is:

```text
Bd_lambda0(d,n,h,k;t)
  = 1_{n-t0 notin I_N^core(L_N)}.
```

The two boundary intervals are:

```text
J_L(d,h,k;t)={n: n-t0 <= L_N},
J_R(d,h,k;t)={n: n-t0 > N-L_N},
```

intersected with the row's interval averaging domain and `cutoff0`.

Their normalized lengths are:

```text
ell_r(d,h,k;t)=E_n 1_{J_r(d,h,k;t)}(n),
r in {L,R}.
```

The actual one-point boundary means are:

```text
M_r^act(d,h,k;t)
  = E_n 1_{J_r}(n) mu_s0(n-t0).
```

The Module 207 local factor for a singleton subset is:

```text
Theta_{w,S1}^proj(d,h,k;t)
  = prod_{p>w}
      (1-1/p)^(-1)
      (1-r_p(S1;d,h,k;t)/p).
```

For a singleton primitive form:

```text
r_p(S1;d,h,k;t)=1
```

for every prime `p>w`.

## 4. Assumptions

This module assumes the fixed-row discipline from Modules 224, 234, 242:

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

It also assumes the normalized one-point W-tail convention from Module 207:

```text
primes p<=w are handled by the W-residue convention,
Theta_{w,S}^proj is an Euler product only over p>w,
one primitive active form has one forbidden residue class modulo p>w.
```

All failures at primes `p<=w` belong to:

```text
WResOne_242.
```

Prime powers belong to:

```text
PPOne_242.
```

Cutoff, range, normalization, centering, and zero-mode mismatches belong to:

```text
CutOne_242,
RangeOne_242,
NormZeroOne_242.
```

No side slot is assumed small in this module.

## 5. Proof / disproof / reduction

### A. Singleton Euler factor

For:

```text
S1={(00,0)},
L_0(n;t)=n-t0,
```

the active form occupies exactly one residue class modulo any prime:

```text
r_p(S1;d,h,k;t)=1.
```

Therefore the local prime factor from Module 207 is:

```text
theta_{p,S1}^proj
  = (1-1/p)^(-1)(1-1/p)
  = 1.
```

Multiplying over primes `p>w` gives:

```text
Theta_{w,{(00,0)}}^proj(d,h,k;t)=1.
```

This calculation is independent of `d,h,k`; those variables do not enter a
one-form local obstruction. It is also independent of `t0` at primes `p>w`,
because translating a single primitive form changes which residue class is
forbidden but not how many residue classes are forbidden.

### B. Boundary model main term

Module 242 defined:

```text
M_r^mod(d,h,k;t)
  = ell_r(d,h,k;t)
    |Theta_{w,{(00,0)}}^proj(d,h,k;t)|.
```

Using:

```text
Theta_{w,{(00,0)}}^proj=1,
```

the model term reduces to:

```text
M_r^mod(d,h,k;t)=ell_r(d,h,k;t).
```

Thus the pointwise error can be rewritten as:

```text
Err_r^243(d,h,k;t)
  = E_n 1_{J_r}(n) mu_s0(n-t0)
    - ell_r(d,h,k;t).
```

This is the exact one-point boundary prime-mean error after W-tail local
normalization.

### C. Shifted interval reading

Set:

```text
m=n-t0.
```

Then:

```text
E_n 1_{J_r}(n) mu_s0(n-t0)
```

is the same one-point mean as:

```text
E_m 1_{I_r(t0)}(m) mu_s0(m),
```

where `I_r(t0)` is the translate of `J_r` under `m=n-t0`, with the same
normalization and cutoff inherited from the row.

This observation is structural only. It does not imply that the mean of
`mu_s0` over `I_r(t0)` equals its length. That equality is exactly the
one-point boundary prime-mean estimate to be tested later.

### D. W-residue synchronization

The equality:

```text
Theta_{w,{(00,0)}}^proj=1
```

does not say anything about admissibility at primes `p<=w`. Those primes are
outside the Euler product. If the fixed W-tricked class requires:

```text
n-t0 == b mod W,
```

or a finite admissible residue family, then the boundary interval pieces
`J_r` must be synchronized with that convention.

Any mismatch is not part of the local factor. It is:

```text
WResOne_242.
```

In a pure model or exact W-residue convention this row may be zero; otherwise
it remains an explicit side-error row.

### E. Range and cutoff synchronization

The boundary intervals are defined after intersecting with the row's interval
averaging domain and `cutoff0`. If the translation:

```text
m=n-t0
```

moves part of `J_r` outside the allowed range for `mu_s0(m)`, the discrepancy
belongs to:

```text
RangeOne_242
```

or:

```text
CutOne_242.
```

This is not a change in the singleton Euler factor. It is a finite-interval
support issue.

### F. Prime-power and zero-mode slots

If:

```text
nu_s0=nu_s0^pr+pp_s0
```

in the active class, then the singleton mean splits into a prime part and a
prime-power part. The latter belongs to:

```text
PPOne_242.
```

If centering, interval normalization, or kernel truncation inserts constants
into this one-point boundary row, the discrepancy belongs to:

```text
NormZeroOne_242.
```

Neither slot is absorbed into `Theta_{w,{(00,0)}}^proj`.

### G. Resulting prototype target

After the singleton local model is simplified, the prototype target becomes:

```text
BIHLErr_243
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_{r in {L,R}}
          |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|
  = o_W(1),
```

together with:

```text
CutOne_242=o_W(1),
RangeOne_242=o_W(1),
WResOne_242=o_W(1),
PPOne_242=o_W(1),
NormZeroOne_242=o_W(1) when active.
```

This is the exact row that Module 244 should reduce to a W-admissible
one-point boundary prime-mean estimate. No endpoint estimate is used.

## 6. Edge cases

- The simplification `Theta_{w,{(00,0)}}^proj=1` holds for the normalized
  W-tail singleton model only. It does not erase W-residue constraints at
  primes `p<=w`.
- If the active weight is not normalized to have one-point W-tail mean `1`,
  the main term must use the declared one-point normalization factor instead
  of `ell_r`.
- If `L_0(n;t)=n-t0` is evaluated outside the allowed finite interval, the
  issue is `RangeOne_242`, not a local Euler-factor correction.
- If `J_r` is shorter than the range of the available one-point prime theorem,
  the row may be blocked analytically even though the local factor is `1`.
- If `|W_M|` has large absolute mass, the one-point mean error must beat that
  multiplier in the averaged target.
- If `pp_s0` is active, the prime-power row is not part of the singleton
  local factor.
- If centering or truncated projection creates constant leakage, it belongs
  to `NormZeroOne_242`.
- This module treats only the same-vertex row `(00,0)`. Off-vertex rows can
  have additional range and residue synchronization and are not proved here.
- This module does not transfer model or W-tricked estimates to the actual
  sharp moving selector.

## 7. Where it fits in the project map

The Phase F2 chain now has:

```text
Module 242
  -> fixed the active one-point row:
     BoundaryIntervalHL_234({(00,0)},(00,0)).

Module 243
  -> derives the exact singleton local factor:
     Theta_{w,{(00,0)}}^proj=1,
     so the model main term is ell_r.

Module 244
  -> should reduce the row to a W-admissible one-point boundary prime-mean
     estimate in the chosen selector class.
```

This module narrows the active analytic problem. The local factor is not the
obstruction in the same-vertex one-point row; the obstruction is the
`|W_M|`-averaged boundary mean of `mu_s0-1` on very short endpoint intervals,
plus the named side-error slots.

## 8. What remains open

This module does not prove:

- `BIHLErr_243=o_W(1)`;
- `BIHLErr_242=o_W(1)`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242`;
- `BoundaryIntervalHL_234({(00,0)},(00,0))`;
- any off-vertex one-point row;
- any two-point or larger `BoundaryIntervalHL_234(S,lambda)`;
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

- Do not cite `Theta_{w,{(00,0)}}^proj=1` as proof of the boundary mean
  estimate.
- Do not use W-tail singleton normalization to erase W-residue constraints at
  primes `p<=w`.
- Do not replace `E_n 1_{J_r} mu_s0(n-t0)` by `ell_r` without proving
  `BIHLErr_243=o_W(1)`.
- Do not use full-interval first-moment Hardy-Littlewood as a boundary
  interval theorem.
- Do not cite ordinary pair-BDH as a one-point boundary prime-mean theorem.
- Do not use cancellation from `W_M` after the row has taken `|W_M|`.
- Do not change selector class, projection, W-residue convention, dyadic
  shell, denominator grid, or cutoff to prove the prototype.
- Do not hide prime-power, range, cutoff, normalization, or zero-mode errors
  inside the singleton local factor.
- Do not transfer this same-vertex calculation to off-vertex rows without a
  separate range and residue audit.
- Do not prove the prototype by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
