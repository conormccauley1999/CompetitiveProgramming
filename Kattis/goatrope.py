i = [float(v) for v in raw_input().split()]
gx, gy, x1, y1, x2, y2 = i[0], i[1], i[2], i[3], i[4], i[5]
x, y = max(min(gx, x2), x1), max(min(gy, y2), y1)
print (((gx - x) ** 2) + ((gy - y) ** 2)) ** 0.5