from functools import reduce
def hull(cs):
    tl, tr, tn = 1, -1, 0
    def cmp(a, b):
        return (a > b) - (a < b)
    def trn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)
    def klft(hl, r):
        while len(hl) > 1 and trn(hl[-2], hl[-1], r) != tl:
            hl.pop()
        if not len(hl) or hl[-1] != r:
            hl.append(r)
        return hl
    cs.sort()
    l = reduce(klft, cs, [])
    u = reduce(klft, reversed(cs), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

def dist(a, b):
    return pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 0.5)

n = int(input())
cs = []
for _ in range(n): cs.append(tuple(map(int, input().split())))
hs = hull(cs)
mx = 0
for i in range(len(hs)):
    for j in range(i + 1, len(hs)):
        mx = max(mx, dist(hs[i], hs[j]))
print(mx)
