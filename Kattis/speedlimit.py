while True:
	n = int(raw_input())
	if n == -1: break
	m, pt = 0, 0
	for x in range(0, n):
		i = raw_input().split(" ")
		s, t = int(i[0]), int(i[1])
		m += (t - pt) * s
		pt = t
	print m, "miles"