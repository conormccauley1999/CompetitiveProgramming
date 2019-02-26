# Problem 7

pn = 10001
pf = 1

ps = set([2])

n = 3

while pf < pn:

	isp = True

	for p in ps:
		if n % p == 0:
			isp = False
			break

	if isp:
		ps.add(n)
		pf += 1

	n += 2

print n - 2
