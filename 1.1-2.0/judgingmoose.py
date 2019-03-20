i = [int(v) for v in raw_input().split(" ")]
if sum(i) == 0: print "Not a moose"
else:
	v = 2 * max(i)
	if i[0] != i[1]: print "Odd " + str(v)
	else: print "Even " + str(v)