from math import log10, floor, e, pi

while True:
    try:
        n = int(input())
        if n <= 1:
            print(1)
        else:
            print(floor(n * log10(n / e) + log10(2 * pi * n) / 2) + 1)
    except Exception as e:
        quit()
