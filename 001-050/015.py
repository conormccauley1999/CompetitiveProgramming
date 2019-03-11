# Problem 15

s = 21
nl = []

for i in range(1, (s ** 2) + 1):
	j = i - 1
	if (j - s) < 1 or j % s == 0: nl.append(1)
	else:
		v1 = nl[j - 1]
		v2 = nl[j - s]
		nl.append(v1 + v2)

print nl.pop()
