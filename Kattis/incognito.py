def sol():
    n = int(input())
    d = {}
    for _ in range(n):
        a, c = input().split()
        if c not in d: d[c] = ["none"]
        d[c].append(a)
    m = 1
    for c in d: m *= len(d[c])
    return m - 1

t = int(input())
for _ in range(t):
    print(sol())
