# Problem 69

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ps = primesLessThan(getRoot(1000000))
r = 0
mx = 0

for n in xrange(1, 1000001):
	x = float(n) / float(phi(n, ps))
	if x > mx:
		mx = x
		r = n

print r
