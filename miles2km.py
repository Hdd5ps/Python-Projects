'''
   Miles to kilometers table
   INPUT: none
   OUTPUT: nicely formatted table of conversions
'''
KM_MILE = 1.60934

#print header first
print("Miles             Kilometers")
print("----------------------------")

miles = 0 #start at 0

while miles <= 100: #stop at 100

   kilometers = miles * KM_MILE
   print(format(miles,"^7d"),format(kilometers,'20.2f'))
   miles = miles + 5

print("----------------------------")