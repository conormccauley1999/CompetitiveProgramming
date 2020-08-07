bss = '123456789abcdefghijklmnopqrstuvwxyz0'

def f():
    x, op, y, _, z = input().split()
    acc = []
    if all(c == '1' for d in [x, y, z] for c in d):
        if op == '+' and len(x) + len(y) == len(z):
            acc.append(1)
        elif op == '-' and len(x) - len(y) == len(z):
            acc.append(1)
        elif op == '*' and len(x) * len(y) == len(z):
            acc.append(1)
        elif op == '/' and len(x) / len(y) == len(z):
            acc.append(1)
    for b in range(2, 37):
        try:
            u, v, w = int(x, b), int(y, b), int(z, b)
            if op == '+' and u + v == w:
                acc.append(b)
            elif op == '-' and u - v == w:
                acc.append(b)
            elif op == '*' and u * v == w:
                acc.append(b)
            elif op == '/' and u / v == w:
                acc.append(b)
        except:
            continue
    if not len(acc):
        print('invalid')
        return
    o = ''
    for b in acc:
        o += bss[b - 1]
    print(o)
for _ in range(int(input())):
    f()
