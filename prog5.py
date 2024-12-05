'''
	CSC 1010 class
	Oct. 7, 2024
	Program 5 attempt
	
	INPUT: a positive odd integer
	
	OUTPUT: an empty diamond of the correct size (number of lines = input)
	
	ALGORITHM:
	
		1. get the number from the user
			1a. Use input validation
			1b. Fix any even number by adding 1
		
		2. Print the diamond
			2a. print the first line
			2b. loop to print the top half
			2c. loop to print the bottom half
			3d. print the last line
'''

#input with validation
numLines = int (input("Enter a positive odd number: "))
while numLines < 1:
	print("That number is not valid. Please try again.")
	numLines = int (input("Enter a positive odd number: "))

#now deal with even numbers
if numLines % 2 == 0:
	print("That number is even. Changing it to odd by adding 1.")
	numLines += 1

firstLineSpaces = numLines // 2

if numLines == 1:
	print('*')
	exit() #done so stop executing

#print first line
for sp in range(firstLineSpaces):
	print('.',end='')
print('*',end='')
print()

#top half
top = firstLineSpaces
spacesF = top - 1
spacesM = 1
for line in range(top):
	#spaces in front
	for sp in range(spacesF):
		print('.',end='')
	#asterisk
	print('*',end='')
	#spaces in middle
	for sp in range(spacesM):
		print('.', end='')
	#print asterisk
	print('*',end='')
	print()
	#update variables for next line
	spacesF -= 1
	spacesM += 2

#bottom half
#fixing the numbers from last iteration
spacesF += 2
spacesM -= 4

bottom = top - 1
for line in range(bottom):
	#spaces in front
	for sp in range(spacesF):
		print('.',end='')
	#asterisk
	print('*',end='')
	#spaces in middle
	for sp in range(spacesM):
		print('.', end='')
	#print asterisk
	print('*',end='')
	print()
	#update variables for next line
	spacesF += 1
	spacesM -= 2

#print last line
for sp in range(firstLineSpaces):
	print('.',end='')
print('*',end='')
print()

