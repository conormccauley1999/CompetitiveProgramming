i = raw_input().split(" ")
X, Y = int(i[0]), int(i[1])
if ((4 * X) + (3 * Y)) % 2 == 0: print "possible"
else: print "impossible"