from decimal import *
while True:
	i = raw_input().split(" ")
	D, V = Decimal(i[0]), Decimal(i[1])
	if D == Decimal(0) and V == Decimal(0): break
	print ((D ** Decimal(3)) - ((Decimal(6.0) * V) / Decimal(3.141592653589793238462643383))) ** Decimal(0.33333333333333)