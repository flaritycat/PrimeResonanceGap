# Module 224: Fixed boundary/prefix selector-transfer test row

## 1. Precise theorem / claim being advanced

This module fixes the first local row promised by Module 223.

The chosen row is:

```text
Pi = P_M,
edge = cyc_s0 -> int_s0,
selector class = s0 held fixed,
dyadic range = D0<|d|<=2D0,
limit order = w fixed, N -> infinity, then w -> infinity.
```

Here `cyc_s0 -> int_s0` means that the same residual object and the same
selector class `s0` are compared between the finite cyclic projected
major-arc model and the interval projected major-arc model. No selector class
is changed.

Define the fixed test row:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0).
```

Conditional claim:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0)=o_W(1)
  + NormRow_224^P(s0,D0;N,w,rho0)=o_W(1)
    => ActualProjCube_{cyc,s0}^P
       and ActualProjCube_{int,s0}^P
       agree up to o_W(1)
       on the fixed dyadic shell D0<|d|<=2D0.
```

This is a local boundary/prefix transfer criterion, not a proof that the row
is small. Its purpose is to pin the exact support and normalization before
Module 225 expands the row into the residual fourth-moment cube.

## 2. Status label

`CONDITIONAL`

The implication from the row estimate to the fixed cyclic-to-interval transfer
is a triangle-inequality reduction. The smallness of
`BdPrefRow_224^P` and `NormRow_224^P` is not proved here.

## 3. Definitions and variables

Fix one W-tricked selector or model class:

```text
s0 in {model, W, sm, fr}
```

This is part of the definition of the clean first test. The row fixes one of
these classes on both sides of the edge. This module does not use:

```text
fr -> mv,
bern -> sm,
fs -> bern,
sm -> fr.
```

For this fixed class, write:

```text
nu_s0,
f_s0=nu_s0-1,
B_{d,s0}(n)=f_s0(n+d)conj(f_s0(n)).
```

The projected major-arc operator is fixed once and for all in this row:

```text
P_M,
widehat{P_M F}(xi)=m_M(xi)widehat{F}(xi),
m_M(0)=0,
supp(m_M) subset Major(R0,eta0)\{0}.
```

Let:

```text
K_M(t)=sum_xi m_M(xi)e(xi t),
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The single parameter tuple is:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0).
```

It is fixed inside the admissible family `P_adm(N,w)`. The dyadic shell is:

```text
D0<|d|<=2D0,
D0 in D_range(N,Hcal).
```

No conclusion is asserted uniformly over every dyadic shell in this module.
That wider range belongs to later modules.

For:

```text
t=(t0,t1,t2,t3),
```

define the four projected `B_d` slots:

```text
x00=n-t0,
x10=n+h-t1,
x01=n+k-t2,
x11=n+h+k-t3.
```

The residual product is:

```text
ProductB_{d,s0}(n,h,k;t)
  = B_{d,s0}(x00)
    conj(B_{d,s0}(x10))
    conj(B_{d,s0}(x01))
    B_{d,s0}(x11).
```

After forming `B_d`, the eight vertices are:

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

Let:

```text
V(d,n,h,k;t)={v_{ab,e}: a,b,e in {0,1}}.
```

Choose one prefix/boundary scale `L_N=L_N(w,rho0)` with:

```text
L_N=o(N)
```

in the fixed-`w`, `N -> infinity` limit. The interval core is:

```text
I_N^core(L_N)={m in {1,...,N}: L_N < m <= N-L_N}.
```

The exact support of the test row, after the residual product has been
formed, is:

```text
Core_224(d,n,h,k;t)
  = prod_{v in V(d,n,h,k;t)} 1_{v in I_N^core(L_N)}
    prod_{i=0}^3 1_{|t_i|<=T0},

BdPref_224(d,n,h,k;t)
  = 1-Core_224(d,n,h,k;t).
```

Thus the row sees a summand if at least one of the eight residual vertices is
outside the stable interval core, or if the fixed projected kernel truncation
is violated.

The actual boundary/prefix row is:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_{d,s0}(n,h,k;t)|
        BdPref_224(d,n,h,k;t).
```

The normalization row is:

```text
NormRow_224^P(s0,D0;N,w,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      |Vol_cyc(rho0)-Vol_int(d,rho0)| Lambda_{d,s0},
```

where `Vol_cyc` and `Vol_int` are the cyclic and interval normalizing factors
for this exact row, and `Lambda_{d,s0}` is any declared envelope satisfying:

```text
|ActualProjCube_{d,cyc,s0}^P|
  + |ActualProjCube_{d,int,s0}^P|
  <= Lambda_{d,s0}
```

in the row's normalization. If the cyclic and interval averages are normalized
identically on the same core, `NormRow_224^P` is declared to be zero. The
choice must be recorded before the row is estimated.

The W-admissible target for this fixed row is:

```text
lim_{w->infinity} limsup_{N->infinity}
  BdPrefRow_224^P(s0,D0;N,w,rho0)=0,

lim_{w->infinity} limsup_{N->infinity}
  NormRow_224^P(s0,D0;N,w,rho0)=0.
```

## 4. Assumptions

This module assumes only the definitions above and the local bookkeeping
already established in Modules 206, 210, 213, 216, 218, and 222.

The following conventions are fixed and may not vary inside the row:

```text
Pi=P_M,
m_M(0)=0,
same R0 and eta0 on both sides,
same selector class s0 on both sides,
same dyadic D0 shell on both sides,
same W-tricked residue convention on both sides,
same kernel K_M and truncation T0 on both sides,
fixed-w then N -> infinity then w -> infinity.
```

No moving threshold is present, because `s0` is not changed to `mv`.

No Bernoulli or finite-stage extraction is present, because the edge is
`cyc_s0 -> int_s0`, not a probabilistic or construction-space edge.

No major/minor partition change is present, because `P_M` is the only
projection used and it is identical on both sides.

No endpoint estimate is assumed.

## 5. Proof / disproof / reduction

For each fixed `d`, write:

```text
ActualProjCube_{d,cyc,s0}^P
  = E_{n,h,k,t}^{cyc} W_M(t) ProductB_{d,s0}(n,h,k;t),

ActualProjCube_{d,int,s0}^P
  = E_{n,h,k,t}^{int} W_M(t) ProductB_{d,s0}(n,h,k;t),
```

with the same selector class, the same projection, and the same four-slot
kernel. The only declared difference is the cyclic versus interval domain and
normalization.

On the core `Core_224=1`, the cyclic representatives and the interval
representatives agree by construction. Therefore the pointwise difference
between the two summation conventions is supported on:

```text
BdPref_224=1.
```

After taking absolute values and averaging over the fixed dyadic shell:

```text
(1/D0) sum_{D0<|d|<=2D0}
  |ActualProjCube_{d,cyc,s0}^P
    - ActualProjCube_{d,int,s0}^P|

  <= BdPrefRow_224^P(s0,D0;N,w,rho0)
     + NormRow_224^P(s0,D0;N,w,rho0).
```

Thus:

```text
BdPrefRow_224^P=o_W(1)
and
NormRow_224^P=o_W(1)
```

imply the fixed cyclic-to-interval actual-cube transfer:

```text
(1/D0) sum_{D0<|d|<=2D0}
  |ActualProjCube_{d,cyc,s0}^P
    - ActualProjCube_{d,int,s0}^P|
  = o_W(1).
```

This is the whole reduction. It does not estimate the row.

The self-check from Modules 222 and 223 is important: this row is called
local only because the support is explicitly tied to the eight residual
vertices after `B_d` has been formed. A boundary set defined only for one
prime or one `f` factor would not be the same row.

## 6. Edge cases

- If `D0`, `H0`, `K0`, or `T0` is not `o(N)`, the core may have non-negligible
  loss.
- Negative shifts `d` can move the `v_{ab,1}` vertices leftward; they are
  included in the same support condition.
- If `m_M(0) != 0`, zero-frequency leakage is reintroduced and the row is not
  the projected nonzero major row.
- If a smoothed projection is replaced by a sharp projection inside the
  argument, this module no longer applies; that is a projection-boundary row.
- If `s0=fr`, this module still does not touch `fr -> mv`; the moving window
  remains open.
- This module intentionally excludes `s0=bern` and `s0=fs`. An analogous row
  in those classes would still not perform deterministic extraction.
- W-residue failures near the boundary must be accounted for consistently;
  they are not absorbed into `Omega_w^proj`.
- Prime-power artifacts are not removed by this boundary row.
- A small first-moment boundary count is insufficient unless it lifts to the
  displayed residual fourth-moment row.

## 7. Where it fits in the project map

This is the first Phase E module:

```text
Module 222
  -> consolidate selector-transfer graph
Module 223
  -> require one fixed boundary/prefix test row
Module 224
  -> fix the projected-major cyclic-to-interval row
Module 225
  -> expand this row into its residual fourth-moment cube and list envelopes
Module 226
  -> decide whether the row is plausibly local, conditional, or endpoint-strength.
```

The row lives in the consolidated graph position:

```text
Boundary / prefix support rows
  feeding major projected transfer.
```

It is intentionally smaller than:

```text
SharpSelectorTransfer_3,
MajorSelectorTransfer_3^P,
MoveLayerCube_3^Pi,
DetExtract_3^Pi,
FullNonzeroSelectorTransfer_3.
```

## 8. What remains open

This module does not prove:

- `BdPrefRow_224^P=o_W(1)`;
- `NormRow_224^P=o_W(1)` unless a later convention makes it identically zero;
- a residual fourth-moment envelope for the boundary/prefix support;
- model-side boundary synchronization;
- W-residue boundary compatibility;
- prime-power removal near the boundary;
- cyclic-to-interval transfer for every admissible `rho`;
- transfer across dyadic shells other than the fixed shell `D0`;
- any moving-threshold, smoothed-to-sharp, Bernoulli, finite-stage, or actual
  sharp moving-selector transfer;
- `CycIntTransfer_3^major(P_adm)` in full;
- `MajorSelectorTransfer_3^P`;
- `MajorMinorSelCompat_3(P_adm)`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite this module as proving a boundary estimate.
- Do not use this row to transfer from frozen to moving selectors.
- Do not use this row to perform Bernoulli or finite-stage deterministic
  extraction.
- Do not change `P_M`, `R0`, `eta0`, or the major/minor partition while using
  this row.
- Do not replace the eight-vertex support by a one-point boundary condition.
- Do not treat codimension of the boundary as a fourth-moment estimate.
- Do not use ordinary pair-BDH, first-moment Hardy-Littlewood, or first-moment
  boundary counts as substitutes for `BdPrefRow_224^P=o_W(1)`.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
