# Problem 187

from sympy import sieve
sieve.extend_to_no(3000000)
primes = sorted(sieve._list)
M = 10 ** 8
c = 0
for i in range(len(primes)):
    for j in range(i, len(primes)):
        if primes[i] * primes[j] >= M:
            break
        c += 1
print(c)
