# ------------------------------
# Python Variables - Assign Multiple Values
# ------------------------------

# In Python you can assign multiple values to multiple variables in one line.

# Example 1: Assigning multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry

# Example 2: Assigning one value to multiple variables
a = b = c = "Apple"
print(a)  # Apple
print(b)  # Apple
print(c)  # Apple

# Example 3: Unpacking a collection (like a list or tuple) into variables
fruits = ["Mango", "Papaya", "Grapes"]
m, p, g = fruits  # unpack list into three variables
print(m)  # Mango
print(p)  # Papaya
print(g)  # Grapes

# ------------------------------
# 🔹 Key Takeaways
# ------------------------------
# - You can assign multiple values at once: x, y = 5, 10
# - You can assign the same value to multiple variables: x = y = z = 0
# - You can unpack lists, tuples, or other iterables into variables
# - The number of variables must match the number of values (or use * to collect extras)
