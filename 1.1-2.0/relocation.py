i = raw_input().split(" ")
N, Q = int(i[0]), int(i[1])
x = [int(v) for v in raw_input().split(" ")]
for v in range(0, Q):
	i = raw_input().split(" ")
	p, q, r = int(i[0]), int(i[1]), int(i[2])
	if p == 1: x[q - 1] = r
	if p == 2: print abs(x[q - 1] - x[r - 1])