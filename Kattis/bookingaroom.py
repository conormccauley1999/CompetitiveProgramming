r, n = map(int, input().split())
bs = [True] * r
for _ in range(n):
    bs[int(input()) - 1] = False
for i in range(r):
    if bs[i]:
        print(i + 1)
        quit()
print('too late')
