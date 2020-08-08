diff = int(input())
ruth_candle = int(input())
theo_candle = int(input())
theo_age = 3
while True:
    ruth_age = theo_age + diff
    ruth_exp = (ruth_age * (ruth_age + 1) // 2) - 6
    theo_exp = (theo_age * (theo_age + 1) // 2) - 3
    if ruth_candle + theo_candle == ruth_exp + theo_exp:
        print(ruth_candle - ruth_exp)
        break
    theo_age += 1
