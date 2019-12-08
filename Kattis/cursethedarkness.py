from math import sqrt

m = int(raw_input())
for _ in range(m):
	bx, by = map(float, raw_input().split())
	n = int(raw_input())
	r = False
	for _ in range(n):
		cx, cy = map(float, raw_input().split())
		if sqrt(((bx - cx) ** 2) + ((by - cy) ** 2)) <= 8: r = True
	print "light a candle" if r else "curse the darkness"
