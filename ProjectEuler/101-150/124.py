# Problem 124

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ps = npPrimesLessThan(10 ** 8)

def rad(n):
	fs = set()
	for p in ps:
		while n != 1 and n % p == 0:
			fs.add(p)
			n /= p
		if n == 1:
			r = 1
			for f in fs:
				r *= f
			return r
	print "ERROR " + str(n)
	quit()

rs = [(rad(n), n) for n in range(1, 100001)]
print sorted(rs)[9999]
