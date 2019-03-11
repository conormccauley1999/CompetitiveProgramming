# Problem 206

import math

mn = int(math.ceil(math.sqrt(1020304050607080900)))
mx = int(math.floor(math.sqrt(1929394959697989990)))

i = mn - 1
print i
while i <= mx:
    i2 = i ** 2
    if i2 >= 1020304050607080900 and i2 <= 1929394959697989990:
        sqr = str(i2)
        if (
            sqr[0] == "1" and sqr[2] == "2" and
            sqr[4] == "3" and sqr[6] == "4" and
            sqr[8] == "5" and sqr[10] == "6" and
            sqr[12] == "7" and sqr[14] == "8" and
            sqr[16] == "9" and sqr[18] == "0"
        ):
            print i
        if i % 1000000 == 0: print mn, mx, i, i2
    i += 10
