# Python script for a simple recursive thingy
#
# Pick a number, n
# If n is even, set n to n / 2
# Else, set n to 3n+1
# Add 1 to count
# Continue until n is 1
#

limLow = input("Start testing from: ")
limLow = int(limLow)
limHi = input("End testing at: ")
limHi = int(limHi)

bestN = 0
highestCount = 0

for testingNumber in range(limLow, limHi):
	count = 0
	n = testingNumber
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
		if count > highestCount:
			#higher count yay
			highestCount = count
			bestN = testingNumber
	print("Count: " + str(count))
	
		
print("Best N: " + str(bestN))
print("Best Count: " + str(highestCount))
	


