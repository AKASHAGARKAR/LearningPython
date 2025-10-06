# ------------------------------
# Multiline Comments in Python
# ------------------------------

# Python does not have a dedicated syntax for multiline comments like /* ... */ in some other languages.
# To add a multiline comment, you normally insert a '#' at the beginning of each line:

# This is a comment
# written in
# more than just one line
print("Hello, World!")  # This will print: Hello, World!

# ------------------------------
# Using Triple-Quoted Strings as Comments
# ------------------------------
# Not quite as intended, but you can use a multiline string (triple quotes).
# Since Python will ignore string literals that are not assigned to a variable,
# you can add a multiline string (triple quotes) in your code, and place your comment inside it:

"""
This is a 'fake' comment
written in
more than just one line.
Because it is a string not assigned to anything, Python ignores it.
"""

print("Hello, World!")  # This will print: Hello, World! again


"""
Another multiline string acting as a comment.
You can write as much as you want here.
This is often used for docstrings but can also serve as a quick multiline comment.
"""

# ------------------------------
# 🔹 Key Takeaways
# ------------------------------
# - The official way is to put '#' at the start of each line you want to comment.
# - Triple quotes """ ... """ are actually strings, but Python ignores them if they’re not assigned to a variable.
# - Triple quotes are most commonly used for docstrings (documentation inside functions, classes, or modules),
#   but developers sometimes use them as multiline “comments” for convenience.
