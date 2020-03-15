ns = sorted(list(map(int, input().split())))
x, y = ns[1] - ns[0], ns[2] - ns[1]
if x > y:
	print(ns[0] + y)
elif y > x:
	print(ns[1] + x)
else:
	print(ns[2] + x)
