c, mx = 0, 0
for n in range(0, 5):
	s = sum(int(x) for x in raw_input().split(" "))
	if s > mx:
		c = n + 1
		mx = s
print c, mx