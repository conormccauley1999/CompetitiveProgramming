a = 1504170715041707
b = 4503599627370517
sm = mn = mx = a
while mn != 1:
    a = (mn + mx) % b
    mx = max(a, mx)
    if a < mn:
        mn = a
        sm += mn
print(sm)
