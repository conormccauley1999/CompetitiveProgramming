def enc(s):
	o = ""
	char, count = "", 0
	for c in s:
		if c == char:
			count += 1
		else:
			if char != "": o += char + str(count)
			char = c
			count = 1
	return o + char + str(count)

def dec(s):
	o = ""
	for i in range(0, len(s) / 2): o += s[i*2] * int(s[(i*2)+1])
	return o

f, s = raw_input().split()
print enc(s) if f == "E" else dec(s)