a, b, c = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
p = [0] * 101
for i in range(x1, y1):
    p[i] += 1
for i in range(x2, y2):
    p[i] += 1
for i in range(x3, y3):
    p[i] += 1
r = 0
for i in p:
    if i == 3:
        r += c*3
    elif i == 2:
        r += b*2
    elif i == 1:
        r += a
print(r)
