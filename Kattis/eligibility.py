from datetime import datetime

n = int(input())
for _ in range(n):
	n, bd, db, cs = input().split()
	bd = datetime.strptime(bd, '%Y/%m/%d')
	db = datetime.strptime(db, '%Y/%m/%d')
	cs = int(cs)
	E = False
	if bd.year >= 2010:
		print(n, "eligible")
	elif db.year >= 1991:
		print(n, "eligible")
	elif (cs / 5) > 8:
		print(n, "ineligible")
	else:
		print(n, "coach petitions")
