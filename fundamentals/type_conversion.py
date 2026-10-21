# built-in function input() - takes user input from the console
user_input = input('What is your name? ')
print('Hello, ' + user_input + '!') # concatenating strings with user input

# type conversion - built-in function for converions in python
int()
float()
bool()
str()

# type conversion example
birth_year = input('Enter your birth year: ') # input() returns a string
age = 2026 - int(birth_year) # convert string to integer
print('You are ' + str(age) + ' years old.') # convert integer to string for concatenation