# heads or tails game
# print a welcome message

print("Welcome to the Heads or Tails Game!")

# the compiler will randomly choose either heads or tails
# based on the random number generated, 0 will be heads and 1 will be tails

import random

random_side = random.randint(0, 1)
if random_side == 0:
    print("Heads")
else:
    print("Tails")