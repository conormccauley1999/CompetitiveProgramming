from decimal import Decimal

f = { 0: Decimal(1) }
for i in range(1, 10001):
    f[i] = f[i - 1] / Decimal(i)

print(sum(f[i] for i in range(int(input()) + 1)))
