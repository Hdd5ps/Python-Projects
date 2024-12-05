'''
   Lab 3
   CSC 1010 class
   Sept. 5, 2024
   
   Program to determine required final grade to get some desired grade.
   Breakdown:
      Homework   20%
      Labs       20%
      Quizzes    10%
      Tests      30%
      Final Exam 20%
   
   step 1: get the data from the user. get the homework average, lab average,
           quiz average, and test average. finally, get the desired course grade.
   
   step 2: calculate the contribution to the grade for each type of work (homework,
   lab, quiz, test) and then determine the required grade on the final exam
   
   step 3: print the summary table with the components and their contribution to the
   grade (as required). format contribution with 1 decimal place. use the '%' on the
   averages
   
   step 4: output the desired grade and the required grade for the final exam with
           proper formatting

'''
# set up some constants
HW_WEIGHT = .20
LAB_WEIGHT = .20
QUIZ_WEIGHT = .10
TEST_WEIGHT = .30
FINAL_WEIGHT = .20

#step 1
hw_ave = float( input("Homework average? ") ) #get the homework average
#other inputs

#step 2
#perform some calculations
hw_contrib = hw_ave * HW_WEIGHT #contribution to grade from homework

#step 3
#print the summary table
print("Component      Your Average       Course grade amount")
print("-----------------------------------------------------")
print("Homework",format(hw_ave,'18.1f'),"%",format(hw_contrib,'26.1f'),sep='')

#step 4: print the desired grade and required grade