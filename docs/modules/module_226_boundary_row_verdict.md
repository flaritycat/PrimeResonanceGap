# Module 226: Boundary/prefix row verdict

## 1. Precise theorem / claim being advanced

This module classifies the fixed boundary/prefix row from Modules 224-225.

The row is:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
s0 in {model, W, sm, fr},
D0<|d|<=2D0.
```

Verdict:

```text
BdPrefRow_224^P is a conditional local boundary row
only under the strict boundary-support package LocalBdPkg_226.
```

More explicitly:

```text
LocalBdPkg_226(s0,D0,rho0)
  => BdPrefRow_224^P(s0,D0;N,w,rho0)=o_W(1),
```

and therefore, by Module 224,

```text
ActualProjCube_{cyc,s0}^P
  and
ActualProjCube_{int,s0}^P
```

agree on the fixed dyadic shell up to `o_W(1)`.

This row is not proved. It is not accepted as a free side error. It is not
blocked as endpoint-strength in the narrow fixed-row formulation, but it
becomes mixed or endpoint-strength if any of the support-saving requirements
below are replaced by an unlocalized residual fourth-moment estimate.

## 2. Status label

`CONDITIONAL`

The classification is conditional on `LocalBdPkg_226`. The package remains
open.

## 3. Definitions and variables

Use the fixed data from Modules 224 and 225:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
D0<|d|<=2D0,
w fixed, N -> infinity, then w -> infinity.
```

The residual product is:

```text
f=f_s0=nu_s0-1,
B_d(n)=f(n+d)conj(f(n)),
ProductB_d(n,h,k;t)
  = B_d(n-t0)
    conj(B_d(n+h-t1))
    conj(B_d(n+k-t2))
    B_d(n+h+k-t3).
```

The eight vertex labels are:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

The vertices are:

```text
v_{00,0}=n-t0,
v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,
v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,
v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,
v_{11,1}=n+h+k-t3+d.
```

For a boundary scale `L_N=o(N)`:

```text
I_N^core(L_N)={m in {1,...,N}: L_N<m<=N-L_N},

Bd_lambda(d,n,h,k;t)
  = 1_{v_lambda notin I_N^core(L_N)}.
```

The kernel-tail event is:

```text
TailT_224(t)=1_{max_i |t_i|>T0}.
```

The boundary/prefix support satisfies:

```text
BdPref_224
  <= TailT_224 + sum_{lambda in Lambda_8} Bd_lambda.
```

The Module 225 tuple objects are:

```text
BTuple_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        E_n Bd_lambda(d,n,h,k;t)
          prod_{sigma in S} mu_s0(v_sigma),

BdModel_225(S,lambda)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        BdVol_lambda(d,h,k;t)
        |Theta_{w,S}^proj(d,h,k;t)|.
```

Here `mu_s0` is a nonnegative majorant for the fixed class `s0`, and
`Theta_{w,S}^proj` is the exact labeled projected local factor from Module
207.

## 4. Assumptions

Define:

```text
LocalBdPkg_226(s0,D0,rho0)
```

to be the following finite list of W-admissible requirements.

### A. Fixed-row discipline

No parameter or selector change is allowed inside the package:

```text
same P_M, R0, eta0,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same W-residue convention,
same interval cutoff convention,
same fixed-w then N -> infinity then w -> infinity limit order.
```

This excludes:

```text
fr -> mv,
sm -> fr,
bern -> sm,
fs -> bern,
major/minor partition transfer.
```

### B. Absolute majorant and kernel control

The package includes:

```text
AbsMajorant_225(s0),
KernelAbsTail_225(P_M,T0).
```

In particular:

```text
E_t |W_M(t)|=O_W(1),
TailCube_225(T0)=o_W(1).
```

If `E_t |W_M(t)|` grows, the later boundary saving must explicitly dominate
that growth.

### C. Genuine boundary support saving

There must be a saving parameter:

```text
delta_N(w,rho0) -> 0
```

in the fixed-`w`, `N -> infinity` limit such that every boundary local model
obeys a bound of the schematic form:

```text
BdModel_225(S,lambda)
  <= C_{S,lambda}(w,rho0) delta_N(w,rho0) + o_W(1),
```

and:

```text
lim_{w->infinity} limsup_{N->infinity}
  C_{S,lambda}(w,rho0) delta_N(w,rho0)=0.
```

The constants may depend on the fixed row and on `w`, but they must be
compatible with the W-admissible limit order.

### D. Boundary-marked tuple matching

For all:

```text
S subset Lambda_8,
lambda in Lambda_8,
```

the package includes:

```text
BoundaryTupleHL_225(S,lambda):
  |BTuple_225(S,lambda)-BdModel_225(S,lambda)|=o_W(1).
```

This is the weighted boundary-marked tuple input. It cannot be replaced by a
first-moment count of boundary vertices.

### E. Boundary model mass

For all `S` and `lambda`:

```text
BoundaryModelMass_225(S,lambda):
  BdModel_225(S,lambda)=o_W(1).
```

This is implied by the genuine support saving in C when the local factors and
kernel absolute mass are uniformly controlled.

### F. Boundary W-residue, prime-power, zero-mode, and normalization rows

The package includes:

```text
WPPBoundary_225=o_W(1),
NormRow_224^P=o_W(1).
```

If centered products or truncated projections are used, the corresponding
zero-mode leakage term must be included in `NormRow_224^P` or explicitly
added as:

```text
ZeroBd_226=o_W(1).
```

## 5. Proof / disproof / reduction

Module 225 recorded the deterministic reduction:

```text
AbsMajorant_225
  + KernelAbsTail_225
  + BoundaryTupleHL_225(S,lambda)
  + BoundaryModelMass_225(S,lambda)
  + WPPBoundary_225
  + NormRow_224^P=o_W(1)

    => BdPrefRow_224^P=o_W(1).
```

`LocalBdPkg_226` is precisely the strengthened version of those hypotheses
that requires actual boundary support saving in the model mass. Therefore:

```text
LocalBdPkg_226
  => BdPrefRow_224^P=o_W(1).
```

Module 224 then gives:

```text
(1/D0) sum_{D0<|d|<=2D0}
  |ActualProjCube_{d,cyc,s0}^P
    - ActualProjCube_{d,int,s0}^P|
  = o_W(1).
```

This establishes the conditional transfer for the fixed row.

### Why the row is classified as local under `LocalBdPkg_226`

The support is:

```text
TailT_224=1
```

or:

```text
Bd_lambda=1
```

for at least one of the eight residual vertices. Thus every surviving error
term is attached to a boundary, prefix, or kernel-tail set after `B_d` has
already been formed. The package asks for weighted tuple control on that
smaller support, not for the full nonzero residual fourth moment.

### Why the row is not proved

The project has not proved:

```text
BoundaryTupleHL_225(S,lambda),
BoundaryModelMass_225(S,lambda),
KernelAbsTail_225(P_M,T0),
WPPBoundary_225,
NormRow_224^P.
```

Therefore the row remains a conditional local package.

### When the row becomes mixed

The row should be reclassified as mixed if any proof route must also control:

```text
major/minor partition movement,
projection denominator drift,
moving threshold layers,
smoothed-to-sharp transition layers,
Bernoulli or finite-stage extraction,
prime-power or W-residue failures not supported on the boundary,
zero-mode leakage not localized to the interval truncation.
```

Those effects are not part of the fixed row and should not be smuggled into
the boundary notation.

### When the row becomes endpoint-strength

The row should be reclassified as endpoint-strength if the intended proof
replaces the boundary-marked tuple estimates by an unlocalized bound such as:

```text
(1/D0) sum_{D0<|d|<=2D0}
  ||P_M B_{d,s0}||_{U^2}^4=o_W(1)
```

or by a core selector row:

```text
CoreSel_major^P=o_W(1).
```

Those are essentially the projected endpoint or selector-transfer target, not
a boundary transfer estimate.

## 6. Edge cases

- If `L_N/N` does not tend to zero, the row is not a small boundary row.
- If `L_N` tends to zero too quickly compared with weights and kernel mass,
  `BoundaryModelMass_225` may fail.
- If `P_M` has large absolute kernel mass, locality is not enough; the
  boundary saving must beat the kernel growth.
- If structural collision strata lie entirely inside the boundary, they need
  their correct labeled local factors; generic collision-free factors are not
  acceptable.
- If W-residue failures near endpoints are not separated, the row becomes
  mixed with W-transfer.
- If prime powers occur in the fixed class, support sparsity is not enough;
  the boundary-marked projected cube contribution is required.
- If the selector class is changed, this is no longer the Module 224 row.
- If a centered product is used after interval truncation, zero-mode leakage
  must be included.
- Negative shifts remain in the same shell and must satisfy the same boundary
  support and normalization conventions.

## 7. Where it fits in the project map

The Phase E local-row test now has a verdict:

```text
Module 224
  -> fixed BdPrefRow_224^P
Module 225
  -> expanded the row into boundary-marked tuple envelopes
Module 226
  -> classifies the row as conditional local under LocalBdPkg_226,
     mixed if extra transfer rows enter,
     endpoint-strength if unlocalized residual fourth-moment control is used.
```

This completes the local-row test required before endpoint-equivalence
auditing. The next planned step is:

```text
Module 227: endpoint-equivalence arrow inventory.
```

That audit should carry this verdict forward as:

```text
Boundary / prefix transfer:
  conditional local only under LocalBdPkg_226.
```

## 8. What remains open

This module does not prove:

- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
- `BoundaryTupleHL_225(S,lambda)`;
- `BoundaryModelMass_225(S,lambda)`;
- `KernelAbsTail_225(P_M,T0)`;
- `WPPBoundary_225`;
- `NormRow_224^P`;
- `ZeroBd_226` when needed;
- `CycIntTransfer_3^major(P_adm)` in full;
- selector transfer to the actual sharp moving selector;
- smoothed-to-sharp transfer;
- frozen-to-moving transfer;
- Bernoulli or finite-stage deterministic extraction;
- `MajorMinorSelCompat_3(P_adm)`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite the row as proved; it is conditional on `LocalBdPkg_226`.
- Do not call the row local unless the boundary support gives an actual
  weighted saving after the eight-vertex expansion.
- Do not replace `BoundaryTupleHL_225` by first-moment boundary counting.
- Do not use cancellation in `W_M` after taking `|W_M|`.
- Do not let moving-threshold, smoothed-to-sharp, Bernoulli, finite-stage,
  denominator, or major/minor partition transfer enter this fixed row.
- Do not prove the row by assuming the projected residual endpoint.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not transfer a fixed `s0` result to the actual sharp moving selector
  without the selector-transfer packages.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
