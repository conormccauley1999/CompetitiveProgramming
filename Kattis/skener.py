i = raw_input().split(" ")
R, C, ZR, ZC = int(i[0]), int(i[1]), int(i[2]), int(i[3])
rs = []
for x in range(0, R): rs.append(raw_input())
z = []
for r in rs:
	o = ""
	for c in r: o += c * ZC
	for y in range(0, ZR): z.append(o)
for x in z: print x