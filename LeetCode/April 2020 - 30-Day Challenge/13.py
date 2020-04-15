class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if x == 0 else 1 for x in nums]
        sms = [0]
        for i in range(len(nums)):
            sms.append(sms[i] + nums[i])
        mx, ft = 0, {}
        for i in range(len(sms)):
            v = sms[i]
            if v in ft:
                mx = max(mx, i - ft[v])
            else:
                ft[v] = i
        return mx
