# Problem 95

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

c = {}

def nextNum(n):
	if n in c: return c[n]
	ds = getDivisorSum(n)
	c[n] = ds
	return ds

def chainLength(n):
	cl = 0
	n0 = n
	sm = n
	while True:
		n = nextNum(n)
		if cl > 200 or n == 0 or n > 1000000: return 0, 0
		cl += 1
		if n == n0: return cl, sm
		if n < sm: sm = n

mx, sm = 0, 0
for n in xrange(12496, 15000):
	l, s = chainLength(n)
	if l > mx:
		mx, sm = l, s
		print n, mx, sm
print sm
