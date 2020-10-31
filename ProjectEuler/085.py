# Problem 85

def getRect(w, h):
    r = 0

    for x in range(0, w):
        for y in range(0, h):
            r += (w - x) * (h - y)

    return r


def main():
    
    a = 0
    mnD = 2000000

    for w in range(1, 100):
        for h in range(1, 100):
            r = getRect(w, h)
            d = abs(2000000 - r)
            if d < mnD:
                mnD = d
                a = w * h

    return a


print main()
