N = int(raw_input())
X = 0
for i in range(0, N):
	v = int(raw_input())
	X += (v / 10) ** (v % 10)
print X