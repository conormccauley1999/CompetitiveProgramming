# Problem 43

from itertools import permutations

ns = ["".join(p) for p in permutations("0123456789")]
s = 0

for n in ns:
	if (
        int(n[1:4]) % 2 == 0 and
        int(n[2:5]) % 3 == 0 and
        int(n[3:6]) % 5 == 0 and
        int(n[4:7]) % 7 == 0 and
        int(n[5:8]) % 11 == 0 and
        int(n[6:9]) % 13 == 0 and
        int(n[7:10]) % 17 == 0
    ): s += int(n)

print s
