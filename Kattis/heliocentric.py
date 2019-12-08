i = 1
while True:
    try:
        e, m = map(int, raw_input().split())
        r = 0
        while True:
            if (e + r) % 365 == 0 and (m + r) % 687 == 0: break
            r += 1
        print "Case %d: %d" % (i, r)
        i += 1
    except:
        break
