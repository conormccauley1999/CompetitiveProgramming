N = int(raw_input())
for x in range(0, N):
	G = int(raw_input())
	y = [int(v) for v in raw_input().split(" ")]
	z = 0
	for v in y:
		if y.count(v) == 1:
			z = v
			break
	print "Case #" + str(x + 1) + ":", z