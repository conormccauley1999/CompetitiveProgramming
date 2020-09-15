# Problem 113

def cnt(length, inc):
    end = 10 if inc else -1
    step = 1 if inc else -1
    dp = []
    dp.append([1] * 10)
    dp[0][0] = 0
    for _ in range(length - 1):
        dp.append([0] * 10)
    for cur_position in range(1, length):
        for cur_digit in range(10):
            for next_digit in range(cur_digit, end, step):
                dp[cur_position][cur_digit] += dp[cur_position - 1][next_digit]
    return sum(dp[length - 1])

print(sum(cnt(i, True) + cnt(i, False) - 9 for i in range(1, 101)))
