# Problem 64

from math import sqrt, floor

def getContinuedFractionPeriod(n):
	ls = []
	a = floor(sqrt(n))
	r = 1 / (sqrt(n) - a)
	while True:
		ls.append(a)
		a = floor(r)
		r = 1 / (r - a)
	return ls

r = 0
for n in range(2, 10000):
	if sqrt(n) == int(sqrt(n)): continue
	if len(getContinuedFractionPeriod(n)) % 2 == 1: r += 1
print r
