# unfinished

# T+1 (if T > 0)
# H-2
# T-2, H+1

def m(H, T):
	m = 0
	if H % 2 == 1 and T == 0: return -1
	if T % 2 == 1:
		T += 1
		m += 1
	if T % 4 == 0:
		T += 2
		m += 2
	H += (T / 2)
	m += (T / 2)
	m += (H / 2)
	return m

while True:
	i = raw_input().split()
	H, T = int(i[0]), int(i[1])
	if H == 0 and T == 0: break
	print m(H, T)