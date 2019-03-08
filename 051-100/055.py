# Problem 55

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

t = 0
for n in xrange(1, 10000):
	if isLychrel(n): t += 1
print t
