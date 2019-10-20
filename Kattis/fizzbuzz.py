i = raw_input().split(" ")
X, Y, N = int(i[0]), int(i[1]), int(i[2])
for i in range(1, N+1):
	if i % X == 0 and i % Y == 0: print "FizzBuzz"
	elif i % X == 0: print "Fizz"
	elif i % Y == 0: print "Buzz"
	else: print i