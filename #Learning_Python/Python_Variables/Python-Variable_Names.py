# ------------------------------
# Variable Names in Python
# ------------------------------
# Variables can have almost any name, but there are some rules:
# - They must start with a letter or underscore _
# - They can contain letters, numbers, and underscores
# - They are case-sensitive (myvar ≠ Myvar)

# Examples of valid variable names:
myvar = "John"       # all lowercase
my_var = "John"      # underscore between words
_my_var = "John"     # starts with underscore
myVar = "John"       # camelCase style
MYVAR = "John"       # all uppercase (often used for constants)
myvar2 = "John"      # with a number at the end

# Printing the variables:
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# ------------------------------
# Multi-word Variable Names
# ------------------------------
# There are different conventions to name variables with multiple words:

# 1. Camel Case:
# Each word after the first starts with a capital letter:
myVariableName = "John"
print(myVariableName)

# 2. Pascal Case:
# Each word starts with a capital letter:
MyVariableName = "John"
print(MyVariableName)

# 3. Snake Case:
# Each word is separated by an underscore character:
my_variable_name = "John"
print(my_variable_name)

# ------------------------------
# 🔹 Key Takeaways
# ------------------------------
# - Python allows multiple styles for variable names; choose one and be consistent.
# - snake_case is the most common in Python for normal variables and functions.
# - PascalCase is often used for class names.
# - UPPERCASE is used for constants.
# - Variable names are case-sensitive, so myVar and myvar are different.
