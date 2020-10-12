# Problem 243

from sympy.ntheory import sieve

def calc(primes, powers):
    n = 1
    for i in range(COUNT):
        n *= pow(primes[i], powers[i])
    return n

def totient(n, primes, powers):
    t = n
    for i in range(COUNT):
        if not powers[i]:
            continue
        t *= (primes[i] - 1)
        t //= primes[i]
    return t

COUNT = 20
MAX_POW = 5
R = 15499 / 94744

sieve.extend_to_no(COUNT)
primes = list(sieve._list[:COUNT])

powers = [0] * COUNT
mn = 10 ** 10

mx = pow(COUNT, MAX_POW)
for i in range(mx):
    if not i % 10000:
        print(i, mn, mx)
    _i = i
    for j in range(COUNT):
        powers[j] = _i % MAX_POW
        _i //= MAX_POW
    n = calc(primes, powers)
    if n == 1:
        continue
    r = totient(n, primes, powers) / (n - 1)
    if r < R:
        mn = min(n, mn)
