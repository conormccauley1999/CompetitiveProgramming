R, L, F = "Right", "Left", "Forward"

x, y = map(int, input().split())
n = int(input())
ds = [input() for _ in range(n)]

def sol(ds, i, s):
	p, q = 0, 0
	c = 0
	for j in range(n):
		d = ds[j] if i != j else s
		if d == L:
			c = (c - 1) % 4
		elif d == R:
			c = (c + 1) % 4
		else:
			if c == 0:
				q += 1
			elif c == 1:
				p += 1
			elif c == 2:
				q -= 1
			else:
				p -= 1
	return p == x and q == y

def z():
	for i in range(n):
		for d in [R, L, F]:
			if d == ds[i]:
				continue
			if sol(ds, i, d):
				print(i + 1, d)
				return

z()
