def f(n):
    r = {}
    for _ in range(n):
        xs = input().split()
        for x in xs[1:]:
            if x not in r:
                r[x] = [xs[0]]
            else:
                r[x].append(xs[0])
    for k in sorted(r.keys()):
        print(k, *sorted(r[k]))

while True:
    n = int(input())
    if n == 0:
        break
    f(n)
    print()
