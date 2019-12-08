i = 1
while True:
    try:
        a = map(int, raw_input().split())
        b = map(int, raw_input().split())
        x = (a[0] * b[1]) - (a[1] * b[0])
        print "Case %d:" % (i)
        print b[1] / x, -a[1] / x
        print -b[0] / x, a[0] / x
        i += 1
    except:
        break
    try:
        c = raw_input()
    except:
        break
