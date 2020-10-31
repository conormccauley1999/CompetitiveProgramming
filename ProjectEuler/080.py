# Problem 80

from decimal import *
getcontext().prec = 103

sm = 0

for n in range(1, 100):
	if n in [1, 4, 9, 16, 25, 36, 49, 64, 81]: continue
	r = str(Decimal(n).sqrt()).replace(".", "")[:100]
	sm += sum(int(d) for d in r)

print sm
