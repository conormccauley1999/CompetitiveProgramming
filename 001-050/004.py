# Problem 4

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

lp = 0

for i in xrange(100, 1000):
	for j in xrange(100, 1000):
		p = i * j
		a = str(p)
		b = rev(a)
		if a == b and p > lp: lp = p

print lp
