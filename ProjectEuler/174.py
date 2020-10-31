# Problem 174

MAX = 1000000
p = lambda x: 4 * (x  - 1)

_c = {}
def c(n):
    if n not in _c:
        _c[n] = 0
    _c[n] += 1

for x in range(MAX, 2, -1):
    t = p(x)
    y = x - 2
    while t <= MAX and y >= 1:
        c(t)
        t += p(y)
        y -= 2

s = 0
for k in _c:
    if _c[k] <= 10:
        s += 1
print(s)
