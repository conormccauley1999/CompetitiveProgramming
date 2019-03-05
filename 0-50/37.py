# Problem 37

from common import *

sm = 0
cnt = 0

for n in range(11, 1000000, 2):
	if isPrime(n) and isPrimeTruncatableLR(n):
		print n, sm, cnt
		sm += n
		cnt += 1

print sm, cnt
