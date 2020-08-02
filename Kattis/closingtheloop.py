def f():
    _ = input()
    xs = input().split()
    rs = []
    bs = []
    for x in xs:
        if x[-1] == 'R':
            rs.append(int(x[:-1]))
        else:
            bs.append(int(x[:-1]))
    rs.sort(reverse=True)
    bs.sort(reverse=True)
    c = True
    if len(rs) < len(bs):
        c = False
    m = min(len(rs), len(bs))
    rs = rs[:m]
    bs = bs[:m]
    t = 0
    while True:
        if c:
            if not len(rs):
                break
            t += rs[0] - 1
            rs.pop(0)
        else:
            if not len(bs):
                break
            t += bs[0] - 1
            bs.pop(0)
        c = not c
    return t

t = int(input())
for i in range(t):
    print(f'Case #{i + 1}: {f()}')
