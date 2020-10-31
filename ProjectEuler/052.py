# Problem 52

from itertools import permutations

for i in xrange(1, 10000000):
	p = ["".join(x) for x in permutations(str(i))]
	if (
		str(2 * i) in p and
		str(3 * i) in p and
		str(4 * i) in p and
		str(5 * i) in p and
		str(6 * i) in p
	):
		print i
		break
