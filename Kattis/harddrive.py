n, c, b = map(int, raw_input().split())
bs = map(int, raw_input().split())
h = [-1] * n

for x in bs: h[x - 1] = 0
if c % 2 == 1:
	h[0] = 1
	c -= 1

l = 1
s = ""
s += "1" if h[0] == 1 else "0"

i = 1
while c > 0 and i < n - 1:
	if h[i - 1] in [0, -1] and h[i] == -1:
		h[i] = 1
		s += "1"
		l += 1
		c -= 2
	else:
		s += "0"
		l += 1
	i += 1

print s + (n - l)*"0"
