from decimal import *
pi = Decimal(3.14159265358979323846264338)
while True:
	i = [Decimal(v) for v in raw_input().split()]
	if sum(i) == 0: break
	Ac = pi * i[0] * i[0]
	As = Decimal(4) * i[0] * i[0]
	print Ac, As * (i[2] / i[1])