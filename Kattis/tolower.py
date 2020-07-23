p, t = map(int, input().split())
v = 0
for i in range(p):
    a = True
    for j in range(t):
        m = input()
        a &= m[1:].lower() == m[1:]
    if a:
        v += 1
print(v)
