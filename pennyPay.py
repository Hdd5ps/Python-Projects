'''
   Pennies for pay
   to display money amount per day for 31 days
   where pay is double the prevous day in pennies
   INPUT: none

   OUTPUT: a table with pay per day and final total pay, ninely formatted
'''

pay = 1 #holds the pay per day in pennies
day = 1 #keeps track of which day
totalPay = 0 #stores the total amount paid for the month

print("Day            Pay")
print("------------------")

while day <= 31: #go for 31 days in the month
    #print the information for each day to the screen
    print(format(day,"2d"),f"{'$':>10s}{pay/100:>13.2f}",sep='')
    #add pay to total
    totalPay = totalPay + pay
    #update pay
    pay = pay * 2
    #update day
    day = day + 1

print("Total made in the month", format(totalPay/100, ",.2f"))