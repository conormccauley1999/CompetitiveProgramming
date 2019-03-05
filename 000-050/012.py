# Problem 12

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

n = 1
while True:
	tn = getTriangularNumber(n)
	if getDivisorCount(tn) > 500: break
	n += 1

print tn
