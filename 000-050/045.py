# Problem 45

from common import *

n = 286

while True:
	tn = getTriangularNumber(n)
	if isPentagonalNumber(tn) and isHexagonalNumber(tn):
		print tn
		break
	n += 1
