# Problem 56

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

mx = 0
for a in range(1, 100):
	for b in range(1, 100):
		s = digitalSum(a ** b)
		mx = s if s > mx else mx
print mx
