n = int(raw_input())
def sm(n):
	s = 0
	while n:
		s += n % 10
		n /= 10
	return s
while n > 0:
	if n % sm(n) == 0:
		print n
		break
	n += 1