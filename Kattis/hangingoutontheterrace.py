i = raw_input().split(" ")
L, x = int(i[0]), int(i[1])
r = 0
t = 0
for x in range(0, x):
	i = raw_input().split(" ")
	n = int(i[1])
	if i[0] == "enter":
		if t + n > L: r += 1
		else: t += n
	else: t -= n
print r