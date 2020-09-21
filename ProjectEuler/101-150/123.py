# Problem 123

from sympy import sieve
sieve.extend_to_no(100000)

ps = sieve._list
mx = 10 ** 10

for n in range(1, len(ps) + 1):
    if not n % 1000:
        print(n)
    p = ps[n - 1]
    r = (pow(p - 1, n) + pow(p + 1, n)) % pow(p, 2)
    if r > mx:
        print(n)
        quit()
