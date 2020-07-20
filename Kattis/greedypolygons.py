from math import sin, tan, pi
t = int(input())
for _ in range(t):
    n, l, d, g = map(int, input().split())
    A = 0.25 * n * l * l * (1 / tan(pi / n))
    A += n * l * d * g
    A += n * (360 / n) * pi * d * d * g * g / 360
    print(A)
