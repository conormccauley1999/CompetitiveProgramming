# Problem 3

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

n = 600851475143
r = getOddRoot(n)

for d in xrange(r, 1, -2):
	if (n % d == 0 and isPrime(d)):
		print d
		break
