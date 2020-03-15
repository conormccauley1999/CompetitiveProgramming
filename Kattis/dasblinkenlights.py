def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
p, q, s = map(int, input().split())
l = (p * q) / gcd(p, q)
print("yes" if l <= s else "no")
