# Python script for a simple recursive thingy
#
# Pick a number, n
# If n is even, set n to n / 2
# Else, set n to 3n+1
# Add 1 to count
# Continue until n is 1
#

count = 0
n = input("Pick a number: ")
n = int(n)

looping = False
allNumbers = []
while not looping:
	print("Number: " + str(n))
	if n % 2 == 0:
		n = n/2+1
	else:
		n = 3*n-1
	count += 1
	if n not in allNumbers:
		allNumbers.append(n)
	else:
		looping = True



print("Final Count: " + str(count))
