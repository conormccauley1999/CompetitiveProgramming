# Problem 112

def isBouncy(n):
    ds = [int(x) for x in list(str(n))]
    isInc = True
    isDec = True
    for i in range(0, len(ds)-1):
        if ds[i] < ds[i+1]: isDec = False
        if ds[i] > ds[i+1]: isInc = False
        if (not isInc) and (not isDec): return True
    return False

def main():
    b = 0
    t = 100
    while True:
        if isBouncy(t):
            b += 1
        p = float(b) / float(t)
        if p == 0.99: return t
        t += 1

print main()
