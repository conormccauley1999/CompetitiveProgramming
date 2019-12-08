def solve(n, cs):
	ss = sorted(cs)
	if cs == ss[::-1]:
		print "1 " + str(n)
		return
	if cs == ss:
		print "1 1"
		return
	di, ii = -1, -1
	cd = False
	for x in range(0, n - 1):
		if not cd and cs[x] > cs[x + 1]:
			if di != -1:
				print "impossible"
				return
			else:
				di = x
				cd = True
		if cd and cs[x] < cs[x + 1]:
			ii = x
			cd = False
	if cd and cs[n - 2] > cs[n - 1]:
		ii = n - 1
	if ii == -1:
		ii = n - 1
	while di >= 1 and cs[di] == cs[di - 1]:
		di -= 1
	while ii <= n - 2 and cs[ii] == cs[ii + 1]:
		ii += 1
	if di != 0 and cs[ii] < cs[di - 1]:
		print "impossible"
		return
	print di + 1, ii + 1

n = int(raw_input())
cs = map(int, raw_input().split())
solve(n, cs)
