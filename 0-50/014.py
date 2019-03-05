# Problem 14

r = 1
lc = 1

for n in xrange(1, 1000000):

	s = n
	c = 0

	while n != 1:
		if n % 2 == 0: n /= 2
		else: n = (n * 3) + 1
		c += 1

	if c > lc:
		lc = c
		r = s

print r
