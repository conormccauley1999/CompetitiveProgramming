# Problem 381

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from math import factorial as f

def k(p):
    n = 1+((p-4)*(1+((p-3)*(1+((p-2)*p)))))
    d = (p-4)*(p-3)*(p-2)*(p-1)
    print n, d
    return n/d

ps = npPrimesLessThan(100000000)

sm = 0
for i in xrange(2, len(ps)):
    p = int(ps[i])
    a = -1 % p
    b = 1 % p
    c = ((p - 1) / 2) % p
    d = (((-1) ** ((p / 3) + 1)) * int((p + 1) / 6)) % p
    h = int(p / 24)
    r = p - (24 * h)
    e = ((r * h) + (((r * r) - 1)/ 24)) % p
    sm += (a + b + c + d + e) % p
    
print sm
