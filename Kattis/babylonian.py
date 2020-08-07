def f():
    s = input().split(',')[::-1]
    t = 0
    m = 1
    for i in range(len(s)):
        if s[i] == '':
            m *= 60
            continue
        t += int(s[i]) * m
        m *= 60
    print(t)

for _ in range(int(input())):
    f()
