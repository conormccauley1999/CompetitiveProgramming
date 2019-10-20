T = int(raw_input())
r = []
for x in range(0, T):
	n = int(raw_input())
	s = set()
	for y in range(0, n): s.add(raw_input())
	r.append(len(s))
for x in r: print x