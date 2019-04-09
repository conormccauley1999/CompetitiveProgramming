S, E = "S", "E"

t = int(raw_input())

for x in range(1, t + 1):
	n = int(raw_input())
	p = raw_input()
	r = ""
	for m in p:
		if m == S: r += E
		else: r += S
	print "Case #" + str(x) + ": " + r
