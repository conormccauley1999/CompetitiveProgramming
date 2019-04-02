# Problem 10

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

print sum(primesLessThan(2000000))
