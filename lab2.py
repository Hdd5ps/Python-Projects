'''
   Step 1: Get the number of inches from the user.
   This requires converting the string to an integer.
   Store the value in a variable called inches.
   
   Step 2: Calculate the number of feet by dividing the inches
   by 12 (integer division). And then, update the leftover inches
   by modding by 12 (remainder). Variable called feet.
   
   Step 3: Calculate the number of yards by dividing the feet by
   3 (integer division). And then, update the leftover feet by
   modding by 3. Variable called yards.
   
   Step 4: Print the yards, feet, and inches.   
'''
#step 1
inches = int( input("Enter the number of inches:") )
#print(type(inches))

#step 2
feet = inches // 12
leftoverInches = inches % 12

#step 3
yards = feet // 3
leftoverFeet = feet % 3
print(format(yards,'010d'),"yds",sep='',end='')
print(leftoverFeet,"'",sep='',end='')
print(leftoverInches,'"',sep='')
