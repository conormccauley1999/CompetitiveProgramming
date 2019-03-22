ps = {}
while True:
	i = raw_input().split()
	if len(i) == 1: break
	m, l, r = int(i[0]), i[1], i[2]
	if l not in ps: ps[l] = [False, 0]
	if not ps[l][0]:
		if r == "right":
			ps[l][0] = True
			ps[l][1] += m
		else: ps[l][1] += 20
s, x = 0, 0
for p in ps.values():
	if p[0]:
		s += 1
		x += p[1]
print s, x