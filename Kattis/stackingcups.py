N = int(raw_input())
c = []
for x in range(0, N):
	i = raw_input().split(" ")
	if i[0].isdigit(): c.append([int(i[0])*0.5, i[1]])
	else: c.append([int(i[1]), i[0]])
c.sort()
for x in c: print x[1]