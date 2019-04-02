# Problem 47

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ps = sorted(list(primesLessThan(10000)))

for n in xrange(100, 300000):
	if hasNPrimeFactors(n, 4, ps) and hasNPrimeFactors(n + 1, 4, ps) and hasNPrimeFactors(n + 2, 4, ps) and hasNPrimeFactors(n + 3, 4, ps):
		print n
		break
