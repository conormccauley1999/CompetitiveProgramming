t = int(raw_input())
for _ in xrange(t):
	n, m = map(int, raw_input().split())
	mx = 0
	for _ in xrange(m):
		a, b = map(int, raw_input().split())
		if a > mx: mx = a
		if b > mx: mx = b
	print mx - 1