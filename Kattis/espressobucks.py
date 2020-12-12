n, m = map(int, input().split())
gs = []
for _ in range(n):
    gs.append(list(input()))
for y in range(n):
    for x in range(m):
        if gs[y][x] == '#': continue
        elif (x > 0 and gs[y][x-1] == 'E') or (y > 0 and gs[y-1][x] == 'E'): continue
        else: gs[y][x] = 'E'

for g in gs:
    print(''.join(g))
