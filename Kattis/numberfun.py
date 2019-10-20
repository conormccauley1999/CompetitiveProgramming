N = int(raw_input())
r = []
for x in range(0, N):
	i = [float(v) for v in raw_input().split(" ")]
	if (
		(i[0] + i[1] == i[2]) or
		(i[0] * i[1] == i[2]) or
		(i[0] - i[1] == i[2]) or
		(i[1] - i[0] == i[2]) or
		(i[0] / i[1] == i[2]) or
		(i[1] / i[0] == i[2])
	): r.append("Possible")
	else: r.append("Impossible")
for x in r: print x