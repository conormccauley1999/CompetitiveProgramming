n = int(input())
vs = []
for _ in range(n):
    vs.append(int(input()))
c = 0
while len(vs):
    ds = [vs[0]]
    for i in range(1, len(vs)):
        if vs[i - 1] < vs[i]:
            ds.append(vs[i])
        else:
            break
    for i in ds:
        vs.remove(i)
    c += 1
print(c)
