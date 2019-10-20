T = int(raw_input())
r = []
for x in range(0, T):
	i = [int(v) for v in raw_input().split(" ")][0:-1]
	s = 0
	for y in range(1, len(i)):
		d = i[y] - (2 * i[y - 1])
		if d > 0: s += d
	r.append(s)
for x in r: print x