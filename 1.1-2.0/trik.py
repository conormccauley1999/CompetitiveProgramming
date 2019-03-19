i = raw_input()
C = [1,0,0]
for x in i:
	if x == "A": C[0], C[1] = C[1], C[0]
	if x == "B": C[1], C[2] = C[2], C[1]
	if x == "C": C[0], C[2] = C[2], C[0]
if C[0]: print 1
if C[1]: print 2
if C[2]: print 3