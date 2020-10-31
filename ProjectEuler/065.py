# Problem 65

def sd(n):
    
    sm = 0

    while n != 0:
        sm += n % 10
        n //= 10
    
    return sm

def lst(n):
    
    d = []
    k = 1
    
    for i in range(1, n + 1):
        if (i - 2) % 3 == 0:
            d.append(2 * k)
            k += 1
        else:
            d.append(1)
    
    return d[::-1]

def e(n):
    
    vs = lst(n - 1)
    num, den = 1 + (vs[0] * vs[1]), vs[0]

    for i in range(2, len(vs)):
        num, den = den, num
        num = num + (vs[i] * den)
    
    num, den = den, num
    num += (2 * den)

    return sd(num)

print e(100)
