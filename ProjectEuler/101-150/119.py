# UNSOLVED
# Problem 119

def f(n):
	s = 0
	while n != 0:
		s += n % 10
		n //= 10
	return s

a = 0
n = 10
while a < 30:
	s = float(f(n))
	m = n
	while s != 1 and m % s == 0:
		m /= s
		if m == 1:
			a += 1
			print a, n
			break
	n += 1

print n - 1
