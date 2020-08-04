x = 'simon says '
t = int(input())
for _ in range(t):
    s = input()
    if s.startswith(x):
        print(s[len(x):])
    else:
        print()
