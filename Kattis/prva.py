r, c = map(int, input().split())
g = []
for _ in range(r):
    g.append(input())
h = list(map(''.join, zip(*g)))
w = []
for _ in g:
    w.extend(list(filter(lambda s: len(s) > 1, _.split('#'))))
for _ in h:
    w.extend(list(filter(lambda s: len(s) > 1, _.split('#'))))
print(sorted(w)[0])
