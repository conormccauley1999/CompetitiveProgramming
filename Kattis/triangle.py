import decimal
decimal.getcontext().prec = 100
from math import ceil, log10

def sol(n):
	n = decimal.Decimal(n)
	r = (decimal.Decimal(3) ** (n + decimal.Decimal(1))) / (decimal.Decimal(2) ** n)
	return len('{0:.0f}'.format(r))

t = 1
while True:
	try:
		n = int(input())
		print(f"Case {t}: {sol(n)}")
	except:
		break
	t += 1
