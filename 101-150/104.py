# Problem 104

from math import log10

def isPandigital(n):
	ds = set()
	while n:
		d = n % 10
		if d == 0: return False
		ds.add(d)
		n //= 10
	return len(ds) == 9

def p(n):
	x = n % 1000000000
	if not isPandigital(x): return False
	l = int(log10(n)) + 1
	x = n / (10 ** (l - 9))
	return isPandigital(x)

a = 1
b = 1

k = 3
while True:
	a, b = (a + b), a
	if p(a): break
	if k % 10000 == 0: print k
	k += 1

print k
