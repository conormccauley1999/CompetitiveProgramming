# Doesn't pass: TLE

from math import log10

def a(f):
    x = 1
    while f != 1:
        x += 1
        f /= x
    return x

f = int(input())
d = len(str(f))
if d < 4:
    print(a(f))
    quit()
n = 7
sm = sum(log10(x) for x in range(2, n))
while True:
    sm += log10(n)
    n += 1
    if sm > d:
        print(n - 2)
        break
