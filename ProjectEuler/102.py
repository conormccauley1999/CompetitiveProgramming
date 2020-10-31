# Problem 102

from math import sqrt

def getTriangles():
    ts = []
    with open("../files/102.txt") as f:
        lns = f.readlines()
    lns = [x.strip() for x in lns]
    for ln in lns:
        pts = [int(x) for x in ln.split(",")]
        t = [[pts[0], pts[1]], [pts[2], pts[3]], [pts[4], pts[5]]]
        ts.append(t)
    return ts

def sign(P, Q):
    return (Q[0] * (Q[1] - P[1])) - (Q[1] * (Q[0] - P[0]))

def containsOrigin(t):

    A = [t[0][0], t[0][1]]
    B = [t[1][0], t[1][1]]
    C = [t[2][0], t[2][1]]
    
    x = sign(A, B) < 0
    y = sign(B, C) < 0
    z = sign(C, A) < 0
    
    return x == y and y == z

def main():
    
    ts = getTriangles()

    r = 0
    for t in ts:
        c = containsOrigin(t)
        if c: r += 1

    return r

print main()
