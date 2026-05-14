# Module 247: Fourth plan challenge for the one-point prototype

## 1. Precise theorem / claim being advanced

This module performs the fourth 15-iteration plan challenge required by the
long-term schedule. It questions the Phase F2 branch after Modules 242-246.

The active chain is:

```text
OnePointBIHL_242(s0,D0,rho0)
  <= KernelAvgStrength_245(s0,D0,rho0)
     + OnePointSideRows_246(s0,D0,rho0).
```

Define:

```text
PlanChallenge_4_247
```

to be the governance review asking whether the one-point prototype has exposed
a genuinely smaller target than the projected residual endpoint, or whether it
has only renamed endpoint-strength assumptions.

The challenge verdict is:

```text
Continue Phase F2 through Modules 248 and 249, but only in narrowed
proof-or-blocked mode.
```

The narrowed rule is:

```text
Module 248 must test available local tools against OPMeanErr_244 and the
side rows. Module 249 must give a verdict for OnePointBIHL_242: conditional
local, mixed, endpoint-strength, or false/blocked as a shortcut.
```

No further one-point machinery should be added before that verdict.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a planning and audit module. It introduces no new analytic estimate
and proves no boundary mean theorem, side row, endpoint, or selector transfer.

## 3. Definitions and variables

The fixed row remains:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active same-vertex one-point prototype is:

```text
OnePointBIHL_242(s0,D0,rho0)
  = BoundaryIntervalHL_234({(00,0)},(00,0)).
```

The active one-point form is:

```text
m0(n,t)=n-t0.
```

The active boundary intervals are:

```text
J_L(d,h,k;t) = {n: m0(n,t) <= L_N},
J_R(d,h,k;t) = {n: m0(n,t) > N-L_N}.
```

The weighted one-point mean target is:

```text
OPMeanErr_244(s0,D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t}|W_M(t)|
        sum_{r in {L,R}}
          |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|.
```

The strength package from Module 245 is:

```text
KernelAvgStrength_245(s0,D0,rho0)
  => OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

The side package from Module 246 is:

```text
OnePointSideRows_246(s0,D0,rho0)
  = CutOne_242 + RangeOne_242 + WResOne_242
    + PPOne_242 + NormZeroOne_242
```

with each row required to be `o_W(1)` in the fixed normalization.

Define:

```text
F2NarrowVerdict_247
```

as the decision:

```text
continue to Module 248 and Module 249 only;
do not add new side packages before a proof-or-blocked verdict;
do not call the prototype local unless the needed mean and side rows are
proved by fixed-row local estimates.
```

## 4. Assumptions

This challenge assumes only the recorded module chain:

```text
Modules 242-246.
```

It does not assume:

```text
KernelAvgStrength_245,
OnePointSideRows_246,
OPMeanErr_244=o_W(1),
OnePointBIHL_242,
FixedSupportTupleHL_238,
LocalBdPkg_226,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
RBDH_pair_short,
CPC_3^sharp,
AU^3.
```

The challenge questions from the long-term plan are:

```text
Q1. Are we relying on a convenient boundary mean theorem?
Q2. Are the side rows actually local, or quietly endpoint-strength?
Q3. Does OPMeanErr_244 require too-short an interval PNT or kernel smoothing?
Q4. Has the one-point prototype exposed a smaller target, or merely renamed
    the projected residual endpoint?
Q5. Should Phase F2 continue to Module 248, narrow, or redirect?
```

## 5. Proof / disproof / reduction

This section answers the challenge questions.

### Q1. Convenient boundary mean theorem

The branch is currently relying on a missing theorem:

```text
OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

Module 245 correctly refused to identify this with an ordinary unweighted
prime number theorem. The estimate is weighted by:

```text
|W_M(t)|
```

and is localized to moving boundary intervals `J_L,J_R`. Therefore a generic
first-moment Hardy-Littlewood statement, or a full-interval mean statement,
does not automatically imply the needed estimate.

Verdict:

```text
The boundary mean input is convenient but unproved.
```

It may still be smaller than the residual endpoint if Module 248 can identify
a genuine fixed-row route, such as a boundary-length majorant, a relative
boundary PNT in the active range, or a Holder route with enough kernel
integrability. Without such a route, it remains open.

### Q2. Side rows local or endpoint-strength

Module 246 made the side rows explicit:

```text
CutOne_242,
RangeOne_242,
WResOne_242,
PPOne_242,
NormZeroOne_242.
```

The optimistic reading is:

```text
CutOne_242 and RangeOne_242 may be zero by convention;
WResOne_242 may be zero under an exact W-admissible row;
PPOne_242 may be local under weighted prime-power sparsity;
NormZeroOne_242 may be local under exact normalization and zero-mode control.
```

The cautious reading is:

```text
each row becomes mixed if it changes selector class, projection, cutoff,
range, denominator grid, or W-residue convention.
```

Verdict:

```text
The side rows are not yet proved local. They are only plausible local rows
under exact fixed-row conventions or explicitly weighted one-point estimates.
```

They must stay outside `KernelAvgStrength_245`; otherwise the project would
hide transfer assumptions inside the mean theorem.

### Q3. Short intervals and kernel smoothing

The active boundary intervals may be much shorter than the ambient interval.
Even if the length is deterministic and small, the required estimate is not:

```text
E_n 1_J(n)(mu_s0(n-t0)-1)=o(1)
```

in isolation. It is:

```text
(1/D0) sum_d E_{h,k,t}|W_M(t)|
  sum_r |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)| = o_W(1).
```

Thus there are two independent stresses:

```text
boundary interval length,
absolute projected-kernel mass.
```

If the proof smooths the boundary, changes `P_M`, or uses cancellation in
`W_M`, it no longer proves the fixed prototype without a transfer row.

Verdict:

```text
OPMeanErr_244 may require a short-interval PNT or a kernel-averaged substitute
whose strength is not currently in the ledger.
```

Module 248 must make this comparison concrete rather than treating the input
as harmless.

### Q4. Smaller target or renamed endpoint

The one-point prototype is formally smaller than the projected residual cube:

```text
one active form,
same vertex,
fixed selector class,
fixed dyadic shell,
fixed boundary intervals,
no off-vertex tuple local factor.
```

That is useful. It reduced a nonempty tuple-HL obstruction to one explicit
weighted boundary mean plus five named side rows.

But the analytic status is still not a proof. The prototype becomes a renamed
endpoint if its only route uses:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
RBDH_pair_short,
CPC_3^sharp,
AU^3,
generic selector transfer,
unlocalized projected residual fourth-moment control.
```

Verdict:

```text
The branch has exposed a smaller diagnostic target, but has not yet exposed a
proved smaller theorem.
```

This is progress as a map, not as a closed estimate.

### Q5. Continue, narrow, or redirect

The best next move is not to abandon the branch immediately, because Module
248 can still test actual local tools against a small target. But continuing
to add abstractions would blur the issue.

Decision:

```text
Continue Phase F2 through Module 249 only, in narrowed proof-or-blocked mode.
```

The narrowed instructions are:

```text
Module 248:
  compare OPMeanErr_244 and the five side rows against available tools:
  first-moment HL, W-tricked PNT, short-interval PNT ranges, prime-power
  sparsity, W-residue exactness, normalization, and ordinary pair-BDH.

Module 249:
  give the one-point prototype verdict:
  conditional local, mixed, endpoint-strength, or false/blocked as a shortcut.
```

Stop condition:

```text
If Module 248 finds no fixed-row route for OPMeanErr_244 that survives
|W_M|, then Module 249 should mark the prototype as blocked or mixed rather
than adding a new package.
```

## 6. Edge cases

- If `s0=model` makes `mu_model=1` exactly on the active row, the mean term is
  zero, but that proves only a model convention row, not the W, smoothed,
  frozen, or actual selector row.
- If `CutOne_242`, `RangeOne_242`, or `WResOne_242` are declared zero by
  convention, Module 248 must cite the exact convention. A plausibility
  statement is not enough.
- If the boundary interval length is `o(N)`, a mass bound may close a model or
  majorant row, but cancellation of `mu_s0-1` still needs its own estimate
  unless the proof uses only boundary volume.
- If `A_W(M)` is large, every pointwise, prime-power, residue, range, and
  cutoff estimate must beat the absolute kernel mass.
- If the proof uses smoothed boundaries, it must record a cutoff transfer row.
- If the proof uses a smoothed projection, it must record a projection
  transfer row.
- If the proof uses cancellation in the signed kernel `W_M`, it does not prove
  the fixed row after `|W_M|`.
- If a short-interval prime theorem is invoked, its range, W-uniformity,
  residue restrictions, and selector class must match the fixed row.
- If ordinary pair-BDH appears in Module 248, it must be treated as a possible
  comparison tool only, not as a substitute for the one-point boundary mean.

## 7. Where it fits in the project map

This challenge sits inside Phase F2:

```text
Module 242
  -> fixed the one-point same-vertex prototype.

Module 243
  -> computed the exact singleton local model.

Module 244
  -> reduced the row to OPMeanErr_244 plus side rows.

Module 245
  -> audited the strength needed after the |W_M| average.

Module 246
  -> audited the cutoff, range, W-residue, prime-power,
     normalization, and zero-mode side rows.

Module 247
  -> challenges the branch and narrows the next two modules.
```

The next module is:

```text
Module 248: one-point available-tools comparison.
```

It should be a proof attempt in miniature:

```text
ordinary first-moment tools,
W-tricked PNT tools,
short-interval range limits,
prime-power sparsity,
W-residue exactness,
normalization / zero-mode control,
ordinary pair-BDH comparison.
```

## 8. What remains open

This module does not prove:

- `KernelAvgStrength_245(s0,D0,rho0)`;
- `OPMeanErr_244(s0,D0,rho0)=o_W(1)`;
- `OnePointSideRows_246(s0,D0,rho0)`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242(s0,D0,rho0)`;
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

- Do not call the one-point prototype solved because the local model is
  `Theta=1`.
- Do not treat `OPMeanErr_244` as a standard PNT corollary without checking
  boundary length, W-uniformity, selector class, and `|W_M|`.
- Do not hide side rows inside the boundary mean theorem.
- Do not use cancellation in `W_M` after the fixed-row average takes
  `|W_M|`.
- Do not replace fixed-row estimates by smoothed or changed-projection
  estimates without transfer rows.
- Do not use ordinary pair-BDH, first-moment HL, or rectangle-HL as a shortcut
  to residual boundary control.
- Do not upgrade model, W, smoothed, or frozen selector statements to the
  actual sharp moving selector.
- Do not close the prototype by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
