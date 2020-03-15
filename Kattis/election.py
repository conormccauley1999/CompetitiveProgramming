from math import ceil

def f(n):
	f = 1
	for i in range(n, 1, -1): f *= i
	return f

def c(n, r):
	return f(n) // (f(r) * f(n - r))

def P(N, V1, V2):
	M = (N // 2) + 1
	if V1 >= M: return 100
	if V2 >= M: return 0
	R = N - (V1 + V2)
	D = M - V1
	p = 0
	for d in range(D, R + 1):
		p += c(R, d) * (0.5 ** d) * (0.5 ** (R - d))
	return p * 100


T = int(input())
for _ in range(T):
	N, V1, V2, W = map(int, input().split())
	p = P(N, V1, V2)
	if p == 0:
		print("RECOUNT!")
	elif p <= W:
		print("PATIENCE, EVERYONE!")
	else:
		print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
