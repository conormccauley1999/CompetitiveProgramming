import sys
from collections import Counter
from decimal import Decimal

sys.setrecursionlimit(1500)

def fr(n):
    r = Decimal(1)
    for i in range(2, int(n) + 1):
        r *= Decimal(i)
    return r

_f = { 0: 1 }
def f(n):
    if n >= 1500:
        return fr(n)
    if n not in _f:
        _f[n] = n * f(n - 1)
    return _f[n]

_b = {}
def b(n, k):
    if (n, k) not in _b:
        _b[(n, k)] = f(n) / (f(k) * f(n - k))
    return _b[(n, k)]

n = Decimal(input())
xs = list(map(Decimal, input().split()))
cs = Counter(xs)
t = sum(xs)
p = f(t)
for x in xs:
    p /= f(x)
for _ in range(int(t)):
    p /= Decimal(365)

p *= b(Decimal(365), n)
p *= f(sum(cs[c] for c in cs))
for c in cs:
    p /= f(cs[c])

print(p.log10())
