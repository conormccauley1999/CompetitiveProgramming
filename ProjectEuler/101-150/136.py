# Problem 136

MAX = 50000000

ns = [0] * MAX
for x in range(1, MAX):
    for a in range((x // 4) + 1, x):
        v = x * (4*a - x)
        if v >= MAX:
            break
        ns[v] += 1

print(sum(int(ns[n] == 1) for n in range(1, MAX)))
