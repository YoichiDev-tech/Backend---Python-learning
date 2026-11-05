# this is a simple rollercoaster program that calculates the ticket price based on height and age
# need to add logical operators 
# to check if the person is tall enough to ride the rollercoaster 
# and then calculate the ticket price based on age

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age == 1 or age == 3:
        print("Sorry, you are too young to ride the rollercoaster.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Please have a free ride on us.")
    elif age >= 56 and age <= 90:
        print("Sorry, you need to be with someone to be able to ride.") 
    else:
        bill = 12
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")