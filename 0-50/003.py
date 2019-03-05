# Problem 3

from common import *

n = 600851475143
r = getOddRoot(n)

for d in xrange(r, 1, -2):
	if (n % d == 0 and isPrime(d)):
		print d
		break
