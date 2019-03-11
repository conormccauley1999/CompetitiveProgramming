# Problem 22

import string

ns = open("../files/22.txt").read().replace('"', '').split(',')
ns.sort()

s = 0

for n in ns:
	v = 0
	for c in n: v += (string.ascii_lowercase.index(c.lower()) + 1)
	s += v * (ns.index(n) + 1)

print s
