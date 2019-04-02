C = float(raw_input())
L = int(raw_input())
s = 0.0
for x in range(0, L):
	i = raw_input().split(" ")
	w, l = float(i[0]), float(i[1])
	s += (C * w * l)
print s