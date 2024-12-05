'''
	Input Validation
	Oct. 2, 2024
'''

while True:
	try:
		numLines = int(input("Enter number of lines (positive odd number): "))
		break
		#input validation
	except ValueError:
		print("Did not enter an integer.")

	
while numLines <= 0 or numLines % 2 == 0:

	if numLines <= 0:
		print(numLines,"is not valid. Please enter a postive odd number.")
	else:
		print(numLines,"is an even number. Please enter a posititve odd number.")
	try:
		numLines = int(input("Enter number of lines (positive odd number): "))
	#input validation
	except TypeError:
		print("Did not enter an integer.")

top = numLines//2+1
bottom = numLines//2
spaces = 0
asterisks = numLines

#top half
for line in range(top):
	#spaces first
	for space in range(spaces):
		print(' ',end='')
	#asterisks next
	for ast in range(asterisks):
		print('*',end='')
	#advance to next line
	print()
	#update for next line
	spaces += 1
	asterisks -= 2
	
#fix spaces and asterisks for bottom
spaces = spaces - 2
asterisks = asterisks + 4

#bottom half
for line in range(bottom):
	#spaces first
	for space in range(spaces):
		print(' ',end='')
	#asterisks next
	for ast in range(asterisks):
		print('*',end='')
	#advance to next line
	print()
	#update for next line
	spaces -= 1
	asterisks += 2
