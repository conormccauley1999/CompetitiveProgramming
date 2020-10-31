# Problem 35

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

count = 13

for n in range(101, 1000000, 2):

	string = str(n)
	length = len(string)

	has_no_chars = True
	for char in ['0', '2', '4', '6', '8']:
		if char in string:
			has_no_chars = False

	if has_no_chars:

		all_prime = True

		for i in range(0, length):

			string = string[-1:] + string[0:-1]

			if not isPrime(int(string)):

				all_prime = False
				break

		if all_prime:
			count += 1

print count
