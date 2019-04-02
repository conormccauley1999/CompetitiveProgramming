t = int(raw_input())
r = []
for a in range(0, t):
	n = int(raw_input())
	xs = [int(v) for v in raw_input().split(" ")]
	mx, mn = max(xs), min(xs)
	m = (mx - mn) / 2
	r.append(2 * ((m - mn) + (mx - m)))
for x in r: print x