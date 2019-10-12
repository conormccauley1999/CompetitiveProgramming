# Problem 666

k, m = 2, 2

def _r(k, m):
	r = {}
	r[0] = 306
	for n in range(1, k * m): r[n] = r[n - 1] ** 2 % 10007
	for n in r: r[n] %= 5
	return r

def _p(k, m, r):
	p = {}
	for i in range(k):
		q = [0] * 5
		for j in range(m): q[r[i * m + j]] += 1
		s = float(sum(q))
		for x in range(5): q[x] /= s
		p[i] = q
	return p

r = _r(k, m)
p = _p(k, m, r)

for x in p:
	print x, p[x]
