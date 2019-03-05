# Problem 25

i = 2
x, y, z = 1, 1, 0

while len(str(z)) < 1000:
	z = x + y
	x = y
	y = z
	i += 1

print i
