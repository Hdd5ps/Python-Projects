'''
Lab 5
09/19/2024
Kamal Raj Timilsena
Write a Python program that will calculate individual income tax. The progressive income tax is
calculated on the gross income for a person based on the following tax brackets:
Rate Income amount
10% Up to $9,525.00 On the first 9525
12% $9,525.01 to $38,700.00 Only on the amount over 9525
22% 38,700.01 to $82,500.00 Only on the amount over 38700
24% $82,500.01 to $157,500.00 Only on the amount over 82500
32% $157,500.01 to $200,000.00 Only on the amount over 157500
35% $200,000.01 to $500,000.00 Only on the amount over 200000
37% Over $500,000.00 Only on the amount over 500000
Your program should prompt the user to enter their income for the year. Your program will calculate the
the income tax based on the progressive table listed above. You will have to calculate the correct tax
based on the brackets and only charge the full tax rate on the amount that reaches the associated
threshold.
Your output should look exactly like the following:
Yearly Income: $ 100,000.00
Tax rate: 24%
Income tax: $ 18,289.50
You need to format your output exactly like shown above. The ‘:’ are aligned, the ‘$’ are aligned, and the
decimal with 2 decimals after are aligned.
Remember to analyze the problem according to what data needs to be input, what calculations you have
to perform, and what data needs to be printed.
'''
#declare constants(tax percentage on each bracket)

rate1 = 0.1
rate2 = 0.12
rate3 = 0.22
rate4 = 0.24
rate5 = 0.32
rate6 = 0.35
rate7 = 0.37

#declare constants(tax bracket upper limits)

limit1 = 9525
limit2 = 38700
limit3 = 82500
limit4 = 157500
limit5 = 200000
limit6 = 500000

#step1 prompt the user to enter their income for the year

income = float(input("Enter the annual income: "))

#step2 calculate the amount in each range

range1 = limit2 - limit1
range2 = limit3 - limit2
range3 = limit4 - limit3
range4 = limit5 - limit4
range5 = limit6 - limit5
range6 = income - limit6

#step3 calculate the tax amount in each bracket

tax1 = limit1 * rate1
tax2 = range1 * rate2
tax3 = range2 * rate3
tax4 = range3 * rate4
tax5 = range4 * rate5
tax6 = range5 * rate6
tax7 = range6 * rate7

#step4 conditions which adds tax on specific bracket

if income < limit1:
    tax = tax1

elif limit1 < income < limit2:
    tax = tax2 + tax1

elif limit2 < income < limit3:
    tax = tax3 + tax2 + tax1

elif limit3 < income < limit4:
    tax = tax4 + tax3 + tax2 + tax1

elif limit4 < income < limit5:
    tax = tax5 + tax4 + tax3 + tax2 + tax1

elif limit5 < income < limit6: 
    tax = tax6 + tax5 + tax4 + tax3 + tax2 + tax1

elif income >= limit6:
    tax = tax7 + tax6 + tax5 + tax4 + tax3 + tax2 + tax1

#step5 display the output on the screen 
    
print("Yearly Income:         $", format(income, '14,.02f'))

if income < limit1:
    print("Tax Rate: ", format(rate1, '28.0%'))

elif limit1 < income < limit2:
    print("Tax Rate: ", format(rate2, '28.0%'))

elif limit2 < income < limit3:
    print("Tax Rate: ", format(rate3, '28.0%'))

elif limit3 < income < limit4:
    print("Tax Rate: ", format(rate4, '28.0%'))

elif limit4 < income < limit5:
    print("Tax Rate: ", format(rate5, '28.0%'))

elif limit5 < income < limit6:
    print("Tax Rate: ", format(rate6, '28.0%'))

elif income >= limit6:
    print("Tax Rate: ", format(rate7, '28.0%'))

print("Income Tax:            $", format(tax, '14,.02f'))



