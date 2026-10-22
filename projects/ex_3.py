# ask the user for their name and a budget
name = input('What is your name? ').title()
product_names = []
prices_list = []
budget = float(input('What is your current budget? '))

# ask the user to enter 4 product names
for item in range(4):
    products = input('What is the name of the product? ')
    product_names.append(products)

# ask the user to enter 4 prices
for item in range(4):
    prices = float(input('What is the price of your item? '))
    prices_list.append(prices)

# calculate and display the total cost and average product price
total = sum(prices_list)
average = sum(prices_list) / len(prices_list)

print(f'\nWelcome, {name}!')
print(f'The total is €{total:.2f}')
print(f'The average is €{average:.2f}')

# print a receipt containing each product and its price
print('\nReceipt:')
for item in range(4):
    receipt = f'{product_names[item]}: €{prices_list[item]:.2f}'
    print(receipt)

# check whether the total exceeds the customer's budget
if total > budget:
    print("The grocery's total exceeds the budget")
else:
    print("The grocery has been completed successfully")

# print only products costing more than €10
for item in range(4):
    if prices_list[item] > 10:
        print(f'{product_names[item]} costs more than €10')

# check whether a product is present in the list
print('Notebook' in product_names)
