''' Conversion program
    Jacob Somervell
    Sept. 2, 2024
    CSC 1010 class
    A small program to determine the amount of cups 
    of ingredients for some number of cookies
'''
#define some constants for the program

BASE_SUGAR = 1.5 #1.5 cups for 48
BASE_BUTTER = 1.0 #1 cup for 48
BASE_FLOUR = 2.75
BASE_COOKIES = 48.0
SUGAR_PER_COOKIE = BASE_SUGAR / BASE_COOKIES
BUTTER_PER_COOKIE = BASE_BUTTER / BASE_COOKIES
FLOUR_PER_COOKIE = BASE_FLOUR / BASE_COOKIES

'''
    step 1: get the number of cookies from user (float or integer?)

    step 2: print out the sugar line, formatted correctly, and print out the number of
            cups of sugar required

    step 3 and 4: same as 2, but for butter and flour respectively

    done
'''
#step 1
print("How many cookies?")
cookies = float( input() )

#step 2
print("Sugar:",format(SUGAR_PER_COOKIE * cookies, '8.2f'), "cups")
#step 3
print("Butter:",format(BUTTER_PER_COOKIE * cookies, '7.2f'), "cups")
#step 4
print("Flour:",format(FLOUR_PER_COOKIE * cookies, '8.2f'), "cups")