f = lambda s, d: s[0]*(s[0] + 7) + s[1]*s[1] + (s[2]+d)*(s[2]+d)
n = int(raw_input())
for _ in range(n):
	a, b, c, d = map(int, raw_input().split())
	s = sorted([a, b, c])
	m = f(s, d)
	i = 0
	while d != 0 and i < 10000:
		s[0] += 1
		d -= 1
		s.sort()
		m = max(m, f(s, d))
		i += 1
	print m
