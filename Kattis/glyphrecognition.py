n = int(raw_input())
ps = [tuple(map(int, raw_input().split())) for _ in range(n)]

k, m = solve(ps)

print "%d %f" % (k, m)
