# Problem 21

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

t = 0

for a in range(1, 10000):
	b = getDivisorSum(a)
	c = getDivisorSum(b)
	if a == c and a != b and a < 10000 and b < 10000: t += a + b

print t / 2
