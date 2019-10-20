from decimal import *
N = int(raw_input())
d = []
for x in range(0, N): d.append([Decimal(v) for v in raw_input().split()])
r = Decimal(0)
for x in range(0, N - 1):
	r += Decimal(0.5) * (d[x][1] + d[x+1][1]) * (d[x+1][0] - d[x][0])
print r * Decimal(0.001)