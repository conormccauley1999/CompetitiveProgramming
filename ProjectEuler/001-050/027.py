# Problem 27

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ps = set()

def main():

	s, p = 0, 0

	a = -999
	while a < 1000:
		b = -1000
		while b <= 1000:
			n = 0
			while True:
				x = (n * n) + (a * n) + b
				if isPrimeCache(x):
					if n > s:
						s = n
						p = a * b
				else: break
				n += 1
			b += 1
		a += 1

	return p

def isPrimeCache(n):
	if n < 0: return False
	elif n in ps: return True
	elif isPrime(n):
		ps.add(n)
		return True
	else: return False

print main()
