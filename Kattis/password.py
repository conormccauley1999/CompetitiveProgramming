n = int(input())
ps = []
for _ in range(n):
    _, p = input().split()
    ps.append(float(p))
ps.sort(reverse=True)
print(sum(ps[i] * (i + 1) for i in range(n)))
