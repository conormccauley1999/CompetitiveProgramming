t = int(raw_input())

def cf(n):
	s = str(n)
	if "4" in s: return True, len(s) - (s.index("4") + 1)
	else: return False, 0

for x in range(1, t + 1):
	n = int(raw_input())
	i = 1
	while True:
		ci = cf(i)
		if ci[0]: i += (10 ** ci[1])
		else:
			cn = cf(n - i)
			if cn[0]: i += (10 ** cn[1])
			else:
				print "Case #" + str(x) + ":", i, (n - i)
				break

