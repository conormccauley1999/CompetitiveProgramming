def x():
	a, b, c, n = map(int, input().split())
	if not a or not b or not c:
		return False
	if n < 3:
		return False
	return (a + b + c) >= n
print("NO" if not x() else "YES")
