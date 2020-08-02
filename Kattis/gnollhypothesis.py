import operator as op
from functools import reduce

_ncr = {}
def ncr(n, r):
	if (n, r,) not in _ncr:
		if n < r:
			return 0
		a = reduce(op.mul, range(n, n - r, -1), 1)
		b = reduce(op.mul, range(1, r + 1), 1)
		_ncr[(n, r,)] = a // b
	return _ncr[(n, r,)]

n, k = map(int, input().split())
vs = list(map(float, input().split()))

rs = []
for i in range(n):
	rs.append(sum(vs[(i - j) % n] * ncr(n - j - 1, k - 1) / ncr(n, k) for j in range(n)))
print(*rs)
