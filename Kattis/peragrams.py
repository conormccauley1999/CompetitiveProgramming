from collections import Counter
s = input()
c = dict(Counter(s))
r = sum(0 if c[k] % 2 == 0 else 1 for k in c) - 1
print(0 if r < 0 else r)
