while True:
    try:
        s = input()
        i = 0
        o = []
        c = False
        x = ''
        while i < len(s):
            if c:
                if s[i] in '0123456789abcdefABCDEF':
                    x += s[i]
                else:
                    o.append(x)
                    c = False
                    x = ''
            else:
                if s[i] == '0' and i < len(s) - 1 and s[i + 1] in 'xX':
                    x = s[i:i+2]
                    c = True
                    i += 1
            i += 1
        if x != '':
            o.append(x)
        for p in o:
            print(p, int(p[2:], 16))
    except:
        break
