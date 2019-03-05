# Problem 32

sm = 0
products = []

digits = [1,2,3,4,5,6,7,8,9]

for a in range(1, 1000):

	for b in range(1, 10000):

		product = a*b
		string = str(a) + str(b) + str(product)

		if (product not in products) and (len(string) == 9):

			result = 0
			for digit in digits:
				if str(digit) in string:
					result += 1

			if result == 9:
				products.append(product)
				sm += product

print sm
