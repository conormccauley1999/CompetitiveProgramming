t = 1
while True:
    n = int(input())
    ds = {}
    if n == 0:
        break
    for _ in range(n):
        ws = input().split()
        a = ws[-1].lower()
        if a not in ds:
            ds[a] = 0
        ds[a] += 1
    print(f'List {t}:')
    for i in sorted(ds.items()):
        print(f'{i[0]} | {i[1]}')
    t += 1
