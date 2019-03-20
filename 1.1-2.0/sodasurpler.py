i = raw_input().split(" ")
e, f, c = int(i[0]), int(i[1]), int(i[2])
t = 0
b = e + f
while b >= c:
	t += b / c
	b = (b % c) + (b / c)
print t