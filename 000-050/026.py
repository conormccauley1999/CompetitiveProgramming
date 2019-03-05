# Problem 26

def rc(n):
	r = 1
	for i in range(0, n): r = (r * 10) % n
	s = r
	r, l = (r * 10) % n, 1
	while (r != s):
		r = (r * 10) % n
		l += 1
	return l

r = [rc(n) for n in range(1, 1000)]
print r.index(max(r)) + 1
