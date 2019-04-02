s = raw_input()
o = ""
for c in s:
	if o == "" or o[len(o)-1] != c: o += c
print o