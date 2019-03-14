# Problem 87

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

v = 50000000

rt = getRoot(v)
ps = set(npPrimesLessThan(rt))
ps2, ps3, ps4 = set(), set(), set()

for p in ps:
	x = p
	p *= x
	ps2.add(p)
	p *= x
	if p > v: continue
	ps3.add(p)
	p *= x
	if p > v: continue
	ps4.add(p)

t = set()

for p1 in ps2:
	for p2 in ps3:
		for p3 in ps4:
			x = p1 + p2 + p3
			if x < v: t.add(p1 + p2 + p3)

print len(t)
