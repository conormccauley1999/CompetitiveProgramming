# Problem 100

from math import sqrt

# not sure why this version's answer isn't valid

t = 10 ** 12

while True:
	x = 0.5 * ((t * t) - t)
	b = 0.5 * (1.0 + sqrt(1.0 + (4.0 * x)))
	if b % 1 == 0:
		print int(b), t
		break
	t += 1

# this is an alternative method that works

r = 6
b = 15

while True:
	r = (2 * b) + (r - 1)
	b = b + (2 * r)
	if (r + b) > t:
		print int(b), r + b
		break
