# Problem 72 -- incomplete

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

def getPrimeDivisors(n, ps):
	ds = set()
	for p in ps:
		if n == 1: return ds
		if n % p == 0:
			ds.add(p)
			n /= p
	return ds

mx = 1000000
ps = list(npPrimesLessThan(mx + 1))
np = len(ps)
ds = {}#buildPrimeDivisors(ps, mx)

for n in xrange(2, mx + 1):
	if n % 100 == 0: print n
	ds[n] = getPrimeDivisors(n, ps) # need more efficient method

s = mx - 1

for n in xrange(2, mx + 1):
	dsn = ds[n]
	for m in xrange(n, mx + 1):
		dsm = ds[m]
		valid = True
		for d in dsm:
			if d in dsn:
				valid = False
				break
		if valid: s += 1

print s
