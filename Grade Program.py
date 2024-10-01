'''
Lab 3
Kamal Raj Timilsena
Sept 5 2024
Breakdown:


step 1: get the data from the user. get the homework average, lab average, quiz average, and test average. Finally, get the disired course grade.

step 2: calculate the contribution to the grade for each type of work (homework, lab, quiz, test) and then determine the required grade on the final exam.

step 3: pring the summary table with the components and their contribution to the grade (as required). format contribution with 1 decimal place. use th e'%" on the averages

step 4: output the disired grade and the required grade for the final exam.

'''
#declare constants

Hw_Worth = 0.2

Lab_Worth = 0.2

Quiz_Worth = 0.1

Test_Worth = 0.3

Final_Worth = 0.2


# Step 1: Get the data from the user

hw_ave = float(input("Enter the Homework Average: "))

lab_ave = float(input("Enter the Lab Average: "))

quiz_ave = float(input("Enter the Quiz Average: "))

test_ave = float(input("Enter the Test Average: "))

desired_grade = float(input("Enter the Desired grade: "))


# Step 2: Calculate the contribution to the grade for each type of work 

hw_grade = hw_ave * Hw_Worth

lab_grade = lab_ave * Lab_Worth

quiz_grade = quiz_ave * Quiz_Worth

test_grade = test_ave * Test_Worth

before_final_grade = hw_grade + lab_grade + quiz_grade + test_grade

required_final_grade = (desired_grade - before_final_grade)/Final_Worth 


# Step 3: Print the summary table with the components and their contribution to the grade

print("Component		Your Average	Course grade amount")

print("------------------------------------------------------------")

print("Homework", format(hw_ave,'25.1f'),"%",format(hw_grade,'26.1f'),sep='')

print("Lab", format(lab_ave,'30.1f'),"%",format(lab_grade,'26.1f'),sep='')

print("Quiz", format(quiz_ave,'29.1f'),"%",format(quiz_grade,'26.1f'),sep='')

print("Test", format(test_ave,'29.1f'),"%",format(test_grade,'26.1f'),sep=''
)
print("------------------------------------------------------------")

print("Grade before taking the final: ", format(before_final_grade,'29.1f'),sep='')

print("Desired Grade: ", format(desired_grade, '45.1f'), sep='')

# Step 4: Output the desired grade and the required grade for the final exam

print("Grade needed on final to get desired grade: ", format(required_final_grade, '16.1f'), sep='')
