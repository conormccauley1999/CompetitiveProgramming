w, a = raw_input(), raw_input()
l, t = len(w), 0
for c in a:
	if l == 0: break
	elif c in w: l -= w.count(c)
	else: t += 1
print "WIN" if t < 10 else "LOSE"