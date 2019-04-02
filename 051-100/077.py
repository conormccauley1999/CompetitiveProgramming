# Problem 77

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

mx = 100
ps = list(npPrimesLessThan(mx + 1))

ws = [0] * (mx + 1)
ws[0] = 1
for i in xrange(0, len(ps)):
	for j in xrange(ps[i], (mx + 1)):
		ws[j] += ws[j - ps[i]]

for x in range(0, (mx + 1)):
	if ws[x] > 5000:
		print x
		break
