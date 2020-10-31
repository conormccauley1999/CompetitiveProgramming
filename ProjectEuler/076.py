# Problem 76

from math import floor

cache = {}

def w(t, n):
    if t == 0 or n == 1:
        return 1
    else:
        s = 0
        for i in range(0, int(floor(float(t) / float(n))) + 1):
            x = t - (i * n)
            y = n - 1
            if (x, y) in cache:
                v = cache[(x, y)]
            else:
                v = w(x, y)
                cache[(x, y)] = v
            s += v
        return s

print w(100, 100)
