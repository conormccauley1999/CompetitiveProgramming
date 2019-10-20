from math import sin, ceil, radians
i = raw_input().split(" ")
h, v = int(i[0]), int(i[1])
print int(ceil(h / sin(radians(v))))