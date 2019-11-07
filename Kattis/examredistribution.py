n = int(raw_input())
vs = map(int, raw_input().split())
ts = sorted([(vs[i], i + 1) for i in range(n)])[::-1]
sm = 0
for i in range(1, n): sm += ts[i][0]
if ts[0][0] > sm:
	print "impossible"
else:
	x = ""
	for t in ts: x += str(t[1]) + " "
	print x
