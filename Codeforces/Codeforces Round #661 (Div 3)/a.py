def f():
    n = int(input())
    vs = sorted(map(int, input().split()))
    if len(vs) == 1:
        return "YES"
    for i in range(1, n):
        if abs(vs[i - 1] - vs[i]) > 1:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(f())
