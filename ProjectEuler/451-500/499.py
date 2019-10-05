
# Problem 499
# See https://arxiv.org/pdf/1209.4203v4.pdf

from decimal import *

# Solve for z
def solve(f, s, e):
	a = Decimal(0.01) # step
	b = Decimal(0.5)  # adjustment
	while True:
		diff = f(s) - Decimal(0)
		if abs(diff) < e: return s
		if diff > Decimal(0): s += a
		else: s -= a
		a *= b

# Precision
getcontext().prec = 40

# Variables
M = Decimal(10 ** 9) # wealth
c = Decimal(15)      # cost
t = 40               # number of terms

# Generate coefficients and degrees of p(z)
x = [Decimal(2) ** Decimal(-i) for i in range(1, t + 1)]
y = [Decimal(2) ** Decimal(i - 1) - c for i in range(1, t + 1)]

# p(z) = 1 = sum(z^(2^(i-1) - cost) / 2^i) - (see pg. 1 - generating function)
pz = lambda z: sum(x[i] * (Decimal(z) ** y[i]) for i in range(t)) - Decimal(1)

# Solve for z
r = solve(pz, Decimal(1.0), Decimal(1e-30))

# P_ruin(M) = 1 - (max root ^ M) - (see pg. 2 - equation (3))
print Decimal(1) - (r ** M)
