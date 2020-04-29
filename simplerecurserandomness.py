# Python script for a simple recursive thingy
#
# Pick a number, n
# If n is even, set n to n / 2
# Else, set n to 3n+1
# Add 1 to count
# Continue until n is 1
#

import random

count = 0
numOfRandoms = input("Number of random tests: ")
numOfRandoms = int(numOfRandoms)
limUpper = int(input("Upper limit for random numbers: "))
limLower = int(input("Lower limit for random numbers: "))


for i in range(0, numOfRandoms):
	n = random.randrange(limLower, limUpper)
	while n > 1:
		print("Number: " + str(n))
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n+1
		count += 1
	print("Final Count: " + str(count))
