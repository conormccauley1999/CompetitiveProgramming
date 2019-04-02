h = [c[0] for c in raw_input().split(" ")]
m = max(h, key=h.count)
print sum(c == m for c in h)