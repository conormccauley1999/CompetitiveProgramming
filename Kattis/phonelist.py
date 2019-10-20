def c(ps):
	ps.sort()
	for i in range(1, len(ps)):
		if ps[i].startswith(ps[i - 1]): return False
	return True

t = int(raw_input())
for x in range(0, t):
	n = int(raw_input())
	ps = [str(raw_input()) for y in range(0, n)]
	print "YES" if c(ps) else "NO"