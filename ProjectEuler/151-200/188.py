# Problem 188

import sys
sys.setrecursionlimit(2000)

def f(n, k):
	return n if k == 1 else pow(n, f(n, k - 1), 10 ** 8)

print f(1777, 1855)
