def f(a, b, c, d, x):
	p = x % (a + b)
	p = p > 0 and p <= a
	q = x % (c + d)
	q = q > 0 and q <= c
	if p and q:
		print("both")
	elif not p and not q:
		print("none")
	else:
		print("one")
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
a, b, c, d = map(int, input().split())
p, m, g = map(int, input().split())
f(a, b, c, d, p)
f(a, b, c, d, m)
f(a, b, c, d, g)
