"""
Name: Muqeet Ali
Contact: 03112645806
Email Address: Muqeetali6@gmail.com

Problem Statement:
Create a Python program to calculate profit and loss based on user input. The program should:
1. Take input for the cost price and selling price of an item.
2. Calculate the profit or loss.
3. Display the results clearly.
"""

Qty = 1000
enter_selling_product = input("Enter the product name: ")
enter_selling_price = float(input("Enter the selling price: "))
enter_cost_price = float(input("Enter the cost price: "))
enter_quantity = int(input("Enter the quantity: "))

if enter_selling_price > enter_cost_price:
    profit =  enter_selling_price - enter_cost_price
    print("Profit of Rs. ", profit)
    Quantity = Qty - enter_quantity
    print("Remaining Inventory: ", Quantity)
elif enter_selling_price == enter_cost_price:
    print("The item was sold at the same price as the cost price. No profit or loss.")
    Quantity = Qty - enter_quantity
    print("Remaining Inventory: ", Quantity)
else:
    loss = enter_cost_price - enter_selling_price
    print("Loss of Rs:", loss)
    Quantity = Qty - enter_quantity
    print("Remaining Inventory:", Quantity)
