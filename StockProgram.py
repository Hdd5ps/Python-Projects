'''
Sep 4 2024
Kamal Raj Timilsena
PURCHASE        SALE
2000 shares     2000 shares
$40 per shares  42.75 per shares
3% commission   3% commission

Stock Name (string)
step 1: Get input data from the user. Name of the stock, No. of shares bought (float), cost-per share (float) , no. shares sold (float), sold-per-share (float).
step 2: Process the data. Calculate the total paid for the stock, purchase commission, sales amount, sales commission, Total Profit. 
step 3: Output the result. Display the stock name, purchase details, sales detail and the total profit. This must me formatted as required(2 decimal places & in columns)
'''
CommRate = 0.03 #the commission rate

#step1
StockName = input("Enter the name of stock: ")
SharesBought = float(input("Enter the number of shares bought: "))
CostPerShare = float(input("Enter the cost per share of shares bought: "))
SharesSold = float(input("Enter the number of shares sold: "))
PricePerShare = float(input("Enter the cost per share of shares sold: "))

#step2
PurchaseCost = SharesBought * CostPerShare
PurchaseCommission = PurchaseCost * CommRate
SaleAmount = SharesSold * PricePerShare
SaleCommission = SaleAmount * CommRate
TotalProfit = SaleAmount - (PurchaseCommission + SaleAmount + SaleCommission) 

#step3
print(StockName)
print("--------------------------")
print("Shares	  Price	     Total")
print("Purchase")
print( format(SharesBought, '8,.2f'), end='')
print( format(CostPerShare, '7,.2f'), end='')
print( format(PurchaseCost, '11,.2f'))
print("Sale")
print( format(SharesSold, '8,.2f'), end='')
print( format(PricePerShare, '7,.2f'), end='')
print( format(SaleAmount, '11,.2f'))
print("Sale Commission:", format(SaleCommission, '9,.2f'))
print("--------------------------")
print("Total Profit:", format(TotalProfit, '12,.2f'))
