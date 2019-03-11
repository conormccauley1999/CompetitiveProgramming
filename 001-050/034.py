# Problem 34

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

sum_total = 0

for n in range(10, 1000000):

	digits = []
	for char in str(n):
		digits.append(int(char))

	sum_for_n = 0

	for digit in digits:
		sum_for_n += factorialRecursive(digit)

	if sum_for_n == n:
		sum_total += n

print sum_total
