# Problem 110

from sympy.ntheory import sieve

COUNT = 13
MAX_POW = 4
LIM = 4000000

sieve.extend_to_no(COUNT)
primes = list(sieve._list[:COUNT])

def f(powers):
    n = 1
    for i in range(COUNT):
        n *= pow(primes[i], powers[i])
    return n

def g(powers):
    d = 1
    for i in range(COUNT):
        d *= (2 * powers[i]) + 1
    return (d // 2) + 1

powers = [0] * COUNT
mn = 10 ** 20

mx = pow(MAX_POW, COUNT)
for i in range(mx):
    _i = i
    for j in range(COUNT):
        powers[j] = _i % MAX_POW
        _i //= MAX_POW
    if g(powers) > LIM:
        mn = min(mn, f(powers))
print(mn)
