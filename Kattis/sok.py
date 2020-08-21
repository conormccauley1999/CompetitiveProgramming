a, b, c = map(float, input().split())
i, j, k = map(float, input().split())
m = min(a / i, b / j, c / k)
print(a - (m * i), b - (m * j), c - (m * k))
