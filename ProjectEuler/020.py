# Problem 20

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

print sum([int(x) for x in str(factorialRecursive(100))])
