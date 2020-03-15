while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    xa, xb = a, b
    na, nb = [a], [b]
    s = 0
    while True:
        if xa in nb:
            sa = s if a != 1 else 0
            sb = nb.index(xa)
            c = xa
            break
        if xb in na:
            sb = s if b != 1 else 0
            sa = na.index(xb)
            c = xb
            break
        if xa != 1:
            xa = int(xa / 2) if xa % 2 == 0 else 3 * xa + 1
            na.append(xa)
        if xb != 1:
            xb = int(xb / 2) if xb % 2 == 0 else 3 * xb + 1
            nb.append(xb)
        s += 1
    print(f"{a} needs {sa} steps, {b} needs {sb} steps, they meet at {c}")
