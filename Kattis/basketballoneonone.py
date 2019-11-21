s = input()
l = len(s) // 2
a, b = 0, 0
wb2 = False
for i in range(l):
    x, y = s[i * 2], int(s[i * 2 + 1])
    if x == "A": a += y
    else: b += y
    if a > b and a >= 11 and abs(a - b) > 1:
        print("A")
        break
    elif b > a and b >= 11 and abs(a - b) > 1:
        print("B")
		break
