# Problem 46

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from math import sqrt

def valid(c, ps):
	for p in ps:
		if p < c and sqrt(0.5 * (c - p)) % 1 == 0: return True
	return False

m = 10000
ps = primesLessThan(m)
cs = getOddComposites(m, ps)

for c in cs:
	if not valid(c, ps):
		print c
		break
