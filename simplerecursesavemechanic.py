# Python script for a simple recursive thingy
#
# Pick a number, n
# If n is even, set n to n / 2
# Else, set n to 3n+1
# Add 1 to count
# Continue until n is 1
#
# NOW WITH SAVE FEATURE!!!

import io

count = 0
n = input("Pick a number: ")
n = int(n)
filename = input("File name (local): ")
file = open(filename + ".txt", "w", encoding="utf-8")

while n > 1:
	print("Number: " + str(n))
	file.write("Current Number: " + str(n))
	if n % 2 == 0:
		n = n/2
	else:
		n = 3*n+1
	count += 1



print("Final Count: " + str(count))
file.write("Final Count: " + str(count))
