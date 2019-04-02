# Problem 51

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ps = primesBetween(100000, 999999)
ms = getMasks(6)

for p in ps:
	for m in ms:
		f = 0
		c = 0
		for v in range(0, 10):
			n = applyMask(p, v, m)
			if n in ps:
				if f == 0: f = n
				c += 1
		if c >= 8:
			print f
			quit()
