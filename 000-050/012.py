# Problem 12

from common import *

n = 1
while True:
	tn = getTriangularNumber(n)
	if getDivisorCount(tn) > 500: break
	n += 1

print tn
