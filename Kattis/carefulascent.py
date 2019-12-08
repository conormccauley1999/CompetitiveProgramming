from decimal import Decimal

x, y = map(Decimal, raw_input().split())
n = int(raw_input())
ya = Decimal(0)
for i in range(n):
	s = map(Decimal, raw_input().split())
	d = s[1] - s[0]
	ya += s[2] * d
	y -= d
ya += y
print x / ya
