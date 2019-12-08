n = int(raw_input())
l = []
for _ in range(n): l.append(raw_input())
s = sorted(l)
if l == s: print "INCREASING"
elif l == s[::-1]: print "DECREASING"
else: print "NEITHER"
