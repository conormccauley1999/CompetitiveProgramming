n = int(input())
d = {}
for _ in range(n):
    t, p = input().split()
    if t == 'entry':
        if p in d:
            print(p, 'entered (ANOMALY)')
        else:
            print(p, 'entered')
        d[p] = True
    else:
        if p not in d:
            print(p, 'exited (ANOMALY)')
        else:
            print(p, 'exited')
            del d[p]
