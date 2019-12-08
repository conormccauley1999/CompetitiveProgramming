S = raw_input()
E = int(raw_input())
ws = []
for _ in range(E):
	xs = raw_input().split()
	for x in xs:
		if S[-len(x):] == x:
			ws += xs
			continue
P = int(raw_input())
for _ in range(P):
	x = raw_input()
	f = False
	for w in ws:
		if x[-len(w):] == w:
			f = True
			print "YES"
			break
	if not f:
		print "NO"
