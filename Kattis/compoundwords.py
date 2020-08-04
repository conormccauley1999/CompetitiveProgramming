xs = []
while True:
    try:
        vs = input().split()
        xs.extend(vs)
    except:
        ws = set([])
        for x1 in xs:
            for x2 in xs:
                if x1 == x2:
                    continue
                ws.add(x1 + x2)
        for w in sorted(list(ws)):
            print(w)
        quit()
