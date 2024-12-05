'''
Input validation example
'''
printChar = '0'
while True:
	try:
		num = int(input("Enter a postive odd number: "))
		break
	except ValueError:
		print("Integer not provided. Try again.")

while num <=0 or num%2 == 0:

	if num <= 0:
		print("You entered a non-positive number. Try again.")
	else:
		print("You entered an even number. Try again.")
		
	while True:
		try:
			num = int(input("Enter a postive odd number: "))
			break
		except ValueError:
			print("Integer not provided. Try again.")

#normal code goes here!
top = num//2 + 1
bottom = num//2
asterisks = num
spaces = 0

#print the top half
for line in range(top):
	#print spaces first
	for space in range(spaces):
		print(' ',end='')
	#print asterisks next
	for ast in range(asterisks):
		print(printChar,end='')
	#go to next line
	print()
	spaces += 1
	asterisks -= 2

#now the bottom half
#fix the asterisks and spaces
spaces = spaces - 2
asterisks = asterisks + 4

for line in range(bottom):
	#print spaces first
	for space in range(spaces):
		print(' ',end='')
	#print asterisks next
	for ast in range(asterisks):
		print(printChar,end='')
	#go to next line
	print()
	spaces -= 1
	asterisks += 2
