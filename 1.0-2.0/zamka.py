L = int(raw_input())
D = int(raw_input())
X = int(raw_input())

def sm(n):
	s = 0
	while n != 0:
		s += n % 10
		n /= 10
	return s

mn, mx = 0, 0
for n in xrange(L, D+1):
	if sm(n) == X:
		mn = n
		break
for n in xrange(D, L-1, -1):
	if sm(n) == X:
		mx = n
		break
print mn
print mx