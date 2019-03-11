# Problem 89

with open("../files/89.txt") as f:
	nums = f.readlines()
nums = [num.strip() for num in nums]

rules = [
	["IIIII", "V"],
	["IIII", "IV"],
	["VIV", "IX"],
	["VVVVV", "XXV"],
	["VVVV", "XX"],
	["XXVXX", "XLV"],
	["VV", "X"],
	["XXXXX", "L"],
	["XXXX", "XL"],
	["LXL", "XC"],
	["LL", "C"],
	["CCCCC", "D"],
	["CCCC", "CD"],
	["DCD", "CM"],
	["DD", "M"]
]

total = 0

for num in nums:
	pre = num
	l1 = len(num)
	for rule in rules:
		num = num.replace(rule[0], rule[1])
	l2 = len(num)
	total += (l1 - l2)

print total
