'''
    CSC 1010 class (2pm)
    Sept. 4, 2024
    Stock analysis program
    
    Step 1: get the data from the user: name of stock, shares bought,
            cost per share, shares sold, price per share
    
    Step 2: calculate the purchase cost for stock, the purchase commission,
            the sale amount, the sale commmission, and the total profit
            
    Step 3: print out the name of the stock, the purchase details (shares,
            cost per, total, and commission), the sale details (shares,
            price per, total, and commission), and the total profit
            format with 2 decimal places and aligned in columns
'''
COMM_RATE = 0.03 #the commission rate

#step 1
stock_name = input("Enter the name of the stock: ")
shares_bought = float( input("Enter the number of shares bought: ") )
cost_per_share = float( input("Enter the cost per share bought: ") )
shares_sold = float( input("Enter the number of shares sold: ") )
price_per_share = float( input("Enter the price received per share: ") )

#step 2
purchase_cost = shares_bought * cost_per_share
purchase_commission = purchase_cost * COMM_RATE
sale_amount = shares_sold * price_per_share
sale_commission = sale_amount * COMM_RATE
total_profit = sale_amount - ( purchase_cost + \
               purchase_commission + sale_commission)

#step 3
print(stock_name)
print("----------------------------------")
print("  Shares       Price         Total")
print("Purchase")
print( format(shares_bought, '10,.2f'), end='')
print( format(cost_per_share, '10,.2f'), end='')
print( format(purchase_cost, '14,.2f'))
print("Purchase commission:", format(purchase_commission,'13,.2f') )
print("Sale")
print( format(shares_sold, '10,.2f'),end='')
print( format(price_per_share, '10,.2f'), end='')
print( format(sale_amount, '14,.2f'))
print("Sale commission:", format(sale_commission,'17,.2f') )
print("----------------------------------")
print("Total profit:", format(total_profit, '20,.2f'))