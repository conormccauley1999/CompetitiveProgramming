# Problem 39

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ms = 0
pmx = 0

for p in range(1, 1001):
	n = numberOfRATsWithPerimiter(p)
	if n > ms: ms, pmx = n, p

print pmx
