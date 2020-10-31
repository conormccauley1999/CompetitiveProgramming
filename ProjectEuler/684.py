# Problem 684

M = 1000000007

def S(k):
    x = k // 9
    y = k % 9
    p = pow(10, x, M)
    sm = (((6 * p) - 6) - (9 * x)) + ((p * (((y + 1) * (y + 2) // 2) - 1)) - y)
    return sm

f, g = 1, 2
sm = 0
for i in range(2, 91):
    sm += S(f)
    print(i, f, sm % M)
    f, g = g, f + g
print(sm % M)
