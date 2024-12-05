'''
    Program 5 attempt
    CSC 1010
    Oct. 7, 2024

    INPUT: a positive odd number
    
    OUTPUT: an empty diamond of that size
    
    ALGORITHM:
    
    1. get the data from the user
        1a. check for positive
        1b. fix even numbers
    
    2. print the diamond
        2a. print the first line
        2b. print the top half
        2c. print the bottom half
        2d. print the last line

'''
#get input and validate
numLines = int(input("Enter a positive odd number: "))
while numLines < 1:
    print("That number is not positive. Try again.")
    numLines = int(input("Enter a positive odd number: "))

#fix even numbers
if numLines % 2 == 0:
    print("That number is even. We are adding 1 to make it odd.")
    numLines += 1

if numLines == 1:
	print('*')
	exit() #we are done

#print the first line
firstLinespaces = numLines // 2
for sp in range(firstLinespaces):
    print(" ",end ='')
print('*',end='')
print()

#print the top half
top = firstLinespaces
spacesFront = top - 1
spacesMid = 1
for line in range(top):
    #print leading spaces
    for sp in range(spacesFront):
        print(' ',end='')
    #print an asterisk
    print('*',end='')
    #print middle spaces
    for sp in range(spacesMid):
        print(' ',end='')
    print('*',end='')
    print()
    #update variables for next iteration
    spacesFront -= 1
    spacesMid += 2
#fix the number of spaces
spacesFront += 2
spacesMid -= 4

#print the bottom half
bottom = top - 1
for line in range(bottom):
    #print leading spaces
    for sp in range(spacesFront):
        print(' ',end='')
    #print an asterisk
    print('*',end='')
    #print middle spaces
    for sp in range(spacesMid):
        print(' ',end='')
    print('*',end='')
    print()
    #update variables for next iteration
    spacesFront += 1
    spacesMid -= 2

for sp in range(firstLinespaces):
    print(" ",end ='')
print('*',end='')
print()
