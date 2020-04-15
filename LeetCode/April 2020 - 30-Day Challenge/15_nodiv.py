class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        lo, ro = [1] * ln, [1] * ln
        lo[0] = nums[0]
        ro[ln - 1] = nums[ln - 1]
        for i in range(1, ln - 1):
            j = ln - i - 1
            lo[i] = lo[i - 1] * nums[i]
            ro[j] = ro[j + 1] * nums[j]
        ro[0] = nums[0] * ro[1]
        lo[ln - 1] = nums[ln - 1] * lo[ln - 1]
        out = [0] * ln
        out[0] = ro[1]
        out[ln - 1] = lo[ln - 2]
        for i in range(1, ln - 1):
            out[i] = lo[i - 1] * ro[i + 1]
        return out
