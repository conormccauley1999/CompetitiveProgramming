def parse(vs, es):
    for e in es:
        if e in ['+', '-', '=']:
            continue
        if e not in vs:
            return 'unknown'
    t = vs[es[0]]
    for i in range(1, len(es), 2):
        if es[i] == '+':
            t += vs[es[i + 1]]
        else:
            t -= vs[es[i + 1]]
    if t not in vs.values():
        return 'unknown'
    for k, v in vs.items():
        if t == v:
            return k

vs = {}
while True:
    try:
        xs = input().split()
        if xs[0] == 'clear':
            vs = {}
        elif xs[0] == 'def':
            vs[xs[1]] = int(xs[2])
        else:
            print(*xs[1:], parse(vs, xs[1:-1]))
    except:
        quit()
