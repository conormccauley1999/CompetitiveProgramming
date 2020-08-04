c, n = map(int, input().split())
k = 0
for i in range(n):
    l, e, s = map(int, input().split())
    if l > k:
        print('impossible')
        quit()
    if k + (e - l) > c:
        print('impossible')
        quit()
    k -= l
    k += e
    x = c - k
    if s != 0 and x != 0:
        print('impossible')
        quit()
    if i == n - 1 and k != 0:
        print('impossible')
        quit()
print('possible')
