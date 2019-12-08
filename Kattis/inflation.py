n = int(raw_input())
bs = map(float, range(1, n + 1))
cs = sorted(map(float, raw_input().split()))
fs = [cs[i] / bs[i] for i in range(n)]
if max(fs) > 1.0: print "impossible"
else: print min(fs)
