'''
Kamal Raj Timilsena
Oct 6
Question:
Write a python program that will read in a positive odd integer and print an empty "diamond"
of asterisks(*) that has that number (the one typed in) of lines.

    Step 1: take input
    Step 2: input validation
    Step 3: calculate star and spaces and print the diamond
    '''

#step 1
while True:
    try:
        size = int(input("Enter a positive odd integer: "))
    except ValueError:
        print("Integer not provided. Try again.")
        continue  # run the loop again if input is invalid

    # Step 2
    if size > 0 and size / 2 != size // 2:
        break  #exit the loop if its a postive odd number
    elif size < 0: 
        print("You typed a negative number. Please, try again.")
        continue
    elif size / 2 == size // 2:
        print("You typed an even number. Please, try again.")
        continue  # Go back to the start of the loop for new input
   
# Go back to the start of the loop for new input


# Step 3

# Upper part of the diamond
for i in range(size // 2 + 1): # Print leading spaces
    for j in range(size // 2 - i):
        print(" ", end='')  # Print space without newline
    
    # Print the first star without newline
    print("*", end='')
    
    # Print spaces between stars (only if it's not the top line)
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end='')  # Print space without newline
        print("*", end='')  # Print second star without newline
    
    print()  # Move to the next line

# Lower part of the diamond
for i in range(size // 2 - 1, -1, -1): # Print leading spaces
    for j in range(size // 2 - i):
        print(" ", end='')  # Print space without newline
    
    # Print the first star without new line
    print("*", end='')  
    
    # Print spaces between stars (only if it's not the bottom line)
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end='')  # Print space without newline
        print("*", end='')  # Print second star without newline
    
    print()  # Move to the next line
