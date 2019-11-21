n = int(input())
ax = [input() for _ in range(n)]
ay = [""] * n
r = True

for i in range(n):
    for j in range(n):
        ay[i] += ax[j][i]

for i in range(n):
    r &= ax[i].count("W") == (n / 2)
    r &= ay[i].count("W") == (n / 2)
    r &= ax[i].count("WWW") == 0
    r &= ay[i].count("WWW") == 0
    r &= ax[i].count("BBB") == 0
    r &= ay[i].count("BBB") == 0

print(1 if r else 0)
