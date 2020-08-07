def f():
    l, r = map(int, input().split())
    print(((l + r) * (l + r + 1) // 2) + 1 + r)

for _ in range(int(input())):
    f()
