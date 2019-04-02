import string
a = string.ascii_uppercase
s = raw_input()
t = s[:len(s)/2]
u = s[len(s)/2:]
v = sum(a.index(c) for c in t)
w = sum(a.index(c) for c in u)
x = "".join([a[(a.index(c) + v) % 26] for c in t])
y = "".join([a[(a.index(c) + w) % 26] for c in u])
print "".join([a[(a.index(x[i]) + a.index(y[i])) % 26] for i in range(0, len(x))])