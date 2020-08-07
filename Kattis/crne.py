n = int(input())
e = not n % 2
if not e:
    n += 1
r = (n // 2) + 1
o = r * r
if not e:
    o -= r
print(o)
