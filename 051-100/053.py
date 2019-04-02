# Problem 53

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

t = 0

for n in range(1, 101):
	for r in range(1, n):
		if c(n, r) > 1000000: t += 1

print t
