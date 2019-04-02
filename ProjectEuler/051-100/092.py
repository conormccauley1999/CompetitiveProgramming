# Problem 92

cache_1 = set([])
cache_89 = set([])

def chain(n):
    r = 0
    for d in str(n):
        r += (int(d) ** 2)
    return r

def main():    
    total = 0
    for n in range(1, 10000000):
        r = n
        while r != 1 and r != 89:
            r = chain(r)
            if r in cache_1: r = 1
            elif r in cache_89: r = 89
        if r == 89:
            total += 1
            cache_89.add(n)
        else:
            cache_1.add(n)
        if n % 100000 == 0: print n
    return total

print main()
