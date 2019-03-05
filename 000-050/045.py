# Problem 45

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

n = 286

while True:
	tn = getTriangularNumber(n)
	if isPentagonalNumber(tn) and isHexagonalNumber(tn):
		print tn
		break
	n += 1
