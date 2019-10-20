S = int(raw_input())
def works(S, n):
	sm = n
	x = 1
	while sm < S:
		if x % 2 == 0: sm += n
		else: sm += (n - 1)
		x += 1
	return sm == S
r = []
for n in range(2, S):
	if S % n == 0: r.append([n, n])
	if works(S, n): r.append([n, n-1])
r.sort()
print str(S) + ":"
for x in r: print str(x[0]) + "," + str(x[1])