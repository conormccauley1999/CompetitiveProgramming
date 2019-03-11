# Problem 36

s = 0

for i in xrange(1, 1000000):
    if ((str(i)) == (str(i)[::-1])) and ((bin(i)[2:]) == ((bin(i)[2:])[::-1])):
        s += i

print s