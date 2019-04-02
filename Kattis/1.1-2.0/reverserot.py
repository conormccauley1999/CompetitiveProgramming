import string
a = string.ascii_uppercase + "_."
while True:
	i = raw_input()
	if i == "0": break
	j = i.split(" ")
	N, s = int(j[0]), j[1][::-1]
	o = ""
	for c in s: o += a[(a.index(c) + N) % 28]
	print o