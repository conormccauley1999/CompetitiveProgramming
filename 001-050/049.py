# Problem 49

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *
from itertools import permutations

ps = primesLessThan(10000)
s = ""

for p in ps:
	if (p + 3330) in ps and (p + 6660) in ps:
		prms = ["".join(prm) for prm in permutations(str(p))]
		if str(p + 3330) in prms and str(p + 6660) in prms:
			s = str(p) + str(p + 3330) + str(p + 6660)

print s
