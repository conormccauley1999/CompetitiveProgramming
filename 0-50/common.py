from math import sqrt, floor

def even(n):
	return n if n % 2 == 0 else n - 1

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

	if n == 1: return False
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
			for j in xrange(long(i * i), n + 1, i): m.add(j)
	return p

def sumOfSquares(n):
	return sum(getSquares(n))

def squareOfSum(n):
	return sum(range(1, n + 1)) ** 2

def getSquares(n):
	return [(i * i) for i in range(1, n + 1)]

def getTriangularNumber(n):
	return (n * (n + 1)) / 2

def isTriangularNumber(n):
	s = sqrt((8 * n) + 1)
	return s == int(s)

def getPentagonalNumber(n):
	return 0.5 * n * ((3 * n) - 1)

def isPentagonalNumber(n):
	return (1 + sqrt((24 * n) + 1)) % 6 == 0

def getHexagonalNumber(n):
	return n * ((2 * n) - 1)

def isHexagonalNumber(n):
	return ((sqrt((8 * n) + 1) + 1) / 4) % 1 == 0

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

def isPrimeTruncatableLR(n): # LR = Left and right

	strLeft = str(n)[1:]
	strRight = str(n)[:-1]

	while len(strLeft) > 0:
		if not isPrime(int(strLeft)) or not isPrime(int(strRight)): return False
		strLeft = strLeft[1:]
		strRight = strRight[:-1]

	return True

def isPandigitalInt(n):
	return isPandigital(str(n))

def isPandigital(s):

	cs = [str(i) for i in range(1, 10)]
	if len(s) != 9: return False

	for c in cs:
		if c not in s: return False

	return True

def numberOfRATsWithPerimiter(p):
	s = 0
	mx = even(p) - 1
	for a in range(2, mx, 2):
		for b in range(2, mx, 2):
			c = p - (a + b)
			if (c * c) == (a * a) + (b * b): s += 1
	return s

def getNthDigitOfFractionalPart(n):
	r = ""
	x = 1
	while len(r) < n:
		r += str(x)
		x += 1
	return int(r[n - 1])
