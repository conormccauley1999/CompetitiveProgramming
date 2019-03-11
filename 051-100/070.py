# Problem 70

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

lops = npPrimesLessThan(getRoot(10000000))
ps = npPrimesLessThan(5000000)
hips = set()
for p in ps:
	if p not in lops: hips.add(p)

mnR = 99999999999999
mnN = 0

for p in lops:
    for q in hips:
        pq = p * q
        if pq > 10000000: continue
        ph = (p - 1) * (q - 1)
        if isPerm(pq, ph):
            r = float(pq) / float(ph)
            if r < mnR:
                mnR = r
                mnN = pq
                print p, q, mnN, ph, mnR

print mnR, mnN
