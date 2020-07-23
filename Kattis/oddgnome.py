def f():
    vs = list(map(int, input().split()))
    n, gs = vs[0], vs[1:]
    for i in range(1, n - 1):
        if gs[i - 1] + 1 != gs[i]:
            return i + 1
t = int(input())
for _ in range(t):
    print(f())
