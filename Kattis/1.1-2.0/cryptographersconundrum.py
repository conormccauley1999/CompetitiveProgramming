s = raw_input()
d = 0
for i in range(0, len(s)):
	if i % 3 == 0 and s[i] != "P": d += 1
	if i % 3 == 1 and s[i] != "E": d += 1
	if i % 3 == 2 and s[i] != "R": d += 1
print d