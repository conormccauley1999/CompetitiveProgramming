N = int(raw_input())
r = set()
for x in range(0, N):
	i = raw_input().split(" ")
	s, t = int(i[0]), int(i[1])
	for y in range(s, t+1): r.add(y)
print len(r)