from math import sqrt
ls = list(map(int, input().split()))
s = sum(ls) / 2
print(sqrt((s - ls[0]) * (s - ls[1]) * (s - ls[2]) * (s - ls[3])))
