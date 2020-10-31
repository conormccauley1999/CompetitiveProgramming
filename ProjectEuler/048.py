# Problem 48

t = 0
for n in range(1, 1001):
    m = n
    for i in range(1, n): m *= n
    t += m
print str(t)[-10:]
