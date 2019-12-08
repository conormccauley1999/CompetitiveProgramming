N = int(raw_input())
for i in range(0, N):
	r, e = 0, int(raw_input())
	if e == 0: r = 1
	while e:
		e /= 10
		r += 1
	print r