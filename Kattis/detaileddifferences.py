n = int(raw_input())
r = []
for i in range(0, n):
	a = raw_input()
	b = raw_input()
	r.append(a)
	r.append(b)
	o = ""
	for x in range(0, len(a)):
		if a[x] == b[x]: o += "."
		else: o += "*"
	r.append(o)
	r.append("")
for x in r: print x