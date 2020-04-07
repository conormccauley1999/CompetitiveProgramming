class Solution:
	def countElements(self, arr: List[int]) -> int:
		sa = set(arr)
		cnt = 0
		for i in range(len(arr)):
			if arr[i] + 1 in sa:
				cnt += 1
		return cnt
