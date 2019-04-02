def m(a):
	if all(y >= x for x, y in zip(a, a[1:])): return len(a)
	else: return max(m(a[:len(a)/2]), m(a[len(a)/2:]))

n = int(raw_input())
a = map(int, raw_input().split())

print m(a)
