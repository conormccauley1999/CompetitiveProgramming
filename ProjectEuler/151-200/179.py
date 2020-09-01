from sympy import divisor_count

c = 0
x = divisor_count(1)
for n in range(2, int(1e7)):
    y = divisor_count(n)
    if x == y:
        c += 1
    x = y
    if n % 100000 == 0:
        print(n, c)
print(c)
