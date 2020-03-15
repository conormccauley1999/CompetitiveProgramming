# UNSOLVED
# Problem 243

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from common import *

ps = sorted(list(npPrimesLessThan(10 ** 8)))

def phi(n):
	if n % 10000 == 0: print(n)
	r = n
	i = 0
	while n != 1:
		p = ps[i]
		if n % p == 0:
			r *= (1 - (1.0 / p))
		while n % p == 0: n /= p
		i += 1
	return r

def R(d):
	return phi(d) / (d - 1)

x = 15499.0 / 94744.0
d = 13
while True:
	if R(d) < x:
		print(d)
		break
	d += 1
