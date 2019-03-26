"""def mst(p):
	l = 0
	visited = set()
	stack = [p[p.keys()[0]]]
	while len(stack) != 0:
		node = stack.pop()
		# to-do
	return l

t = int(raw_input())
for _ in xrange(t):
	n, m = map(int, raw_input().split())
	p = {}
	for _ in xrange(m):
		a, b = map(int, raw_input().split())
		if a in p: p[a].add(b)
		else: p[a] = set([b])
		if b in p: p[b].add(a)
		else: p[b] = set([a])
	print mst(p)
"""