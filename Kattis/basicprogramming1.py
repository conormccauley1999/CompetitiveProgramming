alph = "abcdefghijklmnopqrstuvwxyz"
N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
	print(7)
elif t == 2:
	if A[0] > A[1]:
		print("Bigger")
	elif A[0] == A[1]:
		print("Equal")
	else:
		print("Smaller")
elif t == 3:
	print(sorted([A[0], A[1], A[2]])[1])
elif t == 4:
	print(sum(A))
elif t == 5:
	print(sum(x if x % 2 == 0 else 0 for x in A))
elif t == 6:
	s = ""
	for i in range(N):
		s += alph[A[i] % 26]
	print(s)
elif t == 7:
	i = 0
	v = set([])
	while True:
		i = A[i]
		if i in v:
			print("Cyclic")
			break
		v.add(i)
		if i < 0 or i >= N:
			print("Out")
			break
		elif i == N - 1:
			print("Done")
			break
