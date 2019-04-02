i = raw_input().split(" ")
N, M = int(i[0]), int(i[1])
a = [0] * (N + M)
for x in range(1, N + 1):
	for y in range(1, M + 1):
		a[x + y - 1] += 1
r = []
mx = max(a)
for i in range(0, len(a)):
	if a[i] == mx: r.append(i + 1)
for i in r: print i