n = int(input())
sm = n
while n != 1:
    if not n % 2:
        n = n // 2
    else:
        n = 3*n + 1
    sm += n
print(sm)