# tip calculator
# print a welcome message
print('Welcome to the tip calculator!')
# ask the user for the total bill
message = input('What was the total bill? £')
# ask the user how much tip would like to give | this is a percentage
tip_percentage = input('How much tip would you like to give? 10 12 15? ')
# ask the user how many people to split the bill
people = input('How many people to split the bill with? ')
# calculate the exact tip amount
tip = int(tip_percentage) / 100 * int(message) + int(message)
# compute the split amount
split_amount = int(message) / int(people)
# unused round function
round(split_amount, 2)
# print the tip and split amount
print(f'The tip amount is: £{tip}')
print(f'Each person should pay: £{split_amount}')
