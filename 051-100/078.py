# Problem 78

from math import ceil

gCache = {}
pCache = { 0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7 }

def g(n):

	if n in gCache: return gCache[n]

	k = (-1 if n % 2 == 0 else 1) * int(ceil(n / 2.0))
	gv = (k * ((3 * k) - 1)) / 2

	gCache[n] = gv
	return gv

def p(n):

	if n in pCache: return pCache[n]

	pv = 0

	i = 1
	while True:

		s = -1 if int(ceil(i / 2.0)) % 2 == 0 else 1
		gv = g(i)

		if (n - gv) < 0: break
		pv += s * p(n - gv)

		i += 1

	pCache[n] = pv
	return pv

def main():
	
	n = 1
	
	while True:
		if p(n) % 1000000 == 0: break
		n += 1

	return n

print main()
