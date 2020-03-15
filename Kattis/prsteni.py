def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
n = int(input())
R = list(map(int, input().split()))
for i in range(1, n):
	g = gcd(R[0], R[i])
	print(f"{R[0] // g}/{R[i] // g}")
