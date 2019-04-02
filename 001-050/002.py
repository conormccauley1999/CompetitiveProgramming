# Problem 2

s = 0
x, y = 0, 1

while (x + y <= 4000000):
	z = x + y
	x = y
	y = z
	if (z % 2 == 0): s += z

print s
