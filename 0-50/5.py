# Problem 5

from common import *

def main():

	i = 20
	d = range(2, 21)

	while True:
		for j in d:
			if i % j != 0: break
			if j == 20: return i
		i += 20

	return -1

print main()
