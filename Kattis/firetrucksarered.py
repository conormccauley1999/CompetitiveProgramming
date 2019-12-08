n = int(raw_input())

C = [set() for _ in xrange(n)]
R = {}

for i in xrange(n):
	cs = map(int, raw_input().split()[1:])
	for c in cs:
		C[i].add(c)
		if c not in R: R[c] = set()
		R[c].add(i)

vis = [False] * n
vis[0] = True
res = []

stk = [0]
while stk:
	u = stk.pop()
	for c in C[u]:
		for v in R[c]:
			if not vis[v]:
				res.append([u, v, c])
				stk.append(v)
				vis[v] = True
		R[c] = set()

if any(not x for x in vis):
	print "impossible"
else:
	for r in res:
		print r[0] + 1, r[1] + 1, r[2]
