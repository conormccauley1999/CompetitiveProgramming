# Problem 216

from sympy.ntheory.primetest import isprime

c = 0
for n in range(2, 50000001):
    if not n % 1000000:
        print(n)
    if isprime(2*pow(n, 2) - 1):
        c += 1

print(c)
