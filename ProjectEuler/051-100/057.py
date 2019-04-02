# Problem 57

import sys
sys.setrecursionlimit(1100)

a_cache = [0] * 1000
b_cache = [0] * 1000
a_cache[0] = 3
b_cache[0] = 2

def a(n):
    c = a_cache[n - 1]
    if c != 0: return c
    a_v = 3 if n == 1 else b(n) + b(n - 1)
    a_cache[n - 1] = a_v
    return a_v

def b(n):
    c = b_cache[n - 1]
    if c != 0: return c
    b_v = 2 if n == 1 else b(n - 1) + a(n - 1)
    b_cache[n - 1] = b_v
    return b_v

def ab(n):
    return len(str(a(n))), len(str(b(n)))

def main():

    amount = 0

    for n in range(1, 1001):
        a, b = ab(n)
        amount += 1 if a > b else 0

    return amount

print main()
