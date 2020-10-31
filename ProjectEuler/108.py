# Problem 108

from sympy import divisors

f = lambda n: (len(divisors(n * n)) // 2) + 1

n = 5
while f(n) <= 1000:
    n += 1
print(n)
