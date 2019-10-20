N = int(raw_input())
if N > 150: N = 150
_f = { 1: 1 }
_s = { 0: 1, 1: 0 }
for i in xrange(2, N + 1):
	_f[i] = i * _f[i - 1]
	_s[i] = (i - 1) * (_s[i - 1] + _s[i - 2])
print 1 - (float(_s[N]) / float(_f[N]))
