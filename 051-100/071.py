# Problem 71

from math import floor
from fractions import gcd

r = 0
mx = int(floor(1000000.0 / 7.0))
for i in xrange(mx, 1, -1):
    n = (i * 3) - 1
    d = i * 7
    if gcd(n, d) == 1:
        r = n
        break
print n
