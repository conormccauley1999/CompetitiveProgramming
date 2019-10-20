from decimal import *
import string
a = string.ascii_uppercase + " '"
pi = Decimal(3.14159265358979323846264)

def steps(c1, c2):
	return min((a.index(c1) - a.index(c2)) % 28, (a.index(c2) - a.index(c1)) % 28)

def dist(s):
	return (Decimal(pi) * Decimal(60) * Decimal(s)) / Decimal(28)

def time(c1, c2):
	return (dist(steps(c1, c2)) / Decimal(15)) + Decimal(1)

N = int(raw_input())
for x in range(0, N):
	s = raw_input()
	r = Decimal(1)
	for i in range(0, len(s) - 1): r += time(s[i], s[i + 1])
	print r