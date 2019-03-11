# Problem 31

cs = [1, 2, 5, 10, 20, 50, 100, 200]

def w(t, c):
	if c == 1 or t == 0: return 1
	else: return sum(w(t - (i * c), cs[cs.index(c) - 1]) for i in range(0, (t / c) + 1))

print w(200, 200)
