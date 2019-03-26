n = int(raw_input())
r = 0
for x in range(0, n):
	i = raw_input()
	if "CD" not in i: r += 1
print r