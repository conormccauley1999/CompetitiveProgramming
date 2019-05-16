# Problem 323

def P(n):
	return (1 - (2 ** (-n))) ** 32

print sum(1 - P(n) for n in range(100000))
