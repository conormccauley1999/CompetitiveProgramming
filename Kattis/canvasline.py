N = int(raw_input())
M = [[0, set()] for _ in xrange(N)]
C = [tuple(map(int, raw_input().split())) for _ in xrange(N)]
_ = int(raw_input())
P = map(int, raw_input().split())
R = []

def add(i, p):
	global M, R
	M[i][0] += 1
	M[i][1].add(p)
	R.append(p)

def tryAdd(i, p):
	global N, M, C

	# canvas full OR peg already there -> RETURN
	if M[i][0] == 2 or p in M[i][1]: return

	# if not possible intersection -> ADD
	if p != C[i][1]:
		add(i, p)
		return

	# if last canvas -> ADD
	if i == N - 1:
		add(i, p)
		return

	# if definite intersection
	if C[i][1] == C[i + 1][0]:
		# if next canvas full -> RETURN
		if M[i + 1][0] == 2: return
		add(i, p)
		# manually update next canvas
		M[i + 1][0] += 1
		M[i + 1][1].add(p)
		return

	# else -> ADD
	add(i, p)

def solve():
	global N, M, C, P, R

	for i in xrange(N):
		c = C[i]
		for p in P:
			if c[0] <= p and p <= c[1]:
				M[i][0] += 1
				M[i][1].add(p)
			if M[i][0] >= 3:
				print "impossible"
				return

	for i in xrange(N):
		tryAdd(i, C[i][1])
		tryAdd(i, C[i][1] - 1)
		tryAdd(i, C[i][1] - 2)

	print len(R)
	print " ".join(map(str, R))

solve()
