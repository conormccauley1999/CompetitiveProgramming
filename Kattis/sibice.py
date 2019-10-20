i = raw_input().split(" ")
N, W, H = int(i[0]), int(i[1]), int(i[2])
mx = (W**2 + H**2) ** 0.5
ms = []
for x in range(0, N): ms.append(int(raw_input()))
for m in ms:
	if m <= mx: print "DA"
	else: print "NE"