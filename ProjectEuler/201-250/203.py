from sympy import sieve

M = 51
t = []
s = set([1])
for n in range(M):
    r = [1]
    for k in range(1, n + 1):
        if k == n:
            r.append(1)
        else:
            v = t[n - 1][k - 1] + t[n - 1][k]
            s.add(v)
            r.append(v)
    t.append(r)

sieve.extend_to_no(int(max(s) ** 0.5) // 8)
primes = sorted(sieve._list)
nums = sorted([*s])

sm = 0
for num in nums:
    f = True
    for prime in primes:
        p2 = prime * prime
        if p2 > num:
            break
        elif num % p2 == 0:
            f = False
            break
    if f:
        sm += num
print(sm)
