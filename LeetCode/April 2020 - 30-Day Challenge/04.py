class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		N = len(nums)
		for i in range(N):
			c = i
			if nums[i] == 0:
				continue
			while nums[c - 1] == 0 and c != 0:
				nums[c - 1], nums[c] = nums[c], nums[c - 1]
				c -= 1
