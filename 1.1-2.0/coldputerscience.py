n = int(raw_input())
ts = [int(t) for t in raw_input().split(" ")]
r = 0
for t in ts:
	if t < 0: r += 1
print r