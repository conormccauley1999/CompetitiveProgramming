p = int(raw_input())
for _ in xrange(p):
	k, n = map(int, raw_input().split())
	a = n * (n + 1) / 2
	b = n * n
	c = n * (n + 1)
	print k, a, b, c