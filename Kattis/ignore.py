while True:
    try:
        k = int(input())
        ns = []
        while k:
            k, r = divmod(k, 7)
            ns.append(str(r))
        o = ''
        for n in ns:
            o += ['0','1','2','5','9','8','6'][int(n)]
        print(o)
    except Exception as e:
        break
