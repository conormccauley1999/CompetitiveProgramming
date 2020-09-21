# Problem 231

from copy import deepcopy
from sympy.ntheory import factorint

def mul(facts_a, facts_b):
	facts_c = deepcopy(facts_a)
	for fact in facts_b:
		if fact not in facts_a:
			facts_c[fact] = 0
		facts_c[fact] += facts_b[fact]
	return facts_c

def div(facts_a, facts_b):
	facts_c = deepcopy(facts_a)
	for fact in facts_b:
		if fact not in facts_c or facts_c[fact] < facts_b[fact]:
			raise Exception('Float division')
		facts_c[fact] -= facts_b[fact]
	return facts_c

def exp(facts_a, exp):
	facts_c = deepcopy(facts_a)
	for fact in facts_c:
		facts_c[fact] *= exp
	return facts_c

M = 20000000

d = {}
for n in range(2, M + 1):
    if n % 1000000 == 0:
        print(f'd = {n}')
    d[n] = factorint(n)
