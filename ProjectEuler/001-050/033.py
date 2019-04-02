# Problem 33

num_prod, den_prod = 1, 1

for n in range(10, 100):
	for d in range(10, 100):

		if (n < d) and (n % 10 != 0) and (d % 10 != 0):

			n_last = int(str(n)[1])
			d_first = int(str(d)[0])

			if n_last == d_first:

				if (float(n) / float(d)) == (float(str(n)[0]) / float(str(d)[1])):
					num_prod *= n
					den_prod *= d

print float(den_prod) / float(num_prod)
