C = float(raw_input())
L = int(raw_input())
wl = [tuple(map(float, raw_input().split())) for _ in range(L)]
print sum(C * x[0] * x[1] for x in wl)
