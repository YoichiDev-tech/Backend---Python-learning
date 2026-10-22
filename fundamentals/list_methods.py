numbers = [1, 2, 3, 4, 5]

numbers.append(6) # the append method adds the item at the end
numbers.insert(0, -1) # the insert method adds the item at the beginning
numbers.remove(3) # it removes the items passed
numbers.clear() # removes all the items from the list
# it expects no value in parenthesis

print(numbers)

# boolean expression
print(1 in numbers) # it returns a boolean value

# to know the length of the list
# the length built-in is the one to use
print(len(numbers))