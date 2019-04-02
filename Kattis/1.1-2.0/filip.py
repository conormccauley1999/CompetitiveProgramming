i = raw_input().split(" ")
n = [int(i[0][::-1]), int(i[1][::-1])]
print max(n)