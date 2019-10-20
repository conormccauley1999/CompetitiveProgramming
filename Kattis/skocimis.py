K = [int(v) for v in raw_input().split(" ")]
t = 0
while True:
	K.sort()
	d1, d2 = K[1] - K[0], K[2] - K[1]
	if d1 == 1 and d2 == 1: break
	if d1 >= d2: K[2] = K[0] + 1
	else: K[0] = K[1] + 1
	t += 1
print t