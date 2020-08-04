from collections import Counter

n = int(input())
vs = list(map(int, input().split()))
cs = Counter(vs)

mx = -1
for x in cs:
    if cs[x] == 1:
        mx = max(mx, x)
if mx == -1:
    print('none')
else:
    print(vs.index(mx) + 1)
