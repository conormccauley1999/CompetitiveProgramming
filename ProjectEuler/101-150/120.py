# Problem 120

def r(a):
	return max((((a - 1) ** n) + ((a + 1) ** n)) % (a ** 2) for n in range(1, 2000))

print sum(r(a) for a in range(3, 1001))
