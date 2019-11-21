from decimal import Decimal

g = lambda x: int(Decimal(x) * 100)

vs = map(g, raw_input().split())
f = g(raw_input()) * 3

mx, mn, sm = max(vs), min(vs), sum(vs)

if sm - mn <= f:
	print "infinite"
elif sm - mx > f:
	print "impossible"
else:
	print "%.2f\n" % ((f - (sm - (mx + mn))) / 100.0)
