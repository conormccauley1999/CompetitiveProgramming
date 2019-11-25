p = int(raw_input())
for k in range(p):
	n = int(raw_input().split()[1])
	print "%d %d" % (k + 1, n + ((n * (n + 1)) / 2))
