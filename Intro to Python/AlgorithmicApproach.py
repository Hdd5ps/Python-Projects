'''
Write a while loop that lets the user enter a number. The number should be multiplied by 10, and the result assigned to a variable named product. The loop should iterate as long 
as product is less than 100.
product = 1

while product < 100:
    product = int(input("Enter a number you would like to be multiplied by 10: "))
    product *= 10

Write a while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user if he or she wishes to perform the operation
again. If so, the loop should repeat, otherwise it should terminate.
'''
answers = ['yes', 'Yes', "YES", "Y", "y", "ok", "okay"]
answer = 'yes'

while answer in answers:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print("Sum of number's assigned is: ", num1 + num2)
    answer = input("Peform the operation again? Please reply 'yes' or 'no'")



