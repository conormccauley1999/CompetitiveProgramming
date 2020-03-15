ls = list(map(int, input().split()))
while True:
    if ls[0] > ls[1]:
        ls[0], ls[1] = ls[1], ls[0]
        print(*ls)
    if ls[1] > ls[2]:
        ls[1], ls[2] = ls[2], ls[1]
        print(*ls)
    if ls[2] > ls[3]:
        ls[2], ls[3] = ls[3], ls[2]
        print(*ls)
    if ls[3] > ls[4]:
        ls[3], ls[4] = ls[4], ls[3]
        print(*ls)
    if ls == sorted(ls):
        break

