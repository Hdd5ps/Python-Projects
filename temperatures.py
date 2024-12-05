''' 
Temperature chart
'''
'''
    Algorithm:
    step 1: print the header
    step 2: set up a loop to go through the Fahrenheit values
         step 2a: caculate the Celsius value
         step 2b: print the current line
         step 2c: update the variable for the next iteration
    step 3: done
'''
#set up the header
print("Fahrenheit          Celsius")
print("---------------------------")

F = 0.0
C = 0.0

while F <= 212: 
    #calculate the celsius Temperature
    C = (F - 32)*(5/9)
    #print the correct line formatted appropriately
    
    print( format(F,'10.1f'), format(C, '16.1f') )
    #update F
    F = F + 2