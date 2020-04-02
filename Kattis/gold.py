W, H = map(int, input().split())
G = []
P = (0, 0)
for y in range(H):
    i = input()
    if 'P' in i: P = (i.index('P'), y)
    G.append(i)
S = 0
V = set()

def g(x, y):
    return G[y][x]

def gn(p):
    ns = []
    if p[0] > 0: ns.append((p[0] - 1, p[1]))
    if p[0] < (W - 1): ns.append((p[0] + 1, p[1]))
    if p[1] > 0: ns.append((p[0], p[1] - 1))
    if p[1] < (H - 1): ns.append((p[0], p[1] + 1))
    return ns

def dr(ns):
    d = False
    for n in ns:
        d |= (g(n[0], n[1]) == 'T')
    return d

def f(p):
    global S, V
    if p in V: return
    V.add(p)
    t = g(p[0], p[1])
    if t == '#' or t == 'T': return
    elif t == 'G':
        S += 1
    ns = gn(p)
    if dr(ns):
        return
    for n in ns:
        f(n)

if not dr(gn(P)): f(P)
print(S)
