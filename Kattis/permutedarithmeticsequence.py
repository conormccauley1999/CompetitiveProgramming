def f():
    vs = list(map(int, input().split()))[1:]
    ss = sorted(vs)
    ds = []
    for i in range(1, len(vs)):
        ds.append(vs[i] - vs[i - 1])
    if len(set(ds)) == 1:
        return 'arithmetic'
    es = []
    for i in range(1, len(ss)):
        es.append(ss[i] - ss[i - 1])
    if len(set(es)) == 1:
        return 'permuted arithmetic'
    return 'non-arithmetic'

for _ in range(int(input())):
    print(f())
