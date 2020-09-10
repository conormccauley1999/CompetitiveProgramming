# Problem 173

MAX = 1000000
p = lambda x: 4 * (x  - 1)

c = 0
for x in range(MAX, 2, -1):
    t = p(x)
    y = x - 2
    while t <= MAX and y >= 1:
        c += 1
        t += p(y)
        y -= 2
print(c)
