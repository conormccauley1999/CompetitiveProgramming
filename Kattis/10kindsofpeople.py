import copy

def genComponent(x0, y0, a, t):
	w, h = len(a), len(a[0])
	c, s = set(), []
	s.append((x0, y0))
	while len(s) != 0:
		p = s.pop()
		x, y = p[0], p[1]
		if x < 0 or y < 0 or x >= w or y >= h: continue
		if a[x][y] != t: continue
		c.add(p)
		a[x][y] = None
		s.append((x+1, y))
		s.append((x-1, y))
		s.append((x, y+1))
		s.append((x, y-1))
	return c

def genGraphComponents(a):
	w, h = len(a), len(a[0])
	cb, cd = [], []
	for x in xrange(w):
		for y in xrange(h):
			if a[x][y] == None: continue
			elif a[x][y]: cd.append(genComponent(x, y, a, a[x][y]))
			else: cb.append(genComponent(x, y, a, a[x][y]))
	return cb, cd

def path(p1, p2, G):
	for c in G:
		if p1 in c:
			if p2 in c: return True
			else: return False
	return False

a = []
r, c = map(int, raw_input().split())
for x in range(0, r):
	b = []
	i = raw_input()
	for j in i: b.append(True if j == "1" else False)
	a.append(b)

b = copy.deepcopy(a)
Gb, Gd = genGraphComponents(a)

n = int(raw_input())
for x in range(0, n):
	x1, y1, x2, y2 = map(lambda x: int(x) - 1, raw_input().split())
	p1, p2 = (x1, y1), (x2, y2)
	t1, t2 = b[x1][y1], b[x2][y2]
	if t1 != t2: print "neither"
	elif t1 and path(p1, p2, Gd): print "decimal"
	elif not t1 and path(p1, p2, Gb): print "binary"
	else: print "neither"
