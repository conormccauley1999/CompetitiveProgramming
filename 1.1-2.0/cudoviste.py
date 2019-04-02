i = raw_input().split()
R, C = int(i[0]), int(i[1])
a = [raw_input() for x in range(0, R)]
o = [0] * 5
for x in range(0, R - 1):
	for y in range(0, C - 1):
		s = a[x][y:y+2] + a[x+1][y:y+2]
		if "#" not in s: o[s.count("X")] += 1
for x in o: print x