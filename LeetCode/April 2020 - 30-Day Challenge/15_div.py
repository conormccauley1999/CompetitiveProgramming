class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        for n in nums:
            if n != 0: p *= n
        zs = nums.count(0)
        out = [0] * len(nums)
        if zs == 1:
            zi = nums.index(0)
            out[zi] = p
        elif zs == 0:
            for i in range(len(nums)):
                out[i] = p // nums[i]
        return out
