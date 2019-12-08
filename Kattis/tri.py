i = [int(v) for v in raw_input().split(" ")]
a, b = "", ""
if 	 i[0] + i[1] == i[2]: a, b = "+", "="
elif i[0] == i[1] + i[2]: a, b = "=", "+"
elif i[0] * i[1] == i[2]: a, b = "*", "="
elif i[0] == i[1] * i[2]: a, b = "=", "*"
elif i[0] - i[1] == i[2]: a, b = "-", "="
elif i[0] == i[1] - i[2]: a, b = "=", "-"
elif i[0] / i[1] == i[2]: a, b = "/", "="
elif i[0] == i[1] / i[2]: a, b = "=", "/"
print str(i[0]) + a + str(i[1]) + b + str(i[2])