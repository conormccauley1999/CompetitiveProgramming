# Problem 61

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from itertools import permutations

def isCyclic(a, b):
    return str(a)[2:] == str(b)[:2]

def findCycle(pa, pb, pc, pd, pe, pf):
    for a in pa:
        for b in pb:
            if not isCyclic(a, b): continue
            for c in pc:
                if not isCyclic(b, c): continue
                for d in pd:
                    if not isCyclic(c, d): continue
                    for e in pe:
                        if not isCyclic(d, e): continue
                        for f in pf:
                            if not isCyclic(e, f): continue
                            if isCyclic(f, a):
                                return True, (a + b + c + d + e + f)
    return False, 0

p3 = []
for i in range(1, 150):
    n = int(getTriangularNumber(i))
    if n >= 1000 and n < 10000: p3.append(n)
p4 = []
for i in range(1, 150):
    n = int(getSquareNumber(i))
    if n >= 1000 and n < 10000: p4.append(n)
p5 = []
for i in range(1, 150):
    n = int(getPentagonalNumber(i))
    if n >= 1000 and n < 10000: p5.append(n)
p6 = []
for i in range(1, 150):
    n = int(getHexagonalNumber(i))
    if n >= 1000 and n < 10000: p6.append(n)
p7 = []
for i in range(1, 150):
    n = int(getHeptagonalNumber(i))
    if n >= 1000 and n < 10000: p7.append(n)
p8 = []
for i in range(1, 150):
    n = int(getOctagonalNumber(i))
    if n >= 1000 and n < 10000: p8.append(n)

p = [p3, p4, p5, p6, p7, p8]
x = [0, 1, 2, 3, 4, 5]

prms = list(permutations(x))

for prm in prms:
    res = findCycle(p[prm[0]], p[prm[1]], p[prm[2]], p[prm[3]], p[prm[4]], p[prm[5]])
    if res[0]:
        print res[1]
        break
