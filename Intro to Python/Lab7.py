'''
Repetition
Oct 10 2024
Kamal Raj Timilsena
Write a Python program that lets the user play craps. Craps is a dice game where the player rolls two six-sided dice. The sum of the 
numbers on top is used to determine what happens. 
'''
import random # imports a package of library which gives random numbers if called
die1 = random.randrange(1, 7) #between 1 and 6
die2 = random.randrange(1, 7) #between 1 and 6

answer = ['y', 'yes', 'Yes', 'YES', 'Y', 'YEs', 'yeS', 'yES'] 

winfirst = [7, 11]
losefirst = [2, 3]
other = [1, 4, 5, 6, 8, 9, 10, 12]

while die1 + die2 in other:
    print("Point is", die1 ,"+", die2 ,"=", die1 + die2)
    die1 = random.randrange(1, 7) #between 1 and 6
    die2 = random.randrange(1, 7) #between 1 and 6
    
    if die1 + die2 in losefirst:
        print("You lost")
        question = print("Do you you want to proceed with new dice? y/n")
    
        if question in answer:
            die1 = random.randrange(1, 7) #between 1 and 6
            die2 = random.randrange(1, 7) #between 1 and 6

            if die1 + die2 in winfirst:
                print("You won")
                question = print("Do you you want to proceed with new dice? y/n")
    
                if question in answer:
                    die1 = random.randrange(1, 7) #between 1 and 6
                    die2 = random.randrange(1, 7) #between 1 and 6

                    while die1 + die2 != 7:
                        print("Point is", die1 ,'+', die2 ,'=', die1 + die2)
                        die1 = random.randrange(1, 7) #between 1 and 6
                        die2 = random.randrange(1, 7) #between 1 and 6

                        if die1 + die2 in losefirst:
                            print("You lost")
                            question = print("Do you you want to proceed with new dice? y/n")
                            if question in answer:
                                die1 = random.randrange(1, 7) #between 1 and 6
                                die2 = random.randrange(1, 7) #between 1 and 6

                        if die1 + die2 in winfirst:
                            print("You won")
                            question = print("Do you you want to proceed with new dice? y/n")
                
                            if question in answer:
                                die1 = random.randrange(1, 7) #between 1 and 6
                                die2 = random.randrange(1, 7) #between 1 and 6

if die1 + die2 in losefirst:
        print("You lost")
        question = print("Do you you want to proceed with new dice? y/n")
    
        if question in answer:
            die1 = random.randrange(1, 7) #between 1 and 6
            die2 = random.randrange(1, 7) #between 1 and 6

            if die1 + die2 in winfirst:
                print("You won")
                question = print("Do you you want to proceed with new dice? y/n")
    
            if question in answer:
                die1 = random.randrange(1, 7) #between 1 and 6
                die2 = random.randrange(1, 7) #between 1 and 6

                while die1 + die2 != 7:
                    print("Point is", die1 ,'+', die2 ,'=', die1 + die2)
                    die1 = random.randrange(1, 7) #between 1 and 6
                    die2 = random.randrange(1, 7) #between 1 and 6

                    if die1 + die2 in losefirst:
                        print("You lost")
                        question = print("Do you you want to proceed with new dice? y/n")
                        if question == answer:
                            die1 = random.randrange(1, 7) #between 1 and 6
                            die2 = random.randrange(1, 7) #between 1 and 6

                        if die1 + die2 in winfirst:
                            print("You won")
                            question = print("Do you you want to proceed with new dice? y/n")
                
                            if question in answer:
                                die1 = random.randrange(1, 7) #between 1 and 6
                                die2 = random.randrange(1, 7) #between 1 and 6  