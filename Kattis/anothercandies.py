t = int(input())
for _ in range(t):
    input()
    n = int(input())
    s = 0
    for __ in range(n):
        s += int(input())
    print('YES' if s % n == 0 else 'NO')
