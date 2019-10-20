N = int(raw_input())
for x in range(0, N):
	i = raw_input()
	if i == "P=NP": print "skipped"
	else: print sum([int(v) for v in i.split("+")])