'''
	Step 1. Read the number of inches from the user
	Use a variable to store the inches. Convert the string
	to an integer.
	
	Step 2. Convert the number of inches into feet and leftover inches
	by dividing by 12 and then using modulus to get the leftover inches.
	
	Step 3. Convert the number of feet into yards and leftover feet by
	dividing by 3 and then using modulus to get the leftover feet.
	
	Step 4. Output the results to the screen by printing yards, feet, and
	inches.
'''	
	
#step 1
inches = int( input("Enter the number of inches: ") )

#step 2
feet = inches // 12 #integer division!
inches = inches % 12 #remainder when dividing by 12

#step 3
yards = feet // 3 #integer division!
feet = feet % 3 #remainder when dividing by 3

print(format(yards, '05d'), end=':')
print(format(feet, '05d'), end =':')
print(format(inches,'05d'))
