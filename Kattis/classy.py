def f():
    n = int(input())
    ps = []
    for _ in range(n):
        xs = input().split()
        p = xs[0][:-1]
        rs = xs[1].split('-')[::-1]
        ss = 0
        for r in rs:
            ss *= 10
            if r == 'upper':
                ss += 3
            elif r == 'middle':
                ss += 2
            else:
                ss += 1
        while len(str(ss)) != 10:
            ss *= 10
            ss += 2
        ss *= -1
        ps.append((ss, p))
    for p in sorted(ps):
        print(p[1])
    print('=' * 30)

t = int(input())
for _ in range(t):
    f()
