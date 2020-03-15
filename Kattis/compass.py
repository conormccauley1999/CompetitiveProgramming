n1, n2 = int(input()), int(input())
if n1 == n2:
	print(0)
elif abs(n1 - n2) == 180:
	print(180)
elif n1 > n2:
	if (360 - n1) + n2 < n1 - n2:
		print(360 - n1 + n2)
	else:
		print(n2 - n1)
else:
	if (360 - n2) + n1 < n2 - n1:
		print(-360 - n1 + n2)
	else:
		print(n2 - n1)
