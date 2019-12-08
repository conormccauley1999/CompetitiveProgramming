o = "ABCDEFGHIJKLMNO."
s = 0
for y in range(4):
	l = raw_input()
	for x in range(4):
		c = l[x]
		if c == ".": continue
		i = o.index(c)
		s += abs(x - (i % 4)) + abs(y - (i / 4))
print s