n, p = map(int, input().split())
vs = list(map(int, input().split()))
for i in range(n):
    vs[i] -= p
mx = -10e8
mxh = 0
for i in range(n):
    mxh = mxh + vs[i]
    mx = max(mx, mxh)
    mxh = max(mxh, 0)
print(mx)
