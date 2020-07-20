def f(g, a, x, y):
    c = 0
    for i in range(x, x + a):
        for j in range(y, y + a):
            if g[j][i] == '*':
                c += 1
    return c
r, s, k = map(int, input().split())
g = []
for _ in range(r):
    g.append(list(input()))
mx = 0
mxc = (1, 1)
for x in range(1, s - k + 2):
    for y in range(1, r - k + 2):
        c = f(g, k - 2, x, y)
        if c > mx:
            mx = c
            mxc = (x - 1, y - 1,)
g[mxc[1]][mxc[0]] = '+'
g[mxc[1]][mxc[0] + k - 1] = '+'
g[mxc[1] + k - 1][mxc[0]] = '+'
g[mxc[1] + k - 1][mxc[0] + k - 1] = '+'
for x in range(mxc[0] + 1, mxc[0] + k - 1):
    g[mxc[1]][x] = '-'
    g[mxc[1] + k - 1][x] = '-'
for y in range(mxc[1] + 1, mxc[1] + k - 1):
    g[y][mxc[0]] = '|'
    g[y][mxc[0] + k - 1] = '|'
print(mx)
for _ in g:
    print(''.join(_))
