# Problem 40

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import getNthDigitOfFractionalPart as d

print d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
