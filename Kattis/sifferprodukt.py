n = int(input())
while n >= 10:
    v = 1
    for c in str(n):
        if c != '0':
            v *= int(c)
    n = v
print(n)