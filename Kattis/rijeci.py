K = int(raw_input())
if K == 1:
	print 0, 1
else:
	x = [0, 1]
	y = [1, 1]
	for i in range(0, K - 1):
		t = [y[0]+x[0], y[1]+x[1]]
		x = y
		y = t
	print x[0], y[0]