# Problem 66

import time
from math import sqrt, floor

def isSolution(x, y, d):
	return (x * x) - (d * y * y) == 1

def getMinDiophantineX(n):
	m = 0
	d = 1
	an = a0 = int(floor(sqrt(n)))
	hn, h1, h2 = a0, 1, 0
	kn, k1, k2 = 1, 0, 0
	while not isSolution(hn, kn, n):
		m = (d * an) - m
		d = (n - (m * m)) / d
		an = int(floor((a0 + m) / d))
		h2 = h1
		h1 = hn
		hn = (h1 * an) + h2
		k2 = k1
		k1 = kn
		kn = (k1 * an) + k2
	return hn

r = 0
mx = 0
for d in xrange(1, 1001):
	if int(sqrt(d)) == sqrt(d): continue
	x = getMinDiophantineX(d)
	if x > mx:
		mx = x
		r = d
print r
