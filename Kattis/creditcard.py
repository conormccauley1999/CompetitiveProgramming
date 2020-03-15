from math import ceil
import decimal
decimal.getcontext().prec = 40
def rnd(v):
	#return ceil(v * 100) / decimal.Decimal(100)
	i = str(v).index(".")
	x = str(v)[i + 3]
	if x in "56789":
		return decimal.Decimal(str(v)[:i + 3]) + decimal.Decimal(0.01)
	else:
		return decimal.Decimal(str(v)[:i + 3])
def f(r, b, m):
	p = 1
	while p <= 1200:
		c = b
		d = (b * r) - m
		b = rnd((b * r) - m)
		#if round(d, 2) != b: print(round(d, 2), b, d)
		if b <= 0: return p
		p += 1
		if b >= c: return 1201
	return 1201
t = int(input())
for _ in range(t):
	r, b, m = map(decimal.Decimal, input().split())
	p = f(1 + (r / 100), b, m)
	print(p if p <= 1200 else "impossible")
