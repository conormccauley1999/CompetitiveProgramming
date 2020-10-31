# Problem 99

from math import log10

with open("../files/99.txt") as f:
    lns = f.readlines()

lns = [ln.strip() for ln in lns]

mx = 0
mxLn = 0

for i in range(0, len(lns)):
    n = [int(x) for x in lns[i].split(',')]
    v = n[1] * log10(n[0])
    if v > mx:
        mx = v
        mxLn = i

print mx, mxLn + 1
