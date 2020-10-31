# Problem 64

from math import sqrt, floor

def getContinuedFractionPeriod(n):
	if int(sqrt(n)) == sqrt(n): return 0
	m = 0
	d = 1
	a = a0 = floor(sqrt(n))
	p = 0
	while a != 2 * a0:
		m = d * a - m
		d = (n - (m * m)) / d
		a = floor((a0 + m) / d)
		p += 1
	return p

r = 0
for n in range(2, 10001):
	if sqrt(n) == int(sqrt(n)): continue
	if getContinuedFractionPeriod(n) % 2 == 1: r += 1
print r
