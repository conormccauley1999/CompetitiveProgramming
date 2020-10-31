# Problem 387

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

cache = set()

def sumDigits(n):
    sm = 0
    while n != 0:
        sm += n % 10
        n //= 10
    return sm

pc = set()
def isPrime2(n):
    if n in pc: return True
    elif not isPrime(n): return False
    else:
        pc.add(n)
        return True

hc = set()
def isHarshad(n, s):
    if n in hc: return True
    elif n % s != 0: return False
    else:
        hc.add(n)
        return True

sc = set()
def isStrong(n, s):
    if n in sc: return True
    elif (not isHarshad(n, s)) or (not isPrime2(n / s)): return False
    else:
        sc.add(n)
        return True

def main():

    num = range(0, 10)
    odd = range(1, 10, 2)
    
    sm = 0
    
    curLen = 2
    curHar = []

    for n in range(10, 100):
        s = sumDigits(n)
        if isHarshad(n, s): curHar.append(n)

    for h in curHar:
        s = sumDigits(h)
        if isStrong(h, s):
            t = h * 10
            for d in odd:
                n = t + d
                if isPrime2(n): sm += n
    
    while curLen < 15:

        newHar = []
        
        for h in curHar:
            t = h * 10
            for d in num:
                n = t + d
                s = sumDigits(n)
                if isHarshad(n, s):
                    newHar.append(n)
        
        for h in newHar:
            s = sumDigits(h)
            if isStrong(h, s):
                t = h * 10
                for d in odd:
                    n = t + d
                    if n < 100000000000000 and isPrime2(n) and n not in cache:
                        sm += n
                        cache.add(n)
        
        curHar = newHar
        curLen += 1
        print "all less than 10 ^", curLen+1, sm
    
    return sm

print main()
