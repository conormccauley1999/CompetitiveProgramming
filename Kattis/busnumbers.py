n = int(input())
vs = list(map(int, input().split()))
bs = [False] * 1001
for v in vs:
    bs[v] = True
rs = []
i = 1
while i <= 1000:
    if bs[i]:
        s = i
        e = i
        i += 1
        while i <= 1000 and bs[i]:
            i += 1
            e += 1        
        if s + 1 == e:
            rs.append(s)
            rs.append(e)
        elif s != e:
            rs.append(f'{s}-{e}')
        else:
            rs.append(s)
    i += 1
print(*rs)
