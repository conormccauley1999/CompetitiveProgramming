n = int(input())
vs = list(map(int, input().split()))
c, w = 1, vs[0]
for v in vs[1:]:
    if v > w:
        c += 1
    w = v
print(c)
