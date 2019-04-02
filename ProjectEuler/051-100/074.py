# Problem 74

from math import factorial

cache = {}
fs = []

for i in range(0, 10):
	fs.append(factorial(i))

def getChainLen(n):
	ts = set()
	ts.add(n)
	cl = 1
	while True:
		m = sum(fs[d] for d in [int(x) for x in list(str(n))])
		if m in cache: return cl + cache[m]
		if m in ts: return cl
		ts.add(m)
		n = m
		cl += 1

c = 0
for n in xrange(1, 1000000):
	cl = getChainLen(n)
	cache[n] = cl
	if cl == 60: c += 1
print c
