# UNSOLVED
# Problem 650

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

ps = npPrimesLessThan(10 ** 8)

def factorPow(fs, n):
	for f in fs:
		fs[f] *= n
	return fs

def factorMul(fs1, fs2):
	for v in fs2:
		if v in fs1: fs1[v] += fs2[v]
		else: fs1[v] = fs2[v]
	return fs1

def factorDiv(fs1, fs2):
	for v in fs2:
		if v in fs1: fs1[v] -= fs2[v]
		else: fs1[v] = -fs2[v]
	return fs1

_fs = {}
def factors(n):
	if n in _fs: return _fs[n]
	fs = {}
	for p in ps:
		while n != 1 and n % p == 0:
			if p in fs: fs[p] += 1
			else: fs[p] = 1
			n /= p
		if n == 1:
			_fs[n] = fs
			return fs
	print "ERROR " + str(n)
	quit()

def B(n):
	return n

_D = {}
def D(n):
	if n in _D: return _D[n]
	fs = factors(n)
	v = 1
	for f in fs:
		v *= (((f ** (fs[f] + 1)) - 1) / (f - 1))
	_D[n] = v
	return v

def S(n):
	return sum(D(B(k)) for k in range(1, n + 1))

print S(20000)
