A, B, C = "ABC", "BABC", "CCAABB"
N = int(raw_input())
s = raw_input()
v = [0, 0, 0]
for i in range(0, N):
	x = s[i]
	if x == A[i % 3]: v[0] += 1
	if x == B[i % 4]: v[1] += 1
	if x == C[i % 6]: v[2] += 1
m = max(v)
print m
if v[0] == m: print "Adrian"
if v[1] == m: print "Bruno"
if v[2] == m: print "Goran"