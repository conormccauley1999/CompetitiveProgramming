def f(xs):
    s = ""
    vs = []
    for x in xs:
        try:
            vs.append(float(x))
        except:
            s += x + " "
    print(sum(vs) / len(vs), s)

while True:
    try:
        f(list(input().split()))
    except:
        break
