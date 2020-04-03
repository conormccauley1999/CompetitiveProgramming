class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		mx = -2147483647
		cur = 0
		for i in range(len(nums)):
			cur += nums[i]
			if (mx < cur): mx = cur
			if (cur < 0): cur = 0
		return mx
