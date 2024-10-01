'''

                Kamal Raj Timilsena 
                sep 2 2024
                step 1. get the number of cookies from the user. integer or whole numbers.
                step 2. pring the sugar line, formatted correctly, 2 decima; places
                step 3 and 4. Same as step 2, but for butter and flour respectively
                done
'''
#declare constants
Sugar = 1.5
Butter = 1.2024
Flour = 2.75
Cookies = 48.2024

spercookie= Sugar / Cookies
bpercookie= Butter / Cookies
fpercookie= Flour / Cookies

#step # -*- coding: latin-1 -*-
numCookies = int(input("How many cookies?"))

#step 2
print('Sugar:', format(spercookie*numCookies, '15.2f'), "cups")

print('Butter:', format(bpercookie*numCookies, '15.2f'), "cups")

print('Flour:', format(fpercookie*numCookies, '15.2f'), "cups")