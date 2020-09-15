# Problem 389 - UNSOLVED

MAX = 4 * 6 * 8 * 12 * 20
dp = [0] * MAX

# ...

t, c = 0, 0
for i in range(MAX):
    t += (i + 1) * dp[i]
    c += dp[i]
m, v = t / c, 0
for i in range(MAX):
    v += dp[i] * pow((i + 1) - m, 2)
v /= c
print(v)
