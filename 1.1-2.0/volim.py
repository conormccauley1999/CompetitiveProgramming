K = int(raw_input())
N = int(raw_input())
p = K
tm = 0
pa = 0
for x in range(0, N):
	i = raw_input().split(" ")
	T, Z = int(i[0]), i[1]
	tm += T
	if tm >= 210 and pa == 0: pa = p
	if Z == "T": p += 1
	if p == 9: p = 1
print pa