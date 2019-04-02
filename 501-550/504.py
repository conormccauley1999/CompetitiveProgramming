# Problem 504

from fractions import gcd

m = 100
squares = set()
for i in range(0, 2*m):
    squares.add((i+1)**2)

g = {}
for x in range(1, m+1):
    for y in range(x, m+1):
        z = gcd(x, y)
        g[(x, y)] = z
        g[(y, x)] = z

def gcdc(x, y):
    return g[(x, y)]

total = 0
for a in range(1, m+1):
    print a
    for b in range(1, m+1):
        for c in range(1, m+1):
            for d in range(1, m+1):
                A = 0.5 * (a + c) * (b + d)
                p = gcdc(a, b) + gcdc(a, d) + gcdc(c, b) + gcdc(c, d)
                i = int((A + 1) - (0.5 * p))
                if i in squares: total += 1

print total
