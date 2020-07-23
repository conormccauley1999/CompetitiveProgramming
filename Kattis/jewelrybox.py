t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    f = lambda h: h * (x - (2 * h)) * (y - (2 * h))
    p = 0.0000001
    l, r = 0.0, 0.5 * min(x, y)
    while abs(r - l) >= p:
        lt = l + (r - l) / 3.0
        rt = r - (r - l) / 3.0
        if f(lt) < f(rt):
            l = lt
        else:
            r = rt
    print(f((l + r) / 2.0))
