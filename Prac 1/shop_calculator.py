'''item_1_price = float(input("Enter price for item 1:"))
'''
number_of_items = int(input("Enter Number of Items:"))
while number_of_items <= 0:
    print("Invalid Number of items")
    number_of_items = int(input("Enter Number of Items:"))

items_asked_for = 0
total_price = 0
while items_asked_for != number_of_items:
    item_price = float(input("Enter price of item:"))
    items_asked_for = items_asked_for +1
    total_price = total_price + item_price


discount = total_price * 1.10 - total_price
if total_price > 100:
    total_price = total_price - discount
print("Total Price for", (number_of_items), "items is $", float(total_price))