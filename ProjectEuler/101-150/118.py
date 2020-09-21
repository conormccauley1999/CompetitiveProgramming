# Problem 118

from copy import deepcopy
from itertools import permutations
from sympy.ntheory import isprime

ns = []
for l in range(1, 10):        
    for p in permutations(range(1, 10), r=l):
        n = 0
        for d in p:
            n *= 10
            n += d
        ns.append(n)

vs = [n for n in ns if isprime(n)]
ds = [set(map(int, str(v))) for v in vs]
mi = len(vs)
rs = set()
def f(i, cv, cd):
    global vs, mi, rs, ds
    if len(cd) == 9:
        rs.add(frozenset(cv))
        return
    for j in range(i, mi):
        v, d = vs[j], ds[j]
        if not cd.isdisjoint(d):
            continue
        _cv = deepcopy(cv)
        _cv.add(v)
        _cd = cd | d
        f(j + 1, _cv, _cd)

f(0, set(), set())
print(len(rs))
