lo, hi = 1, 1000
while lo <= hi:
    m = (hi + lo) // 2
    print(m, flush=True)
    r = input()
    if r == 'higher':
        lo = m + 1
    elif r == 'lower':
        hi = m - 1
    else:
        break
