''' 
    CSC 1010 class
    Sept. 4, 2024
    Stock analysis program

    Step 1: get the data: name of the stock,
          number of shares bought, purchase price
          per share
    
    Step 2: get the sale data: number of shares
          sold, price per share
    
    Step 3: calculate the total paid for stock,
          commission on purchase, total gained from
          sale, commission on sale, total profit
    
    Step 4: output in nice format, use 2 decimal places
          with proper alignment
'''
COMM_RATE = 0.03 #3% commission rate

#step 1
stock_name = input("Enter the name of the stock: ")
shares_bought = float( input("Shares purchased: ") )
purchase_price_per_share = float( input("Price per share: ") )

#step 2
shares_sold = float( input("Shares sold: ") )
sale_price_per_share = float( input("Price per share sold: ") )

#step 3
total_paid_for_shares = shares_bought * purchase_price_per_share
purchase_comm = COMM_RATE * total_paid_for_shares
total_from_sale = shares_sold * sale_price_per_share
sales_comm = total_from_sale * COMM_RATE
total_profit = total_from_sale - (total_paid_for_shares + \
               purchase_comm + sales_comm)

#step 4
print(stock_name)
print("---------------------------------------")
print("Purchase")
print("Shares           Price            Total")
print(format(shares_bought,'010,.2f'),end='')
print(format(purchase_price_per_share, '12,.2f'),end='')
print(format(total_paid_for_shares, '17,.2f'))
print("Purchase commission", format(purchase_comm, '20,.2f'), sep='' )
print("Sale")
print(format(shares_sold,'10,.2f'),end='')
print(format(sale_price_per_share, '12,.2f'),end='')
print(format(total_from_sale, '17,.2f'))
print("Sale commission", format(sales_comm, '23,.2f') )
print("-------------------------------------")
print("Total profit:",format(total_profit,'26,.2f'), sep='' )
