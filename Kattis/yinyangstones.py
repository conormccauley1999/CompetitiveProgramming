s = input()
w, b = 0, 0
for c in s:
	if c == "W":
		w += 1
	else:
		b += 1
print(1 if w == b else 0)
