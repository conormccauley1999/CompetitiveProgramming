from sympy import divisors

N = 60

def g(d, n):
    for i in range(1, n):
        if pow(2, i) % d == 1:
            return 0
    return d + 1

print(sum(g(d, N) for d in divisors(pow(2, N) - 1)))
