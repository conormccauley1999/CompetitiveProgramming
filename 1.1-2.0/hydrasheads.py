# T-1 -> T+2 -> T+1 (if T > 0)
# H-2 -> ...
# T-2 -> H+1

# if T is 0 and H is odd -> impossible
# T+1
# get T to
#	4n if H is even
# 	2n if H is odd
# T-2 repeatedly
# H-2 repeatedly

def m(H, T):
	if T == 0 and H % 2 == 1: return -1
	m = 0
	while not (T % 4 == 0 and H % 2 == 0) and not (T % 4 != 0 and T % 2 == 0 and H % 2 == 1):
		T += 1
		m += 1
	while T != 0:
		T -= 2
		H += 1
		m += 1
	while H != 0:
		H -= 2
		m += 1
	return m

while True:
	i = raw_input().split()
	H, T = int(i[0]), int(i[1])
	if H == 0 and T == 0: break
	print m(H, T)