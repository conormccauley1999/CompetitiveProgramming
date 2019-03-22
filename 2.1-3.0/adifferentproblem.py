from sys import stdin
for l in stdin:
	i = [int(v) for v in l.split()]
	print abs(i[0] - i[1])