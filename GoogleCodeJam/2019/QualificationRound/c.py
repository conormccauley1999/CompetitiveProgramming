from collections import deque
from fractions import gcd
import string

a = string.ascii_uppercase
t = int(raw_input())

for x in xrange(t):

	n, l = map(int, raw_input().split())
	vs = map(int, raw_input().split())

	i, _ = next((i, b) for i, (a, b) in enumerate(zip(vs, vs[1:])) if a != b)
	p, q = vs[i:(i + 2)]

	rs = deque()
	rs.append(p / gcd(p, q))
	for v in vs[i:]: rs.append(v / rs[-1])
	for v in reversed(vs[:i]): rs.appendleft(v / rs[0])

	ls = dict(zip(sorted(set(rs)), a))
	s = "".join(map(ls.get, rs))
	
	print "Case #{}: {}".format((x + 1), s)

"""
from fractions import gcd
from copy import deepcopy
import string
a = string.ascii_uppercase
t = int(raw_input())
for x in xrange(t):
	n, l = map(int, raw_input().split())
	vs = map(int, raw_input().split())
	p = gcd(vs[0], vs[1])
	ps = [(vs[0] / p), p, (vs[1] / p)]
	for i in range(2, l): ps.append(vs[i] / ps[i])
	pc = deepcopy(ps)
	pc = list(set(pc))
	pc.sort()	
	s = "".join(a[pc.index(v)] for v in ps)
	print "Case #{}: {}".format((x + 1), s)
"""
