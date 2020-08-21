def sd(n):
    sm = 0
    while n:
        sm += n % 10
        n //= 10
    return sm
t = int(input())
for _ in range(t):
    n = int(input())
    d = sd(n)
    for i in range(n - 1, -1, -1):
        if sd(i) == d - 1:
            print(i)
            break
