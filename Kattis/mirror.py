def f():
    r, c = map(int, input().split())
    g = []
    for _ in range(r):
        g.append(input())
    for _r in g[::-1]:
        print(_r[::-1])
t = int(input())
for i in range(t):
    print("Test %d" % (i + 1,))
    f()
