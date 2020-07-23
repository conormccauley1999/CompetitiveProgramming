import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom

n = int(input())
for _ in range(n):
    r, s, x, y, w = map(int, input().split())
    p = (s - r + 1) / s
    q = sum((p ** _x) * ((1 - p) ** (y - _x)) * ncr(y, _x) for _x in range(x, y + 1))
    if q * (w - 1) > (1 - q):
        print("yes")
    else:
        print("no")
