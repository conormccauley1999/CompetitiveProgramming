# Problem 9

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

for a in range(1, 1001):
	sa = a * a
	for b in range(a + 1, 1001):
		sb = b * b
		for c in range(b + 1, 1001):
			sc = c * c
			if (sa + sb) == sc:
				if a + b + c == 1000:
					print a * b * c
