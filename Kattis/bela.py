d = {
	"A":[11,11],
	"K":[4,4],
	"Q":[3,3],
	"J":[20,2],
	"T":[10,10],
	"9":[14,0],
	"8":[0,0],
	"7":[0,0]
}
i = raw_input().split(" ")
N, B = int(i[0]), i[1]
t = 0
for x in range(0, 4 * N):
	h = raw_input()
	if h[1] == B: t += d[h[0]][0]
	else: t += d[h[0]][1]
print t