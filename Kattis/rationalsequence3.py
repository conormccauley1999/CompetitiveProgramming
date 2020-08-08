def f():
    _, n = map(int, input().split())
    if n == 1:
        return '1/1'
    p, q = 1, 1
    b = bin(n)[2:]
    for d in b[1:]:
        if d == '1':
            p += q
        else:
            q += p
    return f'{p}/{q}'

t = int(input())
for i in range(t):
    print(i + 1, f())
