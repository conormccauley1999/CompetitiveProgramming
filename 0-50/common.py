from math import sqrt, floor

def getEvenRoot(n):
	r = getRoot(n)
	if r % 2 == 0: return r
	else: return r - 1

def getOddRoot(n):
	r = getRoot(n)
	if r % 2 == 1: return r
	else: return r - 1

def getRoot(n):
	return int(floor(sqrt(n)))

def isPrime(n):

	if n == 2: return True
	if n == 3: return True
	if n % 2 == 0: return False
	if n % 3 == 0: return False

	i = 5
	w = 2

	while i * i <= n:
		if n % i == 0: return False
		i += w
		w = 6 - w

	return True

def rev(s):
	return s[::-1]

def primesLessThan(n):
	p, m = [], set()
	for i in xrange(2, n + 1):
		if i not in m:
			p.append(i)
			for j in xrange(i * i, n + 1, i): m.add(j)
	return p

def sumOfSquares(n):
	return sum(getSquares(n))

def squareOfSum(n):
	return sum(range(1, n + 1)) ** 2

def getSquares(n):
	return [(i * i) for i in range(1, n + 1)]

def getTriangularNumber(n):
	return (n * (n + 1)) / 2

def getDivisorCount(n):
	d, r = 1, getRoot(n)
	for i in range(r, 0, -1):
		if n % i == 0: d += 1
	return d * 2

def getDivisorSum(n):
	s = 0
	for i in range(1, (n / 2) + 1, 1):
		if n % i == 0: s += i
	return s

def factorialRecursive(n):
	f = 1
	for i in xrange(n, 1, -1): f *= i
	return f
