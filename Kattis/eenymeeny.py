l = len(raw_input().split())
n = int(raw_input())
a = [raw_input() for _ in range(n)]
t1, t2 = [], []
x = True
ci = 0
while len(a):
	ri = (ci + l - 1) % len(a)
	if x: t1.append(a[ri])
	else: t2.append(a[ri])
	x = not x
	a.pop(ri)
	ci = 0 if ri >= len(a) else ri
print len(t1)
for p in t1: print p
print len(t2)
for p in t2: print p
