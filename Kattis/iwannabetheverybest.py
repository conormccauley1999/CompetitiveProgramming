n, k = map(int, raw_input().split())
pa, pd, ph = [], [], []
for i in range(n):
	a, d, h = map(int, raw_input().split())
	pa.append(tuple([a, i]))
	pd.append(tuple([d, i]))
	ph.append(tuple([h, i]))
pa.sort()
pd.sort()
ph.sort()
p = set()
for i in range(k):
	p.add(pa[n - (i + 1)][1])
	p.add(pd[n - (i + 1)][1])
	p.add(ph[n - (i + 1)][1])
print len(p)
