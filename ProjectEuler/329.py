# Problem 329

def gcd(a, b):
	return gcd(b % a, a) if a else b


def sieve(n):
	ps = [True] * (n + 2)
	ps[0] = False
	ps[1] = False
	for i in range(2, n + 2):
		if not ps[i]: continue
		j = i * i
		while j <= n + 1:
			ps[j] = False
			j += i
	return ps


M = 15
N = 500
S = [
	True, True, True, True, False,
	False, True, True, True, False,
	True, True, False, True, False
]
P = sieve(N)


_dp = {}
def dp(t, p):
	if (t, p) in _dp: return _dp[(t, p)]
	
	"""
	n/3 | S[t] | P[p+1]
	2/3 | 1    | 1
	1/3 | 1    | 0
	1/3 | 0    | 1
	2/3 | 0    | 0
	
	n = S[t] ^ P[p+1] ? 1 : 2
	"""
	n = 1 if S[t] ^ P[p + 1] else 2
	
	if t == M - 1: return n
	
	if p == 0:
		n *= 2 * dp(t + 1, p + 1)
	elif p == N - 1:
		n *= 2 * dp(t + 1, p - 1)
	else:
		n *= dp(t + 1, p - 1) + dp(t + 1, p + 1)

	_dp[(t, p)] = n
	return n


n = sum(dp(0, i) for i in range(N))
d = N * (3 ** M) * (2 ** (M - 1))
g = gcd(n, d)
print("%d/%d" % (n / g, d / g))
