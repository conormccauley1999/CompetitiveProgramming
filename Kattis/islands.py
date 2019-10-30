def f(l):
	t = 0
	for s in range(1, 11):
		for e in range(s, 11):
			if min(l[s:e+1]) > max(l[s-1], l[e+1]):
				t += 1
	return t

p = int(raw_input())
for _ in range(p):
	i = map(int, raw_input().split())
	k = int(i[0])
	l = map(int, i[1:])
	print k, f(l)
