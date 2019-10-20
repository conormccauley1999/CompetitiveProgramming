import string
i = raw_input()
l = float(len(i))
w, lc, uc, s = 0, 0, 0, 0
for c in i:
	if c in string.ascii_uppercase: uc += 1.0
	elif c in string.ascii_lowercase: lc += 1.0
	elif c == "_": w += 1.0
	else: s += 1.0
print w / l
print lc / l
print uc / l
print s / l