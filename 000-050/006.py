# Problem 6

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

print squareOfSum(100) - sumOfSquares(100)
