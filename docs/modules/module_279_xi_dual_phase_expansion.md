# Module 279: Exact dual and phase expansion of `Xi_273^0`

## 1. Precise theorem / claim being advanced

This module expands the graph-restriction functional from Module 278 inside
the fixed minimal family `P_minor^0`.

Define:

```text
XiDualPhaseExpansion_279(P_minor^0).
```

The claim is structural:

```text
Xi_273^0(lambda;sigma)
is exactly a data-dependent shell-restricted dual correlation of the cyclic
residual products B_d^0.
```

The expansion identifies the linear dual form, the `TT*` square, the
fourth-power phase kernel, and every set whose membership depends on the
residual coefficients `beta_0(d,xi)`.

This module does not prove `PhaseKernelBound_273^0`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The identities are exact in `P_minor^0`. They are not cancellation estimates
and cannot be used as a substitute for `PhaseKernelBound_273^0`,
`TransIncBound_269`, or `NarrowMinorArc_3^B`.

## 3. Definitions and variables

Use the fixed Module 278 family:

```text
P_minor^0:
  s0 = W-cyclic prime-only model in one residue b mod W,
  G_N=Z/NZ,
  f_0=nu_0-1,
  B_d^0(n)=f_0(n+d)conj(f_0(n)),
  beta_0(d,xi)=widehat{B_d^0}(xi),
  Minor_0(R,eta)={xi != 0}\Major_0(R,eta).
```

Fix:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0) in P_minor^0,
lambda in Lambda_0,
sigma in Lambda_0 with sigma>=lambda.
```

Let:

```text
J=J_trans_0(lambda;sigma)
```

be the Module 278 base-tail shell:

```text
J
  =
  { (d,xi) :
      D<|d|<=2D,
      xi in Minor_0(R,eta),
      |beta_0(d,xi)| >= lambda,
      E_{d,0}(lambda) <= mu_0(lambda),
      N_{xi,0}(lambda) <= K_0(lambda),
      sigma <= |beta_0(d,xi)| < 2sigma }.
```

For each shift and frequency define the shell fibers:

```text
S_d(J)= { xi : (d,xi) in J },
D_xi(J)= { d : (d,xi) in J }.
```

For unit coefficients `omega=(omega_{d,xi})_{(d,xi) in J}` with
`|omega_{d,xi}|<=1`, define:

```text
K_{d,omega}^J(n)
  =
  sum_{xi in S_d(J)} omega_{d,xi} e_N(-xi n),

L_{xi,omega}^J(n)
  =
  sum_{d in D_xi(J)} omega_{d,xi} B_d^0(n).
```

Then:

```text
Xi_273^0(lambda;sigma)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J} omega_{d,xi} beta_0(d,xi) |.
```

## 4. Assumptions

This module assumes only the definitions and fixed conventions of
`P_minor^0`.

It does not assume:

```text
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransGateSideRows_274,
DegFreePhaseGate_275,
TransIncBound_269,
ThresholdOnlyClosure_270,
PhaseIncidenceGate_271,
AvailableToolClosure_272,
MinorArcTransfer_3^B,
NarrowMinorArc_3^B,
selector transfer,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Linear dual form

For fixed `omega`, define:

```text
X_J(omega)
  =
  sum_{(d,xi) in J} omega_{d,xi} beta_0(d,xi).
```

Using:

```text
beta_0(d,xi)=E_{n in G_N} B_d^0(n)e_N(-xi n),
```

one obtains the exact shift-fiber form:

```text
X_J(omega)
  =
  E_{n in G_N}
    sum_{D<|d|<=2D}
      B_d^0(n) K_{d,omega}^J(n).
```

Equivalently, the exact frequency-fiber form is:

```text
X_J(omega)
  =
  E_{n in G_N}
    sum_{xi in Minor_0(R,eta)}
      e_N(-xi n) L_{xi,omega}^J(n).
```

Thus:

```text
Xi_273^0(lambda;sigma)
  =
  sup_{|omega|<=1} |X_J(omega)|.
```

This is only a rewriting. It supplies no bound for `Xi_273^0`.

### B. `TT*` square

For fixed `omega`:

```text
|X_J(omega)|^2
  =
  E_{n,m in G_N}
    sum_{d_1,d_2}
      B_{d_1}^0(n) conj(B_{d_2}^0(m))
      K_{d_1,omega}^J(n)
      conj(K_{d_2,omega}^J(m)).
```

Expanding the kernels gives:

```text
|X_J(omega)|^2
  =
  E_{n,m}
    sum_{(d_1,xi_1) in J}
    sum_{(d_2,xi_2) in J}
      omega_{d_1,xi_1} conj(omega_{d_2,xi_2})
      B_{d_1}^0(n) conj(B_{d_2}^0(m))
      e_N(-xi_1 n + xi_2 m).
```

Substituting `B_d^0(n)=f_0(n+d)conj(f_0(n))` yields the exact four-form
phase expansion:

```text
|X_J(omega)|^2
  =
  E_{n,m}
    sum_{e_1,e_2 in J}
      Omega_2(e_1,e_2)
      f_0(n+d_1)conj(f_0(n))
      conj(f_0(m+d_2))f_0(m)
      e_N(-xi_1 n + xi_2 m),
```

where:

```text
e_i=(d_i,xi_i),
Omega_2(e_1,e_2)=omega_{e_1}conj(omega_{e_2}).
```

No diagonal equation has been imposed. The phases `xi_1` and `xi_2` range
over the data-dependent shell fibers.

### C. Fourth-power phase kernel

A future large-sieve, Bessel, or incidence estimate may try to control
`Xi_273^0` through higher moments. The exact fourth-power identity is:

```text
|X_J(omega)|^4
  =
  E_{n_1,n_2,n_3,n_4}
    sum_{e_1,e_2,e_3,e_4 in J}
      Omega_4(e_1,e_2,e_3,e_4)
      B_{d_1}^0(n_1)
      conj(B_{d_2}^0(n_2))
      conj(B_{d_3}^0(n_3))
      B_{d_4}^0(n_4)
      e_N(-xi_1 n_1 + xi_2 n_2 + xi_3 n_3 - xi_4 n_4),
```

with:

```text
e_i=(d_i,xi_i),
Omega_4(e_1,e_2,e_3,e_4)
  =
  omega_{e_1}conj(omega_{e_2})conj(omega_{e_3})omega_{e_4}.
```

After expanding the four `B_d^0` factors, the eight residual slots are:

```text
f_0(n_1+d_1), conj(f_0(n_1)),
conj(f_0(n_2+d_2)), f_0(n_2),
conj(f_0(n_3+d_3)), f_0(n_3),
f_0(n_4+d_4), conj(f_0(n_4)).
```

The corresponding phase is:

```text
e_N(-xi_1 n_1 + xi_2 n_2 + xi_3 n_3 - xi_4 n_4).
```

This is the exact restricted shell phase kernel. It is not the full-frequency
orthogonality kernel. It becomes a system of diagonal equations only after
one sums over a complete frequency family, which `J` is not.

### D. Data-dependent set ledger

The following objects are fixed once `rho_0` is fixed:

```text
G_N,
the two-sided dyadic shift shell D<|d|<=2D,
the W-residue b,
the cyclic cutoff,
the major/minor parameters R, eta,
the threshold schedules mu_0, K_0.
```

The following objects depend on the residual coefficients `beta_0(d,xi)`:

```text
A_N^0,
Lambda_0,
Spec_{d,0}^minor(lambda),
E_{d,0}(lambda),
N_{xi,0}(lambda),
BadShift_0(lambda),
BadFreq_0(lambda),
I_trans_0(lambda),
J_trans_0(lambda;sigma),
S_d(J),
D_xi(J),
K_{d,omega}^J,
L_{xi,omega}^J.
```

The coefficients:

```text
omega_{d,xi}
```

are adversarial dual variables chosen after the shell `J` has been fixed.
Any theorem for `Xi_273^0` must handle them uniformly.

### E. Consequence for the next module

A theorem for fixed frequency sets would concern a prescribed family such as:

```text
S_d fixed independently of beta_0,
or S fixed independently of d and beta_0.
```

The actual `Xi_273^0` contains:

```text
S_d(J)= { xi :
  xi in Minor_0(R,eta),
  |beta_0(d,xi)| lies in a shell,
  row and column threshold tests pass }.
```

Therefore a fixed-set estimate does not automatically imply
`PhaseKernelBound_273^0`. One would need either:

```text
1. a theorem uniform over all admissible data-dependent shell fibers;
2. a selection theorem transferring fixed-set estimates to J;
3. or a direct estimate for X_J(omega).
```

This is the question assigned to Module 280.

## 6. Edge cases

- If `J` is empty, `Xi_273^0(lambda;sigma)=0`; this does not prove any
  nonempty-shell estimate.
- The supremum over `omega` is part of the target. Choosing favorable phases
  is not allowed.
- The shell fibers are not monotone in `lambda`, because `mu_0(lambda)` and
  `K_0(lambda)` can vary.
- The same frequency appearing in two shifts is not a diagonal equation.
- The same shift appearing in two frequencies is not a full-frequency moment.
- Full cyclic orthogonality applies only after summing over all frequencies,
  not over `Minor_0` or over `J`.
- The lower cutoff `lambda_min` and low-level leakage remain outside this
  module.
- Any interval, sharp-selector, smoothed-selector, or residue-averaged
  version is outside `P_minor^0`.

## 7. Where it fits in the project map

```text
Module 278
  -> MinimalTransverseFamily_278(P_minor^0)

Module 279
  -> XiDualPhaseExpansion_279(P_minor^0)
     exact data-dependent shell expansion of Xi_273^0
```

The next useful step is:

```text
Module 280:
  compare fixed frequency-set estimates with the data-dependent shell sets
  in P_minor^0, and decide whether any fixed-set theorem can transfer to
  Xi_273^0.
```

## 8. What remains open

This module does not prove:

- `PhaseKernelBound_273^0`;
- any bound for `Xi_273^0`;
- fixed-set to shell-set transfer;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
- `TransGateSideRows_274`;
- `DegFreePhaseGate_275`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- `PhaseIncidenceGate_271`;
- `AvailableToolClosure_272`;
- `MinorArcTransfer_3^B`;
- `NarrowMinorArc_3^B`;
- selector transfer to the actual sharp moving selector;
- `ProjectedModelNeutrality_3^major`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat the dual expansion as cancellation.
- Do not replace `J_trans_0(lambda;sigma)` by a fixed frequency set without a
  selection theorem.
- Do not replace restricted shell sums by full-frequency orthogonality.
- Do not drop the adversarial coefficients `omega_{d,xi}`.
- Do not use `PhaseKernelBound_273^0` as an input to prove itself.
- Do not cite this module as a transverse estimate.
