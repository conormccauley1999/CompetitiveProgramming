# Problem 145

from math import floor, log10
odd = [1, 3, 5, 7, 9]

oddCache = set()
def allOdd(n):
    if n in oddCache: return True
    while n != 0:
        if n % 10 not in odd: return False
        n //= 10
    oddCache.add(n)
    return True

def rev(n):
    lg = -1
    m = n
    while m > 0:
        m //= 10
        lg += 1
    sm = 0
    while n != 0:
        sm += (n % 10) * (10 ** lg)
        lg -= 1
        n //= 10
    return sm

revCache = set()
def isReversable(n):
    if n % 10 == 0: return False
    if n in revCache: return True
    r = rev(n)
    s = n + r
    if allOdd(s):
        revCache.add(n)
        revCache.add(r)
        return True
    return False

def main():
    totalRev = 0
    for n in xrange(1000000000):
        if isReversable(n): totalRev += 1
        if n % 1000000 == 0: print n, totalRev
    return totalRev

print main()
