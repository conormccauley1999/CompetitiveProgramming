def f():
    k, s = input().split()
    b8 = '0'
    try:
        b8 = int(s, 8)
    except:
        pass
    b10 = int(s)
    b16 = int(s, 16)
    print(k, b8, b10, b16)

n = int(input())
for _ in range(n):
    f()
