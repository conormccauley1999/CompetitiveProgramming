class Solution:
	def isHappy(self, n: int) -> bool:
		v = set([n])
		while n != 1:
			n = sum(int(d) ** 2 for d in str(n))
			if n != 1 and n in v:
				return False
			v.add(n)
			return True
