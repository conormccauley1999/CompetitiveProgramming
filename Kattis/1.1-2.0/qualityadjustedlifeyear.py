N = int(raw_input())
r = 0
for x in range(0, N):
	i = raw_input().split(" ")
	q, y = float(i[0]), float(i[1])
	r += q * y
print r