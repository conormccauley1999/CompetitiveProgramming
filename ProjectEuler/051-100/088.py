# Problem 88

M = 12000

_f = {}
def f(k, left, min_div, cur_sum, used):
    if left == 1:
        assert(cur_sum <= k)
        used += k - cur_sum
        if used <= M and (used not in _f or k < _f[used]):
            _f[used] = k
        return
    for i in range(2, min_div + 1):
        if left % i == 0:
            f(k, left // i, min(i, min_div), cur_sum + i, used + 1)

for i in range(2, (M * 2) + 1):
    f(i, i, i, 0, 0)

r = set()
for k in range(2, M + 1):
    r.add(_f[k])
print(sum(r))
