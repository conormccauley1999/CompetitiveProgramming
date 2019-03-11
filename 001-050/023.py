# Problem 23

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

a = []
r = [True] * 28123

for n in range(1, 28124):
	if getDivisorSum(n) > n: a.append(n)

for x in range(0, len(a)):
	for y in range(0, len(a)):
		s = a[x] + a[y]
		if s <= 28123: r[s - 1] = False

s = 0

for i in range(0, len(r)):
	if r[i]: s += (i + 1)

print s
