# Module 248: One-point available-tools comparison

## 1. Precise theorem / claim being advanced

This module compares the one-point prototype from Modules 242-247 against the
available local tools and common shortcuts.

The active reduction is:

```text
KernelAvgStrength_245(s0,D0,rho0)
  + OnePointSideRows_246(s0,D0,rho0)
    => OnePointBIHL_242(s0,D0,rho0).
```

Define:

```text
ToolCompare_248(s0,D0,rho0)
```

to be the ledger classifying each possible tool as:

```text
exact local,
conditional local,
mixed,
endpoint-strength,
false / blocked as a shortcut,
open.
```

The comparison output is:

```text
1. Exact model normalization can close only the model branch, and only with
   exact side-row conventions.

2. Ordinary first-moment Hardy-Littlewood, full-interval W-tricked PNT, and
   ordinary pair-BDH do not prove OPMeanErr_244 in the fixed |W_M|-weighted
   boundary normalization.

3. Relative short-interval W-PNT, boundary-length majorants, and Holder
   kernel routes remain conditional local routes only if their hypotheses
   exactly match the fixed row and beat the absolute kernel mass.

4. Prime-power, W-residue, cutoff, range, normalization, and zero-mode tools
   can support the side rows only by exact convention or by separate fixed-row
   weighted estimates.
```

Thus Module 248 does not prove the one-point prototype. It prepares Module
249 to give a proof-or-blocked verdict.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module is a tool comparison and shortcut audit. It records conditional
routes and blocked shortcuts, but it proves no new prime theorem, side row, or
endpoint estimate.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active one-point form is:

```text
m0(n,t)=n-t0.
```

The active boundary intervals are:

```text
J_L(d,h,k;t)={n: m0(n,t) <= L_N},
J_R(d,h,k;t)={n: m0(n,t) > N-L_N}.
```

The fixed-row weighted average is:

```text
E_K F
  = (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)| F(d,h,k;t).
```

The pointwise one-point errors are:

```text
e_r(s0;d,h,k;t)
  = E_n 1_{J_r}(n)(mu_s0(m0(n,t))-1),
```

and:

```text
E_1(s0;d,h,k;t)
  = sum_{r in {L,R}} |e_r(s0;d,h,k;t)|.
```

The main target is:

```text
OPMeanErr_244(s0,D0,rho0)
  = E_K E_1(s0;d,h,k;t)
  = o_W(1).
```

The boundary length budget is:

```text
BLength_245(D0,rho0)
  = E_K sum_{r in {L,R}} E_n 1_{J_r}(n).
```

The side-row package is:

```text
OnePointSideRows_246
  = CutOne_242 + RangeOne_242 + WResOne_242
    + PPOne_242 + NormZeroOne_242,
```

with each row required to be `o_W(1)`.

The tool labels used below mean:

```text
exact local:
  zero or identity-level closure in the same fixed row.

conditional local:
  closure under a named fixed-row estimate that is smaller than the residual
  endpoint and does not change selector, projection, cutoff, W-residue
  convention, dyadic shell, or limit order.

mixed:
  the tool needs selector transfer, projection smoothing, cutoff transfer,
  denominator-grid movement, or a change of row.

endpoint-strength:
  the tool closes the row only by assuming projected residual fourth-moment
  control or an endpoint-equivalent package.

false / blocked as a shortcut:
  the named tool controls the wrong object or lacks required normalization.

open:
  no estimate is supplied.
```

## 4. Assumptions

This module assumes only the reductions already recorded:

```text
Module 244:
  OPMeanErr_244 + side rows => OnePointBIHL_242.

Module 245:
  KernelAvgStrength_245 => OPMeanErr_244=o_W(1).

Module 246:
  OnePointSideRows_246 names the five side rows.
```

No tool listed in this module is assumed to hold unless explicitly marked as a
conditional hypothesis.

The comparison forbids changing:

```text
s0,
P_M,
K_M,
D0<|d|<=2D0,
J_L,J_R,
cutoff0,
W-residue convention,
prime-only / prime-power convention,
fixed-w then N -> infinity then w -> infinity limit order.
```

## 5. Proof / disproof / reduction

### A. Exact model normalization

Tool:

```text
mu_model(m)=1
```

on the active intervals, with exact cutoff, range, W-residue, prime-power,
normalization, and zero-mode conventions.

Then:

```text
e_r(model;d,h,k;t)=0
```

for both `r in {L,R}`, so:

```text
OPMeanErr_244(model,D0,rho0)=0.
```

Classification:

```text
exact local for the model branch only.
```

Limits:

```text
does not prove the W branch,
does not prove the smoothed branch,
does not prove the frozen branch,
does not prove the actual moving selector.
```

If any side row is not exact by convention, the model branch still requires
the corresponding side estimate from Module 246.

### B. Ordinary first-moment Hardy-Littlewood

Tool:

```text
ordinary first-moment HL for one linear form, without the fixed |W_M|
boundary normalization.
```

This may resemble:

```text
E_n mu(n-a) = 1+o(1)
```

or a full-interval asymptotic for a single shifted form. It does not imply:

```text
E_K sum_r |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|=o_W(1).
```

The missing features are:

```text
boundary intervals J_L,J_R,
absolute value before the kernel average,
|W_M(t)| weighting,
W-uniform residue conventions,
selector class s0,
side-row accounting.
```

Classification:

```text
false / blocked as a shortcut.
```

Upgrade required:

```text
ordinary first-moment HL would have to be replaced by
WOneBoundaryPNT_244 or an equivalent fixed-row boundary theorem.
```

That replacement is exactly an open input, not an available shortcut.

### C. Full-interval W-tricked PNT

Tool:

```text
full-interval W-tricked PNT in the admissible residue class.
```

This can support normalization of the W-tricked weight on long full intervals.
It still does not prove the boundary target unless it is localized to
`J_L,J_R` and survives `|W_M|`.

A useful weaker consequence may be a mass majorant:

```text
E_n 1_{J_r}(n) mu_W(m0(n,t))
  <= C_mean(w,rho0) E_n 1_{J_r}(n) + err_r^mass(d,h,k;t).
```

By Module 245 this gives a conditional local route only if:

```text
(C_mean+1)BLength_245 + E_K sum_r |err_r^mass| = o_W(1).
```

Classification:

```text
full-interval cancellation: false / blocked as a shortcut;
mass-majorant use: conditional local if the displayed bound holds.
```

If the proof changes the W-family, residue convention, interval cutoff, or
selector class, the route becomes mixed.

### D. Relative short-interval W-PNT

Tool:

```text
uniform relative W-tricked PNT on every active translated boundary interval.
```

The needed form is:

```text
|e_r(W;d,h,k;t)|
  <= eps_rel(N,w,rho0) E_n 1_{J_r}(n)
     + err_r^rel(d,h,k;t),
```

with:

```text
eps_rel(N,w,rho0) BLength_245
  + E_K sum_r |err_r^rel(d,h,k;t)|
  = o_W(1).
```

Classification:

```text
conditional local if available in exactly this fixed row.
```

Failure modes:

```text
open if the intervals are too short for the available theorem;
mixed if the theorem uses smoothed intervals or a changed projection;
blocked if it lacks W-uniformity or the active residue convention;
endpoint-strength if it is proved only through residual fourth-moment control.
```

### E. Boundary-length majorant

Tool:

```text
positivity plus small weighted boundary length.
```

Using:

```text
|e_r| <= E_n 1_{J_r} mu_s0(m0(n,t)) + E_n 1_{J_r},
```

a mass majorant gives:

```text
OPMeanErr_244
  <= (C_mean+1)BLength_245 + MassErr.
```

Classification:

```text
conditional local if BLength_245 and MassErr are o_W(1) in the fixed row.
```

This route does not require cancellation of `mu_s0-1`, but it requires the
weighted boundary support to be small enough after the absolute kernel mass.
If `BLength_245` is not small, the route fails.

### F. Holder kernel route

Tool:

```text
unweighted L^p control of one-point errors plus L^q control of |W_M|.
```

The required inequality is:

```text
OPMeanErr_244
  <= K_q(M) E_p(s0),
```

where:

```text
K_q(M)=(E_t |W_M(t)|^q)^(1/q),
E_p(s0)=((1/D0)sum_d E_{h,k,t} E_1(s0;d,h,k;t)^p)^(1/p).
```

Thus the route closes only if:

```text
K_q(M) E_p(s0)=o_W(1).
```

Classification:

```text
conditional local if both factors are fixed-row estimates and no projection
or selector is changed.
```

An unweighted `L^1` average alone is insufficient unless paired with a
pointwise or integrability bound that controls correlation with `|W_M|`.

### G. Prime-power sparsity

Tool:

```text
prime-power sparsity for pp_s0.
```

It addresses only:

```text
PPOne_242
  = E_K sum_r E_n 1_{J_r}(n)|pp_s0(m0(n,t))|.
```

Classification:

```text
exact local if pp_s0=0 by convention;
conditional local if the displayed weighted boundary mass is o_W(1);
false / blocked as a proof of OPMeanErr_244 itself.
```

Full-interval prime-power sparsity is not enough unless it is converted to
the fixed `|W_M|` boundary average.

### H. W-residue exactness

Tool:

```text
exact W-admissible residue construction for m0(n,t).
```

It addresses only:

```text
WResOne_242.
```

Classification:

```text
exact local if the same W-residue convention is used in the source row,
the W-tricked weight, and Theta_{w,{(00,0)}}^proj=1;
conditional local if the W-failure set has weighted one-point mass o_W(1);
mixed if residue conventions are compared across selector classes or W-families.
```

It is not a substitute for the boundary prime mean theorem.

### I. Cutoff, range, normalization, and zero-mode conventions

Tools:

```text
exact cutoff identity,
exact range truncation,
exact normalization,
exact zero-mode removal.
```

They address:

```text
CutOne_242,
RangeOne_242,
NormZeroOne_242.
```

Classification:

```text
exact local if built into the fixed row;
conditional local if the corresponding weighted defect is o_W(1);
mixed if the proof changes cutoff, range, projection, centering, or selector;
endpoint-strength if only residual fourth-moment control bounds the defect.
```

In particular, cyclic zero-mode cancellation does not automatically imply
zero-mode cancellation after interval restriction.

### J. Ordinary pair-BDH

Tool:

```text
ordinary pair-BDH for shifted prime pairs.
```

This controls a pair-correlation variance object. The present target is a
one-point boundary mean with an absolute projected-kernel weight:

```text
E_K sum_r |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|.
```

The objects differ in:

```text
number of prime factors,
boundary localization,
absolute value placement,
kernel weighting,
selector and W-residue discipline,
side-row requirements.
```

Classification:

```text
false / blocked as a shortcut to OPMeanErr_244 or OnePointBIHL_242.
```

It can become relevant only through a separate analytic bridge. If that bridge
uses projected residual fourth-moment control, it is endpoint-strength and
does not make the one-point prototype local.

## 6. Edge cases

- If `s0=model` and every side row is exact, the model prototype is closed by
  convention. This does not transfer to W, smoothed, frozen, or actual
  selectors.
- If the boundary intervals have weighted length `o_W(1)`, the
  boundary-length majorant may close the mean without cancellation. If not,
  cancellation or a stronger kernel route is needed.
- If `A_W(M)` or `K_q(M)` grows, every pointwise, relative, Holder, and
  side-row estimate must beat that growth.
- If a short-interval theorem is stated for intervals not matching
  `J_L,J_R`, it needs a cutoff transfer row.
- If a theorem is uniform in residue classes but not in fixed `w` followed by
  `N -> infinity` and then `w -> infinity`, it does not match the row.
- If a theorem applies to the W branch, it does not automatically apply to the
  smoothed or frozen branches.
- If prime powers, W-residue failures, or zero-mode leakage are sparse only in
  unweighted average, a kernel-correlation estimate is still needed.
- If ordinary pair-BDH is used only to motivate the one-point estimate, it
  remains a heuristic comparison, not a proof step.

## 7. Where it fits in the project map

The Phase F2 chain is now:

```text
Module 242
  -> fixed OnePointBIHL_242.

Module 243
  -> exact singleton local model.

Module 244
  -> OPMeanErr_244 plus side rows.

Module 245
  -> strength audit after |W_M|.

Module 246
  -> side-row audit.

Module 247
  -> plan challenge and narrowed proof-or-blocked mandate.

Module 248
  -> available-tools comparison.
```

The next module should give the promised verdict:

```text
Module 249:
  classify OnePointBIHL_242 as conditional local, mixed, endpoint-strength,
  or false / blocked as a shortcut.
```

The likely input to that verdict is:

```text
No standard shortcut proves the W, smoothed, or frozen one-point row.
Only exact model conventions and explicitly weighted fixed-row estimates
remain viable.
```

## 8. What remains open

This module does not prove:

- `KernelAvgStrength_245(s0,D0,rho0)`;
- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(sm,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(fr,D0,rho0)=o_W(1)`;
- any relative short-interval W-tricked PNT in the required range;
- `BLength_245=o_W(1)`;
- `K_q(M)E_p(s0)=o_W(1)`;
- `OnePointSideRows_246(s0,D0,rho0)`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242(s0,D0,rho0)` outside the exact model convention case;
- any off-vertex one-point row;
- any two-point or higher `BoundaryIntervalHL_234(S,lambda)` row;
- `FixedSupportTupleHL_238`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
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

- Do not treat ordinary first-moment Hardy-Littlewood as a boundary theorem in
  the fixed `|W_M|` normalization.
- Do not use full-interval W-tricked PNT as a short-boundary interval theorem.
- Do not ignore the absolute value before the `d,h,k,t` average.
- Do not assume `A_W(M)` or `K_q(M)` is harmless without a fixed-row bound.
- Do not absorb prime-power, W-residue, cutoff, range, normalization, or
  zero-mode defects into `OPMeanErr_244`.
- Do not use ordinary pair-BDH as a one-point boundary mean theorem.
- Do not change selector class, projection, cutoff, W-residue convention,
  dyadic shell, or limit order inside a tool comparison.
- Do not transfer W estimates to smoothed, frozen, or actual moving selectors
  without named transfer rows.
- Do not close the prototype by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
