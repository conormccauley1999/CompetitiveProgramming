# Problem 73

from math import floor, ceil
from fractions import gcd

mn = 1.0 / 3.0
mx = 0.5

c = 0

for d in range(1, 12001):
    mnN = int(ceil(d * mn))
    mxN = int(floor(d * mx))
    for n in range(mnN, mxN+1):
        if gcd(n, d) == 1:
            v = float(n) / float(d)
            if v > mn and v < mx: c += 1

print c
