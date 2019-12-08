# Problem 605

def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)

n = int(1e8 + 7)
k = int(1e4 + 7)
m = int(1e8)

pn = pow(2, n, m)
pnk = pow(2, n - k, m)

num = pnk * (n + ((pn - 1) * (k - 1)))
den = (pn - 1) * (pn - 1)

g = gcd(num, den)

print ((num / g) * (den / g)) % m
