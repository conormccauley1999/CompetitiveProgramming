a = [int(v) for v in raw_input().split(" ")]
b = [int(v) for v in raw_input().split(" ")]
c = [int(v) for v in raw_input().split(" ")]
x, y = 0, 0
if a[0] != b[0] and a[0] != c[0]: x = a[0]
elif b[0] != a[0] and b[0] != c[0]: x = b[0]
else: x = c[0]
if a[1] != b[1] and a[1] != c[1]: y = a[1]
elif b[1] != a[1] and b[1] != c[1]: y = b[1]
else: y = c[1]
print x, y