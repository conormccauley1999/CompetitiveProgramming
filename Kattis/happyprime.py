def isPrime(n):
	if n == 1: return False
	if n == 2: return True
	if n == 3: return True
	if n % 2 == 0: return False
	if n % 3 == 0: return False
	i = 5
	w = 2
	while i * i <= n:
		if n % i == 0: return False
		i += w
		w = 6 - w
	return True

def f(m):
	if not isPrime(m): return False
	for _ in range(100):
		if m == 1: return True
		m = sum(int(c) ** 2 for c in str(m))
	return False

n = int(raw_input())
for _ in range(n):
	k, m = map(int, raw_input().split())
	print k, m, ("YES" if f(m) else "NO")
