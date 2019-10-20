i = raw_input()
v = [0, 0, 0]
for c in i:
	if c == "T": v[0] += 1
	elif c == "C": v[1] += 1
	else: v[2] += 1
print (min(v) * 7) + sum(x ** 2 for x in v)