# incomplete

def F(n):
	return 0

P = int(raw_input())
for x in range(0, P):
	i = raw_input().split()
	K, n = int(i[0]), [int(v) for v in i[1].split("/")]
	print K, F(n)