
'''
	Output the pay for each day of a month (31 days)
'''

'''Algorithm:
	step 1: set up variables for pay and starting day
	step 2: set up a while loop for the days
		2a: print the day and pay as $/cents
		2b: calculate updates
	step 3: profit???
'''

day = 1
pay = 1

total = 0.0

print("Day          Pay")
print("----------------")

while day <= 31:
	print(format(day,'3d'), format(pay/100,'20,.2f'))
	total = total + pay
	pay = pay * 2
	day = day + 1

print("Total paid is: ", format(total/100,",.2f"))
