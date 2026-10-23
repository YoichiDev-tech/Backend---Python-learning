# Python Fundamentals — Practical Notes

My personal reference for Python concepts, practical exercises,
and key takeaways as I continue learning programming.

## Exercise 1 — Weight Converter

### Concepts practised

- Collecting user input with `input()`.
- Converting input into a numeric type with `int()`.
- Using `if` and `else` to control program flow.
- Comparing strings with `==`.
- Using `.upper()` to make a string comparison case-insensitive.
- Performing arithmetic calculations and displaying results.

### Key takeaways

User input is returned as a string.
Convert it to the appropriate numeric type before performing calculations.

Use conditional statements to execute different code depending on a condition.

String comparisons are case-sensitive unless the values are normalized before comparison.

## Exercise 2 — Number Analyzer

### Concepts practised

- Collecting multiple inputs and converting them into integers
- Creating a list and adding items with `.append()`
- Calculating totals with `sum()` and averages with `len()`
- Using conditional statements to compare numeric values
- Iterating over a list with a `for` loop
- Using `%` (modulo) to check whether a number is even
- Formatting output with f-strings
- Using `print(end=...)` to control how output is separated

### Key takeaways

Keep numbers as numeric values when performing calculations or comparisons.
Convert them to strings only when needed for string operations or output.

A number is even when `number % 2 == 0`.

The `len()` function returns the number of items in a collection,
while `sum()` returns the total of its numeric items.

## Exercise 3 — Mini Store Checkout

### Concepts practised

- Collecting and formatting user input
- Storing product names and prices in separate lists
- Using `range()` to repeat a task a fixed number of times
- Adding items to lists with `.append()`
- Matching related items using list indexes
- Calculating totals and averages
- Using conditional statements to compare a total against a budget
- Filtering products using a loop and a condition
- Checking list membership with the `in` operator
- Formatting currency to two decimal places with f-strings

### Key takeaways

When using parallel lists, related items must stay in the same order.
The same index should refer to the matching product name and price.

Use numeric types for calculations, and format the result for display when needed.

String comparisons and list membership checks are case-sensitive unless you explicitly normalize the values.

## Exercise 4 — Tip Calculator

### Concepts practised

- Displaying a welcome message with `print()`
- Collecting multiple user inputs with `input()`
- Converting string input into integers with `int()`
- Performing arithmetic calculations using `+`, `*`, and `/`
- Calculating a percentage using division by `100`
- Calculating a total that includes a tip
- Splitting a bill between multiple people
- Using f-strings to display calculated values
- Understanding the purpose of `round()`

### Key takeaways

The `input()` function always returns a string, even when the user enters a number.

Convert input into a suitable numeric type before performing arithmetic.
`int()` converts a value to an integer, while `float()` allows decimal values.

To calculate a percentage of a bill:

`tip_amount = bill * tip_percentage / 100`

To calculate the total bill including the tip:

`total_bill = bill + tip_amount`

To split the total equally between people:

`amount_per_person = total_bill / people`

The `round()` function returns a rounded value.
Calling `round(amount, 2)` without assigning or printing the result does not change the original variable.

F-strings allow expressions and variables to be embedded directly into strings using `{}`.

### Important distinction

The tip amount, total bill, and amount per person are three different values.

- **Tip amount:** The extra amount added to the original bill
- **Total bill:** The original bill plus the tip
- **Amount per person:** The total bill divided by the number of people

When working with money, `float` is useful for beginner exercises.
In real financial applications, `decimal.Decimal` is generally preferable for decimal arithmetic.

### Concepts to revisit

- `int()` versus `float()`
- Calculating percentages correctly
- Operator precedence in arithmetic expressions
- Rounding and formatting decimal values
- Handling invalid input and preventing division by zero
- Using meaningful variable names to distinguish intermediate calculations
