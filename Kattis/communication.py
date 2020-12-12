n = int(input())
xs = [*map(int, input().split())]
d = {}
for i in range(256):
    v = i ^ (i << 1) % 256
    d[v] = i
print(*[d[x] for x in xs])
