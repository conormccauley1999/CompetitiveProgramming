N = int(raw_input())
r = []
for x in range(0, N):
	i = raw_input().split(" ")
	b, p = int(i[0]), float(i[1])
	bpm = (60.0 * b) / p
	mna = bpm - (60.0  / p)
	mxa = bpm + (60.0  / p)
	r.append([mna, bpm, mxa])
for s in r: print s[0], s[1], s[2]