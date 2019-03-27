# Problem 91

def rat(x1, y1, x2, y2):
	if x1 == 0 and x2 == 0: return False
	if y1 == 0 and y2 == 0: return False
	a = x1**2 + y1**2
	b = x2**2 + y2**2
	c = (x1 - x2)**2 + (y1 - y2)**2
	return a + b == c or a + c == b or b + c == a

mx = 100
t = 0
for x1 in xrange(0, (mx + 1)):
	for y1 in xrange(0, (mx + 1)):
		if (x1, y1) == (0, 0): continue
		for x2 in xrange(0, (mx + 1)):
			for y2 in xrange(0, (mx + 1)):
				if (x2, y2) == (0, 0) or (x1, y1) == (x2, y2): continue
				if rat(x1, y2, x2, y2): t += 1
print t / 2
