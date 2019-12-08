from math import factorial as f

def C(n, r):
	return f(n) / f(r) / f(n-r)

n, k = map(int, raw_input().split())
p = map(float, raw_input().split())
r = ""

for i in range(n):
	s = 0
	for d in range(n):
		s += p[(i - d) % n] * (C(n - d - 1, k - 1) / C(n, k))
	r += str(s) + " "

print r
