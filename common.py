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

def primesBetween(mn, mx):
	ps = primesLessThan(mx + 1)
	px = set()
	for p in ps:
		if p >= mn: px.add(p)
	return px

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

def getOddComposites(m, ps):
	cs = []
	for n in xrange(9, m, 2):
		if n not in ps: cs.append(n)
	return cs

def hasNPrimeFactors(x, n, ps):
	f = 0
	for p in ps:
		if x == 1: break
		if x % p == 0: f += 1
		while x % p == 0: x /= p
	return f >= n

def getMasks(l):
	ms = []
	for i in range(0, (2 ** (l - 1)) - 1):
		m = str(bin(i))[2:].zfill(l - 1)
		m += "1"
		ms.append(m)
	return ms

def applyMask(n, v, m):
	n = str(n)
	v = str(v)
	r = ""
	for i in range(0, (len(m) - 1)):
		r += v if m[i] == "0" else n[i]
	r += n[len(m) - 1]
	return int(r)

def c(n, r):
	return factorialRecursive(n) / (factorialRecursive(r) * factorialRecursive(n - r))

def isPalindromic(n):
	return str(n) == rev(str(n))

def addReverse(n):
	return n + int(rev(str(n)))

def isLychrel(n):
	for i in range(0, 50):
		n = addReverse(n)
		if isPalindromic(n): return False
	return True

def digitalSum(n):
	return sum(int(d) for d in str(n))

def getNumLengthQuick(n):
	if n < 10000:
		if n < 100:
			if n < 10: return 1
			else: return 2
		else:
			if n < 1000: return 3
			else: return 4
	else:
		if n < 1000000:
			if n < 100000: return 5
			else: return 6
		else:
			if n < 10000000: return 7
			else:
				if n < 100000000: return 8
				else: return 9
