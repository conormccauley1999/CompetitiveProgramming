def f():
    P, Q = map(int, list(input().split())[1].split('/'))
    p, q = P, Q
    t = []
    while (p, q,) != (1, 1,):
        if p > q:
            p, q = p - q, q
            t.append('1')
        else:
            p, q = p, q - p
            t.append('0')
    t.append('1')
    return int(''.join(t[::-1]), 2)

t = int(input())
for i in range(t):
    print(i + 1, f())
