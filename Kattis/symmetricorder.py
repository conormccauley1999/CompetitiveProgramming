def order(ns):
	o = [""] * len(ns)
	for i in range(0, len(ns)):
		if i % 2 == 0: o[i / 2] = ns[i]
		else: o[len(ns) - ((i / 2) + 1)] = ns[i]
	return o
r = []
while True:
	N = int(raw_input())
	if N == 0: break
	ns = [""] * N
	for i in range(0, N): ns[i] = raw_input()
	r.append(order(ns))
for i in range(0, len(r)):
	print "SET " + str(i + 1)
	for n in r[i]: print n