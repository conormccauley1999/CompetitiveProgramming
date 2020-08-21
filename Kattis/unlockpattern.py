from math import sqrt
gs = []
for _ in range(3):
    gs.extend(list(map(int, input().split())))
cs = []
for i in range(1, 10):
    ix = gs.index(i)
    cs.append((ix % 3, ix // 3))
d = 0
for i in range(8):
    d += sqrt(abs(cs[i][0] - cs[i+1][0])**2 + abs(cs[i][1] - cs[i+1][1])**2)
print(d)
