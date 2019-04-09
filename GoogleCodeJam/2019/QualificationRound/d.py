import sys

ZERO, ONE = "0", "1"

def solveHard(N, B, F):
	return [0, 1]

def solveEasy(N, B, F):
	h = (N + 1) // 2
	rs = []
	i = 0
	while i < F and h:
		q = ""
		x = 0
		c = ZERO
		while x < N:
			q += c * h
			x += h
			if c == ZERO: c = ONE
			else: c = ZERO
		if h == 1: h = 0
		else: h = (h + 1) // 2
		i += 1
		print(q[:N])
		#sys.stdout.flush()
		r = input()
		rs.append(r)
	idw = [""] * (N - B)
	for i in range(N - B):
		for j in range(len(r)):
			idw[i] += rs[j][i]
	idw = map(lambda x: int(x, 2), idw)
	ids = [x for x in range(N) if x not in idw]
	return ids

def solve(N, B, F):
	#return solveEasy(N, B, F) if F == 10 else solveHard(N, B, F)
	return solveEasy(N, B, F)

T = int(input())
for _ in range(T):
	N, B, F = map(int, input().split())
	r = " ".join(map(str, solve(N, B, F)))
	print(r)
	#sys.stdout.flush()
	_ = input()
