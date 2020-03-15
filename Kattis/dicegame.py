a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())
g = a1 + a2 + ((b1 - a1) / 2) + ((b2 - a2) / 2)
e = a3 + a4 + ((b3 - a3) / 2) + ((b4 - a4) / 2)
if g > e:
    print("Gunnar")
elif e > g:
    print("Emma")
else:
    print("Tie")
