from decimal import *

n = int(raw_input())
m, s = Decimal(0), Decimal(0)

for _ in xrange(n):
	i = raw_input().split()
	m += Decimal(i[0])
	s += Decimal(i[1])

r = s / (m * Decimal(60))

if r <= Decimal(1.0): print "measurement error"
else: print r
