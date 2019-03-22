from decimal import *
rs = [Decimal(v) for v in raw_input().split()]
at = rs[0] ** 2
ac = (rs[0] - rs[1]) ** 2
print Decimal(100) * (ac / at)