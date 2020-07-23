n, s, k = map(int, input().split())

dp = []
for _ in range(n):
    dp.append([0.0] * s)
dp[0][0] = 1.0

for i in range(n - 1):
    for j in range(s - 1):
        dp[i + 1][j] += dp[i][j] * ((j + 1) / s)
        dp[i + 1][j + 1] += dp[i][j] * (1 - ((j + 1) / s))
    dp[i + 1][s - 1] += dp[i][s - 1]

t = 0
for j in range(k - 1, s):
    t += dp[n - 1][j]

print(t)
