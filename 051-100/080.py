# Problem 80

from numpy import sqrt

sm = 0
for n in range(1, 100):
	if n in [1, 4, 9, 16, 25, 36, 49, 64, 81]: continue
	r = str(sqrt(n))[:100].replace(".", "")
	sm += sum(int(d) for d in r)
print sm
