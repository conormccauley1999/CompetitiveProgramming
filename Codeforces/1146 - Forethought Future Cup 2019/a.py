s = raw_input()
l = len(s)
a = s.count("a")
b = l - a
if a > b: print l
else: print a + (a - 1)