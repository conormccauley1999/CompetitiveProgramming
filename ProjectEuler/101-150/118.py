M = 987654321

pa = [True] * (M + 1)
p = 2
while p * p <= M:
    if not pa[p]:
        continue
    q = p * p
    while q <= M:
        pa[q] = False
        q += p
    p += 1

ps = set()
for i in range(2, M + 1):
    if pa[i]:
        ps.add(i)

print(sorted(list(ps))[:20])
