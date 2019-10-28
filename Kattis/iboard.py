def f(s):
	x = ""
	for c in s:
		b = ''.join(format(ord(c), 'b'))
		if len(b) != 7: x += "0"
		x += b
	return x.count("0") % 2 == 0 and x.count("1") % 2 == 0

while True:
	try:
		s = raw_input()
		print "free" if f(s) else "trapped"
	except:
		break
