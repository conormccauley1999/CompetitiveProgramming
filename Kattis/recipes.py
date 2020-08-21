t = int(input())
for i in range(t):
    print(f'Recipe # {i + 1}')
    r, p, d = map(int, input().split())
    js = []
    sw = 0
    for _ in range(r):
        n, w, q = input().split()
        w, q = float(w), float(q)
        if q == 100:
            sw = w * (d / p) / 100
        js.append((n, q))
    for j in js:
        print(j[0], j[1] * sw)
    print('-' * 40)
