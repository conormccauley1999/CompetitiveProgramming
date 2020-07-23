def f(n):
    x = n
    ds = []
    while n:
        ds.append(n % 10)
        n //= 10
    if len(set(ds)) != 6:
        return 0
    for d in ds:
        if d == 0:
            return 0
        elif x % d != 0:
            return 0
    return 1

l, h = map(int, input().split())
c = 0
for n in range(l, h + 1):
    c += f(n)
print(c)
