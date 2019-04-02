# Problem 75
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

from fractions import gcd
from math import sqrt

res = {}

mx = 1500000
rt = int(sqrt(mx))

for m in range(2, rt):
	for n in range(1, m):
		# not both odd
		if (m + n) % 2 == 0: continue
		# coprime
		if gcd(m, n) != 1: continue
		# primitive triple
		a = (m * m) - (n * n)
		b = 2 * m * n
		c = (m * m) + (n * n)
		l = a + b + c
		l0 = l
		# non-primitive triples
		while l <= mx:
			res[l] = res.get(l, 0) + 1
			l += l0

t = 0
for x in res:
	if res[x] == 1:
		t += 1
print t