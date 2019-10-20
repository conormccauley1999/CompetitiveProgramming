def f(n):
	if n <= 1: return 1
	else: return n * f(n - 1)

T = int(raw_input())
r = []
for x in range(0, T):
	N = int(raw_input())
	r.append(f(N) % 10)
for x in r: print x