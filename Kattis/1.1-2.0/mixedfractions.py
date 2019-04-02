while True:
	i = raw_input().split(" ")
	a, b = int(i[0]), int(i[1])
	if a == 0 and b == 0: break
	c, d = a / b, a % b
	print c, d, "/", b