'''docstring'''
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales > 0 and sales <1000:
    bonus = sales * 1.10
    print("Your bonus is")
    print(bonus - sales)
    sales = float(input("Enter sales: $"))
else:
    if sales > 1000:
        bonus = sales * 1.15
        print ("Your bonus is")
        print(bonus - sales)
        sales = float(input("Enter sales: $"))