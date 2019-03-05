# Problem 64

import time
from math import sqrt, floor

def getPeriod(ns):
	return # to-do

def getContinuedFractionPeriod(n):
	period = []
	a = floor(sqrt(n))
	r = 1 / (sqrt(n) - a)
	while True:
		a = floor(r)
		r = 1 / (r - a)

r = 0
for n in range(2, 10000):
	if sqrt(n) == int(sqrt(n)): continue
	if len(getContinuedFractionPeriod(n)) % 2 == 1: r += 1
print r
