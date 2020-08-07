def f():
    n, sl, tl = input().split()
    sb, tb = len(sl), len(tl)
    ds = n[::-1]
    b10 = 0
    m = 1
    for i in range(len(ds)):
        b10 += sl.index(ds[i]) * m
        m *= sb
    bo = 0
    if b10 == 0:
        return tl[0]
    ns = []
    while b10:
        b10, r = divmod(b10, tb)
        ns.append(tl[r])
    return ''.join(reversed(ns))

for n in range(int(input())):
    print(f'Case #{n + 1}: {f()}')
