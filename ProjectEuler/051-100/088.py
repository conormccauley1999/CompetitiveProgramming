# Problem 88
# Unfinished - takes too long to run

_g = {}
def g(goal, cur_prod, cur_sum, vals_left, min_divisor):
    key = (goal, cur_prod, cur_sum, vals_left,)
    if key in _g:
        return _g[key]
    if goal == cur_prod and goal == cur_sum and vals_left == 0:
        result = True
    elif cur_prod > goal or cur_sum > goal:
        result = False
    elif vals_left == 0 and (cur_prod != goal or cur_sum != goal):
        result = False
    elif cur_prod != goal and cur_sum == goal:
        result = False
    elif goal % cur_prod != 0:
        result = False
    else:
        for divisor in range(min_divisor, goal):
            if goal % divisor == 0 and g(goal, cur_prod * divisor, cur_sum + divisor, vals_left - 1, divisor):
                _g[key] = True
                return True
        result = False
    _g[key] = result
    return result


def f(k):
    goal = k + 1
    while True:
        for divisor in range(1, goal):
            if goal % divisor == 0 and g(goal, divisor, divisor, k - 1, divisor):
                print(k, goal)
                return goal
        goal += 1


r = set()
for k in range(2, 12001):
    r.add(f(k))
print(sum(r))
