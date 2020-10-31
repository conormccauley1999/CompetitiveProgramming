# Problem 72

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

def phi(n, ds):
	r = n
	for p in ds:
		r *= (p - 1.0) / p
	return r

def buildPrimeDivisors(ps, mx):
	ds = {}
	for i in xrange(0, mx): ds[i] = set()
	for p in ps:
		n = p
		while n <= mx:
			ds[n - 1].add(p)
			n += p
	return ds

mx = 1000000
ps = list(npPrimesLessThan(mx + 1))
np = len(ps)
ds = buildPrimeDivisors(ps, mx)

s = 0

for n in xrange(2, mx + 1):
	s += phi(n, ds[n - 1])

print s
