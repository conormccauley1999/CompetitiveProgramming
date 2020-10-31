# Problem 63

t = 0
for i in range(1, 200):
    for j in range(1, 200):
        k = i ** j
        if len(str(k)) == j: t += 1
print t
