# Problem 27

from common import *

print len(primesLessThan(1000))

"""
maxN = 0
prod = 0

for b in range(-1000, 1001):
    if not isPrime(b): continue
    for a in range(-999, 1000):
        n, x = 0, b
        while isPrime(x):
            x = (n * n) + (a * n) + b
            n += 1
        if n > maxN:
            maxN, prod = n, a * b

print prod
"""
