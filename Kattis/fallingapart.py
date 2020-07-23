n = int(input())
vs = sorted(list(map(int, input().split())))
a, b = 0, 0
t = True
while n:
    if t:
        a += vs[n - 1]
    else:
        b += vs[n - 1]
    n -= 1
    t = not t
print(a, b)
