r = set()
for i in range(0, 10):
	v = int(raw_input())
	r.add(v % 42)
print len(r)