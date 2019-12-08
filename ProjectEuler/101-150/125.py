# Problem 125

from math import floor, sqrt

m = 10 ** 8
r = int(floor(sqrt(m)))
s = set()

for a in range(1, r + 1):
	b = a + 1
	sm = (a ** 2) + (b ** 2)
	while sm < m:
		s.add(sm)
		b += 1
		sm += b ** 2

def p(n):
	s = str(n)
	return s == s[::-1]

print sum(n for n in s if p(n))
