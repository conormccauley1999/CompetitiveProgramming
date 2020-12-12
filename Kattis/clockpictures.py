n = int(input())
xs = sorted([*map(int, input().split())])
ys = sorted([*map(int, input().split())])
u, v = xs[0], ys[0]
xs = [x - u for x in xs]
ys = [y - v for y in ys]
da = []
db = []
m = 360000
for i in range(n):
    j = (i + 1) % n
    da.append((xs[j] - xs[i]) % m)
    db.append((ys[j] - ys[i]) % m)
def f(a, b):
    N, i, j = len(a), 0, 0
    while i < N and j < N:
        k = 1
        while k <= N and a[(i+k)%N] == b[(j+k)%N]:
            k += 1
        if k > N:
            return True
        if a[(i+k)%N] > b[(j+k)%N]:
            i += k
        else:
            j += k
    return False
if f(da, db):
    print('possible')
else:
    print('impossible')
