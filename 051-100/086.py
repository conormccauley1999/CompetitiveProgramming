# Problem 86 -- incomplete

import time
from math import sqrt

def f(w, h, d, x):
	l = sqrt((x ** 2) + (d ** 2)) + sqrt(((w - x) ** 2) + (h ** 2))
	return l

def getMinDist(w, h, d):
	e = 0.001
	d = 0.000001
	a, b = 0.0, w
	x = (b - a) / 2.0
	print x
	while True:
		l1, l2 = f(w, h, d, (x - e)), f(w, h, d, (x + e))
		e *= 0.99
		if abs(l1 - l2) < d: return x
		elif l1 > l2: a = x
		else: b = x

for w in range(1, 101):
	for h in range(1, 101):
		for d in range(1, 101):
			x = getMinDist(w, h, d)
			print w, h, d, x
			#if x % 1 == 0: print w, h, d, x
