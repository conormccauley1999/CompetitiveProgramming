t = int(input())
for _ in range(t):
    input()
    c, e = map(int, input().split())
    cs = list(map(int, input().split()))
    es = list(map(int, input().split()))
    ac = sum(cs) / c
    ae = sum(es) / e
    cnt = 0
    for i in range(c):
        nac = ((ac * c) - cs[i]) / (c - 1)
        nae = ((ae * e) + cs[i]) / (e + 1)
        if nac > ac and nae > ae:
            cnt += 1
    print(cnt)
