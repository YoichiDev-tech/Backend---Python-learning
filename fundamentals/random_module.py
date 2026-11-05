import random

# generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(a=1, b=10)
print(random_integer)

# generate a random float between 0 and 1 (inclusive)
random_float = random.random() # random() takes no arguments and returns a float between 0.0 inclusive and 1.0 non inclusive
print(random_float)

random_float_number = random.random() * 10 # multiply the random float by 10 to get a float between 0 inclusive and 10 non inclusive
print(random_float_number)

random_float_number_2 = random.uniform(a=1, b=10) # generate a random float between 1 and 10 (inclusive)
print(random_float_number_2)