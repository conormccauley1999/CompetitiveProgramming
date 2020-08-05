import copy

def f():
    n = int(input())
    ws = list(map(int, input().split()))
    mx = 0
    e = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = ws[i] + ws[j]
            if s not in e:
                e[s] = set([])
            e[s].add((i, j,))
    for k in e:
        used = set([])
        t = 0
        for p in e[k]:
            if p[0] in used or p[1] in used:
                continue
            used.add(p[0])
            used.add(p[1])
            t += 1
        mx = max(mx, t)
    return mx

t = int(input())
for _ in range(t):
    print(f())
