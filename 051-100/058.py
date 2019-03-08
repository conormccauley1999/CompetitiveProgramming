# Problem 58

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from math import ceil

def getDiag(diags, n):
    return diags[n - 2] + (2 * int(ceil((n - 1) / 4.0)))

def main():
    diags = [1]
    diagCount = 1
    primes = []
    primeCount = 0
    sides = 3
    while True:
        for i in range(0, 4):
            diag = getDiag(diags, diagCount + 1)
            diags.append(diag)
            if isPrime(diag):
                primes.append(diag)
                primeCount += 1
            diagCount += 1
        ratio = float(primeCount) / float(diagCount)
        if ratio < 0.1: return sides
        sides += 2
    return -1

print main()
