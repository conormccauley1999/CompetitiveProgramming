# Problem 371 - UNSOLVED
# answer = ~40.66
from random import randint

def f():
    s = set([])
    c = 0
    while True:
        r = randint(0, 999)
        c += 1
        if r != 0 and 1000 - r in s:
            return c
        s.add(r)

M = 100000000
t = 0
for i in range(1, M + 1):
    t += f()
    if i % 100000 == 0:
        print(t / i)
print(t / M)
