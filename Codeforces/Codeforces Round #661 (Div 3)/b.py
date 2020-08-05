def f():
    n = int(input())
    va = list(map(int, input().split()))
    vb = list(map(int, input().split()))
    xa, xb = min(va), min(vb)
    ms = 0
    for i in range(n):
        da = va[i] - xa
        db = vb[i] - xb
        if da == 0:
            ms += db
        elif db == 0:
            ms += da
        else:    
            mn = min(da, db)
            ms += mn
            da -= mn
            db -= mn
            ms += da + db
    return ms

t = int(input())
for _ in range(t):
    print(f())
