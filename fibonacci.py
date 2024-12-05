'''
	Fibonacci sequence
	starting with 1,1
	CSC 1010
	Sept. 18, 2024
'''

x = 1
y = 1 #starting values



counter = 2 #starting after the first two

maxFib = int(input("Enter the number you want to go to: "))

print(x)
print(y)

while counter < maxFib:
	newVal = x + y #sum of previous 2
	x = y #update x to y
	y = newVal #update y to new value for next iteration
	print( format(newVal, '30,d') )
	counter = counter + 1
	
