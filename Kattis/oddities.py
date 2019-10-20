N = int(raw_input())
r = []
for i in range(0, N):
	x = int(raw_input())
	if x % 2 == 0: r.append(str(x) + " is even")
	else: r.append(str(x) + " is odd")
for s in r: print s