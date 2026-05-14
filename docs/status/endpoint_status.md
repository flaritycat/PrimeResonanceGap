# Endpoint status

## Current `s=2` endpoint class

```text
RBDH_pair_short(Hcal)
  <=> CPC_3^sharp(Hcal)
  <=> SPAC_2^sharp
  <=> SU2Pair_2^sharp
  <=> DyadicDerivativeU^2
  <=> AU^3
```

Status: **OPEN**, with analytic-engine work remaining, modulo side packages.

## RBDH representative

For W-tricked `nu` and:

```text
P_d(n)=nu(n+d)conj(nu(n))
```

prove uniformly for dyadic `D <= Hcal(N)`:

```text
(1/D) sum_{D<|d|<=2D}
(1/N) sum_h
| N^{-1} sum_n Phi(n/N,h/N) P_d(n+h)conj(P_d(n))
  - Sigma_w(d,h) N^{-1} sum_n Phi(n/N,h/N) |^2 = o(1)
```

## Direct CPC representative

```text
(1/D) sum_{D<|d|<=2D} ||R_d||_{U^2}^4 = o(1)
R_d(n)=P_d(n)-kappa_w(d)
```

## Residual cube solve-target

The direct route reduces to:

```text
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1)
B_d(n)=f(n+d)conj(f(n))
f=nu-1
```

Status: **OPEN**.
