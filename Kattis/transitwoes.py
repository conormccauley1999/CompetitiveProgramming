s, t, n = map(int, input().split())
ds = tuple(map(int, input().split()))
bs = tuple(map(int, input().split()))
cs = tuple(map(int, input().split()))
x = s
for i in range(len(bs)):
    x += ds[i]
    if x % cs[i]:
        x += (cs[i] * (1 + (x // cs[i]))) - x
    x += bs[i]
x += ds[-1]
print('yes' if x <= t else 'no')
