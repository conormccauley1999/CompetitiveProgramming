# Problem 90

from itertools import combinations

ss = ((0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1))
ds = set(range(10))
cs = set()
cwr = list(combinations(ds, 6))

for x in cwr:
    x = list(x)
    if 6 in x and 9 not in x:
        x.append(9)
    elif 9 in x and 6 not in x:
        x.append(6)
    for y in cwr:
        y = list(y)
        if 6 in y and 9 not in y:
            y.append(9)
        elif 9 in y and 6 not in y:
            y.append(6)
        z = True
        for s in ss:
            if not (s[0] in x and s[1] in y) and not (s[1] in x and s[0] in y):
                z = False
                break
        if z and (tuple(y), tuple(x)) not in cs:
            cs.add((tuple(x), tuple(y)))

print(len(cs))
