# Output Variables
# The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
# print(x + y)  # This would cause a TypeError

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

# Additional examples demonstrating variable output:

# Using f-strings for formatted output (Python 3.6+)
name = "Alice"
age = 25
print(f"{name} is {age} years old")

# Multiple data types with comma separation
number = 42
text = "The answer is"
is_correct = True
print(text, number, is_correct)

# String concatenation with explicit conversion
x = 10
y = " apples"
print(str(x) + y)
