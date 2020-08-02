from collections import Counter

_f = { 0: 1 }
def f(n):
    if n not in _f:
        _f[n] = n * f(n - 1)
    return _f[n]

def g(s):
    cs = Counter(s)
    vs = cs.values()
    l = len(s)
    r = f(l)
    for v in vs:
        r //= f(v)
    return r

while True:
    try:
        i = input()
        print(g(i))
    except:
        break
