i = raw_input().split(" ")
G, S, C = int(i[0]), int(i[1]), int(i[2])
p = (G * 3) + (S * 2) + C
o = ""
if p >= 8: o = "Province"
elif p >= 5: o = "Duchy"
elif p >= 2: o = "Estate"
if o != "": o += " or "
if p >= 6: o += "Gold"
elif p >= 3: o += "Silver"
else: o += "Copper"
print o