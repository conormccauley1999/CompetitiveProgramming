n = int(raw_input())
s = raw_input().split()
m = int(raw_input())

W = {}

for _ in range(m):
	d, e, v = raw_input().split()
	if d not in W: W[d] = [[], []]
	if v == "correct":
		W[d][0].append(e)
	else:
		W[d][1].append(e)

tc, ti = 0, 0
wc, wi = "", ""

for x in s:
	c, i = map(len, W[x])
	tc = c if tc == 0 else tc * c
	ti = (i + c) if ti == 0 else ti * (i + c)
	wc += "" if c == 0 else "%s " % (W[x][0][0])
	if i == 0:
		if c == 0: wi += ""
		else: wi += "%s " % (W[x][0][0])
	else: wi += "%s " % (W[x][1][0])

ti -= tc

if tc == 1 and ti == 0:
	print wc
	print "correct"
elif tc == 0 and ti == 1:
	print wi
	print "incorrect"
else:
	print "%d correct" % (tc)
	print "%d incorrect" % (ti)
