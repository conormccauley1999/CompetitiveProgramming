n, t = map(int, input().split())
vs = list(map(int, input().split()))
x = 0
for i in range(n):
    x += vs[i]
    if x > t:
        print(i)
        quit()
print(n)
