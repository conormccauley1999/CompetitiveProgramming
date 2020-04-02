R, C = map(int, input().split())
G = [input() for _ in range(R)]
V = set()

def gn(p):
    ns = []
    if p[0] > 0: ns.append((p[0] - 1, p[1]))
    if p[0] < (C - 1): ns.append((p[0] + 1, p[1]))
    if p[1] > 0: ns.append((p[0], p[1] - 1))
    if p[1] < (R - 1): ns.append((p[0], p[1] + 1))
    return ns

def f(p):
    global V
    ns = gn(p)
    for n in ns:
        if n in V or G[n[1]][n[0]] == 'W': continue
        V.add(n)
        f(n)

def sol():
    global V
    ac = True
    for r in G:
        for c in r:
            ac &= (c == 'C' or c == 'W') 
    if ac: return 0
    s = 0
    for x in range(C):
        for y in range(R):
            if G[y][x] == 'W' or G[y][x] == 'C': continue
            p = (x, y)
            if p not in V:
                s += 1
                V.add(p)
                f(p)
    return s

print(sol())
