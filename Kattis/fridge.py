digits = list(map(int, list(raw_input())))
count = [0] * 10
for digit in digits: count[digit] += 1
result = 0
isFirstNum = True
while True:
	i = 1 if isFirstNum else 0	
	minVal, minI = 1001, 0
	while i < 10:
		if count[i] < minVal: minVal, minI = count[i], i
		i += 1
	result = (result * 10) + minI
	if isFirstNum and 0 in count[1:]: break
	if not isFirstNum and 0 in count: break
	count[minI] -= 1
	isFirstNum = False
print result
