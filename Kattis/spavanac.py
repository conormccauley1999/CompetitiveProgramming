i = raw_input().split(" ")
H, M = int(i[0]), int(i[1])
if M < 45: H = (H - 1) % 24
M = (M - 45) % 60
print H, M