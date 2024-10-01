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


#step1 Declare constants

#(tax percentage on each bracket)

rate1 = 0.1
rate2 = 0.12
rate3 = 0.22
rate4 = 0.24
rate5 = 0.32
rate6 = 0.35
rate7 = 0.37

#(tax bracket upper limits)

limit1 = 9525
limit2 = 38700
limit3 = 82500
limit4 = 157500
limit5 = 200000
limit6 = 500000


#step2 Prompt the user to enter their income for the year

income = float(input("Enter the annual income: "))


#step3 Initialize tax variable

tax = 0


#step4 Calculate the tax based on the brackets

if income <= limit1:
    tax = income * rate1
    rate = rate1

elif income <= limit2:
    tax = limit1 * rate1 + (income - limit1) * rate2
    rate = rate2

elif income <= limit3:
    tax = limit1 * rate1 + (limit2 - limit1) * rate2 + (income - limit2) * rate3
    rate = rate3

elif income <= limit4:
    tax = limit1 * rate1 + (limit2 - limit1) * rate2 + (limit3 - limit2) * rate3 + (income - limit3) * rate4
    rate = rate4

elif income <= limit5:
    tax = limit1 * rate1 + (limit2 - limit1) * rate2 + (limit3 - limit2) * rate3 + (limit4 - limit3) * rate4 + (income - limit4) * rate5
    rate = rate5

elif income <= limit6:
    tax = limit1 * rate1 + (limit2 - limit1) * rate2 + (limit3 - limit2) * rate3 + (limit4 - limit3) * rate4 + (limit5 - limit4) * rate5 + (income - limit5) * rate6
    rate = rate6

else:
    tax = limit1 * rate1 + (limit2 - limit1) * rate2 + (limit3 - limit2) * rate3 + (limit4 - limit3) * rate4 + (limit5 - limit4) * rate5 + (limit6 - limit5) * rate6 + (income - limit6) * rate7
    rate = rate7


#step5 display the output on the screen 
    
print("Yearly Income:         $", format(income, '14,.02f'))

print("Tax Rate: ", format(rate, '28.0%'))

print("Income Tax:            $", format(tax, '14,.02f'))
