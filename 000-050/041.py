# Problem 41

from common import *
import itertools

ns = sorted(list(itertools.permutations("7654321")), reverse=True)
for n in ns:
	n = int("".join(n))
	if isPrime(n):
		print n
		break
