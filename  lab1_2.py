#lab 1-2:create variables and display with precisions
print("profit form stock")
purchasePrice = 10

sellingPrice = 15
percentProfit = 100 * ((sellingPrice - purchasePrice) / purchasePrice)

#display all the values 
print("profit from stock")
print("Purchase Price = $",purchasePrice)
print("Selling Price = $", sellingPrice)
print(f"Percent of Profit = {percentProfit:.2f} %")
