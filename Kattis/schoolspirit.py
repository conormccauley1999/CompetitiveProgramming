n = int(input())
ss = []
for _ in range(n):
    ss.append(int(input()))
ss.sort(reverse=True)
gs = 0.2 * sum(ss[i] * (0.8 ** i) for i in range(n))
sm = 0
for i in range(n):
    _ss = ss.copy()
    del _ss[i]
    _ss.sort(reverse=True)
    sm += 0.2 * sum(_ss[j] * (0.8 ** j) for j in range(n - 1))
print(gs)
print(sm / n)
