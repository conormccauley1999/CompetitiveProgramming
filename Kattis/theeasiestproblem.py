def sm(n):
	s = 0
	while n:
		s += n % 10
		n /= 10
	return s

while True:
	N = int(raw_input())
	if N == 0: break
	s = sm(N)
	p = 11
	while sm(N * p) != s:
		p += 1
	print p