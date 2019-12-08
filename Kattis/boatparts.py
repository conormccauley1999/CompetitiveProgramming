def solve():
	p, n = map(int, raw_input().split())
	s = set()
	for i in range(n):
		s.add(raw_input())
		if len(s) == p:
			print i + 1
			return
	print "paradox avoided"
solve()
