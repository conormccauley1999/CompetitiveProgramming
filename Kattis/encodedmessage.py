n = int(raw_input())
def decode(m):
	l = len(m)
	r = int(l ** 0.5)
	a = []
	for x in range(0, r):
		b = []
		for y in range(0, r): b.append(m[(x * r) + y])
		a.append(b)
	n = []
	for x in range(0, r):
		b = []
		for y in range(0, r): b.append(a[y][x])
		n.append(b)
	o = ""
	for x in n[::-1]: o += ''.join(x)
	return o
r = []
for x in range(0, n): r.append(decode(raw_input()))
for x in r: print x