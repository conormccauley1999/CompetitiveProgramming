# Problem 44

from common import *

for k in range(1, 10000):
    for j in range(k, 1, -1):
        pk = getPentagonalNumber(k)
        pj = getPentagonalNumber(j)
        d = pk - pj
        s = pk + pj
        if d > 0 and isPentagonalNumber(d) and isPentagonalNumber(s):
        	print int(d)
        	break
