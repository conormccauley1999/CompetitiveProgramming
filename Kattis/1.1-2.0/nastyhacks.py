N = int(raw_input())
x = []
for k in range(0, N):
	i = raw_input().split(" ")
	r, e, c = int(i[0]), int(i[1]), int(i[2])
	if e - c > r: x.append("advertise")
	elif e - c < r: x.append("do not advertise")
	else: x.append("does not matter")
for s in x: print s