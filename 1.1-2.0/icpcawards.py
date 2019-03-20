N = int(raw_input())
ts = []
for x in range(0, N): ts.append(raw_input().split(" "))
y = set()
for t in ts:
	if len(y) == 12: break
	if t[0] not in y:
		print t[0], t[1]
		y.add(t[0])