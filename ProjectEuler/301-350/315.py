MN, MX = int(1e7), int(2e7)

ps = [True] * (MX + 1)
ps[0] = ps[1] = False
p = 2
while p * p <= MX:
    if ps[p]:
        for q in range(p * 2, MX + 1, p):
            ps[q] = False
    p += 1

CODE = [
    [1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,1,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]
]

TRNA = [sum(c) for c in CODE]
TRNB = []
for i in range(10):
    c = []
    for j in range(10):
        if i == j:
            c.append(0)
        else:
            c.append(sum(abs(CODE[i][k] - CODE[j][k]) for k in range(7)))
    TRNB.append(c)

st, mt = 0, 0
for i in range(MN, MX + 1):
    if ps[i]:
        j = i
        s, m = 0, 0
        for d in map(int, str(j)):
            m += TRNA[d]
        while j > 9:
            x = 0
            for d in map(int, str(j)):
                x += d
                s += TRNA[d]
            o, n = str(j)[::-1], str(x)[::-1]
            lo, ln = len(o), len(n)
            for i in range(lo):
                if i < ln:
                    m += TRNB[int(o[i])][int(n[i])]
                else:
                    m += TRNA[int(o[i])]
            j = x
        s += TRNA[j]
        m += TRNA[j]
        s *= 2
        st += s
        mt += m

print(st - mt)
