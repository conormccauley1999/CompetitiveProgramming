# Problem 347

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from math import log, floor

def main(N):
    primes = list(npPrimesLessThan(N / 2))
    len_primes = len(primes)
    sm = 0
    for i in xrange(0, (len_primes - 1)):
        for j in xrange((i + 1), len_primes):
            p, q = primes[i], primes[j]
            if p * q > N:
                if j == (i + 1): return int(sm)
                break
            lrgst = 0
            flr = N // q
            v_p = p
            while v_p <= flr:
                e = floor(log(floor(N / v_p), q))
                v_q = v_p * (q ** e)
                if v_q > lrgst: lrgst = v_q 
                v_p *= p
            sm += lrgst
    return int(sm)
print main(10000000)
