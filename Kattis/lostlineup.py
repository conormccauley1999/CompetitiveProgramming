n = int(raw_input())
a = map(int, raw_input().split())
print '1 '  + ' '.join(map(str, [a.index(i) + 2 for i in range(0, n - 1)]))
