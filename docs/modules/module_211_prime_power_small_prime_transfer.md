# Module 211: Prime-power and small-prime transfer for the projected major-arc model

## 1. Precise theorem / claim being advanced

This module states the transfer package that removes prime-power and
small-prime artifacts from the projected major-arc model.

Define:

```text
PPSPTransfer_3^major(P_adm).
```

Conditional claim:

```text
WProjectedLocalMatch_3^major,prime(P_adm)
  + PPSPTransfer_3^major(P_adm)
    => WProjectedLocalMatch_3^major,actual-W(P_adm).
```

Here `prime` means the W-tricked prime-only model whose local factors are
encoded by `Omega_w^proj`, while `actual-W` means the W-tricked
von-Mangoldt-type weight before prime-power artifacts have been removed.

The module does not prove prime-power removal. It records the exact strength
needed: removal must hold in the projected residual fourth-moment norm, or in
the equivalent projected cube average. Ordinary first-moment negligibility of
prime powers is not enough for this endpoint.

## 2. Status label

`CONDITIONAL`

The implication is formal once the named transfer errors are
W-admissible. The actual W-admissible estimates are open.

## 3. Definitions and variables

Let:

```text
W=prod_{p<=w} p
```

and work in a fixed admissible residue class `b mod W`, with `(b,W)=1`, or in
the project-specific finite family of admissible W-residue classes.

Let the actual W-tricked von-Mangoldt-type weight be:

```text
nu=nu_W.
```

Let the prime-only part be:

```text
nu^pr=nu_W^pr,
```

obtained by retaining only values for which the represented integer is prime.
Define the prime-power remainder:

```text
pp=nu-nu^pr.
```

Then:

```text
f=nu-1,
f^pr=nu^pr-1,
f=f^pr+pp.
```

For a shift `d`, define:

```text
B_d(n)=f(n+d)conj(f(n)),
B_d^pr(n)=f^pr(n+d)conj(f^pr(n)),
Delta B_d(n)=B_d(n)-B_d^pr(n).
```

The exact bilinear error expansion is:

```text
Delta B_d(n)
  = pp(n+d)conj(f^pr(n))
    + f^pr(n+d)conj(pp(n))
    + pp(n+d)conj(pp(n)).
```

If the centering convention is used, set:

```text
c_d=E_n B_d(n),
c_d^pr=E_n B_d^pr(n),
B_d^circ=B_d-c_d,
(B_d^pr)^circ=B_d^pr-c_d^pr.
```

The projected major-arc operator is the same `P_M` used in Modules 206-210,
with multiplier `m_M` and zero-mode convention:

```text
m_M(0)=0
```

when the nonzero residual cube is being measured.

For:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
```

the projected cube uses the four shifted pair terms:

```text
B_d(n-t0),
conj(B_d(n+h-t1)),
conj(B_d(n+k-t2)),
B_d(n+h+k-t3),
```

with:

```text
W_M(t)=K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

Let:

```text
ActualProjCube_d^P[nu]
```

denote the projected major-arc cube formed with `B_d`, and let:

```text
ActualProjCube_d^P[nu^pr]
```

denote the same cube formed with `B_d^pr`, using the same interval, W-residue
class, cutoff, kernel, projection, and selector convention.

The prime-only local model is:

```text
ModelProjCube_d^P[prime]
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

The factor `Omega_w^proj` is the projected residual inclusion-exclusion
Euler model from Module 207. Its product is over primes `p>w`; primes `p<=w`
are not local Euler factors in this model, because they have been absorbed by
the W-trick and the admissible residue classes.

## 4. Assumptions: the transfer package

`PPSPTransfer_3^major(P_adm)` consists of the following W-admissible
conditions.

### A. Exact small-prime absorption

For every included projected vertex, the represented integer must remain in an
admissible W-residue class. In the single-residue notation this means that
all vertices are represented as:

```text
W x + b
```

with `(b,W)=1`, after the shifts and cutoffs used by `rho`.

If multiple residue classes are used, the tuple of residues must be
admissible at every prime `p<=w`. Define:

```text
SPResErr_major(N,w;rho)
```

as the projected cube contribution from vertices or tuple residues that fail
this small-prime compatibility. The package requires:

```text
SPResErr_major(N,w;rho)=o_W(1).
```

When the W-trick is exact and all shifted vertices keep admissible residues,
this term is identically zero. Otherwise it is an explicit error term; it is
not part of `Omega_w^proj`.

### B. Prime-power projected cube removal

Define the direct projected cube prime-power error:

```text
PPCubeErr_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_d^P[nu]
        - ActualProjCube_d^P[nu^pr]|.
```

The package requires:

```text
PPCubeErr_major(N,w;rho)=o_W(1).
```

Equivalently, one may prove a stronger projected norm estimate:

```text
PPNormErr_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      || P_M(Delta B_d) ||_{U^2}^4
  = o_W(1),
```

together with the projected envelope bounds needed to convert this norm error
into `PPCubeErr_major=o_W(1)`. Without those envelope bounds, the norm line is
only a proposed sufficient route, not the transfer package itself.

If the target cube is centered, the corresponding required norm is:

```text
(1/D) sum_{D<|d|<=2D}
  || P_M(B_d^circ-(B_d^pr)^circ) ||_{U^2}^4
  = o_W(1).
```

The zero-mode part:

```text
c_d-c_d^pr=E_n Delta B_d(n)
```

must be tracked separately if `P_M` does not annihilate constants after
interval or kernel truncation.

### C. Prime-power support and weight envelope

Let:

```text
PPSet(N,w)= { n : Wn+b=q^a for some prime q and a>=2 }
```

or the corresponding residue-family version. The package may be proved from
a stronger support-envelope condition such as:

```text
(1/D) sum_{D<|d|<=2D}
  E_{n,h,k,t} |W_M(t)| |ProductB_d^{at least one pp}(n,h,k;t)|
  = o_W(1).
```

Here `ProductB_d^{at least one pp}` means the full four-factor projected cube
expansion after replacing at least one of the eight underlying `f`-vertices by
`pp`.

This condition is stronger than a first-moment estimate for `pp`, because the
other vertices still carry W-tricked prime weights and the projection kernel.

### D. Model-side prime-power exclusion

The model used in Modules 206-210 is the prime-only local model:

```text
Omega_w^proj.
```

If a proposed model includes a prime-power correction, write:

```text
Omega_{w,actual}^proj
  = Omega_w^proj + Omega_{w,pp}^proj.
```

Then the model-side prime-power error is:

```text
PPModelErr_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t) Omega_{w,pp}^proj(d,h,k;t) |.
```

The package requires:

```text
PPModelErr_major(N,w;rho)=o_W(1).
```

The default convention is `Omega_{w,pp}^proj=0`; in that convention the whole
prime-power burden is on `PPCubeErr_major`.

### E. Boundary and W-residue interaction

Prime powers can intersect the boundary, kernel tail, or W-residue failure
sets from Module 210. Define:

```text
PPBdErr_major(N,w;rho)
```

as the portion of the projected cube in which at least one `pp` vertex also
lies in a boundary, wraparound, kernel-tail, cutoff-mismatch, or W-residue
failure region.

The package requires:

```text
PPBdErr_major(N,w;rho)=o_W(1).
```

This term prevents double counting between:

```text
CycIntTransfer_3^major(P_adm)
```

and:

```text
PPSPTransfer_3^major(P_adm).
```

One may instead impose a disjoint accounting convention, but the convention
must be stated before the estimate is used.

### F. Uniform W-admissibility

Every term above must satisfy:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} Err(N,w;rho)=0.
```

The order:

```text
N -> infinity first, then w -> infinity
```

is mandatory. No estimate may choose `w` depending on `N` after the
`N -> infinity` limit has been taken, except through a separately named
W-growth theorem already present in the project.

The full transfer package is:

```text
PPSPTransfer_3^major(P_adm):
  SPResErr_major
  + PPCubeErr_major
  + PPModelErr_major
  + PPBdErr_major
  = o_W(1).
```

The displayed sum means that each component is W-admissible uniformly over
`P_adm`.

## 5. Proof / reduction

Assume:

```text
WProjectedLocalMatch_3^major,prime(P_adm).
```

That is:

```text
(1/D) sum_{D<|d|<=2D}
  |ActualProjCube_d^P[nu^pr]
    - ModelProjCube_d^P[prime]|
  = o_W(1),
```

with the same projected vertices, kernel, cutoff, interval convention, and
selector class.

For each `d`, insert and subtract the prime-only cube:

```text
ActualProjCube_d^P[nu] - ModelProjCube_d^P[prime]
  = (ActualProjCube_d^P[nu]
      - ActualProjCube_d^P[nu^pr])
    + (ActualProjCube_d^P[nu^pr]
      - ModelProjCube_d^P[prime]).
```

If the model convention includes a prime-power correction, insert and subtract
that correction as well:

```text
ModelProjCube_d^P[actual]
  = ModelProjCube_d^P[prime] + ModelProjCube_d^P[pp].
```

After absolute values and averaging over `D<|d|<=2D`, the error is bounded by:

```text
PPCubeErr_major
  + MatchErr_major^prime
  + PPModelErr_major
  + SPResErr_major
  + PPBdErr_major.
```

The W-admissibility of these terms gives:

```text
WProjectedLocalMatch_3^major,actual-W(P_adm).
```

This is only a transfer statement. It does not estimate `PPCubeErr_major` or
prove the prime-only matching theorem.

## 6. Why first moment is insufficient

A typical first-moment statement has the shape:

```text
E_n |pp(n)| = o(1).
```

The projected residual endpoint asks for a fourth-moment cube built from:

```text
B_d(n)=f(n+d)conj(f(n)).
```

After replacing `f=f^pr+pp`, the error contains terms where one sparse
prime-power vertex is multiplied by up to seven remaining W-tricked prime or
residual vertices, then averaged through the major-arc projection kernel.
Therefore the needed estimate is not merely:

```text
E |pp| small,
```

but a projected multilinear estimate in the same normalization as:

```text
(1/D) sum_{D<|d|<=2D}
  sum_{xi in major, xi != 0} |widehat{B_d}(xi)|^4.
```

This is why ordinary first-moment Hardy-Littlewood input, ordinary pair-BDH,
or unprojected prime-power sparsity cannot be inserted here without the named
transfer package.

## 7. Edge cases

- If all projected vertices preserve an admissible W-residue, small primes
  `p<=w` are absorbed by the W-trick; otherwise the failure belongs to
  `SPResErr_major`.
- Prime powers with base `q<=w` are normally excluded by `(b,W)=1`, but can
  reappear if a shifted vertex leaves the admissible residue class.
- Prime powers with base `q>w` are not removed by the W-trick and must be
  controlled by `PPCubeErr_major`.
- Square terms `q^2` are the largest prime-power support and usually dominate
  any support estimate.
- A first-moment bound for `pp` does not control the projected fourth moment
  when the remaining vertices carry unbounded W-tricked weights.
- Centering can move prime-power mass into `c_d-c_d^pr`; this is harmless only
  if the projection and interval transfer still kill or control constants.
- Boundary removal and prime-power removal must use a stated accounting
  convention, since a prime-power vertex can also lie in the interval boundary
  or kernel-tail region.
- If `P_M` has a long physical kernel, sparse prime-power support can interact
  with long tails; this belongs to `PPBdErr_major` or to the kernel-tail side
  package.
- The transfer must be uniform over `D,R,eta,P_M,H,K,T` in `P_adm`.
- The fixed-`w` limit order cannot be replaced by a diagonal `w=w(N)` argument
  without a separate theorem.

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
  -> cyclic-to-interval boundary transfer
Module 211
  -> prime-power and small-prime transfer.
```

This module fills the `PPErr_major` and small-prime side slots left open in
Modules 206 and 209. It also separates those slots from the boundary package
of Module 210.

The next scheduled module is the compatibility check between pair, rectangle,
and projected cube local models.

## 9. What remains open

This module does not prove:

- `PPSPTransfer_3^major(P_adm)`;
- `PPCubeErr_major=o_W(1)`;
- `PPNormErr_major=o_W(1)`;
- the projected envelope bounds needed to convert `PPNormErr_major` into
  `PPCubeErr_major`;
- `SPResErr_major=o_W(1)` outside exact W-compatible residue conventions;
- `PPModelErr_major=o_W(1)` for any model that includes prime-power
  corrections;
- `PPBdErr_major=o_W(1)`;
- `WProjectedLocalMatch_3^major,prime`;
- `CycIntTransfer_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat first-moment prime-power sparsity as projected fourth-moment
  removal.
- Do not hide prime-power terms inside `Omega_w^proj` unless an explicit
  `Omega_{w,pp}^proj` model and matching theorem are supplied.
- Do not include primes `p<=w` again in the Euler product for
  `Omega_w^proj`; they are handled by the W-trick and residue classes.
- Do not treat W-residue failures caused by projected shifts as prime-only
  local factors.
- Do not use ordinary pair-BDH, first-moment Hardy-Littlewood, or support
  sparsity as a substitute for `PPCubeErr_major`.
- Do not merge `PPSPTransfer_3^major` with boundary transfer without a stated
  disjoint accounting convention.
- Do not transfer this W-tricked prime-only statement to the actual sharp
  moving selector without the selector-transfer package.
- Do not claim projected local-model matching, projected major-arc
  cancellation, the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
