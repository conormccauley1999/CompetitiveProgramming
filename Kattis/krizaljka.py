a, b = input().split()
x, y = 0, 0
for c in a:
    if c in b:
        x = a.index(c)
        y = b.index(c)
        break
for i in range(len(b)):
    if i != y:
        print(('.' * x) + b[i] + ('.' * (len(a) - (x + 1))))
    else:
        print(a)
