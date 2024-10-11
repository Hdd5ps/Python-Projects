'''
Test 2
oct11
Sequence
Selection
repetition => Input Validation(Check user input to ensure it is valid for the program. we often use loops for this.) Its a form of exception handling.
while 
for
'''
# prompt
while True:
    try:
        num = int(input("Enter a positive, odd number: "))
        break
    except ValueError:
        print("Integer not provided. Try again.")

# input validatin condition
while num <= 0 or num % 2 == 0:
    if num <= 0:
        print("You entered a non-postive number. Please try again.")
    else:
        print("Bad input, print a odd number. Please try again ")
    while True:
        try:
            num = int(input("Enter a positive, odd number: "))
            break
        except ValueError:
            print("Integer not provided. Try again.")



    

