# Problem 62

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

def isPerm(c1, c2):
	c1, c2 = str(c1), str(c2)
	if len(c1) != len(c2): return False
	elif sorted(c1) != sorted(c2): return False
	else: return True

def getPerms(cbs, i):
    c = cbs[i]
    prms = 1
    for j in range((i + 1), len(cbs)):
        cur = cbs[j]
        if isPerm(c, cur):
            prms += 1
    return prms

cbs = []
for i in range(4642, 10000):
	cbs.append(i ** 3)

for i in range(0, len(cbs)):
	prms = getPerms(cbs, i)
	if prms >= 5:
		print cbs[i]
		break
