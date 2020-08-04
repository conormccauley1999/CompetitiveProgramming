from math import floor, log10

s = input()
l = len(s)

if l <= 4:
    print({
        1: 1, 1: 1, 2: 2, 6: 3, 24: 4, 120: 5, 720: 6, 5040: 7
    }[int(s)])
else:
    m = [0, 1]
    m.append(log10(2))
    for i in range(3, 300000):
        m.append(m[i - 1] + log10(i))
    for i in range(3, 300000):
        if floor(m[i]) + 1 == l:
            print(i)
