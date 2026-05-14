# Module 210: Cyclic-to-interval boundary transfer for the projected major-arc model

## 1. Precise theorem / claim being advanced

This module states the boundary-transfer package needed to pass from the
finite cyclic projected major-arc model to the actual interval model.

Define:

```text
CycIntTransfer_3^major(P_adm).
```

Conditional claim:

```text
WProjectedLocalMatch_3^major,cyc(P_adm)
  + CycIntTransfer_3^major(P_adm)
    => WProjectedLocalMatch_3^major,int(P_adm).
```

The package tracks wraparound, vertices moved outside the interval by
`d,h,k,t`, kernel truncation, sharp versus smoothed cutoffs, zero-mode
preservation, W-residue compatibility near the boundary, and uniformity over
the admissible parameter family.

This module does not prove the boundary estimates. It only states the exact
transfer contract needed before a cyclic Fourier identity can be used in the
interval major-arc branch.

## 2. Status label

`CONDITIONAL`

The implication follows by triangle inequalities once all named boundary
errors are W-admissible. The actual smallness of those errors is open.

## 3. Definitions and variables

Let:

```text
I_N={1,...,N}
```

or the project-specific interval after W-tricking and residue selection. Let
`G_N` be the cyclic model used for Fourier projection.

As before:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)).
```

For:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
```

let the projected vertices be:

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
W_M(t)=K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The cyclic actual projected cube is:

```text
ActualProjCube_{d,cyc}^P
  = E_{n in G_N,h,k,t} W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3),
```

with all vertices interpreted cyclically.

The interval actual projected cube is:

```text
ActualProjCube_{d,int}^P
  = E_{n in I_N,h,k,t} W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3),
```

where a summand is included only with the interval cutoff convention chosen in
`rho`.

The cyclic model cube is:

```text
ModelProjCube_{d,cyc}^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

The interval model cube is the same local model with the interval cutoff or
core restriction inserted:

```text
ModelProjCube_{d,int}^P
  = E_{h,k,t} W_M(t)
      Cut_N(d,h,k;t) Omega_w^proj(d,h,k;t),
```

where `Cut_N` is either the exact interval volume factor, a smooth cutoff, or
the indicator that all projected vertices lie in the permitted interval. The
choice must match the actual interval cube.

Define:

```text
MatchErr_{cyc}^P
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_{d,cyc}^P - ModelProjCube_{d,cyc}^P|,

MatchErr_{int}^P
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_{d,int}^P - ModelProjCube_{d,int}^P|.
```

## 4. Boundary and transfer errors

`CycIntTransfer_3^major(P_adm)` consists of the following W-admissible errors.

### A. Core and boundary set

Define the core indicator:

```text
Core_N(d,h,k;t,n)=1
```

if every projected vertex:

```text
n + a h + b k + e d - t_{ab}
```

lies in the valid interval and all cutoff conditions in `rho` hold. Let:

```text
Bd_N=1-Core_N.
```

The actual boundary error is:

```text
ActBd_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{n,h,k,t} |W_M(t)|
        |B_d(n-t0)|
        |B_d(n+h-t1)|
        |B_d(n+k-t2)|
        |B_d(n+h+k-t3)|
        Bd_N(d,h,k;t,n).
```

The package requires:

```text
ActBd_major(N,w;rho)=o_W(1)
```

uniformly over `rho in P_adm(N,w)`.

### B. Model boundary synchronization

The model boundary error is:

```text
ModelBd_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t)
          (1-Cut_N(d,h,k;t)) Omega_w^proj(d,h,k;t) |.
```

The package requires:

```text
ModelBd_major(N,w;rho)=o_W(1).
```

If the interval model uses a lower-dimensional boundary local model instead
of discarding the boundary, then `ModelBd_major` is replaced by the matching
error for that boundary model. The same convention must be used on the actual
and model sides.

### C. Cyclic wraparound error

Let `Wrap_N` be the event that a cyclic representative of some projected
vertex differs from its interval representative. Define:

```text
WrapBd_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)| 1_{Wrap_N}.
```

Here:

```text
ProductB_d
  = B_d(n-t0)
    conj(B_d(n+h-t1))
    conj(B_d(n+k-t2))
    B_d(n+h+k-t3).
```

Require:

```text
WrapBd_major(N,w;rho)=o_W(1).
```

This is separate from ordinary interval endpoint loss because cyclic
wraparound can create artificial coincidences.

### D. Kernel truncation and long tails

For a truncation parameter `T`, define:

```text
TailBd_major(N,w;rho,T)
  = (1/D) sum_{D<|d|<=2D}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)|
        1_{max_i |t_i|>T}.
```

Require:

```text
TailBd_major(N,w;rho,T)=o_W(1),
```

and the same truncation must be reflected in `ModelProjCube_{d,int}^P`.

### E. Cutoff mismatch

If the actual interval cube uses a sharp cutoff and the model uses a smooth
cutoff, or conversely, define:

```text
CutoffBd_major(N,w;rho)
```

as the absolute projected-cube difference between the two cutoff conventions.
The package requires:

```text
CutoffBd_major(N,w;rho)=o_W(1).
```

Changing the cutoff changes both the physical average and the local model.

### F. Normalization error

If the interval core has volume different from the cyclic normalization, define:

```text
NormBd_major(N,w;rho)
```

as the resulting difference in the averaged actual and model cubes. Require:

```text
NormBd_major(N,w;rho)=o_W(1).
```

This includes endpoint losses from the dyadic `d` range and the `h,k`
averaging windows.

### G. Zero-mode leakage

In the cyclic model:

```text
m_M(0)=0
```

implies:

```text
P_M B_d=P_M B_d^circ.
```

After interval truncation or kernel truncation, constants can leak back into
the projected cube unless the truncated kernel has negligible total mass. Let:

```text
ZeroLeak_major(N,w;rho)
```

denote the contribution caused by applying the transferred projection to the
constant coefficient `c_d=E_n B_d(n)`. Require:

```text
ZeroLeak_major(N,w;rho)=o_W(1).
```

Equivalently, one may prove a kernel condition such as:

```text
sum_{|t|<=T} K_M(t)=o_W(1)
```

in the normalization used by the interval projection, together with a
compatible bound for the `c_d` contribution.

### H. W-residue boundary compatibility

Boundary truncation must not destroy the W-tricked residue class. Define:

```text
WResBd_major(N,w;rho)
```

for residue-class failures created by interval endpoints, kernel shifts, or
cutoff changes. Require:

```text
WResBd_major(N,w;rho)=o_W(1).
```

Prime powers remain outside this boundary package and are handled in Module
211.

## 5. W-admissible transfer package

The full package is:

```text
CycIntTransfer_3^major(P_adm):
  ActBd_major
  + ModelBd_major
  + WrapBd_major
  + TailBd_major
  + CutoffBd_major
  + NormBd_major
  + ZeroLeak_major
  + WResBd_major
  = o_W(1)
```

where the displayed sum means that each term is W-admissible uniformly:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} Err(N,w;rho)=0.
```

The fixed-`w`, `N -> infinity`, then `w -> infinity` order is mandatory.

## 6. Conditional proof / reduction

For each `d`, write:

```text
Actual_{int}-Model_{int}
  = (Actual_{int}-Actual_{cyc})
    + (Actual_{cyc}-Model_{cyc})
    + (Model_{cyc}-Model_{int}).
```

Taking absolute values and averaging over `D<|d|<=2D` gives:

```text
MatchErr_{int}^P
  <= MatchErr_{cyc}^P
     + ActCycIntErr_major
     + ModelCycIntErr_major.
```

The actual cyclic-to-interval error is bounded by:

```text
ActCycIntErr_major
  <= ActBd_major
     + WrapBd_major
     + TailBd_major
     + CutoffBd_major
     + NormBd_major
     + ZeroLeak_major
     + WResBd_major.
```

The model cyclic-to-interval error is bounded by:

```text
ModelCycIntErr_major
  <= ModelBd_major
     + TailBd_major
     + CutoffBd_major
     + NormBd_major
     + WResBd_major.
```

Therefore, if:

```text
MatchErr_{cyc}^P=o_W(1)
```

and `CycIntTransfer_3^major(P_adm)` holds, then:

```text
MatchErr_{int}^P=o_W(1).
```

This is the stated conditional transfer:

```text
WProjectedLocalMatch_3^major,cyc
  + CycIntTransfer_3^major
    => WProjectedLocalMatch_3^major,int.
```

No boundary term is estimated in this proof.

## 7. Edge cases

- If `D`, `H`, `K`, or `T` is comparable to `N`, the core interval may be too
  small for boundary loss to be negligible.
- Negative shifts `d` must use the same interval convention as positive
  shifts.
- Kernel tails can move otherwise valid vertices outside the interval.
- A sharp kernel cutoff may have poor absolute mass; smoothing changes the
  model and must be recorded.
- Removing boundary regions only from the actual cube breaks model matching.
- Removing boundary regions only from the model cube also breaks matching.
- Interval truncation can reintroduce zero-frequency leakage even when
  `m_M(0)=0` cyclically.
- W-residue compatibility can fail near endpoints after kernel shifts.
- Structural collision strata can intersect boundary strata; the accounting
  must not count them in two incompatible ways.
- Prime-power artifacts are not solved by interval boundary control.

## 8. Where it fits in the project map

The Phase C chain now has:

```text
Module 206
  -> exact projected major-arc target
Module 207
  -> exact projected local singular factors
Module 208
  -> projected collision stratification
Module 209
  -> W-admissible projected local-model theorem
Module 210
  -> cyclic-to-interval boundary transfer.
```

This module supplies one named side package for:

```text
WProjectedLocalMatch_3^major(P_adm).
```

The next scheduled module is the projected major-arc prime-power and
small-prime removal audit.

## 9. What remains open

This module does not prove:

- `CycIntTransfer_3^major(P_adm)`;
- smallness of `ActBd_major`;
- smallness of `ModelBd_major`;
- wraparound removal for the actual projected cube;
- kernel-tail control for the chosen projection;
- cutoff mismatch control;
- normalization transfer;
- zero-mode leakage control;
- W-residue boundary compatibility;
- prime-power removal;
- selector transfer to the actual sharp moving selector;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not use a cyclic Fourier identity as an interval estimate without
  `CycIntTransfer_3^major`.
- Do not hide wraparound, boundary, kernel-tail, cutoff, normalization,
  zero-mode, or W-residue errors in a generic `o(1)`.
- Do not remove a boundary region from only one side of the actual/model
  comparison.
- Do not assume a truncated interval projection still has exact zero-mode
  cancellation.
- Do not treat codimension boundary language as a projected fourth-moment
  estimate.
- Do not transfer this cyclic or interval model to the actual sharp moving
  selector without the selector-transfer package.
- Do not replace the projected residual model by the full eight-form model or
  by the unprojected residual model.
- Do not replace the rectangle local model by a pointwise square of the pair
  local model.
- Do not claim projected local-model matching, projected major-arc
  cancellation, the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
