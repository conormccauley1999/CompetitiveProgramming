# Problem 37

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

sm = 0
cnt = 0

for n in range(11, 1000000, 2):
	if isPrime(n) and isPrimeTruncatableLR(n):
		print n, sm, cnt
		sm += n
		cnt += 1

print sm, cnt
