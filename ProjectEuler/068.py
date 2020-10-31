# Problem 68

"""
   5
    0  6
  4	  1
 9 3 2 7
    8
"""

from itertools import permutations

def toString(r):
	s = str(r[5]) + str(r[0]) + str(r[1]) + \
		str(r[6]) + str(r[1]) + str(r[2]) + \
		str(r[7]) + str(r[2]) + str(r[3]) + \
		str(r[8]) + str(r[3]) + str(r[4]) + \
		str(r[9]) + str(r[4]) + str(r[0])
	return s

def isValidRing(r):
	t = r[5] + r[0] + r[1]
	if (
		r[6] + r[1] + r[2] != t or
		r[7] + r[2] + r[3] != t or
		r[8] + r[3] + r[4] != t or
		r[9] + r[4] + r[0] != t
	): return False
	else: return True

r = [0, 0, 0, 0, 0, 6, 0, 0, 0, 0]

l1 = list(permutations([1, 2, 3, 5, 4]))
l2 = list(permutations([7, 8, 9, 10]))

s = []

for p1 in l1:
	for p2 in l2:
		r[0], r[1], r[2], r[3], r[4] = p1[0], p1[1], p1[2], p1[3], p1[4]
		r[6], r[7], r[8], r[9] = p2[0], p2[1], p2[2], p2[3]
		if isValidRing(r): print toString(r)
