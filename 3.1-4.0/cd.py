while True:
	i = raw_input().split()
	N, M = int(i[0]), int(i[1])
	if N == 0 and M == 0: break
	a, b = set(), set()
	for i in xrange(0, N): a.add(int(raw_input()))
	for i in xrange(0, M): b.add(int(raw_input()))
	print len(a.intersection(b))