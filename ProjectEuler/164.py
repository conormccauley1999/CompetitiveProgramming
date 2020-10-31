# Problem 164

M = 20

dp = []
for i in range(M):
    _dp = []
    for j in range(10):
        __dp = []
        for k in range(10):
            __dp.append(0)
        _dp.append(__dp)
    dp.append(_dp)

for d0 in range(1, 10):
    for d1 in range(10):
        if d0 + d1 > 9:
            break
        dp[1][d0][d1] = 1

for t in range(2, M):
    for d0 in range(10):
        for d1 in range(10):
            for d2 in range(10):
                if d0 + d1 + d2 > 9:
                    break
                dp[t][d1][d2] += dp[t - 1][d0][d1]

s = 0
for d0 in range(10):
    for d1 in range(10):
        s += dp[M - 1][d0][d1]
print(s)
