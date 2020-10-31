# Problem 258

nums = [0] * 4000000
for k in range(1, 56):
    nums[k - 1] = ((100003 - (200003 * k) + (300007 * pow(k, 3))) % 1000000) - 500000
for k in range(56, 4000001):
    nums[k - 1] = ((nums[k - 25] + nums[k - 56] + 1000000) % 1000000) - 500000

mx = min(nums) - 1
# vertical
for x in range(2000):
    mc = 0
    for y in range(2000):
        num = nums[(y * 2000) + x]
        mc += num
        mx = max(mc, mx)
        mc = max(0, mc)
# horizontal
for y in range(2000):
    mc = 0
    for x in range(2000):
        num = nums[(y * 2000) + x]
        mc += num
        mx = max(mc, mx)
        mc = max(0, mc)
# diagonal
mc = 0
for xy in range(2000):
    num = nums[(xy * 2000) + xy]
    mc += num
    mx = max(mc, mx)
    mc = max(0, mc)
# anti-diagonal
mc = 0
for xy in range(2000):
    num = nums[(xy * 2000) + (2000 - xy)]
    mc += num
    mx = max(mc, mx)
    mc = max(0, mc)
print(mx)
