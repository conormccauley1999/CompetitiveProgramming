# Problem 38

from common import *

r = 0

for maxm in range(1, 10):

	for n in range(1, 10000):

		s = ""
		for m in range(1, maxm): s += str(n * m)
		if isPandigital(s) and int(s) > r: r = int(s)

print r
