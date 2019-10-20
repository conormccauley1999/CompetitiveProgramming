from math import sin, cos, radians
def safe(v, o, x, h1, h2):
	t = x / (v * cos(radians(o)))
	y = (v * t * sin(radians(o))) - (0.5 * 9.81 * t * t)
	return (y + 1 <= h2) and (y - 1 >= h1)
N = int(raw_input())
tcs = []
for i in range(0, N): tcs.append([float(v) for v in raw_input().split(" ")])
r = []
for tc in tcs:
	if safe(tc[0], tc[1], tc[2], tc[3], tc[4]): r.append("Safe")
	else: r.append("Not Safe")
for x in r: print x