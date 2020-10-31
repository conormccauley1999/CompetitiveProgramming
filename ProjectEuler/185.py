# Problem 185 - UNSOLVED

from copy import deepcopy

raw_guesses = [
    ['2321386104303845', 0],
    ['3847439647293047', 1],
    ['3174248439465858', 1],
    ['8157356344118483', 1],
    ['6375711915077050', 1],
    ['6913859173121360', 1],
    ['4895722652190306', 1],
    ['5616185650518293', 2],
    ['2615250744386899', 2],
    ['6442889055042768', 2],
    ['2326509471271448', 2],
    ['5251583379644322', 2],
    ['2659862637316867', 2],
    ['4513559094146117', 2],
    ['5855462940810587', 3],
    ['9742855507068353', 3],
    ['4296849643607543', 3],
    ['7890971548908067', 3],
    ['8690095851526254', 3],
    ['1748270476758276', 3],
    ['3041631117224635', 3],
    ['1841236454324589', 3]
]

_raw_guesses = [
    ['70794', 0],
    ['34109', 1],
    ['12531', 1],
    ['90342', 2],
    ['39458', 2],
    ['51545', 2]
]

def is_correct(guesses, result):
    guesses = deepcopy(guesses)
    for i in range(len(result)):
        for j in range(len(guesses)):
            if guesses[j][1][i] == result[i]:
                guesses[j][0] -= 1
    return all(guesses[i][0] == 0 for i in range(len(guesses)))

def rec(guesses, ix, num_guesses, num_digits, _rem_digits):
    all_one = True
    result = []
    for digits in _rem_digits:
        if len(digits) == 0:
            return False, []
        all_one &= len(digits) == 1
        result.append(list(digits)[0])
    if all_one:
        print(result)
        if is_correct(guesses, result):
            return True, result
        return False, result
    if ix >= num_guesses:
        return False, []
    cur_guess = guesses[ix]
    if cur_guess[0] == 1:
        for i in range(num_digits):
            if cur_guess[1][i] not in _rem_digits[i]:
                continue
            rem_digits = deepcopy(_rem_digits)
            rem_digits[i] = set([cur_guess[1][i]])
            for x in range(num_digits):
                if x == i:
                    continue
                if cur_guess[1][i] in rem_digits[x]:
                    rem_digits[x].remove(cur_guess[1][i])
            res = rec(guesses, ix + 1, num_guesses, num_digits, rem_digits)
            if res[0]:
                return res
    elif cur_guess[0] == 2:
        for i in range(num_digits):
            if cur_guess[1][i] not in _rem_digits[i]:
                continue
            for j in range(i + 1, num_digits):
                if cur_guess[1][j] not in _rem_digits[j]:
                    continue
                rem_digits = deepcopy(_rem_digits)
                rem_digits[i] = set([cur_guess[1][i]])
                rem_digits[j] = set([cur_guess[1][j]])
                for x in range(num_digits):
                    if x == i or x == j:
                        continue
                    if cur_guess[1][i] in rem_digits[x]:
                        rem_digits[x].remove(cur_guess[1][i])
                    if cur_guess[1][j] in rem_digits[x]:
                        rem_digits[x].remove(cur_guess[1][j])
                res = rec(guesses, ix + 1, num_guesses, num_digits, rem_digits)
                if res[0]:
                    return res
    elif cur_guess[0] == 3:
        for i in range(num_digits):
            if cur_guess[1][i] not in _rem_digits[i]:
                continue
            for j in range(i + 1, num_digits):
                if cur_guess[1][j] not in _rem_digits[j]:
                    continue
                for k in range(j + 1, num_digits):
                    if cur_guess[1][k] not in _rem_digits[k]:
                        continue
                    rem_digits = deepcopy(_rem_digits)
                    rem_digits[i] = set([cur_guess[1][i]])
                    rem_digits[j] = set([cur_guess[1][j]])
                    rem_digits[k] = set([cur_guess[1][k]])
                    for x in range(num_digits):
                        if x == i or x == j or x == k:
                            continue
                        if cur_guess[1][i] in rem_digits[x]:
                            rem_digits[x].remove(cur_guess[1][i])
                        if cur_guess[1][j] in rem_digits[x]:
                            rem_digits[x].remove(cur_guess[1][j])
                        if cur_guess[1][k] in rem_digits[x]:
                            rem_digits[x].remove(cur_guess[1][k])
                    res = rec(guesses, ix + 1, num_guesses, num_digits, rem_digits)
                    if res[0]:
                        return res
    return False, []

def init(raw_guesses):
    num_guesses = len(raw_guesses)
    num_digits = len(raw_guesses[0][0])
    guesses = []
    for raw_guess in raw_guesses:
        guesses.append([raw_guess[1], [int(c) for c in raw_guess[0]]])
    guesses.sort()
    rem_digits = []
    for _ in range(num_digits):
        rem_digits.append(set(i for i in range(10)))
    ix = 0
    for guess in guesses:
        if guess[0] != 0:
            break
        ix += 1
        for i in range(num_digits):
            rem_digits[i].remove(guess[1][i])
    return ''.join(map(str, rec(guesses, ix, num_guesses, num_digits, rem_digits)[1]))

print(init(raw_guesses))
