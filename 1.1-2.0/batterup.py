N = int(raw_input())
b = [int(v) for v in raw_input().split(" ")]
sm = 0.0
x = 0.0
for s in b:
	if s != -1:
		sm += s
		x += 1.0
print sm / x