def f():
    ss = input().split()
    ws = set([])
    s = input()
    while s != "what does the fox say?":
        ws.add(s.split()[2])
        s = input()
    o = []
    for s in ss:
        if s not in ws:
            o.append(s)
    print(*o)

t = int(input())
for _ in range(t):
    f()
