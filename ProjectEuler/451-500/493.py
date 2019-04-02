# Problem 493

from math import factorial as f

def nCr(n, r):
    return float(f(n)) / (f(r) * f(n - r))

def main():
    return round(7 * (1 - (nCr(60, 20) / nCr(70, 20))), 9)

print main()
