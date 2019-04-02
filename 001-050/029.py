# Problem 29

ts = set()

for a in range(2, 101):
	for b in range(2, 101):
		ts.add(a ** b)

print len(ts)
