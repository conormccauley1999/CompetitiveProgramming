_P = {}
_P[1] = 1
def P(n):
	if n not in _P:
		_P[n] = P(n - 1) + ((n * (n + 1)) / 2)
	return _P[n]

s = set(P(n) for n in range(2, 100))

m = 10 ** 10
for a in range(1, 100):
	for b in range(a + 1, 100):
		c = P(a) + P(b)
		if c in s and c < m: m = c

print m