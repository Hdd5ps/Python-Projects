# Kamal Raj Timilsena
# Date: October 3, 2024
# Lab 6
# This program reads an integer from the user and prints the integer backwards.
# The program continues to read integers until the user specifies the stop value (-17).
# Only non-negative integers are accepted. If an invalid value is entered, the user is asked to enter another value.

# Algorithm:
# Step 1. Prompt the user to enter a positive integer.
# step 2. Verify the number:
#    a. If the number is -17, stop the program.
#    b. If the number is negative, ask the user to enter another value.
#    c. If the number is 0, print "0 is reversed as 0."
# step 3. Reverse the number:
#    a. Initialize a variable to hold the reversed number.
#    b. Use a loop to reverse the digits of the number.
#    c. Print the reversed number with leading zeros preserved.
# step 4. Repeat steps 1 to 3 using a while loop.

# Step 4: Repeat everything with a big scope while loop covering the whole code
while True:
    # Step 1: Take input from the user
    try:
        num = int(input("Enter a positive integer: (-17 to stop): "))
    except ValueError:
        print("Integer not provided. Try again.")
        continue  # run the loop again if input is invalid

    # Step 2: Verify the number
    if num == -17:
        break  # Exit the loop if the user types -17
    elif num < 0:
        print("You typed a negative number. Please, try again.")
        continue  # Go back to the start of the loop for new input
    elif num == 0:
        print("0 is reversed as 0.")
        continue  # Go back to the start of the loop for new input

    # Step 3: Reverse the number
    print(num, "reversed is ", end="")
    new_num = num  # Use a new variable to manipulate the number
    # # Loop to reverse the digits of the number
    
    while new_num > 0:
        ones_place = new_num % 10  # Get the last digit
        print(ones_place, end="") # Print the reversed number
        new_num = new_num // 10  # Remove the last digit from new number
    print()
