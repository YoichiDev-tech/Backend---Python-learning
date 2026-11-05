# pizza order practice
# use nested conditional statement to order 
# and render the price of it (must have different situations)
# work out how much the bill is

print("Welcome to python's pizza delivery!")

size = input("What size of pizza do you want: S, M or L? ")
pepperoni = input("Do you want pepperoni on it: Y or N? ")
extra_cheese =input("Do you want extra cheese on it: Y or N? ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}")