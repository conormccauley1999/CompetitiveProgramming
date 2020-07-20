def f(n):
    a, b = [], []
    for _ in range(n):
        a.append(int(input()))
    for _ in range(n):
        b.append(int(input()))
    sa, sb = sorted(a), sorted(b)
    r = []
    for x in a:
        r.append(sb[sa.index(x)])
    for x in r:
        print(x)
    print()


while True:
    n = int(input())
    if n == 0:
        break
    f(n)
