'''
	Lab 6
	CSC 1010
	October 3, 2024
	
	INPUT: an integer
	OUTPUT: the number reversed
	
	ALGORITHM:
	
	1. ask user for the number
	2. verify input
		a. if < 0, print a statement
		b. if == 0, print the reverse of zero
	3. reverse the number
		a. repeat until the number is zero: (a loop!)
		    i. print the one's digit
		    ii. drop off the one's digit
		    
	4. repeat steps 1 - 3 (use a while loop)
'''

#get the number from the user
#ideally, the try execpt blocks would also work, but we haven't learned it fully
number = int(input("Enter a non-negative integer: (-17 to stop) "))

while number != -17: # not(number == -17)
	
	#input validation
	if number < 0:
		
		print("You've entered a negative value. Try again.")
	
	elif number == 0:
	
		print("0 reversed is 0")
	
	else:
		print(number,"reversed is ", end='')
		#do the reversal code here
		#while number is not zero loop
		    #output 1's digit
		    #drop off 1's digit
		
	print() #neatness
		
	#get the next number, for the next iteration of the loop
	number = int(input("Enter a non-negative integer: (-17 to stop) "))

