i = 1
while True:
    try:
        l = map(int, raw_input().split())[1:]
        mn, mx = min(l), max(l)
        print "Case %d: %d %d %d" % (i, mn, mx, mx - mn)
        i += 1
    except:
        break
