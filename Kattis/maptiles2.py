s = input()
z = len(s)
x, y = 0, 0
for i in range(z):
    n = int(s[i])
    x *= 2
    y *= 2
    if n == 1 or n == 3:
        x += 1
    if n == 2 or n == 3:
        y += 1
print(z, x, y)
