# Problem 650

from copy import deepcopy
from sympy import sieve

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

M = 20000
MOD = 1000000007
sieve.extend_to_no(M)

d = {}
for n in range(2, M + 1):
	if n % 5000 == 0:
		print(f'd = {n}')
	m = n
	_d = {}
	for prime in sieve:
		if prime > m:
			break
		while m % prime == 0:
			if prime not in _d:
				_d[prime] = 0
			_d[prime] += 1
			m //= prime
	d[n] = _d

f = {2: d[2]}
for n in range(3, M + 1):
	if n % 5000 == 0:
		print(f'f = {n}')
	f[n] = mul(f[n - 1], d[n])

B = {2: d[2]}
for n in range(3, M + 1):
	if n % 5000 == 0:
		print(f'B = {n}')
	B[n] = div(mul(B[n - 1], exp(d[n], n)), f[n])

def D(n):
	if n % 100 == 0:
		print(f'D = {n}')
	facts = B[n]
	divs = 1
	for fact in facts:
		divs *= pow(fact, facts[fact] + 1) - 1
		divs //= fact - 1
		divs %= MOD
	return divs

def S(n):
	sm = 1
	for k in range(2, n + 1):
		sm += D(k)
		sm %= MOD
	return sm

print(S(M))
