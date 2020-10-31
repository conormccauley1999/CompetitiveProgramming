# Problem 60

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

def getMinSum(prs):
	ms = 999999999
	for p1 in prs:
		if p1 not in prs: continue
		for p2 in prs[p1]:
			if p2 not in prs: continue
			for p3 in prs[p2]:
				if p3 not in prs: continue
				if p3 not in prs[p1]: continue
				for p4 in prs[p3]:
					if p4 not in prs: continue
					if p4 not in prs[p2] or p4 not in prs[p1]: continue
					for p5 in prs[p4]:
						if p5 not in prs: continue
						if p5 not in prs[p3] or p5 not in prs[p2] or p5 not in prs[p1]: continue
						sm = p1 + p2 + p3 + p4 + p5
						if sm < ms: ms = sm
	return ms

def cnum(a, b):
	l = getNumLengthQuick(b)
	return b + (a * (10 ** l))

ps = list(primesLessThan(10000))
prs = {}
mx = len(ps)

for i in xrange(1, mx):
	vs = []
	for j in xrange(i + 1, mx):
		p, q = ps[i], ps[j]
		a = cnum(p, q)
		if not isPrime(a): continue
		b = cnum(q, p)
		if not isPrime(b): continue
		vs.append(q)
	if len(vs) > 0: prs[p] = vs

print getMinSum(prs)
