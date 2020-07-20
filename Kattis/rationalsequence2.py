def f():
    p, q = map(int, list(input().split())[1].split('/'))
    t = ''
    while (p, q,) != (1, 1,):
        if p > q:
            p, q = p - q, q
            t += '1'
        else:
            p, q = p, q - p
            t += '0'
    t += '1'
    return int(t[::-1], 2)

t = int(input())
for i in range(t):
    print(i + 1, f())
