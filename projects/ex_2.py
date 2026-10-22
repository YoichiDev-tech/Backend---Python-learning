# ask the user to enter 5 numbers
# convert each input into an integer
# store the numbers in a list
# print the list of numbers
# calculate and display their total and average
# use a conditional statement to check whether the average is greater than or equal to 10
# use a loop to print only the even numbers

first_number = int(input('First number: '))
second_number = int(input('Second number: '))
third_number = int(input('Third number: '))
fourth_number = int(input('Fourth number: '))
fifth_number = int(input('Fifth number: '))

numbers = []
numbers.append(first_number)
numbers.append(second_number)
numbers.append(third_number)
numbers.append(fourth_number)
numbers.append(fifth_number)
print(numbers)

total = str(sum(numbers))
print(f'Total: {total}') # the 'f' is used in the same way 
# of a JS's template literal
average = sum(numbers) / len(numbers)
print(f'Average: {average}')


if average >= 10:
    print('The average is at least 10')
else:
    print('The average is lower')


for number in numbers:
    if number % 2 == 0:
        print(number, end=" ") 


# end="\n" -> new line (default)
# end=" " -> space after the output, keeping the next output on the same line
# end="" -> no separator after the output