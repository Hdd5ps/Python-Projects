'''
Output the pay for each day of a month (31 days)

Algorithm:
step1: set up variables for pay and starting day
step2: set up a while loop for the days
step3: print the day a nd pay as $/cents
step4: calculate updates
step5: profit???

'''
day = 1
pay = 1

total = 0.0

print("Day          Pay")
print("----------------")

while day <= 31:
    print(format(day, '3d'), format(pay/100, '25,.2f'))
    total = total + pay
    pay = pay * 2
    day = day + 1

print("Total paid is: ", format(total, '.2f'))