s = raw_input()
i, l = 0, len(s)
v = ["a","e","i","o","u"]
o = ""
while i < l:
	o += s[i]
	if s[i] in v: i += 2
	i += 1
print o