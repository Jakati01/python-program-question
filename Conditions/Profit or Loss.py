''''''''''''''''''''''''''''
Calculate profit or loss.
'''''''''''''''

cost_price = float(input('ENTER THE COST PRICE: '))
selling_price = float(input('ENTER THE SELLING PRICE : '))

if cost_price <= selling_price:
    print("Profit:", selling_price - cost_price)

elif cost_price >= selling_price:
    print("Profit:", cost_price - selling_price)

#else:
     #print("No profit, no loss")


  