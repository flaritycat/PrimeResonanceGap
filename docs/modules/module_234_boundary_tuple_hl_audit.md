# Module 234: Boundary tuple-HL audit for the fixed row

## 1. Precise theorem / claim being advanced

This module audits the actual tuple-matching row left open by Modules 225,
226, and 233:

```text
BoundaryTupleHL_225(S,lambda):
  |BTuple_225(S,lambda)-BdModel_225(S,lambda)|=o_W(1).
```

The fixed context is still:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

Define:

```text
BoundaryTupleAudit_234(S,lambda).
```

The verdict is:

```text
S=emptyset:
  BoundaryTupleHL_225(emptyset,lambda) has zero error by definition.

S nonempty:
  BoundaryTupleHL_225(S,lambda) is a local weighted boundary-HL input
  only if it is proved as a boundary-restricted, W-admissible,
  exact-local-model tuple theorem.
```

For nonempty `S`, the sufficient local criterion is:

```text
BoundaryIntervalHL_234(S,lambda)
  => BoundaryTupleHL_225(S,lambda).
```

If the proof of `BoundaryIntervalHL_234` requires an unlocalized projected
residual fourth-moment estimate, then the row is endpoint-strength in
disguise. If it requires W-residue, prime-power, kernel-tail, or range
packages outside the fixed boundary interval theorem, it is mixed rather than
purely local.

## 2. Status label

`CONDITIONAL`

The empty-subset row is a deterministic identity. The nonempty tuple rows are
classified conditionally, and the required boundary interval-HL estimates are
not proved here.

## 3. Definitions and variables

Use the fixed data:

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

Write the projected vertices as:

```text
v_sigma=n+a_sigma(d,h,k;t),
sigma in Lambda_8.
```

For a fixed boundary label `lambda`, let:

```text
Bd_lambda(d,n,h,k;t)
  = 1_{v_lambda notin I_N^core(L_N)}.
```

The boundary volume is:

```text
BdVol_lambda(d,h,k;t)
  = E_n Bd_lambda(d,n,h,k;t).
```

For a subset `S subset Lambda_8`, Module 225 defined:

```text
BTuple_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        E_n Bd_lambda(d,n,h,k;t)
          prod_{sigma in S} mu_s0(v_sigma),
```

and:

```text
BdModel_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        BdVol_lambda(d,h,k;t)
        |Theta_{w,S}^proj(d,h,k;t)|.
```

The pointwise boundary tuple error is:

```text
ErrTuple_234(S,lambda;d,h,k;t)
  = E_n Bd_lambda(d,n,h,k;t)
      prod_{sigma in S} mu_s0(v_sigma)
    - BdVol_lambda(d,h,k;t)
      |Theta_{w,S}^proj(d,h,k;t)|.
```

The averaged absolute boundary tuple error is:

```text
AbsErrTuple_234(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        |ErrTuple_234(S,lambda;d,h,k;t)|.
```

Then:

```text
AbsErrTuple_234(S,lambda)=o_W(1)
  => BoundaryTupleHL_225(S,lambda).
```

This is stronger than the signed averaged row in Module 225, but it is the
right audit object because the boundary row has already passed to `|W_M|` and
positive majorants.

## 4. Assumptions

`BoundaryIntervalHL_234(S,lambda)` consists of the following fixed-row
requirements.

### A. Fixed-row discipline

No parameter or selector changes are allowed:

```text
same P_M,
same R0 and eta0,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same W-residue convention,
same cutoff0,
same interval convention,
same fixed-w then N -> infinity then w -> infinity limit order.
```

It excludes:

```text
fr -> mv,
sm -> fr,
bern -> sm,
fs -> bern,
major/minor partition transfer.
```

### B. Boundary interval decomposition

For each fixed `(d,h,k,t)`, the support:

```text
{n: Bd_lambda(d,n,h,k;t)=1}
```

is decomposed into at most two boundary intervals:

```text
J_{lambda,r}(d,h,k;t),  r in {left,right},
```

plus any declared cutoff or out-of-range pieces. The normalized interval
lengths are:

```text
ell_{lambda,r}(d,h,k;t)=E_n 1_{J_{lambda,r}}.
```

The decomposition must satisfy:

```text
BdVol_lambda(d,h,k;t)
  = sum_r ell_{lambda,r}(d,h,k;t)
```

up to a separately named cutoff error:

```text
CutBd_234(S,lambda)=o_W(1).
```

### C. Boundary interval weighted HL

For every interval piece `J_{lambda,r}`, the fixed affine system:

```text
n+a_sigma(d,h,k;t),  sigma in S,
```

satisfies the weighted boundary tuple matching:

```text
E_n 1_{J_{lambda,r}}(n)
  prod_{sigma in S} mu_s0(n+a_sigma)

  =
ell_{lambda,r}(d,h,k;t)
  |Theta_{w,S}^proj(d,h,k;t)|
  + Err_{S,lambda,r}(d,h,k;t).
```

The required averaged error is:

```text
BIHLErr_234(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_r |Err_{S,lambda,r}(d,h,k;t)|
  = o_W(1).
```

### D. Structural and arithmetic synchronization

The boundary interval theorem must use the exact projected local factor
`Theta_{w,S}^proj`. If it removes or modifies exceptional sets, it must also
include:

```text
DiagSync_234(S,lambda)=o_W(1),
WResBdTuple_234(S,lambda)=o_W(1),
PPTupleBd_234(S,lambda)=o_W(1),
RangeBdTuple_234(S,lambda)=o_W(1).
```

Here:

- `DiagSync_234` covers structural coincidences or repeated forms inside
  `S`;
- `WResBdTuple_234` covers small-prime and W-residue compatibility near the
  boundary;
- `PPTupleBd_234` covers prime-power artifacts in the tuple weights;
- `RangeBdTuple_234` covers CRT or denominator errors caused by the short
  boundary intervals.

These errors may be zero in a purely model class, but they must be declared.

## 5. Proof / disproof / reduction

### A. The empty subset

When `S=emptyset`:

```text
prod_{sigma in S} mu_s0(v_sigma)=1,
Theta_{w,emptyset}^proj=1.
```

Therefore:

```text
BTuple_225(emptyset,lambda)
  = (1/D0) sum_d E_{h,k,t}|W_M(t)| BdVol_lambda(d,h,k;t)
  = BdModel_225(emptyset,lambda).
```

Thus the empty-subset boundary tuple row has zero error. This is a
deterministic normalization check, not a proof of any nonempty prime-weighted
tuple row.

### B. Reduction from boundary interval-HL to `BoundaryTupleHL_225`

Assume `BoundaryIntervalHL_234(S,lambda)`.

Use the interval decomposition:

```text
Bd_lambda = sum_r 1_{J_{lambda,r}} + cutoff error.
```

Then:

```text
E_n Bd_lambda
  prod_{sigma in S} mu_s0(v_sigma)

  =
sum_r E_n 1_{J_{lambda,r}}
  prod_{sigma in S} mu_s0(v_sigma)
  + cutoff error.
```

Insert the interval-HL formula:

```text
sum_r E_n 1_{J_{lambda,r}}
  prod_{sigma in S} mu_s0(v_sigma)

  =
sum_r ell_{lambda,r}
  |Theta_{w,S}^proj|
  + sum_r Err_{S,lambda,r}.
```

Since:

```text
sum_r ell_{lambda,r}=BdVol_lambda
```

up to `CutBd_234`, the main term is:

```text
BdVol_lambda(d,h,k;t)
  |Theta_{w,S}^proj(d,h,k;t)|.
```

Therefore:

```text
AbsErrTuple_234(S,lambda)
  <= BIHLErr_234(S,lambda)
     + CutBd_234(S,lambda)
     + DiagSync_234(S,lambda)
     + WResBdTuple_234(S,lambda)
     + PPTupleBd_234(S,lambda)
     + RangeBdTuple_234(S,lambda).
```

If every displayed term is `o_W(1)`, then:

```text
AbsErrTuple_234(S,lambda)=o_W(1),
```

and hence:

```text
BoundaryTupleHL_225(S,lambda).
```

This proves only a conditional reduction.

### C. Classification of the nonempty row

For `S` nonempty, the row is local only if the proof genuinely stays inside:

```text
boundary intervals,
the fixed affine forms n+a_sigma,
the exact projected local factor Theta_{w,S}^proj,
the fixed selector class s0,
the fixed dyadic shell D0<|d|<=2D0.
```

It is mixed if it needs:

```text
W-residue boundary transfer,
prime-power boundary transfer,
large CRT range bookkeeping,
kernel-tail removal,
normalization or cutoff transfer.
```

It is endpoint-strength if it is proved by assuming any unlocalized statement
of the form:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
```

or by invoking:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CoreSel_4,
MoveLayerCube_3^Pi,
MajorAnalyticPkg_229.
```

### D. Why the familiar shortcuts still fail

The model-volume criterion from Module 233 does not prove this row, because
it controls:

```text
BdVol_lambda |Theta_{w,S}^proj|
```

and not:

```text
E_n Bd_lambda prod_{sigma in S} mu_s0(v_sigma).
```

A first-moment boundary-volume estimate only controls `BdVol_lambda`.
It says nothing about concentration of the weights `mu_s0(v_sigma)` on the
boundary intervals.

Ordinary pair-BDH controls the wrong object and does not supply the
boundary-marked `S`-tuple asymptotic. First-moment Hardy-Littlewood over the
full interval is also insufficient unless it is upgraded to the boundary
interval, W-admissible, exact-local-model error above.

## 6. Edge cases

- `S=emptyset` is exact and should not be used as evidence for nonempty `S`.
- If `|S|=1`, the row is a one-point boundary weighted mean; it is still not
  implied by boundary volume unless the weight is known not to concentrate on
  the boundary interval.
- If two labels in `S` are structurally identical, the actual tuple may
  contain powers of the same weight. This must be handled by `DiagSync_234`
  or by the exact diagonal model.
- If the boundary intervals are too short for the needed W-uniform tuple
  estimate, `RangeBdTuple_234` may fail.
- If `|W_M|` has large absolute mass, all tuple errors must be strong enough
  after multiplication by that mass.
- If `Theta_{w,S}^proj` is replaced by a generic collision-free factor, the
  row no longer matches Module 225.
- If the proof changes the selector class, it has left the fixed row.
- If prime powers or W-residue failures are present only near endpoints, they
  still require boundary-marked estimates.
- If the proof assumes the unlocalized projected cube, the row is not a local
  boundary row.

## 7. Where it fits in the project map

The fixed-row chain is now:

```text
Module 224
  -> fixed boundary/prefix row
Module 225
  -> tuple and model envelope ledger
Module 226
  -> conditional local verdict under LocalBdPkg_226
Module 233
  -> model mass reduced to boundary volume plus local-factor budgets
Module 234
  -> tuple matching reduced to boundary interval weighted HL,
     with emptyset exact and nonempty S still open.
```

This module narrows `LocalBdPkg_226`: the model side has a volume criterion,
but the actual tuple side requires a genuine boundary-restricted weighted
Hardy-Littlewood theorem or a precise mixed/error package.

## 8. What remains open

This module does not prove:

- `BoundaryIntervalHL_234(S,lambda)` for any nonempty `S`;
- `BIHLErr_234(S,lambda)=o_W(1)` for nonempty `S`;
- `DiagSync_234(S,lambda)`;
- `WResBdTuple_234(S,lambda)`;
- `PPTupleBd_234(S,lambda)`;
- `RangeBdTuple_234(S,lambda)`;
- `BoundaryTupleHL_225(S,lambda)` for nonempty `S`;
- `BoundaryModelMass_225(S,lambda)` beyond the conditional criterion of
  Module 233;
- `KernelAbsTail_225(P_M,T0)`;
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

- Do not use the exact `S=emptyset` row to claim any nonempty tuple row.
- Do not replace `BoundaryTupleHL_225` by first-moment boundary volume.
- Do not replace boundary interval weighted HL by full-interval average HL.
- Do not cite ordinary pair-BDH as a boundary-marked tuple theorem.
- Do not use model mass as a substitute for actual tuple matching.
- Do not use cancellation from `W_M` after taking `|W_M|`.
- Do not replace `Theta_{w,S}^proj` by the full eight-form factor, by
  `Omega_w^proj`, or by a generic collision-free factor.
- Do not replace rectangle faces by `kappa_w(d)^2`.
- Do not change selector class, projection, denominator grid, or dyadic shell
  inside this fixed-row audit.
- Do not prove the nonempty tuple row by assuming the projected residual
  endpoint.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
