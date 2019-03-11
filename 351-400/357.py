# Problem 357

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from math import sqrt, floor

ps = set(npPrimesLessThan(100000001))

def isPGI(n):
    for i in range(1, (int(floor(sqrt(n))) + 1)):
        if n % i == 0:
            if (i + (n / i)) not in ps: return False
    return True

def main():
    
    r = 0
    
    for p in ps:
        n = p - 1
        if n % 4 != 0 and isPGI(n):
            r += n
    
    return r

print main()
