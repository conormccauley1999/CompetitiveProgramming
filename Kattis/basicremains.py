while True:
    i = input()
    if i == '0':
        break
    b, p, m = i.split()
    b = int(b)
    p, m = int(p, b), int(m, b)
    n = p % m
    if n == 0:
        print(0)
    else:
        ns = []
        while n:
            n, r = divmod(n, b)
            ns.append(str(r))
        print(''.join(reversed(ns)))
