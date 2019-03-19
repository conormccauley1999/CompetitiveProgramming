i = raw_input().split(" ")
D, M = int(i[0]), int(i[1])
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
dpm = [31,28,31,30,31,30,31,31,30,31,30,31]
ds = 0
for i in range(1, M): ds += dpm[i - 1]
ds += D
print days[((ds % 7) + 2) % 7]