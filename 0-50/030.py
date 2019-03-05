# Problem 30

mx = 200000
r = 0

for i in xrange(2, mx):
	ds = [int(c) for c in str(i)]
	s = sum(d ** 5 for d in ds)
	if s == i: r += i

print r
