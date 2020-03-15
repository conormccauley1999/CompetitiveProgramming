def f(n):
	f = 1
	for i in range(n, 1, -1): f *= i
	return f

def c(n, r):
	return f(n) // (f(r) * f(n - r))

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	print(c(n, m - 1))
