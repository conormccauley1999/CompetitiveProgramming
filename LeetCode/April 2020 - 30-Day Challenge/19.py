class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N == 0:
            return -1
        elif N == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        F = False
        L, H = 0, N - 1
        M = L + (H - L) // 2
        while H >= L:
            if nums[M] < nums[0] and nums[M] < nums[M - 1]:
                F = True
                break
            elif nums[M] < nums[0]:
                H = M - 1
            else:
                L = M + 1
            M = L + (H - L) // 2    
        L = 0 if target > nums[-1] or not F else M
        H = (M - 1) if target > nums[-1] and F else (N - 1)
        M = L + (H - L) // 2
        while H >= L:
            if nums[M] == target:
                return M
            elif nums[M] > target:
                H = M - 1
            else:
                L = M + 1
            M = L + (H - L) // 2
        return -1
