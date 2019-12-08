while True:
	x = raw_input()
	if x == "0": break
	x1, y1, x2, y2, p = map(float, x.split())
	print ((abs(x1 - x2) ** p) + (abs(y1 - y2) ** p)) ** (1 / p)
