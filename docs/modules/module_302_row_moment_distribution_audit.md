# Module 302: Row-moment distribution audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the row-moment distribution audit selected by
`Reflective_4.md` and Module 300.

Define:

```text
RowMomentDistributionAudit_302(P_minor^0).
```

The audit tests whether current same-family inputs provide a nontrivial
distributional or high-moment gain for:

```text
ShiftMomentP0_284(q;lambda_j)
  =
  D^(-1) sum_{D<|d|<=2D} E_{d,0}(lambda_j)^q
```

strong enough to satisfy:

```text
RowMomentGainTarget_300(q).
```

Verdict:

```text
RowMomentDistributionAudit_302(P_minor^0):
  STRUCTURAL / EXTRACTION.

LayerCakeRowCriterion_302(q):
  STRUCTURAL / EXTRACTION.

CurrentMarkovRowDistribution_302(q):
  FALSE / BLOCKED.

EndpointFourthMomentRowRoute_302:
  FALSE / BLOCKED as a proof route.

RowTailGainTarget_302(q):
  OPEN.

RowSquareMomentTarget_302:
  OPEN.
```

The module does not prove row-barrier smallness. It records that the current
first-energy distribution route gives only the Module 300 ceiling, and that a
fourth-moment large-spectrum route would be circular unless supplied by an
independent non-endpoint theorem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a proof-or-blocked audit of possible row distribution inputs. It
proves no threshold closure and no endpoint estimate.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

The residual derivative coefficients are:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

For `lambda_j in Lambda_0`, define:

```text
Spec_{d,0}^minor(lambda_j)
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j },

E_{d,0}(lambda_j)
  =
  sum_{xi in Spec_{d,0}^minor(lambda_j)}
    |beta_0(d,xi)|^2.
```

Define the row tail distribution:

```text
T_j(u)
  =
  D^(-1)# { d:D<|d|<=2D,
             E_{d,0}(lambda_j)>u }.
```

Let:

```text
E_{d,0}^minor
  =
  sum_{xi in Minor_0(R,eta)} |beta_0(d,xi)|^2,

E2_minor^0(D;R,eta)
  =
  D^(-1) sum_{D<|d|<=2D} E_{d,0}^minor,

C_D=D^(-1)# { d:D<|d|<=2D },
L_{N,w}=1+log(WN+b),
theta_q=(q-1)/q.
```

The row barrier from Module 284 is:

```text
RowBarrierP0_284(q)
  =
  sum_j lambda_j^2
    (L_j C_D)^theta_q
    ShiftMomentP0_284(q;lambda_j)^(1/q).
```

The target extracted by Module 300 is:

```text
RowMomentGainTarget_300(q):
  find U_j such that

  ShiftMomentP0_284(q;lambda_j)^(1/q) <= U_j

  and

  sum_j lambda_j^2 (L_j C_D)^theta_q U_j=o_W(1).
```

## 4. Assumptions

This module assumes Modules 278, 284, 297, 300, `Reflective_4.md`, and the
active status ledger.

It uses only:

```text
normalized Parseval,
the pointwise logarithmic envelope,
the Module 297 local low-level tail result,
and first-moment row energy information.
```

It does not assume:

```text
RowTailGainTarget_302(q),
RowSquareMomentTarget_302,
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ShiftMomentP0_284(q;lambda_j) smallness,
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
PhaseKernelBound_273^0,
PhaseKernelBound_273,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Layer-cake criterion

For each fixed `lambda_j`, set:

```text
X_d=E_{d,0}(lambda_j).
```

For fixed `q>1`:

```text
ShiftMomentP0_284(q;lambda_j)
  =
  D^(-1) sum_d X_d^q.
```

Using the layer-cake identity for nonnegative finite sequences:

```text
D^(-1) sum_d X_d^q
  =
  q int_0^infty u^(q-1) T_j(u) du.
```

Since Module 297 gives:

```text
0<=X_d<=E_{d,0}^minor<=L_{N,w}^4,
```

the integral is actually over:

```text
0<=u<=L_{N,w}^4.
```

Therefore a row distribution theorem strong enough for Module 300 would be a
family of tail bounds:

```text
T_j(u)<=Psi_j(u)
```

such that:

```text
U_j^q
  =
  q int_0^{L_{N,w}^4} u^(q-1) Psi_j(u) du
```

and:

```text
sum_j lambda_j^2 (L_j C_D)^theta_q U_j=o_W(1).
```

Classification:

```text
LayerCakeRowCriterion_302(q):
  STRUCTURAL / EXTRACTION.
```

It is an exact criterion, not an estimate.

### B. Current Markov distribution

The only current row distribution input from first energy is Markov:

```text
T_j(u)
  <=
  min(
    C_D,
    D^(-1) sum_d E_{d,0}(lambda_j) / u
  ).
```

Since:

```text
E_{d,0}(lambda_j)<=E_{d,0}^minor,
```

this gives:

```text
T_j(u)
  <=
  min(
    C_D,
    E2_minor^0(D;R,eta)/u
  ).
```

Insert this into the layer-cake formula and use the cutoff
`L_{N,w}^4`:

```text
ShiftMomentP0_284(q;lambda_j)
  <=
  q int_0^{L_{N,w}^4}
      u^(q-1) min(C_D,E2_minor^0/u) du.
```

The second term gives the same interpolation scale as Module 300:

```text
ShiftMomentP0_284(q;lambda_j)
  <=
  C_q L_{N,w}^{4(q-1)} E2_minor^0(D;R,eta),
```

for a constant `C_q` depending only on `q`.

Using:

```text
E2_minor^0(D;R,eta)<=C_D L_{N,w}^4
```

recovers:

```text
ShiftMomentP0_284(q;lambda_j)^(1/q)
  <=
  C_q' C_D^(1/q)L_{N,w}^4.
```

Substitution into the row barrier gives exactly the Module 300
polylogarithmic ceiling, up to constants:

```text
RowBarrierP0_284(q)
  <=
  O_q(C_D J_Lambda^theta_q L_{N,w}^8).
```

This is not forced to be `o_W(1)`.

Classification:

```text
CurrentMarkovRowDistribution_302(q):
  FALSE / BLOCKED.
```

This does not disprove future row distribution gains. It says only that the
current first-energy Markov route reproduces the already-blocked row-barrier
ceiling.

### C. Fourth-moment large-spectrum route is circular here

For one fixed row and level:

```text
E_{d,0}(lambda_j)
  =
  sum_{|beta_0(d,xi)|>=lambda_j} |beta_0(d,xi)|^2
  <=
  lambda_j^(-2)
  sum_{xi in Minor_0(R,eta)} |beta_0(d,xi)|^4.
```

Averaging in `d` would use:

```text
M_minor^0(D;R,eta)
  =
  D^(-1) sum_{D<|d|<=2D}
    sum_{xi in Minor_0(R,eta)}
      |beta_0(d,xi)|^4.
```

But `M_minor^0(D;R,eta)=o_W(1)` is precisely the minor-arc fourth-moment
endpoint strength represented by `NarrowMinorArc_3^B` inside the local model.
Using it to prove the row side package would be circular unless it is supplied
by an independent theorem outside the target route.

Thus:

```text
EndpointFourthMomentRowRoute_302:
  FALSE / BLOCKED as a proof route.
```

The inequality is valid. The route is not valid as a proof of the row barrier
because it assumes endpoint-strength fourth-moment control.

### D. What a nontrivial row tail gain would need

Define:

```text
RowTailGainTarget_302(q):
  find same-family tail bounds T_j(u)<=Psi_j(u)
  with a gain over Markov from E2_minor^0 alone,
  strong enough that the associated U_j satisfy RowMomentGainTarget_300(q).
```

The gain must be uniform over:

```text
N,w,b,D,R,eta,
both signs of d,
the declared lambda grid,
the declared W-residue convention,
and the fixed N->infinity then w->infinity order.
```

It also must not use:

```text
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
or selector transfer.
```

Classification:

```text
RowTailGainTarget_302(q):
  OPEN.
```

### E. The q=2 concrete subtarget

The smallest concrete high-moment row is the square row:

```text
RowSquareMomentTarget_302:
  prove for q=2 that

  sum_j lambda_j^2 (L_j C_D)^(1/2)
    ShiftMomentP0_284(2;lambda_j)^(1/2)
  =
  o_W(1)
```

inside `P_minor^0`, without endpoint-strength inputs.

Equivalently, one needs same-family bounds for:

```text
D^(-1) sum_{D<|d|<=2D} E_{d,0}(lambda_j)^2
```

stronger than the first-energy Markov/pointwise interpolation route.

Classification:

```text
RowSquareMomentTarget_302:
  OPEN.
```

This target is smaller than the full threshold package. It is still not
proved.

### F. Self-challenge

The tempting overstatement would be:

```text
Since E_{d,0}(lambda_j) is a large-spectrum row, the fourth-moment endpoint
should control it.
```

That is true only as a conditional observation. It cannot be used in a module
whose purpose is to prove a side row feeding that endpoint.

The second tempting overstatement is:

```text
Markov gives a row distribution theorem.
```

It gives a distribution inequality, but it is exactly the first-energy
inequality already used in Module 300. It does not give the required
lambda-summed smallness.

## 6. Edge cases

If:

```text
A_N^0=0
```

or:

```text
Lambda_0=emptyset,
```

then the row sums are empty for that tuple. This is degenerate and does not
prove uniform row-moment gain.

The layer-cake formula uses the `1/D` normalization, so:

```text
T_j(u)<=C_D
```

rather than `T_j(u)<=1` under the two-sided shell convention.

The current Markov bound is valid but too weak. It should not be discarded;
it should be recorded as the baseline that future row-distribution estimates
must beat.

The fourth-moment large-spectrum inequality is valid but circular as a proof
route unless the fourth-moment estimate is independently supplied.

Nothing here transfers from `P_minor^0` to the actual sharp moving selector.

## 7. Project-map location

The row side of the threshold branch now reads:

```text
Module 300:
  energy-only row-barrier route blocked.

Module 302:
  first-energy Markov distribution route blocked;
  endpoint fourth-moment route blocked as circular;
  row-tail and row-square targets remain open.
```

The live local target is:

```text
RowSquareMomentTarget_302
  or a stronger RowTailGainTarget_302(q)
  => RowMomentGainTarget_300(q)
  => possible RowBarrierP0_284(q)=o_W(1).
```

This remains only the row side of the threshold package. The column side,
degeneracy rows, adaptive shell rows, and transfer rows remain separate.

## 8. What remains open

Still open:

```text
RowTailGainTarget_302(q),
RowSquareMomentTarget_302,
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ShiftRemovalBudget_284(q)=o_W(1),
FreqRemovalBudget_284(r)=o_W(1),
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `LayerCakeRowCriterion_302(q)` as an estimate. It is an exact
criterion.

Do not cite `CurrentMarkovRowDistribution_302(q)` as row-barrier smallness.
It reproduces the blocked Module 300 ceiling.

Do not prove a row side package by assuming:

```text
M_minor^0(D;R,eta)=o_W(1),
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
or the original selected-average problem.
```

Do not move this `P_minor^0` row distribution audit to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next target should expand the concrete q=2 row-square object:

```text
Module 303:
  RowSquareMomentExpansion_303(P_minor^0).
```

That module should expand:

```text
D^(-1) sum_{D<|d|<=2D} E_{d,0}(lambda_j)^2
```

into its same-shift frequency-pair form, identify which parts are pure
bookkeeping and which would require new phase or large-spectrum input, and
avoid using the minor-arc fourth-moment endpoint as an assumption.
