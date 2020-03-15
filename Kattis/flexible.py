w, p = map(int, input().split())
ls = [0] + list(map(int, input().split())) + [w]
r = set()
for g in range(1, len(ls)):
    for i in range(0, len(ls) - g):
        r.add(ls[i + g] - ls[i])
print(*sorted(list(r)))
