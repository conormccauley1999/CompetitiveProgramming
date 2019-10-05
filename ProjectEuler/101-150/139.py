# Problem 139

from fractions import gcd
from math import sqrt, floor

r = 0

m = 10 ** 8

for x in range(2, int(sqrt(m))):
	print x, r
	for y in range(1, x):
		if (x + y) % 2 == 0: continue
		if gcd(x, y) != 1: continue
		a, b, c = ((x * x) - (y * y)), (2 * x * y), ((x * x) + (y * y))
		if c % abs(a - b) != 0: continue
		r += floor((m - 1) / (a + b + c))

print int(r)
