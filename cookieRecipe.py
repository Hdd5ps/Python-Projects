'''
   CSC 1010 class
   Sept. 2, 2024
   example program
   This simple program will determine the amounts of ingredients
   required for a specific number of cookies (provided by the user)

'''

'''
    step 1. get the number of cookies from the user. integer or whole numbers
    
    step 2. print the sugar line, formatted correctly, 2 decimal places
    
    steps 3 and 4. Same as step 2, but for butter and flour respectively
    
    done
'''

#declare constants
START_SUGAR = 1.5
START_BUTTER = 1.0
START_FLOUR = 2.75
START_COOKIES = 48.0

SUGAR_PER_COOKIE = START_SUGAR / START_COOKIES
BUTTER_PER_COOKIE = START_BUTTER / START_COOKIES
FLOUR_PER_COOKIE = START_FLOUR / START_COOKIES

#step 1
numCookies = int( input("How many cookies? ") )

#step 2
print("Sugar:", format(SUGAR_PER_COOKIE*numCookies,'15.2f'), "cups" )
print("Butter:", format(BUTTER_PER_COOKIE*numCookies,'14.2f'), "cups" )
print("Flour:", format(FLOUR_PER_COOKIE*numCookies,'15.2f'), "cups" )


