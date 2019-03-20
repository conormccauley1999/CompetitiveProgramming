N = int(raw_input())
for x in range(0, N):
	i = raw_input()
	if i.startswith("Simon says "): print i[11:]