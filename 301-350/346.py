# Problem 346

mx = 10 ** 12
reps = set()

def getRepunit(x, n):
    sm = 1
    k = 1
    while k <= n:
        sm += x ** k
        if sm >= mx: return 0
        k += 1
    return sm

def main():
    sm = 1
    x = 2
    while x <= 999999:
        n = 2
        while n <= 39:
            v = getRepunit(x, n)
            if v not in reps:
                reps.add(v)
                sm += v
            n += 1
        x += 1
    return sm

print main()
