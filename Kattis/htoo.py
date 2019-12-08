def f(s):
	r = {}
	cur_c = ""
	cur_n = 0
	for c in s:
		if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			if cur_c != "":
				if cur_c in r: r[cur_c] += cur_n if cur_n != 0 else 1
				else: r[cur_c] = cur_n if cur_n != 0 else 1
			cur_c = c
			cur_n = 0
		else:
			n = int(c)
			cur_n *= 10
			cur_n += n
	if cur_c in r: r[cur_c] += cur_n if cur_n != 0 else 1
	else: r[cur_c] = cur_n if cur_n != 0 else 1
	return r

m, k = raw_input().split()
k = int(k)
o = raw_input()

m, o = f(m), f(o)
for x in m: m[x] *= k

r = 0
while True:
	v = True
	for x in o:
		if x in m and m[x] >= o[x]:
			m[x] -= o[x]
		else:
			v = False
			break
	if not v: break
	else: r += 1
print r
