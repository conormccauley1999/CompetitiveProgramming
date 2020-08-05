ws = set([])
while True:
    try:
        xs = input().split()
        os = []
        for x in xs:
            if x.lower() in ws:
                os.append('.')
            else:
                os.append(x)
                ws.add(x.lower())
        print(*os)
    except:
        break
