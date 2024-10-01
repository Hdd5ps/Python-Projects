'''
Kamal Raj Timilsena
Sept 7 2024
Program 2
Tony is trying to losesome weight for an upcoming high school reunion. He has carefully calculated his caloric intake and caloric 
expense for the past 7 days. He needs to know how many pounds he can lose in a week and how many weeks it would take to lose 10 
pounds. 
Write a Python program that asks Tony for the caloric intake and expense for each of the seven days, then prints out a summary table
showing his daily caloric deficit for the week, how many  pounds he lost, and how many weeks it would take to lose 10 pounds.
According to "the internet", it takes a caloric deficit of 3500 to lose one pound.

Step 1: Ask Tony for the caloric intake and expense for each of the seven days.

Step 2: Calculate the daily calory deficit, total deficit for week, pounds lost, and weeks to lose 10 pounds.

Step 3: Print oyt  a summary table showing his daily caloric deficit, his deficit for the week, how many pounds he lost, and how 
weeks it would take to lose 10 pounds.
'''

#Declare Constant

CaloricDeficit = 3500

Pounds2Lose = 10

#Days of the week
D1 = 1
D2 = 2 
D3 = 3
D4 = 4
D5 = 5
D6 = 6
D7 = 7

#step 1

CaloricIntake1 = float(input("Tony, Enter the Caloric Intake for Day 1: "))

CaloricExpense1 = float(input("Tony, Enter the Caloric Expense for Day 1: "))

CaloricIntake2 = float(input("Tony, Enter the Caloric Intake for Day 2: "))

CaloricExpense2 = float(input("Tony, Enter the Caloric Expense for Day 2: "))

CaloricIntake3 = float(input("Tony, Enter the Caloric Intake for Day 3: "))

CaloricExpense3 = float(input("Tony, Enter the Caloric Expense for Day 3: "))

CaloricIntake4 = float(input("Tony, Enter the Caloric Intake for Day 4: "))

CaloricExpense4 = float(input("Tony, Enter the Caloric Expenxe for Day 4: "))

CaloricIntake5 = float(input("Tony, Enter the Caloric Intake for Day 5: "))

CaloricExpense5 = float(input("Tony, Enter the Caloric Expense for Day 5: "))

CaloricIntake6 = float(input("Tony, Enter the Caloric Intake for Day 6: "))

CaloricExpense6 = float(input("Tony, Enter the Caloric Expense for Day 6: "))

CaloricIntake7 = float(input("Tony, Enter the Caloric Intake for Day 7: "))

CaloricExpense7 = float(input("Tony, Enter the Caloric Expense for Day 7: "))


#step 2

CaloricDeficit1 = CaloricExpense1 - CaloricIntake1

CaloricDeficit2 = CaloricExpense2 - CaloricIntake2

CaloricDeficit3 = CaloricExpense3 - CaloricIntake3

CaloricDeficit4 = CaloricExpense4 - CaloricIntake4

CaloricDeficit5 = CaloricExpense5 - CaloricIntake5

CaloricDeficit6 = CaloricExpense6 - CaloricIntake6

CaloricDeficit7 = CaloricExpense7 - CaloricIntake7

TotalWeekDeficit = CaloricDeficit1 + CaloricDeficit2 + CaloricDeficit3 + CaloricDeficit4 + CaloricDeficit5 + CaloricDeficit6 + CaloricDeficit7

PoundsLost = (TotalWeekDeficit / 3500)

Weeks2Lose = (Pounds2Lose - PoundsLost) / PoundsLost


#step 3

print("Day 1 intake: ", format(CaloricIntake1, '.0f'))
print("Day 1 expense: ", format(CaloricExpense1, '.0f'))
print("")
print("Day 2 intake: ", format(CaloricIntake2, '.0f'))
print("Day 2 expense: ", format(CaloricExpense2, '.0f'))
print("")
print("Day 3 intake: ", format(CaloricIntake3, '.0f'))
print("Day 3 expense: ", format(CaloricExpense3, '.0f'))
print("")
print("Day 4 intake: ", format(CaloricIntake4, '.0f'))
print("Day 4 expense: ", format(CaloricExpense4, '.0f'))
print("")
print("Day 5 intake: ", format(CaloricIntake5, '.0f'))
print("Day 5 expense: ", format(CaloricExpense5, '.0f'))
print("")
print("Day 6 intake: ", format(CaloricIntake6, '.0f'))
print("Day 6 expense: ", format(CaloricExpense6, '.0f'))
print("")
print("Day 7 intake: ", format(CaloricIntake7, '.0f'))
print("Day 7 expense: ", format(CaloricExpense7, '.0f'))
print("")
print("Summary: ")
print("------------------")
print("Day        Deficit")

print(D1, format(CaloricDeficit1, '16.0f'))
print(D2, format(CaloricDeficit2, '16.0f'))
print(D3, format(CaloricDeficit3, '16.0f'))
print(D4, format(CaloricDeficit4, '16.0f'))
print(D5, format(CaloricDeficit5, '16.0f'))
print(D6, format(CaloricDeficit6, '16.0f'))
print(D7, format(CaloricDeficit7, '16.0f'))

print("Total", format(TotalWeekDeficit, '12.0f'))

print("Pounds Lost: ", format(PoundsLost, '3.2f'))

print("Weeks to lose 10 pounds: ", format(Weeks2Lose + D1, '0.2f'))

